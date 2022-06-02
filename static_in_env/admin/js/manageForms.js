function upload(event) {
    event.preventDefault();
    $('#modal_form').modal('hide');
    if($('#upload_image').val()==''){
        new Noty({text:'Bitte Datei auswählen.',type:'warning',closeWith: ['button']}).show();
        return false;
    }
    var data = new FormData($('#upload_form').get(0));
    showProgress();
    $.ajax({
        url: host_url + '/Admin/ManageForm/Upload',
        type: 'post',
        data: data,
        cache: false,
        processData: false,
        contentType: false,
        success: function(data) {
            if(data.result=='success'){
                new Noty({
                    text: 'Erfolgreich hochgeladen',
                    type: 'success',
                    closeWith: ['button']
                }).show();
            }else {
                new Noty({text:data.message,type:'error',closeWith: ['button']}).show();
            }
            hideProgress();
            window.location.reload();
        }
    });
    return false;
}
$(document).delegate('.btn-remove-form', 'click', function() {
    let form_id = $(this).attr("formId");
    let form_item = $(this).parent().parent();
    swalInit({
        title: 'Sind Sie sicher, dass Sie diesen Formular löschen möchten?',
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
                url: host_url + '/Admin/ManageForm/Delete/'+form_id,
                type: 'get', // This is the default though, you don't actually need to always mention it
                success: function(data) {
                    new Noty({
                        text: 'Erfolgreich entfernt',
                        type: 'success',
                        closeWith: ['button']
                    }).show();
                    form_item.remove();
                },
                failure: function(data) { 
                    
                }
            }); 
        }
    });
    return false;
});
$(document).ready(function(){
    $('.form-control-uniform').uniform();
    $('#upload_form').submit(upload);
});