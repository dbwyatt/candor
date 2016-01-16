$(function() {

	// $('select').select2();

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


	// $('.tooltips').tooltipster();
	$(document).tooltip({
		selector: '.tooltips',
		placement: 'right',
		delay: {show: 2000, hide: 100}
	});

	/***************************************************
	****************************************************

							Inputs

	****************************************************
	***************************************************/

	/**** Handle the label animation ****/
    validateInput2();

	/**** Validation ****/

	// $('select').materialSelect();

	/***************************************************
	****************************************************

							Forms

	****************************************************
	***************************************************/


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

function validateInput2() {
	$('input, select, textarea').each(function() {
        if ($(this).val() != '') {
        	$(this).next().addClass('fixed');
        }
    });

    $('input, select, textarea').on('keyup mouseup change', function() {

		if ( $(this).val() && !$(this).hasClass('fixed') ) {
			$(this).next().addClass('fixed');
		}
		else {
			$(this).next().removeClass('fixed');
		}

	});
}

// select plugin to look material
(function ($) {

	$.fn.materialSelect = function(options) {

		// defaults
		var settings = $.extend({
			// types: basic, checked
			type: 'basic'
		}, options);

		var selections = {};

		function getInput() {
			var input = $('<div>')
			$(input).addClass('custom-select');
			return input;
		}

		function getDropdown() {
			var dropdown = $('<div>');
			$(dropdown).addClass('custom-dropdown');
			$(dropdown).append('<ul>');
			$(dropdown).on('close', function() {
				$(this).hide();
			});

			// $(document).on('click'+Date.now()+' touchend', function (e) {
			// 	console.log(e.target);
			//     // console.log(dropdown);
			//     console.log(dropdown.has(e.target).length);
			//     if (!dropdown.is(e.target) // if the target of the click isn't the container...
			//         && dropdown.has(e.target).length === 0	// ... nor a descendant of the container
			//         && !$('.custom-select').is(e.target)
			//         && $('.custom-select').has(e.target).length === 0
			// 	)
			//     {
			//     	$(dropdown).trigger('close');
			//     }
			// });
			return dropdown;
		}

		function getOptions(external_this) {
			return $(external_this).find('option');
		}

		function convertOptions(original_this, options, dropdown) {
			$(options).each(function() {
				var option = $(this);
				if (option.text() != '') {
					var li = $('<li></li>');
					$(li).prop('value', option.val());
					if (settings.type == 'checked') {
						$(li)
							.append('<input class="dark" type="checkbox" name="'+option.text()+'" id="'+option.text()+'" />')
							.append('<label>'+option.text()+'</label>')
							.on('click', function() {
								var input = $(this).find('input');
								if (input.prop('checked')) {
									input.prop('checked', false);
									updateSelection(original_this, $(this), 'remove');
								}
								else {
									input.prop('checked', true);
									updateSelection(original_this, $(this), 'add');
								}
							});
					}
					else {
						$(li)
							.append(option.text())
							.on('touchend click', function() {
								updateSelection(original_this, $(this), 'replace');
								$(dropdown).toggle();
							});
					}
					$(dropdown).find('ul').append(li);
				}
			});
		}

		function updateSelection(original_this, selection, action) {
			$(original_this).trigger('click');
			if (action == 'add') {
				selections[selection.prop('value')] = selection.prop('value');
				for (var i in selections) {
					$(original_this).find('option');
				}
			}
			else if (action == 'replace') {
				var name = selection.prop('value');
				selections = {};
				selections[name] = name;
			}
			else if (action == 'remove') {
				delete selections[selection.prop('value')];
			}
			console.log(selections);
		}

		function engage() {
			$('.custom-select').each(function() {
		        if ($(this).text() != '') {
		        	$(this).next().addClass('fixed');
		        }
		    });

		    $('.custom-select').on('keyup mouseup change focus', function() {

				if ( $(this).text() != '' && !$(this).hasClass('fixed') ) {
					$(this).next().addClass('fixed');
				}
				else {
					$(this).next().removeClass('fixed');
				}

			});

			// $('.custom-select').on('click touchend', function () {
			// 	$('.custom-dropdown').each(function () {
			// 		if ($(this).css('display') == 'block') {
			// 			$(this).toggle();
			// 		}
			// 	});
			// });

			$('.custom-select').each(function () {
				var clone = $(this).next().next().clone().css('visibility', 'hidden').appendTo($('body'));
				$(this).css('width', clone.width());
				console.log('set width');
				clone.remove();
			});
		}

		this.each(function() {
			$(this).hide();
			var input = getInput();
			var dropdown = getDropdown();
			var options = getOptions(this);
			convertOptions(this, options, dropdown);
			// $(this).on('mousedown touchpress', function(e) {
			// 	e.preventDefault();
			// 	this.blur();
			// 	window.focus();
			// });

			input.on('click', function() {
				$(this).focus();
				dropdown.toggle();	
			});

			$(this).after(input);
			input.next().after(dropdown);
		});

		engage();
		return this;
	}

}( jQuery ));

// $(document).on('touchend click', function (e) {
//     var container = $('.custom-select');
//     var container2 = $('.custom-dropdown');
//     console.log(e.target);
//     // console.log(container2);
//     console.log(container2.has(e.target).length);
//     if (!container.is(e.target) // if the target of the click isn't the container...
//         && container.has(e.target).length === 0	// ... nor a descendant of the container
//         && !container2.is(e.target))
//     {
//     	container2.each(function (e) {
//     		$(container2).trigger('close');
//     	});
//     }
// });