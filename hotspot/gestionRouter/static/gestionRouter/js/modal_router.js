
function abrir_modal_creacion(url){
    
    $('#modal').load(url, function(){
        $(this).modal("show");
    });
};

function registrar_router(){

    $.ajax({
        data: $('#formulario_creacion').serialize(),
        url: $('#formulario_creacion').attr('action'),
        type: $('#formulario_creacion').attr('method'),
        success: function(response){
            console.log(response);
        },
        error: function(errores){
            console.log(errores)
            $('#modal').html(errores.responseJSON.html_formulario);
        }
    });
}