var plan_price;
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
    var validator = $('#frmregdetail').validate({
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
            
            ConfirmPassword: {
                equalTo: '#Password'
            },
            RegEmail: {
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
    $('.carousel').each(function(){
        $(this).find('.carousel-item:first').addClass('active');
        var id = $(this).attr('id');
        $(this).find('.carousel-indicators li').each(function(index){
            $(this).attr('data-target',id);
            $(this).attr('data-slide-to',index);
            if(index==0)$(this).addClass('active');
        });
    }); 
    
    bindpaymentprocessbind(0);
    Bind_onchangepackage(0);
    $('.nav-tabs li.disabled').click(function(event){
        event.preventDefault();
        return false;
    });
    var form = document.querySelector('#frmregdetail');
    var client_token = $('#braintree_token').val();

    braintree.dropin.create({
        authorization: client_token,
        container: '#bt-dropin',
        locale: 'de_DE',
        paypal: {
            flow: 'vault'
        }
    }, function (createErr, instance) {
        $('#btn_submit').click(function (event) {
            event.preventDefault();
            if (!$("#TermsAndConditions").is(':checked')) {
                alert($("#txttermsnconditions").val());
            }
            else if (!$("#privacypolicy").is(':checked')) {
                alert($("#txtprivacypolicy").val());
            } else {
                var paybuttonvalue = $('input[name=paymentprocessbind]:checked').val();

                if (paybuttonvalue == 0) {
                    instance.requestPaymentMethod(function (err, payload) {
                        if (err) {
                            console.log('Error', err);
                            return false;
                        }
                        else {
                            $('#nonce').val(payload.nonce);
                            $('#payment_method_type').val(payload.type);
                            form.submit();
                        }
                    });
                }
                else {
                    form.submit();
                } 
            }
            
        });
    });
});
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
function nextTab() {
    var $active = $('.wizard .nav-tabs li.active');
    $active.removeAttr('class');
    $active.addClass('disabled');
    var cur_tag = $active.find('a[data-toggle="tab"]');
    cur_tag.removeAttr('class');
    var cur_hrf = cur_tag.attr('aria-controls');
    $("#" + cur_hrf).removeClass("active");
    var next_ele = $($active).closest("li").next();
    next_ele.removeAttr('class');
    next_ele.addClass('active');
    var a_tag = next_ele.find('a[data-toggle="tab"]');
    var hrf = a_tag.attr('aria-controls');
    a_tag.attr("class", "active");
    $("#" + hrf).addClass("active");
    $('.nav-tabs li.disabled').click(function(event){
        event.preventDefault();
        return false;
    });
    window.scrollTo(0, 0);
}
function prevTab() {
    var $active = $('.wizard .nav-tabs li.active');
    $active.removeAttr('class');
    $active.addClass('disabled');
    var cur_tag = $active.find('a[data-toggle="tab"]');
    cur_tag.removeAttr('class');
    var cur_hrf = cur_tag.attr('aria-controls');
    $("#" + cur_hrf).removeClass("active");
    var next_ele = $($active).closest("li").prev();
    next_ele.removeAttr('class');
    next_ele.addClass('active');
    var a_tag = next_ele.find('a[data-toggle="tab"]');
    var hrf = a_tag.attr('aria-controls');
    a_tag.attr("class", "active");
    $("#" + hrf).addClass("active");
    $('.nav-tabs li.disabled').click(function(event){
        event.preventDefault();
        return false;
    });
    
    window.scrollTo(0, 0);
}
function fbFocusOnTop(page_index) {
    if(page_index==1){
        if($("#frmregdetail").valid()){
            $.ajax({
                url: host_url + '/checkEmailExist',
                data: "email="+$('#RegEmail').val()+"&csrfmiddlewaretoken="+$('#csrf_token').val(),
                type: 'post', // This is the default though, you don't actually need to always mention it
                success: function(data) {
                    if(data.result=='success'){
                        nextTab();
                    }else {
                        new Noty({
                            text: 'Please input correct addressE-Mail existiert bereits. Bitte wählen Sie eine andere E-Mail-Adresse',
                            type: 'warning',
                            closeWith: ['button']
                        }).show();
                    }
                }
            }); 
        }
    }else if(page_index==4){
        var _data = new FormData($('#frmregdetail').get(0));
        $.ajax({
            url: host_url + '/getAmount',
            data: _data,
            cache: false,
            processData: false,
            contentType: false,
            type: 'post', // This is the default though, you don't actually need to always mention it
            success: function(data) {
                $('#subscription_name').html(data.s_name);
                $('#subscription_price').html(data.s_price + "€");
                // $('#subscription_tax_price').html(data.s_tax_price + "€");
                $('#tracker_name').html(data.t_name);
                $('#tracker_price').html(data.t_price + "€");
                $('#tracker_tax_price').html(data.t_tax_price + "€");
                $('#tracker_activation_price').html(data.t_activate_price.toFixed(2) + "€");
                $('#total_price').html(data.total_price + "€");
                nextTab();
            }
        }); 
    }
    else{
        nextTab();
    }
    return false;
}
function Onchangedeliverycheck() {
    if ($("#Issameshipaddress").prop('checked') == true) {
        $(".shipping-form").hide(300);
        $(".shipping-form .form-control").removeAttr('required');
        $("#same_address_flag").val("true");
    }
    else {
        $('.shipping-form').slideToggle('slow');
        $(".shipping-form .form-control").attr('required','');
        $("#same_address_flag").val("false");
    }
}
function Bind_onchangepackage(index) {
    var price_html = $('#payment_method_'+index).html();
    var name = $('#packagename_'+index).html();
    $('#Payment_Interval').html(price_html);
    $('#h3paymethod').html(name+" - Zahlungsintervall wählen");
}