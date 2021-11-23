var host_url = location.protocol + "//" + location.host;
$(document).ready(function(){
    var elems = Array.prototype.slice.call(document.querySelectorAll('.form-check-input-switchery'));
    elems.forEach(function(html) {
        var switchery = new Switchery(html);
    });
    $('.vehicle-delete').click(function(){
        let vehicle_id = $(this).attr("vehicle_id");
        swalInit({
            title: 'Sind Sie sicher, dass Sie dieses Fahrzeug löschen möchten?',
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
                    url: host_url + '/Admin/ManageVehicles/Delete/'+vehicle_id,
                    type: 'get', // This is the default though, you don't actually need to always mention it
                    success: function(data) {
                        new Noty({
                            text: 'Erfolgreich entfernt',
                            type: 'success',
                            closeWith: ['button']
                        }).show();
                        $('#tr_'+vehicle_id).remove();
                    },
                    failure: function(data) { 
                        
                    }
                }); 
            }
        });
        return false;
    });
    $('#vehicleFilter').on("input",function() {
        var val = this.value;
        $('#vehicleList tr').each(function(){
            console.log($(this).text());
            if(val=='')$(this).show();
            else if($(this).text().toLowerCase().indexOf(val.toLowerCase()) > 0)$(this).show();
            else $(this).hide();
        });
    });
});