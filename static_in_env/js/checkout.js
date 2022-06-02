window.onload = function() {
    var $recaptcha = document.querySelector('#g-recaptcha-response');

    if($recaptcha) {
        $recaptcha.setAttribute("required", "required");
    }
};
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

    var client_token = $('#braintree_token').val();
    var button = document.querySelector('#submit_button');
    var csrf_token = $('#csrf_token').val();
    braintree.dropin.create({
        authorization: client_token,
        container: '#bt-dropin',
        locale: 'de_DE',
        paypal: {
            flow: 'vault'
        }
    }, function (createErr, instance) {
        button.addEventListener('click', function () {
            instance.requestPaymentMethod(function (err, payload) {
                $.ajax({
                    type: 'POST',
                    url: host_url + '/payment',
                    data: {'paymentMethodNonce': payload.nonce,
                            'csrfmiddlewaretoken': csrf_token}
                }).done(function (res) {
                    if(res.result){
                        window.location.href = '/Checkout/Receipt';
                    }else {
                        window.location.reload();
                    }
                });
            });
        });
    });
    bindpaymentprocessbind(0);
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
function bindpaymentprocessbind(val) {
 
    if (val == 0) {
        $("#bindcreditdebitpaymethod").show();
        $("#bindbanktransferbindinfo").hide(); 
    }

    if (val == 1) {
        $("#bindcreditdebitpaymethod").hide();
        $("#bindbanktransferbindinfo").show();

    }
}