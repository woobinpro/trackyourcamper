$(document).ready(function(){
    var location = { lat: parseFloat($('#latitude').html()), lng: parseFloat($('#longitude').html()) }
    var map = new google.maps.Map(document.getElementById("map"), {
        zoom: 15,
        center: location,
    });
    var marker = new google.maps.Marker({
        position: location,
        map: map,
    });
});