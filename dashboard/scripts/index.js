$(function() {

	// $('.navbar-stacked li').on('click', function() {
	// 	$(this).parent().find('.active').removeClass('active');
	// 	$(this).addClass('active');
	// })
	
	// $('#action-container').load('/sell/index.dashboard/');

	var pathname = window.location.pathname.split('/');
    var active_tab = '.' + pathname[pathname.length - 2];
    $(".navbar-stacked " + active_tab).addClass('active');

	$('#main-container').css('height', $(window).outerHeight() - $('.navbar').outerHeight());
	$('.navbar-stacked').css('height', $(this).height() - 69);

	$(window).on('resize', function() {
		$('#main-container').css('height', $(window).outerHeight() - $('.navbar').outerHeight());
		$('.navbar-stacked').css('height', $(this).height() - 69);
	});

	$('.toolbar-button').on('click', function(e) {
		e.preventDefault();
		var $this = $(this);
		if ( !$(this).hasClass('active') ) {
			// $('#action-container').load('/sell/index.' + $(this).attr('data-target') + '/', function() {
				$('.navbar-stacked').find('.active').removeClass('active');
				$this.addClass('active');
				window.location = $(this).attr('data-target');
			// });
		}
	});

	$('.navbar-stacked .toggle').on('click', function() {
		$(this).toggleClass('x').parent().toggleClass('open');
		var status = $(this).parent().hasClass('open') ? 'open' : '';
		console.log(status);
		$.ajax({
			type: 'GET',
			url: '/dashboard/index.menu_status/' + status,
			success: function() {

			},
			error: function() {

			}
		})
	});

}); //ready