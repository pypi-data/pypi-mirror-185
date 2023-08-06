{% load base_taglib %}
function update_script(element){
    var html_id = element.attr('id');
    if(element.is('select')){
        var prop = "enabled";
        var id = element.attr('id');
        var value = element.val();
    }
    else{
        var pieces = html_id.split('-');
        var prop = pieces[0];
        var id = pieces[1];
        var value = element.val();
    }

    $.ajax({
        type:   "POST",
        url:    "{% url 'psu:modify_script' %}",
        data:   {
            id: id, prop: prop, value: value,
            csrfmiddlewaretoken: '{{ csrf_token }}'
        },
        beforeSend:function(){
            element.css('border-color', 'orange');
        },
        success:function(data){
            element.css('border-color', 'green');
            element.val(data)
            //Update the activity date in the view
            var monthNames = [
                "JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"
            ];
            var date = new Date()
            var day = date.getDate();
            var monthIndex = date.getMonth();
            var year = date.getFullYear();
            var date_container = element.closest('tr').find('.date');
            date_container.html(day + ' ' + monthNames[monthIndex] + ' ' + year);
            date_container.attr('title', "Updated just now");
        },
        error:function(){
            element.css('border-color', 'red');
        },
        complete:function(){}
    });
}

function delete_script(element, id){

    $.ajax({
        type:   "POST",
        url:    "{% url 'psu:delete_script' %}",
        data:   {
            id: id, csrfmiddlewaretoken: '{{ csrf_token }}'
        },
        beforeSend:function(){
            element.after(getAjaxLoadImage());
        },
        success:function(data){
            element.closest('tr').remove();
        },
        error:function(){
            element.addClass('ajax-error');
        },
        complete:function(){}
    });
}