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
    if ( $('input, select, textarea').val() ) {
        $('input, select, textarea').next().addClass('fixed');
    }
    
	$('input, select, textarea').on('keyup mouseup change', function() {

		if ( $(this).val() && !$(this).hasClass('fixed') ) {
			$(this).next().addClass('fixed');
		}
		else {
			$(this).next().removeClass('fixed');
		}

	});

	/**** Validation ****/

    function onSignIn(googleUser, element) {
        $(element).append('<i class="fa fa-spinner fa-fw fa-spin"></i>');
        var profile = googleUser.getBasicProfile();
        var scopes = googleUser.getGrantedScopes();
        // console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
        // console.log('Name: ' + profile.getName());
        // console.log('Image URL: ' + profile.getImageUrl());
        // console.log('Email: ' + profile.getEmail());
        // $('.sign-in').text('Welcome, ' + profile.getName());
        // $('#login-slide .close').trigger('click');
        $.ajax({
            type: 'POST',
            url: '/homepage/',
            data: {set: true, csrfmiddlewaretoken: $('[name="csrfmiddlewaretoken"]').val(), name: profile.getName(), image: profile.getImageUrl(), email: profile.getEmail(), id_token: googleUser.getAuthResponse().id_token},
            success: function(ret) {
                if (ret == 'True') {
                    window.location = '/dashboard/';
                }
            },
            error: function(e) {
                console.log(e);
            }
        });
    }

    function signOut() {
        var auth2 = gapi.auth2.getAuthInstance();
        auth2.signOut().then(function () {
            console.log('User signed out.');
            $.ajax({
                type: 'POST',
                url: '/homepage/',
                data: {set: false, csrfmiddlewaretoken: $('[name="csrfmiddlewaretoken"]').val()},
                success: function(ret) {
                    if (ret == 'True') {
                        window.location = '/homepage/';
                    }
                },
                error: function(e) {
                    console.log(e);
                }
            });
        });
    }

    var googleUser = {};
    var startApp = function() {
        gapi.load('auth2', function() {
            // Retrieve the singleton for the GoogleAuth library and set up the client.
            auth2 = gapi.auth2.init({
                client_id: '267671914850-gtsdijk1ela2bc5076t6alla50m2t2ad.apps.googleusercontent.com',
                cookiepolicy: 'single_host_origin',
                // Request scopes in addition to 'profile' and 'email'
                scope: 'profile email https://www.googleapis.com/auth/plus.me https://www.googleapis.com/auth/plus.login'
            });
            attachSignin(document.getElementById('my-signin2'));
        })
    }

    function attachSignin(element) {
        // console.log(element.id);
        auth2.attachClickHandler(element, {},
            function(googleUser) {
                onSignIn(googleUser, element);
            },
            function(error) {
                // alert(JSON.stringify(error, undefined, 2));
            }
        );
    }

    startApp();

}); //ready


function validateInput( $inputs ) {
	var validated = true;
	$inputs.each(function() {
		if ( $(this).val() == '' && !$(this).hasClass('empty') ) {
			$(this).addClass('error').on('focus', function(){ $(this).removeClass('error') });
			validated = false;
		}
	});

	return validated;
}