var isactive_switch;
$(document).ready(function(){
    $("#btn_submit").click(function(){
        let isactive = $("#isactive").prop("checked")?1:0;
        var data = "name="+$('#ShopCategoryName').val()+"&isactive="+isactive;
        if($('#category_id').val()!="")data += "&id="+$('#category_id').val();
        else data += "&id=new";
        $.ajax({
            url: host_url + '/Admin/ShopCategory/Submit',
            data: data,
            type: 'get', // This is the default though, you don't actually need to always mention it
            success: function(result) {
                if(result.type=="new"){
                    new Noty({
                        text: 'Erfolgreich hinzugefügt',
                        type: 'success',
                        closeWith: ['button']
                    }).show();
                    $('#category_list').append("<tr id='tr_"+result.id+"'><td class='name'>"+$('#ShopCategoryName').val()+"</td><input type='hidden' class='isactive' value='"+isactive+"'><td class='text-right'><a href='#' category_id='"+result.id+"' class='btn bg-green-300 btn-sm category-edit mr-1'><i class='icon-pencil7 mr-2'></i> Bearbeiten</a> <a href='#' category_id='"+result.id+"' class='btn bg-danger-300 btn-sm category-delete'><i class='icon-trash mr-2'></i> Löschen</a></td></tr>");
                }else{
                    new Noty({
                        text: 'Erfolgreich geändert',
                        type: 'success',
                        closeWith: ['button']
                    }).show();
                    $('#tr_'+$('#category_id').val()).find('.isactive').val($("#isactive").prop("checked")?1:0);
                    $('#tr_'+$('#category_id').val()).find('.name').html($('#ShopCategoryName').val());
                }
                hideProgress();
            },
            failure: function() { 
                hideProgress();
            }
        }); 
    });
    isactive_switch = new Switchery($('#isactive')[0]);
    
    $('#btn_new').click(function(){
        $('#ShopCategoryName').val("");
        $('#category_id').val("");
        setSwitchery(isactive_switch, false);
        $('#card_title').html("Create Category");
        $('#btn_submit').html('Create');
    });
});
function setSwitchery(switchElement, checkedBool) {
    if((checkedBool && !switchElement.isChecked()) || (!checkedBool && switchElement.isChecked())) {
        switchElement.setPosition(true);
        switchElement.handleOnchange(true);
    }
}
$(document).delegate('.category-edit', 'click', function(){
    let isactive = $('#tr_'+$(this).attr('category_id')).find('.isactive').val();
    let name = $('#tr_'+$(this).attr('category_id')).find('.name').html();
    $('#card_title').html("Update Category");
    $('#btn_submit').html('Update');
    $('#ShopCategoryName').val(name);
    $('#category_id').val($(this).attr('category_id'));
    setSwitchery(isactive_switch, (isactive==1)?true:false);
    return false;
});
$(document).delegate('.category-delete', 'click', function(){
    let category_id = $(this).attr("category_id");
    swalInit({
        title: 'Sind Sie sicher, dass sie diesen Kategorie löschen wollen?',
        text: " ",
        type: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Bestätigen',
        cancelButtonText: 'Abrechen',
        confirmButtonClass: 'btn btn-success',
        cancelButtonClass: 'btn btn-danger',
        buttonsStyling: false
    }).then(function(result) {
        if(result.value) {
            showProgress();
            $.ajax({
                url: host_url + '/Admin/ShopCategory/Delete/'+category_id,
                type: 'get', // This is the default though, you don't actually need to always mention it
                success: function(data) {
                    new Noty({
                        text: 'Erfolgreich entfernt',
                        type: 'success',
                        closeWith: ['button']
                    }).show();
                    $('#tr_'+category_id).remove();
                    hideProgress();
                },
                failure: function() { 
                    hideProgress();
                }
            }); 
        }
    });
    return false;
});