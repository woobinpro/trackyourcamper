$(document).ready(function () {
    $('.upgrade-link').click(function(){
        var package_id = $(this).attr('href');
        var data = new FormData();
        data.append('package_id',package_id);
        data.append('csrfmiddlewaretoken',$('#csrf_token').val());
        $.ajax({
            url: host_url + '/UpgradeSubscription',
            type: 'post',
            data: data,
            cache: false,
            processData: false,
            contentType: false,
            success: function(data) {
                if(data.result=='success'){
                    new Noty({text:"Successfully upgraded!!!",type:'success',closeWith: ['button']}).show();
                }else {
                    new Noty({text:"Oops! Something went wrong.",type:'error',closeWith: ['button']}).show();
                }
            }
        });
        return false;
    });
});