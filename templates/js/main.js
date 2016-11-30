var mymap = L.map('mapid').setView([51.505, -0.09], 13);

var osmUrl='http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
var osmAttrib='Map data © <a href="http://openstreetmap.org">OpenStreetMap</a> contributors';
var osm = new L.TileLayer(osmUrl, {minZoom: 8, maxZoom: 12, attribution: osmAttrib});

mymap.addLayer(osm);

var height = $(window).height();
$('#mapid').css("height",height);
