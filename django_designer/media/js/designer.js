function new_model_form() {
	$('a#add_model').click(function(){
		$('#add_model_form').fadeIn('fast'); 
	});
	
	$('#add_model_form form').ajaxForm({ 
        dataType: 'json',  
        success: function(data){
			if (!data.success) {
				alert(data.error)
				return;
			}
			$('#content').html('Loading...').load(data.url);
		} 
    }); 
}


function model_editor() {
	//*
	$('#edit_model_form form').ajaxForm({ 
		target: '#content'
    });
    //*/
	
	//Attributes popup
	$('.field-line .field input, .field-line .field select').focus(function(){
		var popup = $(this).parent().parent().find('.attrs_popup');
		if (!popup.is(":visible")) {
			$('.attrs_popup').hide();
			popup.fadeIn('fast');
		}
		
		
		$('.field-line').css({'background-color': null})
		$(this).parent().parent().css({'background-color': 'lightgray'})
	});
	
	//Sorting fields
	$('.model-fields').sortable({ handle: '.handle' });
	$( ".model-fields" ).bind("sortstop", function(event, ui) {
		var sort_val = 0;
		$('.model-fields input.sort_field').each(function() {
			sort_val++;
			if ($(this).parent().find('input:text').val() != '') {
				$(this).val(sort_val)
			}
		})
	});
	
	//Fields autocomplete
	var models = new Array();
	for (var i=0; i<MODELS.length; i++) {
		models.push({id:MODELS[i].pk, value:MODELS[i].name})
	}
	function on_item_select(event, ui) {
		if (ui.item)
			$(this).parent().find('input:hidden').val(ui.item.id)
		else
			$(this).parent().find('input:hidden').val('')
	}
	$('.f_relation input.autocomplete').autocomplete({
		source: models,
		select: on_item_select,
		change: on_item_select
	});
	
	//*
	//Field attributes
	function process_attrs() {
		var visible = COMMON_ATTRIBUTES;
		if (FIELD_ATTRIBUTES[$(this).val()]) {
			visible = visible.concat(FIELD_ATTRIBUTES[$(this).val()]);
		}
		$(this).parent().parent().find('.attrs_popup table tr').each(function(){
			if (visible.indexOf($(this).attr('class')) == -1)
				$(this).hide()
			else
				$(this).show()
		})
	}
	$('.f_type select').each(process_attrs).change(process_attrs)
	//*/

}

$(function(){
	
	/*-------------- Ajaxy links --------------------------*/
	$('a.ajax').live('click', function(){
		var target = $(this).attr('target');
		if (!target)
			target = '#content'
		$(target).html('Loading...').load($(this).attr('href'));
		return false;
	})
	
	//TODO: find better way to hanle fancybox and live
	$('a.ajaxbox').live('mouseover', function(){ $(this).fancybox() });

	
	/*-------------- Add application -----------------------*/
	$('div#add_app_form form').ajaxForm({
		target: '#app_list',
		success: function(){ $('div#add_app_form').hide('fast').find('input[name=name]').val('');}
	});
	
	$('a#add_app').click(function(){
		$('div#add_app_form').fadeIn('fast');
		return false;
	});
	
})