var map, marker, coordinate;
// Validation config
var _componentValidation = function() {
    if (!$().validate) {
        console.warn('Warning - validate.min.js is not loaded.');
        return;
    }

    // Initialize
    var validator = $('#merchant_form').validate({
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
            name: {
                minlength: 2
            },
            dealeremail: {
                email: true
            },
            website: {
                url: true
            },
            userid: {
                number: true
            },
            installationflatrate: {
                number: true
            },
            address_street: {
                minlength: 2,
                maxlength: 100
            },
            address_postal: {
                minlength:2,
                maxlength:50
            },
            address_city: {
                minlength: 2,
                maxlength: 100
            },
            address_state: {
                minlength: 2,
                maxlength: 100
            },
            address_country: {
                minlength: 2,
                maxlength: 100
            },
            address_latitude: {
                number: true
            },
            address_longitude: {
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
    $('.select').select2({
        minimumResultsForSearch: Infinity
    });
    $('#merchant_form').submit(function(){
        $('#merchant_brands').val($("select[name='supportedbrand']").val())
    });
    map = new google.maps.Map(document.getElementById("map"), {
        zoom: 15,
        center: { lat: 52.520008, lng: 13.404954 },
    });
    map.addListener("click", (e) => {
        marker.setPosition(e.latLng);
        map.panTo(e.latLng);
        coordinate = e.latLng;
    });
    $('#get_coordinate_from_google').click(function(){
        var center = { lat: 52.520008, lng: 13.404954 };
        if($('#lat_value').val()!="" && $('#lng_value').val()!=""){
            center = { lat: parseFloat($('#lat_value').val()), lng: parseFloat($('#lng_value').val()) };
        }
        if(marker!=undefined)marker.setPosition(center);
        else {
            marker = new google.maps.Marker({
                position: center,
                map: map,
            });
        }
        coordinate = center;
        map.panTo(center);
    });
    $('#btn_apply_coordinate').click(function(){
        if(coordinate!= undefined){
            $('#lat_value').val(coordinate.lat);
            $('#lng_value').val(coordinate.lng);
        }
    });
    $('#get_coordinate').click(function(){
        if($('#street').val()==''){
            new Noty({
                text: 'Bitte geben Sie Straßeninformationen ein',
                type: 'warning',
                closeWith: ['button']
            }).show();
            return false;
        }
        var street = $('#street').val().replaceAll(' ','+');
        showProgress();
        $.ajax({
            url: host_url + '/Admin/ManageUser/GetCoordinate/'+street,
            type: 'get', // This is the default though, you don't actually need to always mention it
            success: function(data) {
                if(data.result=="success"){
                    $('#lat_value').val(data.lat);
                    $('#lng_value').val(data.lng);
                }else {
                    new Noty({text:"Bitte geben Sie Ihre Adresse korrekt ein",type:'warning',closeWith: ['button']}).show();
                }
                hideProgress();
            },
            failure: function() { 
                hideProgress();
            }
        });
        return false;
    });
});