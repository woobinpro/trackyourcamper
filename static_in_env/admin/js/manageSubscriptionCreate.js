// Validation config
var _componentValidation = function() {
    if (!$().validate) {
        console.warn('Warning - validate.min.js is not loaded.');
        return;
    }

    // Initialize
    var validator = $('#subscription_form').validate({
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
            bringbackservicefrom : {step:false},
            bringbackserviceup: {step:false},
            support_service_starttime: {step:false},
            support_service_endtime:{step:false}
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
  
    
});