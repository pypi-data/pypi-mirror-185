{% load base_taglib %}
function update_feature(element){
    var html_id = element.attr('id');
    if(element.is('select')){
        var prop = "status";
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
        url:    "{% url 'psu:modify_feature' %}",
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
            try{
                element.parent().find(".datatable-hidden").html(data);
                $('#feature_table').DataTable().draw();
            }
            catch(ee){}
        },
        error:function(){
            element.css('border-color', 'red');
        },
        complete:function(){}
    });
}

function delete_feature(element, id){

    $.ajax({
        type:   "POST",
        url:    "{% url 'psu:delete_feature' %}",
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

$(document).ready(function() {
    var feature_table = $('#feature_table').DataTable( {
        "pageLength": 100,
        "pagingType": "full_numbers"
    } );
    //Focus on the search box on page load
    $('#feature_table_filter').find('input[type=search]').focus();
} );