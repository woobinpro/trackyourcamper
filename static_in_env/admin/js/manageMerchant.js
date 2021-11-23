function FunsearchDaterecords(){
    var address_info = $('#postal').val().replaceAll(" ","+");
    var radius = $('#selectradious').val();
    var merchant_list_coordinates = ""; 
    $('#merchantList tr').each(function(){
        if(merchant_list_coordinates!="")merchant_list_coordinates += "$";
        merchant_list_coordinates += $(this).find('.latitude').val() + "," + $(this).find('.longitude').val();
    });
    showProgress();
    $.ajax({
        url: host_url + '/Admin/searchFromCoordinate',
        type: 'get',
        data: "center_address="+address_info+"&radius="+radius+"&list_coordinates="+merchant_list_coordinates,
        success: function(data) {
            var count = 0;
            for(var i=0;i<data.result.length;i++){
                if(data.result[i]){$('#merchantList tr:eq('+i+')').show();count++;}
                else $('#merchantList tr:eq('+i+')').hide();
            }
            new Noty({text: count + ' Einzelhändler gefunden',type: 'success',closeWith: ['button']}).show();
            hideProgress();
        },
        failure: function() { 
            hideProgress();
        }
    }); 
}
$(document).ready(function(){
    $('.merchant-delete').click(function(){
        let merchant_id = $(this).attr("merchant_id");
        swalInit({
            title: 'Sind Sie sicher, dass Sie dieses Händlers löschen möchten?',
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
                    url: host_url + '/Admin/ManageMerchant/Delete/'+merchant_id,
                    type: 'get', // This is the default though, you don't actually need to always mention it
                    success: function(data) {
                        new Noty({
                            text: 'Erfolgreich entfernt',
                            type: 'success',
                            closeWith: ['button']
                        }).show();
                        $('#tr_'+merchant_id).remove();
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
        var merchant_id = $(this).attr('merchant_id');
        var current_item = $(this);
        if(cur_val==0){
            var confirm_txt = "Sind Sie sicher, dass Sie diesen Händler aktivieren wollen?";
            var html_str = "<i class='icon-lock2'></i> Deaktivieren";
            var active_icon = "<i class='icon-checkmark4 text-success'></i>";
            var set_val = 1;
        }else {
            var confirm_txt = "Sind Sie sicher, dass Sie diesen Händler deaktivieren möchten?";
            var set_val = 0;
            var html_str = "<i class='icon-unlocked2'></i> Aktivieren";
            var active_icon = "<i class='icon-blocked text-danger'></i>";
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
                    url: host_url + '/Admin/ManageMerchant/ChangeActiveStatus/'+merchant_id+"/"+set_val,
                    type: 'get', // This is the default though, you don't actually need to always mention it
                    success: function(data) {
                        new Noty({
                            text: 'Erfolgreich geändert',
                            type: 'success',
                            closeWith: ['button']
                        }).show();
                        current_item.attr('value', set_val);
                        current_item.html(html_str);
                        $('#tr_'+merchant_id+" td:eq(2)").html(active_icon);
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