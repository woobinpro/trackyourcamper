$(document).delegate('#message_delete', 'click', function() {
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
                    window.location.href = host_url + "/Messagebox";
                },
                failure: function(data) { 
                    
                }
            }); 
        }
    });
    return false;
});