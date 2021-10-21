var markers;
markers = JSON.parse('[{"Merchant_Name":"TYC","latitude":"49,7032737","longtitude":"8,2458955","Address_City":"Westhofen","Address_Country":"Deutschland","Address_Street":"Altbachgasse, 5","Address_Postal":"67593","Address_State":"Rheinland-Pfalz","Dealeremail":"trackyourcamper@gmail.com","Website":null,"Phone":"01725193694","Fax":null,"Oppning_Monday_summer":"Geschlossen","Oppning_Tuesday_summer":"Geschlossen","Oppning_Wednesday_summer":"Geschlossen","Oppning_Thursday_summer":"Geschlossen","Oppning_Friday_summer":"Geschlossen","Oppning_Saturday_summer":"Geschlossen","Oppning_Sunday_summer":"Geschlossen","Oppning_Monday_winter":"08:00 - 17:00","Oppning_Tuesday_winter":"Geschlossen","Oppning_Wednesday_winter":"Geschlossen","Oppning_Thursday_winter":"Geschlossen","Oppning_Friday_winter":"Geschlossen","Oppning_Saturday_winter":"Geschlossen","Oppning_Sunday_winter":"Geschlossen","OpenTimes_OpenTimes_MondayStart":null,"OpenTimes_OpenTimes_MondayEnd":null,"OpenTimes_OpenTimes_TuesdayStart":null,"OpenTimes_OpenTimes_TuesdayEnd":null,"OpenTimes_OpenTimes_WednesdayStart":null,"OpenTimes_OpenTimes_WednesdayEnd":null,"OpenTimes_OpenTimes_ThursdayStart":null,"OpenTimes_OpenTimes_ThursdayEnd":null,"OpenTimes_OpenTimes_FridayStart":null,"OpenTimes_OpenTimes_FridayEnd":null,"OpenTimes_OpenTimes_SaturdayStart":null,"OpenTimes_OpenTimes_SaturdayEnd":null,"OpenTimes_OpenTimes_SundayStart":null,"OpenTimes_OpenTimes_SundayEnd":null,"Summer_OpenTimes_OpenTimes_MondayStart":null,"Summer_OpenTimes_OpenTimes_MondayEnd":null,"Summer_OpenTimes_OpenTimes_TuesdayStart":null,"Summer_OpenTimes_OpenTimes_TuesdayEnd":null,"Summer_OpenTimes_OpenTimes_WednesdayStart":null,"Summer_OpenTimes_OpenTimes_WednesdayEnd":null,"Summer_OpenTimes_OpenTimes_ThursdayStart":null,"Summer_OpenTimes_OpenTimes_ThursdayEnd":null,"Summer_OpenTimes_OpenTimes_FridayStart":null,"Summer_OpenTimes_OpenTimes_FridayEnd":null,"Summer_OpenTimes_OpenTimes_SaturdayStart":null,"Summer_OpenTimes_OpenTimes_SaturdayEnd":null,"Summer_OpenTimes_OpenTimes_SundayStart":null,"Summer_OpenTimes_OpenTimes_SundayEnd":null,"Winter_Monday_close":null,"Winter_tuseday_close":null,"Winter_wednessday_close":null,"Winter_thursday_close":null,"Winter_friday_cloas":null,"Winter_saturday_close":null,"Winter_sunday_close":null,"Summer_Monday_close":null,"Summer_tuseday_close":null,"Summer_wednessday_close":null,"Summer_thursday_close":null,"Summer_friday_close":null,"Summer_saturday_close":null,"Summer_sunday_close":null,"Installationcharges":99.00},{"Merchant_Name":"Haber WOWA","latitude":"49,6106869","longtitude":"8,3203301","Address_City":"Worms","Address_Country":"Deutschland","Address_Street":"Untere Hauptstr., 51","Address_Postal":"67551","Address_State":"Rheinland-Pfalz","Dealeremail":"futurestrike75@googlemail.com","Website":null,"Phone":"01725193694","Fax":null,"Oppning_Monday_summer":"Geschlossen","Oppning_Tuesday_summer":"Geschlossen","Oppning_Wednesday_summer":"Geschlossen","Oppning_Thursday_summer":"Geschlossen","Oppning_Friday_summer":"Geschlossen","Oppning_Saturday_summer":"Geschlossen","Oppning_Sunday_summer":"Geschlossen","Oppning_Monday_winter":"16:00 - 17:00","Oppning_Tuesday_winter":"Geschlossen","Oppning_Wednesday_winter":"Geschlossen","Oppning_Thursday_winter":"Geschlossen","Oppning_Friday_winter":"Geschlossen","Oppning_Saturday_winter":"Geschlossen","Oppning_Sunday_winter":"Geschlossen","OpenTimes_OpenTimes_MondayStart":null,"OpenTimes_OpenTimes_MondayEnd":null,"OpenTimes_OpenTimes_TuesdayStart":null,"OpenTimes_OpenTimes_TuesdayEnd":null,"OpenTimes_OpenTimes_WednesdayStart":null,"OpenTimes_OpenTimes_WednesdayEnd":null,"OpenTimes_OpenTimes_ThursdayStart":null,"OpenTimes_OpenTimes_ThursdayEnd":null,"OpenTimes_OpenTimes_FridayStart":null,"OpenTimes_OpenTimes_FridayEnd":null,"OpenTimes_OpenTimes_SaturdayStart":null,"OpenTimes_OpenTimes_SaturdayEnd":null,"OpenTimes_OpenTimes_SundayStart":null,"OpenTimes_OpenTimes_SundayEnd":null,"Summer_OpenTimes_OpenTimes_MondayStart":null,"Summer_OpenTimes_OpenTimes_MondayEnd":null,"Summer_OpenTimes_OpenTimes_TuesdayStart":null,"Summer_OpenTimes_OpenTimes_TuesdayEnd":null,"Summer_OpenTimes_OpenTimes_WednesdayStart":null,"Summer_OpenTimes_OpenTimes_WednesdayEnd":null,"Summer_OpenTimes_OpenTimes_ThursdayStart":null,"Summer_OpenTimes_OpenTimes_ThursdayEnd":null,"Summer_OpenTimes_OpenTimes_FridayStart":null,"Summer_OpenTimes_OpenTimes_FridayEnd":null,"Summer_OpenTimes_OpenTimes_SaturdayStart":null,"Summer_OpenTimes_OpenTimes_SaturdayEnd":null,"Summer_OpenTimes_OpenTimes_SundayStart":null,"Summer_OpenTimes_OpenTimes_SundayEnd":null,"Winter_Monday_close":null,"Winter_tuseday_close":null,"Winter_wednessday_close":null,"Winter_thursday_close":null,"Winter_friday_cloas":null,"Winter_saturday_close":null,"Winter_sunday_close":null,"Summer_Monday_close":null,"Summer_tuseday_close":null,"Summer_wednessday_close":null,"Summer_thursday_close":null,"Summer_friday_close":null,"Summer_saturday_close":null,"Summer_sunday_close":null,"Installationcharges":149.00},{"Merchant_Name":"Rhein WOMO","latitude":"49,6321577","longtitude":"8,3666022","Address_City":"Worms","Address_Country":"Deutschland","Address_Street":"Rheinstraße 12","Address_Postal":"67547","Address_State":"Rheinland-Pfalz","Dealeremail":"futurestrike75@googlemail.com","Website":null,"Phone":"01725193694","Fax":null,"Oppning_Monday_summer":"Geschlossen","Oppning_Tuesday_summer":"Geschlossen","Oppning_Wednesday_summer":"Geschlossen","Oppning_Thursday_summer":"Geschlossen","Oppning_Friday_summer":"Geschlossen","Oppning_Saturday_summer":"Geschlossen","Oppning_Sunday_summer":"Geschlossen","Oppning_Monday_winter":"16:00 - 17:00","Oppning_Tuesday_winter":"Geschlossen","Oppning_Wednesday_winter":"Geschlossen","Oppning_Thursday_winter":"Geschlossen","Oppning_Friday_winter":"Geschlossen","Oppning_Saturday_winter":"Geschlossen","Oppning_Sunday_winter":"Geschlossen","OpenTimes_OpenTimes_MondayStart":null,"OpenTimes_OpenTimes_MondayEnd":null,"OpenTimes_OpenTimes_TuesdayStart":null,"OpenTimes_OpenTimes_TuesdayEnd":null,"OpenTimes_OpenTimes_WednesdayStart":null,"OpenTimes_OpenTimes_WednesdayEnd":null,"OpenTimes_OpenTimes_ThursdayStart":null,"OpenTimes_OpenTimes_ThursdayEnd":null,"OpenTimes_OpenTimes_FridayStart":null,"OpenTimes_OpenTimes_FridayEnd":null,"OpenTimes_OpenTimes_SaturdayStart":null,"OpenTimes_OpenTimes_SaturdayEnd":null,"OpenTimes_OpenTimes_SundayStart":null,"OpenTimes_OpenTimes_SundayEnd":null,"Summer_OpenTimes_OpenTimes_MondayStart":null,"Summer_OpenTimes_OpenTimes_MondayEnd":null,"Summer_OpenTimes_OpenTimes_TuesdayStart":null,"Summer_OpenTimes_OpenTimes_TuesdayEnd":null,"Summer_OpenTimes_OpenTimes_WednesdayStart":null,"Summer_OpenTimes_OpenTimes_WednesdayEnd":null,"Summer_OpenTimes_OpenTimes_ThursdayStart":null,"Summer_OpenTimes_OpenTimes_ThursdayEnd":null,"Summer_OpenTimes_OpenTimes_FridayStart":null,"Summer_OpenTimes_OpenTimes_FridayEnd":null,"Summer_OpenTimes_OpenTimes_SaturdayStart":null,"Summer_OpenTimes_OpenTimes_SaturdayEnd":null,"Summer_OpenTimes_OpenTimes_SundayStart":null,"Summer_OpenTimes_OpenTimes_SundayEnd":null,"Winter_Monday_close":null,"Winter_tuseday_close":null,"Winter_wednessday_close":null,"Winter_thursday_close":null,"Winter_friday_cloas":null,"Winter_saturday_close":null,"Winter_sunday_close":null,"Summer_Monday_close":null,"Summer_tuseday_close":null,"Summer_wednessday_close":null,"Summer_thursday_close":null,"Summer_friday_close":null,"Summer_saturday_close":null,"Summer_sunday_close":null,"Installationcharges":99.00}]');

