{% load base_taglib %}
function getEmail(id){
    $.ajax({
        type:   "GET",
        url:    '{%url 'psu:display_email' %}',
        data:   { id: id, ts: new Date().getTime() },
        beforeSend:function(){setAjaxLoadDiv();},
        success:function(content){
           var container = $('#email-container');
           var email = $('#email-content');
           email.html(content);
           container.removeClass('hidden');                                 //Show the email
           container.find('#email-action-resend').removeClass('hidden');    //Show the resend button
           container.find('#email-action-resent').addClass('hidden');       //Hide previous resent indicator
           container.find('#email-action-failed').addClass('hidden');       //Hide previous failure indicator
        },
        error:function(ee){},
        complete:function(){clearAjaxLoadDiv();}
    });
}

function resendEmail(){
    var id = $('#email-container').find('input[name=email-instance-id]').val();
    $.ajax({
        type:   "POST",
        url:    '{%url 'psu:resend_email' %}',
        data:   { id: id, csrfmiddlewaretoken: '{{ csrf_token }}' },
        beforeSend:function(){setAjaxLoadDiv();},
        success:function(content){
           var container = $('#email-container');
           container.find('#email-action-resend').addClass('hidden');       //Hide the resend button
           container.find('#email-action-resent').removeClass('hidden');    //Show resent indicator
        },
        error:function(ee){
           var container = $('#email-container');
           container.find('#email-action-resend').addClass('hidden');       //Hide the resend button
           container.find('#email-action-resent').addClass('hidden');       //Hide the resent indicator
           container.find('#email-action-failed').removeClass('hidden');    //Show failure indicator
        },
        complete:function(){clearAjaxLoadDiv();}
    });
}