$(function() {
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
});