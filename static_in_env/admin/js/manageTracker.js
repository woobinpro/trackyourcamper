$(document).ready(function(){
    $('.tracker-delete').click(function(){
        let tracker_id = $(this).attr("tracker_id");
        swalInit({
            title: 'Sind Sie sicher, dass sie diesen Artikel löschen wollen?',
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
                    url: host_url + '/Admin/ManageTracker/Delete/'+tracker_id,
                    type: 'get', // This is the default though, you don't actually need to always mention it
                    success: function(data) {
                        new Noty({
                            text: 'Erfolgreich entfernt',
                            type: 'success',
                            closeWith: ['button']
                        }).show();
                        $('#tr_'+tracker_id).remove();
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
    $('.btn-lock').click(function(){
        var cur_val = $(this).attr('value');
        var item_id = $(this).attr('tracker_id');
        var current_item = $(this);
        if(cur_val==0){
            var confirm_txt = "Sind Sie sicher, dass Sie diesen Artikel aktivieren wollen?";
            var html_str = "<i class='icon-lock2'></i> Deaktivieren";
            var set_val = 1;
        }else {
            var confirm_txt = "Sind Sie sicher, dass Sie diesen Artikel deaktivieren wollen?";
            var set_val = 0;
            var html_str = "<i class='icon-unlocked2'></i> Aktivieren";
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
                    url: host_url + '/Admin/ManageTracker/ChangeActiveStatus/'+item_id+"/"+set_val,
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
});