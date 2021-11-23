let badge_list = ["badge-info", "badge-primary", "badge-secondary", "badge-danger", "badge-success", "badge-warning"];
$(document).ready(function(){
    $('.badge').each(function(index){
        $(this).addClass(badge_list[index % badge_list.length]);
    });
    $('.badge i').click(function(){
        var model_id = $(this).attr('model_id');
        var badge = $(this).parent();
        swalInit({
            title: 'Sind Sie sicher, dass Sie diesen Modell löschen möchten?',
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
                    url: host_url + '/Admin/ModelDelete/'+model_id,
                    type: 'get', // This is the default though, you don't actually need to always mention it
                    success: function(data) {
                        new Noty({
                            text: 'Erfolgreich entfernt',
                            type: 'success',
                            closeWith: ['button']
                        }).show();
                        badge.remove();
                    },
                    failure: function(data) { 
                        
                    }
                }); 
            }
        });
    });
});