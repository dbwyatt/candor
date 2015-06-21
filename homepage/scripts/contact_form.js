$(function() {

	$('#contact-form .btn').on('click', function() {
		$(this).text('Sending...');
	});
	
	$('#contact-form').ajaxForm(function(data) {
		if (data == 'True') {
			$('#contact-form .btn').text('Sent');
			setTimeout(function() {
				$('#contact-form .btn').text('Send');
			}, 2000);
			$('#contact-form').append("<div class='alert alert-info alert-dismissible success' role='alert'><button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button>Thank you! We're very excited to share this product with you soon! We will contact you within 48 hours.</div>");
			// setTimeout(function() {
			// 	$('.close').trigger('click');
			// }, 10000);
			// $('#contact-form').find('input[type="submit"]').prop('disabled', true);
			$('#contact-form input').not('input[type="submit"]').each(function() {
				$(this).val('');
			});
			setTimeout(function() {
				$.ajax({
					type: 'GET',
					url: '/homepage/index.contact/',
					success: function(data) {
						$("#contact-form").remove();
			            $('#contact div:last-child').append(data);
					}
				});
			}, 10000);
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
            $("#contact-form").remove();
            $('#contact div:last-child').append(data);
            $('.errorlist').each(function() {
            	$(this).next().addClass('required').focus(function() {
					if ($(this).hasClass('required')) {
						$(this).val('');
					}
					$(this).removeClass('required');
				});
            });
		}
	}); //contact submit
});