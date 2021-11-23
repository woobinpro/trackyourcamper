// Validation config
var _componentValidation = function() {
    if (!$().validate) {
        console.warn('Warning - validate.min.js is not loaded.');
        return;
    }

    // Initialize
    var validator = $('#vehicle_form').validate({
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
            vehicletype: {
                number: true
            },
            color: {
                minlength: 2
            },
            userid: {
                number: true
            },
            licenseplate: {
                minlength: 2
            },
            buildingyear: {
                number: true
            },
            insucrencecompany: {
                minlength: 2
            },
            brandid: {
                number: true
            },
            modeltypename: {
                minlength: 2
            },
            trackerid: {
                number: true
            },
            tracker_mobilenumber: {
                
            },
            tracker_mobile_apn: {
            },
            date_iso: {
                dateISO: true
            },
            numbers: {
                number: true
            },
            digits: {
                digits: true
            },
            creditcard: {
                creditcard: true
            },
            basic_checkbox: {
                minlength: 2
            },
            styled_checkbox: {
                minlength: 2
            },
            switchery_group: {
                minlength: 2
            },
            switch_group: {
                minlength: 2
            }
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
function getModelList(id){
    if(id=='')return;
    $.ajax({
        url: host_url + '/Admin/ManageVehicles/getModelList/' + id,
        type: 'get',
        data: "",
        success: function(data) {
            var html_str = "";
            for(var i=0;i<data.result.length;i++){
                html_str += "<option value='"+data.result[i].name+"'></option>";
            }
            $('#model_list').html(html_str);
        }
    });
}
$(document).ready(function(){
    _componentValidation();
    $('.form-control-uniform').uniform();
    $('#upload_image').change(function(){
        if($('#upload_image').val()==''){
            new Noty({text:'Bitte Datei auswählen.',type:'warning',closeWith: ['button']}).show();
            return false;
        }
        var data = new FormData();
        data.append('image',$('#upload_image').prop('files')[0]);
        data.append('csrfmiddlewaretoken',$('#csrf_token').val());
        $.ajax({
            url: host_url + '/Admin/ManageVehicles/ImageUpload/0',
            type: 'post',
            data: data,
            cache: false,
            processData: false,
            contentType: false,
            success: function(data) {
                if(data.result=='success'){
                    
                    $('#image_id').val(data.image_id);
                }else {
                    new Noty({text:data.message,type:'error',closeWith: ['button']}).show();
                }
            }
        });
    });
    $('#brandid').change(function(){
        getModelList($(this).val());
    });
    getModelList($('#brandid').val());
});