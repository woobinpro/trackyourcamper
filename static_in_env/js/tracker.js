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
});