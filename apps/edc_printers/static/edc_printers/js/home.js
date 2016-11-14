function edcPrintersReady() {
	
		var post = $.ajax({
		//url: Urls['edc-label:home_url'](),
		type: 'GET',
		dataType: 'json',
		contentType: 'application/json',
		processData: false,
	});

	post.done(function ( data ) {
		updatePage( data );
	});

	post.fail( function( jqXHR, textStatus, errorThrown ) {});
}

function updatePage( data ) {
	var print_server = JSON.parse( data.print_server );
	var printers = JSON.parse( data.printers );

	$( "#div-printers-panel" ).text( 'Printers@' + data.default_cups_server_ip );

	updateLabelTemplates( label_templates );
	//updatePrinters( printers, data.default_printer_label );

	//$( "#alert-print-server-wait" ).hide();
	//$( "#alert-print-error" ).hide();	
	//$( "#alert-print-server-error" ).hide();
	//if( data.print_server_error != '' &  data.print_server_error != null ) {
		//$( "#alert-print-server-error" ).text( data.print_server_error ).append( '<a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>' );
		//$( "#alert-print-server-error" ).show();
	//} else {
		//$( "#alert-print-server-error" ).hide();
	//};
}