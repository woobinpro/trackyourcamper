$(document).ready(function(){
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
});