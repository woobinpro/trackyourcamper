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
function FunsearchDaterecords(){
    var address_info = $('#postal').val().replaceAll(" ","+");
    var radius = $('#selectradious').val();
    var list_coordinates = ""; 
    $('#campingPlaceList tr').each(function(){
        if(list_coordinates!="")list_coordinates += "$";
        list_coordinates += $(this).find('.latitude').val() + "," + $(this).find('.longitude').val();
    });
    showProgress();
    $.ajax({
        url: host_url + '/Admin/searchFromCoordinate',
        type: 'get',
        data: "center_address="+address_info+"&radius="+radius+"&list_coordinates="+list_coordinates,
        success: function(data) {
            var count = 0;
            for(var i=0;i<data.result.length;i++){
                if(data.result[i]){$('#campingPlaceList tr:eq('+i+')').show();count++;}
                else $('#campingPlaceList tr:eq('+i+')').hide();
            }
            new Noty({text: count + ' Campingplätze gefunden',type: 'success',closeWith: ['button']}).show();
            hideProgress();
        },
        failure: function() { 
            hideProgress();
        }
    }); 
}
$(document).delegate('.campingplace-delete', 'click', function() {
    let campingplace_id = $(this).attr("campingplace_id");
    swalInit({
        title: 'Sind Sie sicher, dass Sie diesen Campingplatz löschen möchten?',
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
                url: host_url + '/Admin/ManageCampingPlaces/Delete/'+campingplace_id,
                type: 'get', // This is the default though, you don't actually need to always mention it
                success: function(data) {
                    new Noty({
                        text: 'Erfolgreich entfernt',
                        type: 'success',
                        closeWith: ['button']
                    }).show();
                    $('#tr_'+campingplace_id).remove();
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
