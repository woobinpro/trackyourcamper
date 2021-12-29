$(document).ready(function () {
    $('.nav-item').removeClass('active');
    $('#large_img_slider').owlCarousel({
        autoPlay: 3000,
        items : 1,
        center: true,
        loop:true
    });
    $('#small_img_slider').owlCarousel({
        items : 4
    });
    $('#btn_minus_qty').click(function(){
        var value = parseInt($('#qty').val())-1;
        $('#qty').val(value>1?value:1);
    });
    $('#btn_plus_qty').click(function(){
        $('#qty').val(parseInt($('#qty').val())+1);
    });
});