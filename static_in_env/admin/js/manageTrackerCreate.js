// Validation config
var _componentValidation = function() {
    if (!$().validate) {
        console.warn('Warning - validate.min.js is not loaded.');
        return;
    }

    // Initialize
    var validator = $('#tracker_form').validate({
        ignore: 'input[type=hidden]', // ignore hidden fields
        errorClass: 'validation-invalid-label',
        successClass: 'validation-valid-label',
        validClass: 'validation-valid-label',
        highlight: function(element, errorClass) {
            $(element).removeClass(errorClass);
        },
        unhighlight: function(element, errorClass) {
            $(element).removeClass(errorClass);
        },
        success: function(label) {
            label.addClass('validation-valid-label').text('Success.'); // remove to hide Success message
        },

        // Different components require proper error label placement
        errorPlacement: function(error, element) {

            // Unstyled checkboxes, radios
            if (element.parents().hasClass('form-check')) {
                error.appendTo( element.parents('.form-check').parent() );
            }

            // Input with icons and Select2
            else if (element.parents().hasClass('form-group-feedback') || element.hasClass('select2-hidden-accessible')) {
                error.appendTo( element.parent() );
            }

            // Input group, styled file input
            else if (element.parent().is('.uniform-uploader, .uniform-select') || element.parents().hasClass('input-group')) {
                error.appendTo( element.parent().parent() );
            }

            // Other elements
            else {
                error.insertAfter(element);
            }
        },
        rules: {
            trackercategory : {number:true},
            articlenumber: {number:true},
            price: {number:true},
            dicountprice:{number:true},
            original_qty:{number:true}
        },
        messages: {
            custom: {
                required: 'This is a custom error message'
            },
            agree: 'Please accept our policy'
        }
    });

    // Reset form
    $('#reset').on('click', function() {
        validator.resetForm();
    });
};
function upload(event) {
    event.preventDefault();
    if($('#upload_image').val()==''){
        new Noty({text:'Bitte Datei auswählen.',type:'warning',closeWith: ['button']}).show();
        return false;
    }
    var data = new FormData($('#image_upload').get(0));
    var tracker_id = $('#tracker_id').val();
    showProgress();
    $.ajax({
        url: host_url + '/Admin/ManageTracker/ImageUpload/'+tracker_id,
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
                $('.image-list').prepend("<div class='col-sm-12 image-item' image_id='"+ data.image_id +"'><img src='/static/upload/"+data.image_name+"' width='100%' alt=''><i class='icon-cancel-circle2 text-danger'></i></div>");
            }else {
                new Noty({text:data.message,type:'error',closeWith: ['button']}).show();
            }
            hideProgress();
        }
    });
    return false;
}
$(document).delegate('.image-item i', 'click', function() {
    let image_id = $(this).parent().attr("image_id");
    let image_item = $(this).parent();
    swalInit({
        title: 'Sind Sie sicher, dass Sie diesen bild löschen möchten?',
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
                url: host_url + '/Admin/ManageTracker/ImageDelete/'+image_id,
                type: 'get', // This is the default though, you don't actually need to always mention it
                success: function(data) {
                    new Noty({
                        text: 'Erfolgreich entfernt',
                        type: 'success',
                        closeWith: ['button']
                    }).show();
                    image_item.remove();
                },
                failure: function(data) { 
                    
                }
            }); 
        }
    });
    return false;
});
$(document).ready(function(){
    _componentValidation();
    var elems = Array.prototype.slice.call(document.querySelectorAll('.form-check-input-switchery'));
    elems.forEach(function(html) {
        var switchery = new Switchery(html);
    });
    $('.form-check-input-switchery').change(function(){
        var status = $(this).prop('checked');
        if(status){
            $(this).closest("tr").find("input[type='time']").removeAttr("required");
        }else {
            $(this).closest("tr").find("input[type='time']").attr("required",true);
        }
        $(this).parent().find("input[type='hidden']").val($(this).prop("checked")?1:0);
    });
    $('.form-check-input-switchery').each(function(){
        $(this).parent().find("input[type='hidden']").val($(this).prop("checked")?1:0);
        var status = $(this).prop('checked');
        if(status){
            $(this).closest("tr").find("input[type='time']").removeAttr("required");
        }else {
            $(this).closest("tr").find("input[type='time']").attr("required",true);
        }
    });
    $('.form-control-uniform').uniform();
    $('#image_upload').submit(upload);
    
});