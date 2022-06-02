function contactus(event) {
    event.preventDefault();
    var data = new FormData($('#frmcontactsubmit').get(0));
    $.ajax({
        url: host_url + '/Contact',
        type: 'post',
        data: data,
        cache: false,
        processData: false,
        contentType: false,
        success: function(data) {
            if(data.result=='success'){
                new Noty({
                    text: 'erfolgreich gesendet',
                    type: 'success',
                    closeWith: ['button']
                }).show();
                $('#frmcontactsubmit')[0].reset();
            }else {
                new Noty({text:"Senden ist fehlgeschlagen",type:'error',closeWith: ['button']}).show();
            }
        }
    });
    return false;
}
$(document).ready(function () {
    $('.nav-item').removeClass('active');
    $('.nav-item').each(function(){
        if($(this).find('.nav-link').attr('href')=="/Contactus")$(this).addClass('active');
    });
    $('#frmcontactsubmit').submit(contactus);
});