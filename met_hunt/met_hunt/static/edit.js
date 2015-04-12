$('document').ready(function(){
	$('#edit_form_button').click(function(){
		$edit_form = $('#edit_form');
		text_input = "<input type='text' placeholder='type something'>";
		$edit_form.append(text_input);
	});
});