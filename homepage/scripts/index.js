$(function () {

	// $("#main-container").css({maxWidth: $(window).width(), height: $(window).height() - $(".navbar").height()});
	// $('.overlay').css('min-height', $(window).height() - $(".navbar").height());
	// $(window).on("resize", function() {
	// 	$("#main-container").css({height: $(window).height()});
	// }); // resize

	var image = ['img/apartment.jpg','img/apartment2.jpg','img/apartment3.jpg'];
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


	$('#sign-up').submit(function(e) {
		e.preventDefault();
		var data = $('#sign-up').serialize();
		$.post('register.php', data, function(ret) {
			if (ret == 1) {
				$('#sign-up').append("<div class='alert alert-info alert-dismissible success' role='alert'><button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button>Thank you! Your info has been saved. We're very excited to share this product with you soon! We will contact you when Candor is available.<br><br>If you have any questions regarding Candor or this registration, email us at <a href='mailto:candorcontracts@gmail.com'>candorcontracts@gmail.com</a>.</div>");
				// setTimeout(function() {
				// 	$('.close').trigger('click');
				// }, 10000);
				// $('#sign-up').find('input[type="submit"]').prop('disabled', true);
				$('#sign-up input').not('input[type="submit"]').each(function() {
					$(this).val('');
				});
			}
			else {
				var errors = JSON.parse(ret);
				for (var field in errors) {
					$('#' + field).addClass('required').focus(function() {
						if ($(this).hasClass('required')) {
							$(this).val('');
						}
						$(this).removeClass('required');
					});
				}
			}
		}); //ajax success
	}); //register submit

}); // ready