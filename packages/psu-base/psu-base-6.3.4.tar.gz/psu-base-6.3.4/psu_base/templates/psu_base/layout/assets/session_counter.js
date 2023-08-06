{% load base_taglib %}
{%if 'psu/session/expired' not in request.path%}
    var psu_session_duration = {{request.session.get_expiry_age}} - 30;
    var psu_seconds_left = psu_session_duration;
    var psu_seconds_interval = setInterval(function(){psu_session_duration_decrement();}, 1000);
    var psu_seconds_prompted = false;

    function psu_session_duration_decrement(){
        psu_seconds_left -= 1;
        if(psu_seconds_left <= 0){
            clearInterval(psu_seconds_interval);
        }
        let minutes = parseInt(psu_seconds_left / 60);
        let seconds = psu_seconds_left % 60;
        let seconds_str = ('00' + seconds).substr(-2);
        let time_str = minutes + ":" + seconds_str;
        $('#psu-time-left').html(time_str);

        if(minutes < 3 && !psu_seconds_prompted){
            psu_session_duration_prompt();
        }
    }

    function psu_session_duration_reset(){
        psu_seconds_left = psu_session_duration;
        psu_seconds_prompted = false;
    }

    function psu_session_duration_prompt(){
        {%js_confirm column_class="medium" icon="fa-hourglass-end" title="Inactivity Warning" confirm="I need more time!" cancel="Exit" onconfirm="psu_session_duration_extend();" oncancel="psu_session_duration_expired();" auto_close="Exit|30000"%}
        Your session is about to expire due to a period of inactivity.
        {%end_js_confirm%}
        psu_seconds_prompted = true;
    }

    function psu_session_duration_extend(){
        $.ajax({
            bypassGlobalComplete: true,
            type:   "POST",
            url:    "{%url 'psu:extend'%}",
            data:   {csrfmiddlewaretoken: '{{csrf_token}}'},
            beforeSend:function(){},
            success:function(data){
                psu_session_duration_reset();
            },
            error:function(){},
            complete:function(){}
        });
    }

    function psu_session_duration_expired(){
        {%if logged_in%}
            document.location.href = '{%url 'psu:logout'%}';
        {%else%}
            document.location.href = '{%url 'psu:end_session'%}';
        {%endif%}
    }

    $(document).ajaxComplete(function(e, xhr, settings){
        if (!settings.bypassGlobalComplete){
            psu_session_duration_extend();
        }
    });
{%endif%}