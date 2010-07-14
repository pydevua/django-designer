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


function edit_model_form() {
	$('#edit_model_form form').ajaxForm({ 
		target: '#content'
    });
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