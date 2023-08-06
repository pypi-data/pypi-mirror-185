
    // Show dropdown on click
    $('.dropbtn').click(function(e) {
        e.stopPropagation();  // prevents dropdown closed

        var thisId = $(this).parents('.header-menu').attr('id');

        // Find the other dropdowns
        var otherDropdowns = $(this).parents('.header-right').find('.header-menu');

        // Close any other open dropdowns
        otherDropdowns.toArray().forEach(function (e) {
            console.log(e)
            if (e.id != thisId) {
                console.log(e.id);
                $('#'+e.id).find('.dropdown-content').hide();
            }
        })
        $(this).siblings('.dropdown-content').toggle('medium');
        // console.log('click!');
    })

    // Clicking an item in an open dropdown should not close the dropdown
    $('.dropdown-content a').click(function(e) {
        e.stopPropagation();
    })
    $(document).click( function(event) {
        // Hides dropdown by clicking anywhere outside the dropdown
        $('.dropdown-content:visible').toggle('slow');
        resetDisplay();
    });

    $(window).on('resize', function(){
        // $('.header-right').css('display', '');
        // $('.dropdown-content').css('display', '');
        resetDisplay();
    });

    $('.nav-icon').click(function(e) {
        e.stopPropagation();

        $('.header-right').toggle('medium');
        $('.dropdown-content').delay(240).toggle('slow');
        console.log('expandMenu! ' + $('.header-right').attr('class'));
    });

    var resetDisplay = function() {
        $('.header-right').css('display', '');
        $('.dropdown-content').css('display', '');
    }