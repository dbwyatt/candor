$(function () {

	// $("#main-container").css({maxWidth: $(window).width(), height: $(window).height() - $(".navbar").height()});
	// $('.overlay').css('min-height', $(window).height() - $(".navbar").height());
	// $(window).on("resize", function() {
	// 	$("#main-container").css({height: $(window).height()});
	// }); // resize

	var image = ['static/homepage/media/apartment.jpg','static/homepage/media/apartment2.jpg','static/homepage/media/apartment3.jpg'];
	var image_count = 1;
	setInterval(function() {
		var container = $('.home-background');
		container.animate({opacity: 0}, 500, function() {
			container.css('background-image', 'url(' + image[image_count] + ')');
			container.animate({opacity: 1}, 500);
		});
		if (image_count == 2) {
			image_count = 0;
		}
		else {
			image_count++;
		}
	}, 10000);


	$('#sign-up').ajaxForm(function(data) {
		if (data == 'True') {
			$('#sign-up').append("<div class='alert alert-info alert-dismissible success' role='alert'><button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button>Thank you! Your info has been saved. We're very excited to share this product with you soon! We will contact you when Candor is available.<br><br>If you have any questions regarding Candor or this registration, email us at <a href='mailto:candorcontracts@gmail.com'>candorcontracts@gmail.com</a>.</div>");
			// setTimeout(function() {
			// 	$('.close').trigger('click');
			// }, 10000);
			// $('#sign-up').find('input[type="submit"]').prop('disabled', true);
			$('#sign-up input').not('input[type="submit"]').each(function() {
				$(this).val('');
			});
			setTimeout(function() {
				$.ajax({
					type: 'GET',
					url: '/homepage/index.register/',
					success: function(data) {
						$("#sign-up").remove();
			            $('.overlay').append(data);
					}
				});
			}, 10000);
			$('#sign-up').on('click', '.close', function() {
				$.ajax({
					type: 'GET',
					url: '/homepage/index.register/',
					success: function(data) {
						$("#sign-up").remove();
			            $('.overlay').append(data);
					}
				});
			});
		}
		else {
            $("#sign-up").remove();
            $('.overlay').append(data);
            $('.errorlist').each(function() {
            	$(this).next().addClass('required').focus(function() {
					if ($(this).hasClass('required')) {
						$(this).val('');
					}
					$(this).removeClass('required');
				});
            });
		}
	}); //register submit

	$('#contact-form .btn').on('click', function() {
		$(this).text('Sending...');
	});

	$('#contact-form').ajaxForm(function(data) {
		if (data == 'True') {
			$('#contact-form .btn').text('Sent');
			setTimeout(function() {
				$('#contact-form .btn').text('Send');
			}, 2000);
			$('#contact-form').append("<div class='alert alert-info alert-dismissible success' role='alert'><button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button>Thank you! We're very excited to share this product with you soon! We will contact you when Candor is available.</div>");
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

}); // ready