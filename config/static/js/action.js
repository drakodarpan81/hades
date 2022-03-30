const btnsAgregar = document.querySelectorAll("#btnTest");
const btnsDelete = document.querySelectorAll("#btnDelete");

function submit_jqueryconfirm(url, parameters, callback){
    $.confirm({
        theme: 'material',
        title: 'Confirmación',
        icon: 'fa fa-info',
        content: '¿Desea guardar la información?',
        columnClass: 'medium',
        typeAnimated: true,
        cancelButtonClass: 'btn-primary',
        draggable: true,
        dragWindowBorder: false,
        buttons: {
            info: {
                text: 'Si',
                btnClass: 'btn-primary',
                action: function(){
                    $.ajax({
                        url: url, //window.location.pathname
                        type: 'POST',
                        data: parameters,
                        dataType: 'json'
                    }).done(function(data){
                        if(!data.hasOwnProperty('error')){
                            callback();
                            return false;
                        }

                        message_error(data.error);
                    }).fail(function(jqXHR, textStatus, errorThrown){
                        alert(textStatus + ':' + errorThrown);
                    }).always(function(data){});
                }
            },
            danger: {
                text: 'No',
                btnClass: 'btn-primary',
                action: function(){

                }
            }
        }
    });
}