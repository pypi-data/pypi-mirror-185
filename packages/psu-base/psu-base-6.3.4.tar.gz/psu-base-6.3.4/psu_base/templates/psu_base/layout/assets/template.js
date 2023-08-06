{% load base_taglib %}

{%if can_lookup_id or '~PowerUser'|has_authority:True%}
    /** replace_with_id_tag()
     *
     * Replace the given element with an ID tag
     */
    function replace_with_id_tag(el, identifier){
        if(typeof identifier === 'undefined'){
            identifier = el.html();
        }
        if(identifier.indexOf(' ') > -1){
            console.log("replace_with_id_tag(): Identifier must be a single word.");
            return;
        }

        $.ajax({
            type:   "GET",
            url:    "{%url 'psu:id_tag_tbd' %}/" + identifier,
            data:   {},
            beforeSend:function(){
                el.html(getAjaxLoadImage());
            },
            success:function(id_tag){
                el.html(id_tag);
            },
            error:function(){
                el.html(getAjaxStatusFailedIcon());
            },
            complete:function(){
                el.removeClass('ajax-replace');
            }
        });
    }
{%endif%}

{% if modify_logo %}
    //Set the color of the PSU logo
    {% if modify_logo_calculate %}
        if(typeof setPsuLogoColor === "function"){
            setPsuLogoColor();
        }
    {%else%}
        $('.header-logo').find('img').css('filter', '{{modify_logo_filter}}');
    {%endif%}
{%endif%}

{%include 'psu_base/layout/assets/session_counter.js'%}

$(document).ready(function(){
    let bc = $('#breadcrumb-container');
    if(bc.html() == ''){
        bc.remove();
    }

    setOneTimeLinks();
});