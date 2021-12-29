$(document).ready(function () {
    $('.carousel').each(function(){
        $(this).find('.carousel-item:first').addClass('active');
        var id = $(this).attr('id');
        $(this).find('.carousel-indicators li').each(function(index){
            $(this).attr('data-target',id);
            $(this).attr('data-slide-to',index);
            if(index==0)$(this).addClass('active');
        });
    }); 
});