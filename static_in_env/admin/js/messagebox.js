$.extend( $.fn.dataTable.defaults, {
    autoWidth: false,
    responsive: true,
    searching: false,
    info: false,
    lengthChange: false,
    ordering: false,
    columnDefs: [{ 
        orderable: false
    }],
    dom: '<"datatable-header"fl><"datatable-scroll-wrap"t><"datatable-footer"ip>',
    language: {
        search: '<span>Filter:</span> _INPUT_',
        searchPlaceholder: 'Type to filter...',
        lengthMenu: '<span>Show:</span> _MENU_',
        paginate: { 'first': 'First', 'last': 'Last', 'next': $('html').attr('dir') == 'rtl' ? '&larr;' : '&rarr;', 'previous': $('html').attr('dir') == 'rtl' ? '&rarr;' : '&larr;' }
    }
});
$(document).ready(function(){
    $('.datatable-responsive').DataTable();
    $('.message-table tr').click(function(){
        window.location.href = host_url + "/Message/" + $(this).attr('message_id');
    });
    $('.manage-delete').click(function(e) {
        let message_id = $(this).attr("message_id");
        swalInit({
            title: 'Sind Sie sicher, dass Sie diese Botschaft löschen möchten?',
            text: " ",
            type: 'warning',
            showCancelButton: true,
            confirmButtonText: 'Bestätigen',
            cancelButtonText: 'Abrechen',
            confirmButtonClass: 'btn btn-success',
            cancelButtonClass: 'btn btn-danger',
            buttonsStyling: false
        }).then(function(result) {
            if(result.value) {
                $.ajax({
                    url: host_url + '/MessageDelete/'+message_id,
                    type: 'get', // This is the default though, you don't actually need to always mention it
                    success: function(data) {
                        new Noty({
                            text: 'Erfolgreich entfernt',
                            type: 'success',
                            closeWith: ['button']
                        }).show();
                        $('#tr_'+message_id).remove();
                    },
                    failure: function(data) { 
                        
                    }
                }); 
            }
        });
        e.stopPropagation();
        return false;
    });
});