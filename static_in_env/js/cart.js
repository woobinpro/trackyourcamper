var product_price=0, tax_price=0, total_price=0;
$(document).ready(function () {
    calTotalPrice();
    $('.quantity-left-minus').click(function(){
        var product_id = $(this).closest('tr').attr('product_id');
        var qty = $(this).closest('tr').find('.qty').val();
        var price = $(this).closest('tr').find('.product-price').attr('value');
        var new_qty = (parseInt(qty) - 1 > 1)?parseInt(qty)-1:1;
        setCartlist(product_id, new_qty);
        $(this).closest('tr').find('.qty').val(new_qty);
        $(this).closest('tr').find('.total-price').html(parseFloat(new_qty * parseFloat(price)).toFixed(2) + " €");
        $(this).closest('tr').find('.total-price').attr('value',parseFloat(new_qty * parseFloat(price)).toFixed(2));
        calTotalPrice();
    });
    $('.quantity-right-plus').click(function(){
        var product_id = $(this).closest('tr').attr('product_id');
        var qty = $(this).closest('tr').find('.qty').val();
        var price = $(this).closest('tr').find('.product-price').attr('value');
        var new_qty = parseInt(qty) + 1;
        setCartlist(product_id, new_qty);
        $(this).closest('tr').find('.qty').val(new_qty);
        $(this).closest('tr').find('.total-price').html(parseFloat(new_qty * parseFloat(price)).toFixed(2) + " €");
        $(this).closest('tr').find('.total-price').attr('value',parseFloat(new_qty * parseFloat(price)).toFixed(2));
        calTotalPrice();
    });
    $('.remove-edit a').click(function(){
        var product_id = $(this).closest('tr').attr('product_id');
        $.ajax({
            url: host_url + '/removeCart',
            data: "product_id="+product_id+"&csrfmiddlewaretoken="+$('#csrf_token').val(),
            type: 'post', // This is the default though, you don't actually need to always mention it
            
        }); 
        $(this).closest('tr').remove();
        return false;
    });
    $('#btn_checkout').click(function(event){
        event.preventDefault();
        if($('#login_status').val()==1){
            window.location.href='/Checkout';
            return false;
        }
        swalInit({
            title: 'Please login before proceed to checkout',
            text: " ",
            type: 'warning',
            showCancelButton: true,
            confirmButtonText: 'Confirm',
            cancelButtonText: 'Cancel',
            confirmButtonClass: 'btn btn-success',
            cancelButtonClass: 'btn btn-danger',
            buttonsStyling: false
        }).then(function(result) {
            if(result.value) {
                window.location.href="/Login";
            }
        });
        return false;
    });
});
function calTotalPrice(){
    product_price = 0;
    $('.total-price').each(function(){
        product_price += parseFloat($(this).attr('value'));
    });
    $('#total_price').html((product_price * 100 / 119).toFixed(2)+" €");
    $('#total_tax').html((product_price * 19 / 119).toFixed(2) +" €");
    $('#checkout_price').html((product_price).toFixed(2) +" €");
    var first_category = $('.product-table tbody tr').first().attr('category_id');
    $('#btn_back').attr('href','/Shop/Index/'+first_category);
    
}
function setCartlist(product_id, qty){
    $.ajax({
        url: host_url + '/setCartQty',
        data: "product_id="+product_id+"&qty="+qty+"&csrfmiddlewaretoken="+$('#csrf_token').val(),
        type: 'post', // This is the default though, you don't actually need to always mention it
        success: function(data) {
          
        },
        failure: function(data) { 
            
        }
    }); 
}