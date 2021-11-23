$.extend( $.fn.dataTable.defaults, {
    autoWidth: false,
    responsive: true,
    searching: false,
    info: false,
    lengthChange: false,
    columnDefs: [{ 
        orderable: false,
        targets: [-1]
    }],
    dom: '<"datatable-header"fl><"datatable-scroll-wrap"t><"datatable-footer"ip>',
    language: {
        search: '<span>Filter:</span> _INPUT_',
        searchPlaceholder: 'Type to filter...',
        lengthMenu: '<span>Show:</span> _MENU_',
        paginate: { 'first': 'First', 'last': 'Last', 'next': $('html').attr('dir') == 'rtl' ? '&larr;' : '&rarr;', 'previous': $('html').attr('dir') == 'rtl' ? '&rarr;' : '&larr;' }
    }
});
$(document).delegate('.brand-delete', 'click', function() {
    let brand_id = $(this).attr("brand_id");
    swalInit({
        title: 'Sind Sie sicher, dass Sie diese Marke löschen möchten?',
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
                url: host_url + '/Admin/ManageBrands/Delete/'+brand_id,
                type: 'get', // This is the default though, you don't actually need to always mention it
                success: function(data) {
                    new Noty({
                        text: 'Erfolgreich entfernt',
                        type: 'success',
                        closeWith: ['button']
                    }).show();
                    $('#tr_'+brand_id).remove();
                },
                failure: function(data) { 
                    
                }
            }); 
        }
    });
    return false;
});
$(document).ready(function(){
    $('.datatable-responsive').DataTable();
});
