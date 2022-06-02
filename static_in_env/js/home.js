var review_rate = 0;
// Validation config
var _componentValidation = function() {
    if (!$().validate) {
        console.warn('Warning - validate.min.js is not loaded.');
        return;
    }

    // Initialize
    var validator = $('#review_form').validate({
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
            
            review_email: {
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
$(document).ready(function(){
    _componentValidation();
    var owl = $('.owl-carousel');
    owl.owlCarousel({
        autoPlay: 3000,
        items : 4,
        center: true,
        loop:true,
        responsive: {
            0: {
                items: 1,
                nav: true
            },
            600: {
                items: 3,
                nav: false
            },
            1000: {
                items: 4,
                nav: true,
                loop: false,
                margin: 20
            }
        }
    });
    $('.btn-prev').click(function() {
        owl.trigger('owl.prev');
    })
    $('.btn-next').click(function() {
        owl.trigger('owl.next');
    })
    $('.rate-star').click(function(){
        var index = $(this).attr('index');
        $('.rate-star').each(function(){
            if($(this).attr('index')<=index){
                $(this).removeClass('icon-star-empty3');
                $(this).addClass('icon-star-full2');
            }else {
                $(this).addClass('icon-star-empty3');
                $(this).removeClass('icon-star-full2');
            }
        });
        review_rate = index;
        $('#review_rate').val(review_rate);
    });
    
});
window.onload = function() {
    var $recaptcha = document.querySelector('#g-recaptcha-response');

    if($recaptcha) {
        $recaptcha.setAttribute("required", "required");
    }
};