$(document).ready(function () {
    var elems = Array.prototype.slice.call(document.querySelectorAll('.form-check-input-switchery'));
    elems.forEach(function(html) {
        var switchery = new Switchery(html);
    });
    $('#btn_add_vehicle').click(function(e){
        var rest_count = parseInt($('#rest_count').val());
        // alert(rest_count);
        if(rest_count>0){

        }else{
            e.preventDefault();
            new Noty({text:"Sie können keine Fahrzeuge hinzufügen. Erneuern Sie Ihr Abonnement.",type:'error',closeWith: ['button']}).show();
        }
        
    });
});