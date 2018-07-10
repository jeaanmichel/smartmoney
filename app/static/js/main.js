// ################ Listas #####################
$( '.action' ).hide();
$( '#action-delete-items' ).hide();

$( 'li' ).hover(function(){

    $( this ).find( ".action" ).css("display", "inline-block");
    $( this ).find( ".price" ).css("display", "none");

},function(){

    $( this ).find(".action").css("display", "none");
    $( this ).find(".price").css("display", "inline-block");

});

$( 'li' ).click(function(e){

    e.stopImmediatePropagation();

    var temSelecao = false;

    $( this ).each(function(i, element){

        if($( element ).hasClass( "active" )){

            $( element ).removeClass( "active" );
            console.log("remove classe");
            return false;

        }else{
            $( element ).addClass( "active" );
            console.log("adiciona classe");
            return false;

        }

    });

    $( "li" ).each(function(i, element){

        if( $( element ).hasClass("active") ){

            temSelecao = true;

        }

    });

    if (!temSelecao){

        $("#action-delete-items").css("display", "none");

    }
    else{

        $("#action-delete-items").css("display", "inline-block");

    }

});

$(function(){
    if($('#tipo_parcela-0').is(':checked')){
        desabilitaCampo(false);
    }
    else{
        desabilitaCampo(true);
        limpaCampos();
    }
});

$( document ).ready(function() {
    
    $('.thumbnail').click(function(e) {
        console.log('clicou');
        $( this ).toggleClass( "active" );
        e.stopImmediatePropagation();
        
    });

    $('#tipo_parcela-0').on('change', function(){
        desabilitaCampo(false);
    });
    $('#tipo_parcela-1').on('change', function(){
        desabilitaCampo(true);
        limpaCampos();
    });
    $('#tipo_parcela-2').on('change', function(){
        desabilitaCampo(true);
        limpaCampos();
    });
    
});

function desabilita(valor){
    $( "input[type=radio]" ).prop("disabled", valor);
}

function desabilitaCampo(valor){
    $( "#total_parcelas" ).prop("disabled", valor);
    $( "#valor_parcela").prop("disabled", valor);
}

function limpaCampos(){
    $( "#total_parcelas" ).val(' ');
    $( "#valor_parcela" ).val(' ');
}

function Edit(elm) {
    $.ajax({
        url: '/getuserbyid',
        data: {
            id: $(elm).attr('data-id')
        },
        type: 'POST',
        success: function(res) {
            $( '#username' ).val(res["username"]);
        },
        error: function(error) {
            console.log("Erro: " + error);
        }
    });
}

function ConfirmDelete(elm){
   localStorage.setItem('deleteId',$(elm).attr('data-id'));
   $('#deleteModal').modal();
}

function Delete(){
	$.ajax({
		url : '/deleteuser',
		data : {id:localStorage.getItem('deleteId')},
		type : 'POST',
		success: function(res){
			console.log(res)
		},
		error: function(error){
			console.log(error);
		}
	});
}