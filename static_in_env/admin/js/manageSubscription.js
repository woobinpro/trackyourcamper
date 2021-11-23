$(document).ready(function(){
    $('.subscription-delete').click(function(){
        let item_id = $(this).attr("subscription_id");
        swalInit({
            title: 'Sind Sie sicher, dass Sie dieses Abo-Paket löschen möchten?',
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
                    url: host_url + '/Admin/ManageSubscription/Delete/'+item_id,
                    type: 'get', // This is the default though, you don't actually need to always mention it
                    success: function(data) {
                        new Noty({
                            text: 'Erfolgreich entfernt',
                            type: 'success',
                            closeWith: ['button']
                        }).show();
                        $('#tr_'+item_id).remove();
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
        var item_id = $(this).attr('subscription_id');
        var current_item = $(this);
        if(cur_val==0){
            var confirm_txt = "Sind Sie sicher, dass Sie dieses Abo-Paket aktivieren wollen?";
            var html_str = "<i class='icon-lock2'></i> Deaktivieren";
            var set_val = 1;
        }else {
            var confirm_txt = "Sind Sie sicher, dass Sie dieses Abo-Paket deaktivieren möchten?";
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
                    url: host_url + '/Admin/ManageSubscription/ChangeActiveStatus/'+item_id+"/"+set_val,
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