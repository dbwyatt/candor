$(function() {

	if(window.location.hash) {
	  var hash = window.location.hash.substring(1); //Puts hash in variable, and removes the # character
	  if (hash == 'login') {
	  	$('.start-here').click();
	  }
	  // hash found
	} else {
	  // No hash found
	}

	$('.btn-facebook.login').on('click', function() {
		$(this).append('<i class="fa fa-spinner fa-fw fa-spin"></i>');
		facebookLogin();
	});

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
		delay: {show: 1000, hide: 100}
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

		var items = {};
		var select_id = '';
		var selections = {};

		function getInput() {
			var input = $('<div>');
			input.addClass('custom-select');
			items.custom_input = input;
			return input;
		}

		function getDropdown() {
			var dropdown = $('<div>');
			dropdown.addClass('custom-dropdown');
			dropdown.append('<ul>');
			dropdown.on('close', function() {
				$(this).hide();
			});
			items.custom_dropdown = dropdown;

			return dropdown;
		}

		function getOptions(external_this) {
			var options = $(external_this).find('option');
			items.dropdown_options = options;
			return options;
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
							});
					}
					$(dropdown).find('ul').append(li);
				}
			});
		}

		function updateSelection(original_this, selection, action) {
			// $(original_this).trigger('click');
			var custom_select = $('#'+select_id).parent().find('.custom-select');
			
			if (!custom_select.hasClass('selected')) {
				custom_select.addClass('selected').text(selection.text());
			}
			else {
				custom_select.text(selection.text());
			}



			if (action == 'add') {
				selections[selection.prop('value')] = selection.prop('value');
				$('#'+select_id+' option[value="'+selection.prop('value')+'"]').prop('selected', true);
			}
			else if (action == 'replace') {
				$('#'+select_id+' option').prop('selected', false);
				var name = selection.prop('value');
				selections = {};
				selections[name] = name;
				$('#'+select_id+' option[value="'+selection.prop('value')+'"]').prop('selected', true);
			}
			else if (action == 'remove') {
				$('#'+select_id+' option[value="'+selection.prop('value')+'"]').prop('selected', false);
				delete selections[selection.prop('value')];
				console.log(selections);
				if ($.isEmptyObject(selections)) {
					$('#'+select_id+' option').prop('selected', false);
					custom_select.removeClass('selected').text('');
				}
			}

			
			// $('#'+select_id+' option').prop('selected', false);
			// for (var i in selections) {
				// $('#'+select_id+' option[value="'+selection.prop('value')+'"]').prop('selected', true);
			// }
			console.log(selections);
		}

		function engage(input) {
			$(input).each(function() {
		        if ($(this).text() != '') {
		        	$(this).next().addClass('fixed');
		        }
		    });

		    $(input).on('keyup mouseup change focus', function() {

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

			setTimeout(function() {
				// $('.custom-select').each(function () {
					var clone = $(items.custom_input).next().next().clone().css('visibility', 'hidden').appendTo($('body'));
					$(items.custom_input).css('width', clone.width());
					console.log('set width');
					$(items.custom_input).next().next().css('width', clone.width());
					if (settings.type == 'checked' && clone.height() > 250) {
						$(items.custom_input).next().next().css('width', clone.width() + 10);
					}
					clone.remove();
				// });
			}, 100);

			$(document).off('click.'+Date.now()).on('click.'+Date.now(), function (e) {
				var dropdown = items.custom_dropdown;
				var input = items.custom_input;
				console.log(e.target);
			    // console.log(dropdown);
			    console.log(dropdown.has(e.target).length);
			    if (!(settings.type == 'checked' && dropdown.has(e.target).length > 0)
			    	&& 
			    	(!dropdown.is(e.target) // if the target of the click isn't the container...
			        // && dropdown.has(e.target).length === 0	// ... nor a descendant of the container
			        && !input.is(e.target)
			        && input.has(e.target).length === 0)
				)
			    {

				    dropdown.hide();
			    
			    }
			});
		}

		this.each(function() {
			$(this).hide().val('');
			select_id = $(this).prop('id');
			console.log(select_id);
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
				// $(this).focus();
				dropdown.toggle();
			});

			$(this).after(input);
			input.next().after(dropdown);
			engage();
		});

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