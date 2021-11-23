function FunsearchDaterecords(){
    var address_info = $('#postal').val().replaceAll(" ","+");
    var radius = $('#selectradious').val();
    var company_list_coordinates = ""; 
    $('#securityCompanyList tr').each(function(){
        if(company_list_coordinates!="")company_list_coordinates += "$";
        company_list_coordinates += $(this).find('.latitude').val() + "," + $(this).find('.longitude').val();
    });
    showProgress();
    $.ajax({
        url: host_url + '/Admin/searchFromCoordinate',
        type: 'get',
        data: "center_address="+address_info+"&radius="+radius+"&list_coordinates="+company_list_coordinates,
        success: function(data) {
            var count = 0;
            for(var i=0;i<data.result.length;i++){
                if(data.result[i]){$('#securityCompanyList tr:eq('+i+')').show();count++;}
                else $('#securityCompanyList tr:eq('+i+')').hide();
            }
            new Noty({text: count + ' Sicherheitsfirma gefunden',type: 'success',closeWith: ['button']}).show();
            hideProgress();
        },
        failure: function() { 
            hideProgress();
        }
    }); 
}
$(document).ready(function(){
    $('.company-delete').click(function(){
        let company_id = $(this).attr("company_id");
        swalInit({
            title: 'Sind Sie sicher, dass Sie diese Sicherheitsfirma löschen möchten?',
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
                    url: host_url + '/Admin/ManageSecurityCompany/Delete/'+company_id,
                    type: 'get', // This is the default though, you don't actually need to always mention it
                    success: function(data) {
                        new Noty({
                            text: 'Erfolgreich entfernt',
                            type: 'success',
                            closeWith: ['button']
                        }).show();
                        $('#tr_'+company_id).remove();
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