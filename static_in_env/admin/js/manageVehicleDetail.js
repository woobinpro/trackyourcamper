var host_url = location.protocol + "//" + location.host;
function upload(event) {
    event.preventDefault();
    if($('#upload_image').val()==''){
        new Noty({text:'Bitte Datei auswählen.',type:'warning',closeWith: ['button']}).show();
        return false;
    }
    var data = new FormData($('#image_upload').get(0));
    var vehicle_id = $('#vehicle_id').val();
    $.ajax({
        url: host_url + '/Admin/ManageVehicles/ImageUpload/'+vehicle_id,
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
                $('#vehicle_icon').attr('src','/static/upload/'+data.image_name);
            }else {
                new Noty({text:data.message,type:'error',closeWith: ['button']}).show();
            }
        }
    });
    return false;
}
$(document).ready(function(){
    $('.form-control-uniform').uniform();
    $('#image_upload').submit(upload);
});