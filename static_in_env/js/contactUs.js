$(document).ready(function () {
    $('.nav-item').removeClass('active');
    $('.nav-item').each(function(){
        if($(this).find('.nav-link').attr('href')=="/Contactus")$(this).addClass('active');
    });
});