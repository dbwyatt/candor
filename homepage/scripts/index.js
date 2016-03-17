$(function () {

	// $("#main-container").css({maxWidth: $(window).width(), height: $(window).height() - $(".navbar").height()});
	// $('.overlay').css('min-height', $(window).height() - $(".navbar").height());
	// $(window).on("resize", function() {
	// 	$("#main-container").css({height: $(window).height()});
	// }); // resize

	// var image = ['/static/homepage/media/apartment.jpg','/static/homepage/media/apartment2.jpg','/static/homepage/media/apartment3.jpg'];
	// var image_count = 1;
	// setInterval(function() {
	// 	var container = $('.home-background');
	// 	container.animate({opacity: 0}, 500, function() {
	// 		container.css('background-image', 'url(' + image[image_count] + ')');
	// 		container.animate({opacity: 1}, 500);
	// 	});
	// 	if (image_count == 2) {
	// 		image_count = 0;
	// 	}
	// 	else {
	// 		image_count++;
	// 	}
	// }, 10000);

	$('video').on('ended', function () {
		this.load();
		this.play();
	});

	var slide = slideCalc();

	function slideCalc() {
		var slide = 0;
		if ($('h2.slide:in-viewport').length && $('h2.slide:in-viewport').width() / 4 > $('h2.slide:in-viewport').offset().left)
			slide = $('h2.slide:in-viewport').offset().left;
		else
			slide = $('h2.slide:in-viewport').width() / 4;

		return slide;
	}

	$('h2.slide:in-viewport').stop().delay(1000).animate(
		{
			opacity: 1,
			marginLeft: "-" + slideCalc()
		},
		{
			duration: 1000,
			start: function() {
				$(this).addClass('slid');
			}
		}
	);
	$(window).scroll(function() {
		$('h2.slide:above-the-top').removeClass('slid').removeAttr('style');
		$('h2.slide:below-the-fold').removeClass('slid').removeAttr('style');
		if (!$('h2.slide:in-viewport').hasClass('slid')) {
			$('h2.slide:in-viewport').stop().delay(1000).animate(
				{
					opacity: 1,
					marginLeft: "-" + slideCalc()
				},
				{
					duration: 1000,
					start: function() {
						$(this).addClass('slid');
					}
				}
			);
		}
	});
	$(window).resize(function() {
		if ($('h2.slide:in-viewport').length && $('h2.slide:in-viewport').offset().left < 0) {
			$('h2.slide:in-viewport').stop().animate({
				marginLeft: "+=" + Math.abs($('h2.slide:in-viewport').offset().left)
			}, 0);
		}
		else if ($('h2.slide:in-viewport').length && $('h2.slide:in-viewport').offset().left > 0) {
			if ($('h2.slide:in-viewport').css('margin-left') < $('h2.slide:in-viewport').width() / 4) {	
				$('h2.slide:in-viewport').stop().animate({
					marginLeft: "-=" + Math.abs($('h2.slide:in-viewport').offset().left)
				}, 0);
			}
			else {
				$('h2.slide:in-viewport').stop().animate({
					marginLeft: "-" + $('h2.slide:in-viewport').width() / 4
				}, 0);
			}
		}
	});

	// $('#sign-up').ajaxForm(function(data) {
	// 	if (data == 'True') {
	// 		$('#sign-up').append("<div class='alert alert-info alert-dismissible success' role='alert'><button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button>Thank you! Your info has been saved. We're very excited to share this product with you soon! We will contact you when Candor is available.<br><br>If you have any questions regarding Candor or this registration, email us at <a href='mailto:candorcontracts@gmail.com'>candorcontracts@gmail.com</a>.</div>");
	// 		// setTimeout(function() {
	// 		// 	$('.close').trigger('click');
	// 		// }, 10000);
	// 		// $('#sign-up').find('input[type="submit"]').prop('disabled', true);
	// 		$('#sign-up input').not('input[type="submit"]').each(function() {
	// 			$(this).val('');
	// 		});
	// 		setTimeout(function() {
	// 			$.ajax({
	// 				type: 'GET',
	// 				url: '/homepage/index.register/',
	// 				success: function(data) {
	// 					$("#sign-up").remove();
	// 		            $('.overlay').append(data);
	// 				}
	// 			});
	// 		}, 10000);
	// 		$('#sign-up').on('click', '.close', function() {
	// 			$.ajax({
	// 				type: 'GET',
	// 				url: '/homepage/index.register/',
	// 				success: function(data) {
	// 					$("#sign-up").remove();
	// 		            $('.overlay').append(data);
	// 				}
	// 			});
	// 		});
	// 	}
	// 	else {
 //            $("#sign-up").remove();
 //            $('.overlay').append(data);
 //            $('.errorlist').each(function() {
 //            	$(this).next().addClass('required').focus(function() {
	// 				if ($(this).hasClass('required')) {
	// 					$(this).val('');
	// 				}
	// 				$(this).removeClass('required');
	// 			});
 //            });
	// 	}
	// }); //register submit

	$('#about a').on('click touchstart', function(e) {
		e.preventDefault();
		$('#meet-us').fadeIn();
	});

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

	if ($('#login-slide').length) {
		$('.start-here, .sign-in').on('click', function() {
			$('#login-slide')
				.show('slide', {direction: 'left'}, function() {
					setTimeout(function() {
						$('#login-container').addClass('slide');
					}, 100);
				})
				.on('click', '.close', function() {
					$('#login-container').removeClass('slide');
					setTimeout(function() {
						$('#login-slide').hide('slide', {direction: 'left'});
					}, 300);
				});
		}); // start click
	}

	// $('.start-here, .sign-in').on('click', function() {
	// 	$('#login-slide')
	// 		.addClass('slide')
	// 		.on('click', '.close', function() {
	// 			$('#login-slide').removeClass('slide');
	// 		});
	// }); // start click

}); // ready