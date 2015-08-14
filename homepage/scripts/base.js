$(function() {

	$('a[href*=#]:not([href=#])').click(function() {
		if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') || location.hostname == this.hostname) {

			var target = $(this.hash);
			target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
			if (target.length) {
				$('html,body').animate({
				   scrollTop: target.offset().top
				}, 1000);
				return false;
			}
		}
	});	//nav link click

	// $('a[href=#]').click(function() {
	// 	return false;
	// });	//nav link click

	// $(window).on('scroll', function() {
	// 	if ( $(window).scrollTop() > 70 ) {
	// 		$('.navbar').addClass('navbar-transition').show({'slide': 'top'}).addClass('navbar-fixed-top').removeClass('navbar-transition');
	// 		$('#main-container').css('margin-top', '70px');
	// 	}
	// 	else if ( $(window).scrollTop() < 1 && $('.navbar').hasClass('navbar-fixed-top') ) {
	// 		$('.navbar').removeClass('navbar-fixed-top');
	// 		$('#main-container').css('margin-top', '0');
	// 	}
	// }); //nav adjust on scroll




	/***************************************************
	****************************************************

							Inputs

	****************************************************
	***************************************************/

	/**** Handle the label animation ****/

	$('input').keyup(function() {

		if ( $(this).val() != '' ) {
			$(this).next().addClass('fixed');
		}
		else {
			$(this).next().removeClass('fixed');
		}

	});

	/**** Validation ****/


}); //ready


function validateInput( $inputs ) {
	var validated = true;
	$inputs.each(function() {
		if ( $(this).val() == '' ) {
			$(this).addClass('error').on('focus', function(){ $(this).removeClass('error') });
			validated = false;
		}
	});

	return validated;
}