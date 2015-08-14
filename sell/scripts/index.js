$(function() {
	// $('.navbar-stacked li').on('click', function() {
	// 	$(this).parent().find('.active').removeClass('active');
	// 	$(this).addClass('active');
	// })
	
	// $('#action-container').load('/sell/index.dashboard/');

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
				window.location = '/sell/' + $(this).attr('data-target') + '/';
				$('.navbar-stacked').find('.active').removeClass('active');
				$this.addClass('active');
			// });
		}
	});

	function posting() {

	}

	function editPosting() {

	}

	function dashboard() {

	}

	function messages() {

	}
});