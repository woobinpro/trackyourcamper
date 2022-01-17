function Redirecttologin() {
    window.location = '/Login'
}

function ShopRedirecttoregister() {
    window.location = '/Createaaccount'
}

function Redirecttoregister() {
    window.location = '/Subscription'
}

function Redirecttologout() {
    window.location = '/Admin/Logout'
}

function Redirecttomyaccount() {
    window.location = '/Myaccount'
}
$(document).ready(function(){
    $('.carousel').carousel({
        interval: 5000
    });
});