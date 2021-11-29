$.extend( $.fn.dataTable.defaults, {
    autoWidth: false,
    responsive: true,
    searching: false,
    info: false,
    lengthChange: false,
    aaSorting: [],
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
$(document).delegate('.btn-lock', 'click', function() {
    var cur_val = $(this).attr('value');
    var review_id = $(this).attr('review_id');
    var current_item = $(this);
    if(cur_val==1){
        var confirm_txt = "Sind Sie sicher, das Sie diese Bewertung nicht anzeigen lassen wollen?";
        var html_str = "<i class='icon-lock2'></i> Aktivieren";
        var set_val = 0;
    }else {
        var confirm_txt = "Sind Sie sicher, das Sie diese Bewertung anzeigen lassen wollen?";
        var set_val = 1;
        var html_str = "<i class='icon-unlocked2'></i> Deaktivieren";
    }
    swalInit({
        title: confirm_txt,
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
            showProgress();
            $.ajax({
                url: host_url + '/Admin/Reviewratting/ChangeLock/'+review_id+"/"+set_val,
                type: 'get', // This is the default though, you don't actually need to always mention it
                success: function(data) {
                    new Noty({
                        text: 'Erfolgreich geändert',
                        type: 'success',
                        closeWith: ['button']
                    }).show();
                    current_item.attr('value', set_val);
                    current_item.html(html_str);
                    hideProgress();
                },
                failure: function() { 
                    hideProgress();
                }
            }); 
        }
    });
    return false;
});
$(document).delegate('.review-delete', 'click', function() {
    let item_id = $(this).attr("review_id");
    swalInit({
        title: 'Sind Sie sicher, dass Sie diese Rezension löschen möchten?',
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
                url: host_url + '/Admin/Reviewratting/Delete/'+item_id,
                type: 'get', // This is the default though, you don't actually need to always mention it
                success: function(data) {
                    new Noty({
                        text: 'Erfolgreich entfernt',
                        type: 'success',
                        closeWith: ['button']
                    }).show();
                    $('#tr_'+item_id).remove();
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