$(document).ready(function () {
    Loader(1);
    $('.nav-item').removeClass('active');
    $('.nav-item').each(function(){
        if($(this).find('.nav-link').attr('href')=="/Stocklist")$(this).addClass('active');
    });
    $("#successfullsend").fadeOut(20000);
    $("#txtzipcode").val('');

    var mapOptions = {
        center: new google.maps.LatLng(0, 0),
        zoom: 15,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    var infoWindow = new google.maps.InfoWindow();
    var latlngbounds = new google.maps.LatLngBounds();
    var map = new google.maps.Map(document.getElementById("dvMap"), mapOptions);
    var lineCoordinates = [];

    if (markers.length > 0) {
        for (i = 0; i < markers.length; i++) {
            var data = markers[i]
            var myLatlng = new google.maps.LatLng(data.latitude.replace(',', '.'), data.longtitude.replace(',', '.'));
            var marker = new google.maps.Marker({
                position: myLatlng,
                map: map,
                icon: new google.maps.MarkerImage("http://maps.google.com/mapfiles/ms/icons/red.png")
            });

            latlngbounds.extend(marker.position);

            (function (marker, data) {
                google.maps.event.addListener(marker, "mouseover", function (e) {
                    infoWindow.setContent("<div><b>Name: </b>" + data.Merchant_Name + "</div>");
                    infoWindow.open(map, marker);
                });

                google.maps.event.addListener(marker, "mouseout", function (e) {
                    infoWindow.close();
                });

            })(marker, data);
        }
    }

    var bounds = new google.maps.LatLngBounds();
    //Center map and adjust Zoom based on the position of all markers.
    map.setCenter(latlngbounds.getCenter());
    map.fitBounds(latlngbounds);

});

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

function Bindzipcodedata() {
    Loader(0);
    var zipcode = $("#txtzipcode").val();
    var radious = $("#selectradious").val();

    $.ajax({
        url: 'https://tyc.azurewebsites.net/Stocklist/Zipcodedata',
        data: { zipcode: zipcode, postalcoderange: radious },
        beforeSend: function () { },
        success: function (response) {
            $('#bindallmapdata').empty();
            $('#bindallmapdata').append(response);
            Loader(1);
        }
    });
}