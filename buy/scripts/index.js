$(function() {

    $('#amenities').materialSelect({type:'checked'});
    $('#bath-number').materialSelect();
    $('#bed-number').materialSelect();
    $('#gender').materialSelect();

    $('#AdvButton').on("click", function(){
        var item = document.getElementById("Advanced");
        $(item).toggle();
    });

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
            console.log('else 1');
            console.log(data);
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
        $('#search-form').find('input, select, .custom-select, .custom-dropdown').not('[type="hidden"]').each(function() {
            $(this).val('').removeClass('error').next().removeClass('fixed').removeClass('selected');
            if ($(this).is('select')) $(this).find('option').prop('selected', false);
            if ($(this).is('.custom-select')) $(this).text('');
            if ($(this).is('[type="checkbox"]')) $(this).prop('checked', false);
        });
    });

    $('.contact').on('click', function() {
        $('#post-id').val($(this).data('id'));
    });

    $('#contact-form').ajaxForm(function(data) {
        if (data == 'True') {
            $('#contact-form .send').val('Sent').prop('disabled', true);
            setTimeout(function() {
                $('#contact-form .send').val('Send').prop('disabled', false);
            }, 2000);
            $('#contact-form').append("<div class='alert alert-info alert-dismissible success' role='alert'><button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button>Thank you! We will be in touch with you soon. If you have any questions, please contact us at support@candorcontracts.com.</div>");
            // setTimeout(function() {
            //  $('.close').trigger('click');
            // }, 10000);
            // $('#contact-form').find('input[type="submit"]').prop('disabled', true);
            $('#contact-form input').not('input[type="submit"]').each(function() {
                $(this).val('');
            });
            // setTimeout(function() {
            //     $.ajax({
            //         type: 'GET',
            //         url: '/homepage/index.contact/',
            //         success: function(data) {
            //             $("#contact-form").remove();
            //             $('#contact div:last-child').append(data);
            //         }
            //     });
            // }, 10000);
            $('#contact-form').on('click', '.close', function() {
                $.ajax({
                    type: 'GET',
                    url: '/homepage/index.contact/',
                    success: function(data) {
                        $("#contact-form").remove();
                        $('#contact div:last-child').append(data);
                    }
                });
            });
        }
        else {
            // $("#contact-form").remove();
            $('#contact div:last-child').append(data);
            $('input[type="text"], textarea, input[type="email"]').each(function() {
                if ($(this).val() == '') {
                    $(this).addClass('required').focus(function() {
                        if ($(this).hasClass('required')) {
                            $(this).val('');
                        }
                        $(this).removeClass('required');
                    });
                }
            });
            // $('.errorlist').each(function() {
            //     $(this).next().addClass('required').focus(function() {
            //         if ($(this).hasClass('required')) {
            //             $(this).val('');
            //         }
            //         $(this).removeClass('required');
            //     });
            // });
        }
    }); //contact submit


    
}); //ready