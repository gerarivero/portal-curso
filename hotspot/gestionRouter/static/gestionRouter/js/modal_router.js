
function abrir_modal_creacion(url){
    
    $('#modal').load(url, function(){
        $(this).modal("show");
    });
};