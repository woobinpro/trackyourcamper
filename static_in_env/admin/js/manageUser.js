function searchUser(){
    var role_value = $('#roleFilter').val();
    var customer_number = $('#customerNumberFilter').val();
    $('#userList tr').each(function(){
        $(this).hide();        
        if(role_value=='' && customer_number=="")$(this).show();
        else if(role_value!='' && customer_number!=""){
            if($(this).attr('role').includes(role_value) && $(this).attr('id')=="tr_"+customer_number)$(this).show();
        }else if(role_value!='' && customer_number==""){
            if($(this).attr('role').includes(role_value))$(this).show();
        }else{
            if($(this).attr('id')=="tr_"+customer_number)$(this).show();
        }
    });
}
$(document).ready(function(){
    
    $('.user-delete').click(function(){
        let user_id = $(this).attr("user_id");
        swalInit({
            title: 'Sind Sie sicher, dass Sie dieses Benutzer löschen möchten?',
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
                    url: host_url + '/Admin/ManageUser/Delete/'+user_id,
                    type: 'get', // This is the default though, you don't actually need to always mention it
                    success: function(data) {
                        new Noty({
                            text: 'Erfolgreich entfernt',
                            type: 'success',
                            closeWith: ['button']
                        }).show();
                        $('#tr_'+user_id).remove();
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
        var user_id = $(this).attr('user_id');
        var current_item = $(this);
        if(cur_val==0){
            var confirm_txt = "Sind Sie sicher, dass Sie diesen Benutzer sperren möchten?";
            var html_str = "<i class='icon-lock2'></i> Sperren";
            var set_val = 1;
        }else {
            var confirm_txt = "Sind Sie sicher, dass Sie diesen Benutzer entsperren wollen?";
            var set_val = 0;
            var html_str = "<i class='icon-unlocked2'></i> Freigeben";
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
                    url: host_url + '/Admin/ManageUser/ChangeRock/'+user_id+"/"+set_val,
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