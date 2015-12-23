$(function() {

	$('.prev').on('click', function() {
		var $current = $('.current');
		var $prev = $('[data-next="' + $('.current').attr('data-block') + '"]' );
		if ( $prev.length ) {
			$current.hide('slide', {direction:'up'}, function() {
				$prev.show('slide', {direction:'up'});
				$current.removeClass('current');
				$prev.addClass('current');
			});
		}
	});

	$('.next').on('click', function() {
		var $current = $('.current');
		var validate = validateInput( $current.find('input, select, textarea') );

		if ( validate ) {
			var $next = $('[data-block="' + $('.current').attr('data-next') + '"]' );
			if ( $next.length ) {
				// $current.hide('slide', {direction:'up'}, function() {
					$next.show('slide', {direction:'up'});
					$current.removeClass('current');
					$next.addClass('current');
					$('#main-container').animate({
					   scrollTop: $current.offset().top
					}, 1000);
				// });
			}
		}
	});

});