$(function() {

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