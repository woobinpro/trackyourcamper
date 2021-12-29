var markers, searchResult = [];
var host_url = location.protocol + "//" + location.host;
var merchant_list_coordinates = ""; 
var collapse_flag = false;
$(document).ready(function () {
    Loader(1);
    $('.nav-item').removeClass('active');
    $('.nav-item').each(function(){
        if($(this).find('.nav-link').attr('href')=="/Stocklist")$(this).addClass('active');
    });
    $("#successfullsend").fadeOut(20000);
    $("#txtzipcode").val('');
    $('.list-icons-item').click();
    getMerchantList();

});
function setMap() {
    var mapOptions = {
        center: new google.maps.LatLng(0, 0),
        zoom: 15,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    var infoWindow = new google.maps.InfoWindow();
    var latlngbounds = new google.maps.LatLngBounds();
    var map = new google.maps.Map(document.getElementById("dvMap"), mapOptions);
    var lineCoordinates = [];
    $('#map_div').addClass('wide');
    $('#detail_div').addClass('hide');
    if (markers.length > 0) {
        for (i = 0; i < markers.length; i++) {
            if(searchResult[i]==false)continue;
            var data = markers[i]
            var myLatlng = new google.maps.LatLng(data.address_latitude, data.address_longitude);
            var marker = new google.maps.Marker({
                position: myLatlng,
                map: map,
                icon: new google.maps.MarkerImage("http://maps.google.com/mapfiles/ms/icons/red.png")
            });

            latlngbounds.extend(marker.position);

            (function (marker, data) {
                google.maps.event.addListener(marker, "mouseover", function (e) {
                    infoWindow.setContent("<div><b>Name: </b>" + data.name + "</div>");
                    infoWindow.open(map, marker);
                });

                google.maps.event.addListener(marker, "mouseout", function (e) {
                    infoWindow.close();
                });

                google.maps.event.addListener(marker, "click", function (e) {
                    $('#map_div').removeClass('wide');
                    $('#detail_div').removeClass('hide');
                    $('.card-title').html(data.name);
                    var html_main_info = "<b>Adresse :</b><br>" + data.address_street + "<br>" + data.address_postal + " " + data.address_state + "<br>" + data.address_country+"<br><b>Telefon: </b>" + data.phone + "<br><b>E-Mail: </b>" + data.dealeremail + "<br><b>Montage Pauschale: </b>"+ data.installationflatrate + " €";
                    var open_time = "<div class='row open-time'><div class='col-sm-6'>";
                    open_time += "<h4>Öffnungszeiten im Sommer</h4>";
                    open_time += "<span>Mo</span> <p>";
                    if(data.summer_monday_close == 1){
                        open_time += "<span class='badge badge-danger'>CLOSE</span>";
                    }else {
                        open_time += data.summer_opentimes_opentimes_mondaystart.substring(0,5)+" ~ "+data.summer_opentimes_opentimes_mondayend.substring(0,5);
                    }
                    open_time += "</p><br><span>Di</span> <p>";
                    if(data.summer_tuseday_close == 1){
                        open_time += "<span class='badge badge-danger'>CLOSE</span>";
                    }else {
                        open_time += data.summer_opentimes_opentimes_tuesdaystart.substring(0,5)+" ~ "+data.summer_opentimes_opentimes_tuesdayend.substring(0,5);
                    }
                    open_time += "</p><br><span>Mi</span> <p>";
                    if(data.summer_wednessday_close == 1){
                        open_time += "<span class='badge badge-danger'>CLOSE</span>";
                    }else {
                        open_time += data.summer_opentimes_opentimes_wednesdaystart.substring(0,5)+" ~ "+data.summer_opentimes_opentimes_wednesdayend.substring(0,5);
                    }
                    open_time += "</p><br><span>Do</span> <p>";
                    if(data.summer_thursday_close == 1){
                        open_time += "<span class='badge badge-danger'>CLOSE</span>";
                    }else {
                        open_time += data.summer_opentimes_opentimes_thursdaystart.substring(0,5)+" ~ "+data.summer_opentimes_opentimes_thursdayend.substring(0,5);
                    }
                    open_time += "</p><br><span>Fr</span> <p>";
                    if(data.summer_friday_close == 1){
                        open_time += "<span class='badge badge-danger'>CLOSE</span>";
                    }else {
                        open_time += data.summer_opentimes_opentimes_fridaystart.substring(0,5)+" ~ "+data.summer_opentimes_opentimes_fridayend.substring(0,5);
                    }
                    open_time += "</p><br><span>Sa</span> <p>";
                    if(data.summer_saturday_close == 1){
                        open_time += "<span class='badge badge-danger'>CLOSE</span>";
                    }else {
                        open_time += data.summer_opentimes_opentimes_saturdaystart.substring(0,5)+" ~ "+data.summer_opentimes_opentimes_saturdayend.substring(0,5);
                    }
                    open_time += "</p><br><span>So</span> <p>";
                    if(data.summer_sunday_close == 1){
                        open_time += "<span class='badge badge-danger'>CLOSE</span>";
                    }else {
                        open_time += data.summer_opentimes_opentimes_sundaystart.substring(0,5)+" ~ "+data.summer_opentimes_opentimes_sundayend.substring(0,5);
                    }
                    open_time += "</p></div><div class='col-sm-6'><h4>Öffnungszeiten im Winter</h4>";
                    open_time += "<span>Mo</span> <p>";
                    if(data.winter_monday_close == 1){
                        open_time += "<span class='badge badge-danger'>CLOSE</span>";
                    }else {
                        open_time += data.opentimes_opentimes_mondaystart.substring(0,5)+" ~ "+data.opentimes_opentimes_mondayend.substring(0,5);
                    }
                    open_time += "</p><br><span>Di</span> <p>";
                    if(data.winter_tuseday_close == 1){
                        open_time += "<span class='badge badge-danger'>CLOSE</span>";
                    }else {
                        open_time += data.opentimes_opentimes_tuesdaystart.substring(0,5)+" ~ "+data.opentimes_opentimes_tuesdayend.substring(0,5);
                    }
                    open_time += "</p><br><span>Mi</span> <p>";
                    if(data.winter_wednessday_close == 1){
                        open_time += "<span class='badge badge-danger'>CLOSE</span>";
                    }else {
                        open_time += data.opentimes_opentimes_wednesdaystart.substring(0,5)+" ~ "+data.opentimes_opentimes_wednesdayend.substring(0,5);
                    }
                    open_time += "</p><br><span>Do</span> <p>";
                    if(data.winter_thursday_close == 1){
                        open_time += "<span class='badge badge-danger'>CLOSE</span>";
                    }else {
                        open_time += data.opentimes_opentimes_thursdaystart.substring(0,5)+" ~ "+data.opentimes_opentimes_thursdayend.substring(0,5);
                    }
                    open_time += "</p><br><span>Fr</span> <p>";
                    if(data.winter_friday_cloas == 1){
                        open_time += "<span class='badge badge-danger'>CLOSE</span>";
                    }else {
                        open_time += data.opentimes_opentimes_fridaystart.substring(0,5)+" ~ "+data.opentimes_opentimes_fridayend.substring(0,5);
                    }
                    open_time += "</p><br><span>Sa</span> <p>";
                    if(data.winter_saturday_close == 1){
                        open_time += "<span class='badge badge-danger'>CLOSE</span>";
                    }else {
                        open_time += data.opentimes_opentimes_saturdaystart.substring(0,5)+" ~ "+data.opentimes_opentimes_saturdayend.substring(0,5);
                    }
                    open_time += "</p><br><span>So</span> <p>";
                    if(data.winter_sunday_close == 1){
                        open_time += "<span class='badge badge-danger'>CLOSE</span>";
                    }else {
                        open_time += data.opentimes_opentimes_sundaystart.substring(0,5)+" ~ "+data.opentimes_opentimes_sundayend.substring(0,5);
                    }
                    open_time += "</p></div></div>";
                    $('.card-body').html(html_main_info+"<hr>"+open_time);
                    if(collapse_flag==false){
                        collapse_flag = true;
                        $('.list-icons-item').click();
                    }
                });

            })(marker, data);
        }
    }

    var bounds = new google.maps.LatLngBounds();
    //Center map and adjust Zoom based on the position of all markers.
    map.setCenter(latlngbounds.getCenter());
    map.fitBounds(latlngbounds);
}
function Loader(val) {
    if (val == 0) {
        $('#status').fadeIn();
        $('#preloader').delay(50).fadeIn('slow');
    }
    else {
        $('#status').fadeOut();
        $('#preloader').delay(50).fadeOut('slow');
        $('body').delay(50).css({ 'overflow': 'visible' });
    }
}
function getMerchantList() {
    $.ajax({
        url: host_url + '/Admin/getMerchantList',
        type: 'get',
        success: function(data) {
            markers = data.list;
            for (i = 0; i < markers.length; i++){
                if(merchant_list_coordinates!="")merchant_list_coordinates += "$";
                merchant_list_coordinates += markers[i].address_latitude + "," + markers[i].address_longitude;
                searchResult[i] = true;
            }
            setMap();
        }
    }); 
}
function Bindzipcodedata() {
    var zipcode = $("#txtzipcode").val();
    if(zipcode==''){
        for (i = 0; i < markers.length; i++){
            searchResult[i] = true;
        }
        setMap();
        return;
    }
    var radious = $("#selectradious").val();

    $.ajax({
        url: host_url + '/Admin/searchFromCoordinate',
        type: 'get',
        data: "center_address="+zipcode+"&radius="+radious+"&list_coordinates="+merchant_list_coordinates,
        success: function(data) {
            if(data.result!='error'){
            searchResult = data.result;
            setMap();
            }else{
                new Noty({
                    text: 'Please input correct address',
                    type: 'warning',
                    closeWith: ['button']
                }).show();
            }
        }
    }); 
}