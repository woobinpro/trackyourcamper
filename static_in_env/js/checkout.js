// Validation config
var _componentValidation = function() {
    if (!$().validate) {
        console.warn('Warning - validate.min.js is not loaded.');
        return;
    }

    // Initialize
    var validator = $('#checkout_form').validate({
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
            
            Shiiping_salutation: {
                number: true
            },
            Billing_salutation: {
                number: true
            },
            Billing_ShopEmail: {
                email: true
            }
        },
        messages: {
            custom: {
                required: 'This is a custom error message'
            },
            agree: 'Please accept our policy'
        }
    });

};
$(document).ready(function () {
    _componentValidation();
    Onchangecustomercreate();
});

function Onchangecustomercreate() {

    if ($("#Iscreatenewcustomerornot").prop('checked') == true) {
        $("#divpasswordconfirm").slideToggle('slow');
    }
    else {
        $("#divpasswordconfirm").hide(300);
    }
}
function Onchangedeliverycheck() {
    if ($("#Issameshipaddress").prop('checked') == true) {
        $("#select_shipping_address").hide(300);
        $("#select_shipping_address .form-control").removeAttr('required');
        $("#same_address_flag").val("true");
    }
    else {
        $('#select_shipping_address').slideToggle('slow');
        $("#select_shipping_address .form-control").attr('required','');
        $("#same_address_flag").val("false");
    }
}