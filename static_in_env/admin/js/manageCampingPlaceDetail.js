
$(document).ready(function(){
    $("input[type='checkbox']").each(function(){
        if($(this).val()==1){
            $(this).prop('checked',true);
        }else $(this).prop('checked', false);
        // $(this).attr('disabled','true');
    });
    $('#jui-accordion-collapsible').accordion({
        collapsible: true,
        autoHeight: false,
        heightStyle: "content"
    });
});