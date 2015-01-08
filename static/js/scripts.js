
$(document).ready(function(){/* google maps -----------------------------------------------------*/
google.maps.event.addDomListener(window, 'load', initialize);

function initialize() {
  navigator.geolocation.getCurrentPosition(success, error, options);

  var options = {
    enableHighAccuracy: true,
    timeout: 5000,
    maximumAge: 0
  };
  var derivedlatitude, derivedlongitude, derivedaccuracy;

function success(pos) {
  var crd = pos.coords;
  derivedlatitude  = crd.latitude;
  derivedlongitude = crd.longitude;
  derivedaccuracy  = crd.accuracy;
};

function error(err) {
  console.warn('ERROR(' + err.code + '): ' + err.message);
};
  /* position According to navigator API system */
  var latlng = new google.maps.LatLng(17.99, 4.55);
  console.log(latlng);

  var mapOptions = {
    center: latlng,
    scrollWheel: false,
    zoom: 13,
    style: [{"featureType":"water","elementType":"geometry","stylers":[{"color":"#a2daf2"}]},{"featureType":"landscape.man_made","elementType":"geometry","stylers":[{"color":"#f7f1df"}]},{"featureType":"landscape.natural","elementType":"geometry","stylers":[{"color":"#d0e3b4"}]},{"featureType":"landscape.natural.terrain","elementType":"geometry","stylers":[{"visibility":"off"}]},{"featureType":"poi.park","elementType":"geometry","stylers":[{"color":"#bde6ab"}]},{"featureType":"poi","elementType":"labels","stylers":[{"visibility":"off"}]},{"featureType":"poi.medical","elementType":"geometry","stylers":[{"color":"#fbd3da"}]},{"featureType":"poi.business","stylers":[{"visibility":"off"}]},{"featureType":"road","elementType":"geometry.stroke","stylers":[{"visibility":"off"}]},{"featureType":"road","elementType":"labels","stylers":[{"visibility":"off"}]},{"featureType":"road.highway","elementType":"geometry.fill","stylers":[{"color":"#ffe15f"}]},{"featureType":"road.highway","elementType":"geometry.stroke","stylers":[{"color":"#efd151"}]},{"featureType":"road.arterial","elementType":"geometry.fill","stylers":[{"color":"#ffffff"}]},{"featureType":"road.local","elementType":"geometry.fill","stylers":[{"color":"black"}]},{"featureType":"transit.station.airport","elementType":"geometry.fill","stylers":[{"color":"#cfb2db"}]}]
  };
  
  var marker = new google.maps.Marker({
    position: latlng,
    url: '/',
    animation: google.maps.Animation.DROP
  });
  
  var map = new google.maps.Map(document.getElementById("map-canvas"), mapOptions);
  marker.setMap(map);

};
/* end google maps -----------------------------------------------------*/
});