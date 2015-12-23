$(function() {

    $('#AdvButton').on("click", function(){
        var item = document.getElementById("Advanced");
        if($(item).css('display') == 'none'){
            $(item).show('slide', {direction: 'up'});
        }else{
            $(item).hide('slide', {direction: 'up'});
        }
    });

    validateInput2();

    if ($('#Advanced').find('.fixed').length > 0) {
        $('#Advanced').show();
    }

    $('#search-form .btn').on('click', function() {
        $(this).text('Searching...');
    });
    
    $('#search-form').ajaxForm(function(data) {
        if (data == 'True') {
            $('#search-form .btn').text('Found');
            setTimeout(function() {
                $('#search-form .btn').text('Search');
            }, 2000);
            $('#search-form').append("<div class='alert alert-info alert-dismissible success' role='alert'><button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button>Thank you! We're very excited to share this product with you soon! We will contact you within 48 hours.</div>");
            // setTimeout(function() {
            //  $('.close').trigger('click');
            // }, 10000);
            // $('#search-form').find('input[type="submit"]').prop('disabled', true);
            // $('#search-form input').not('input[type="submit"], input[type="hidden"]').each(function() {
            //     $(this).val('');
            // });
        }
        else {
            console.log('else');
            $('#search-form').empty();
            $('#search-form').append(data);
            $('.errorlist').each(function() {
                $(this).next().addClass('error').focus(function() {
                    if ($(this).hasClass('error')) {
                        $(this).val('');
                    }
                    $(this).removeClass('error');
                });
            });
        }
    }); //contact submit

    $('.clear').on('click', function() {
        $('#search-form').find('input, select').not('[type="hidden"]').each(function() {
            $(this).val('').removeClass('error').next().removeClass('fixed');
        });
    });
    
}); //ready