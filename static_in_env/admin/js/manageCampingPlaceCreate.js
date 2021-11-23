// Validation config
var _componentValidation = function() {
    if (!$().validate) {
        console.warn('Warning - validate.min.js is not loaded.');
        return;
    }

    // Initialize
    var validator = $('#campingplace_form').validate({
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
            
            Name: {
                minlength: 2
            },
            userid: {
                number: true
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

    $("input[type='checkbox']").change(function(){
        if($(this).prop('checked'))$(this).next().val(1);
        else $(this).next().val(0);
    });
    $("input[type='checkbox']").each(function(){
        if($(this).val()==1){
            $(this).prop('checked',true);
        }else $(this).prop('checked', false);
    });
    $("input[type='text']").each(function(){
        if($(this).val()=="None")$(this).val('');
    });
};
$(document).ready(function(){
    _componentValidation();
    $('#jui-accordion-collapsible').accordion({
        collapsible: true,
        autoHeight: false,
        heightStyle: "content"
    });
});