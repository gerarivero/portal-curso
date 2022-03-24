
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

function abrir_modal_eliminacion(url){
    
    $('#modal').load(url, function(){
        $(this).modal("show");
    });
};

function eliminar_router(pk){
    
    $.ajax({
        data: { csrfmiddlewaretoken : $("[name='csrfmiddlewaretoken']").val()},
        url: '/gestionRouter/eliminar_router/'+pk,
        type: 'post',
        success: function(response){
            $('#modal').modal("hide");
            eliminar_fila_tabla(pk)
        },
        error: function(errores){
            //si hay errores se muestra con mensaje en rojo despues de ocultar el modal
            $('#modal').modal("hide");
        }
    });
};

function eliminar_fila_tabla(pk){
    console.log('eliminar fila tabla');
    $('#router_fila_'+pk).remove();
};