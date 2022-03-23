$(function(){
    $('#myDataTable').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        "language": {
            url: "//cdn.datatables.net/plug-ins/1.10.15/i18n/Spanish.json"
        },
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                "action": "searchdata"
            },
            dataSrc: ""
        },
        columns: [
            {"data": "id"},
            {"data": "name"},
            {"data": "des"},
            {"data": "des"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: "text-center",
                orderable: false,
                render: function(data, type, row){
                    var buttons = '<a href="/erp/category/update/'+row.id+'" class="btn btn-outline-info btn-block btn-sm"><i class="fa-solid fa-file-pen"></i>Editar</a> ';
                    buttons += '<a href="/erp/category/delete/'+row.id+'" class="btn btn-outline-danger btn-block btn-sm"><i class="fa-solid fa-trash-can"></i>Eliminar</a>';
                    return buttons;
                }
            },
        ],
        initComplete: function(settings, json){
        }
    });
});