"use strict";
let text = document.getElementById('text');
let bird1 = document.getElementById('bird1');
let bird2 = document.getElementById('bird2');
let btn = document.getElementById('btn');
let rocks = document.getElementById('rocks');
let forest = document.getElementById('forest');
let water = document.getElementById('water');
let header = document.getElementById('header');
window.addEventListener('scroll', function () {
    let value = window.scrollY;
    text.style.top = 50 + value * -.1 + '%';
    bird2.style.top = value * -1.5 + 'px';
    bird2.style.left = value * 2 + 'px';
    bird1.style.top = value * -1.5 + 'px';
    bird1.style.left = value * -5 + 'px';
    btn.style.marginTop = value * 1.5 + 'px';
    rocks.style.top = value * -.12 + 'px';
    forest.style.top = value * .25 + 'px';
    header.style.top = value * .5 + 'px';
});

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showMap, showError);
    } else {
        document.getElementById("map").src = ""; // Efface le contenu de l'iframe
        document.getElementById("map-container").innerHTML = "La géolocalisation n'est pas supportée par ce navigateur.";
    }
  }
  
  
  function showMap(position) {
    var latitude = position.coords.latitude;
    var longitude = position.coords.longitude;
    var mapUrl = "https://www.openstreetmap.org/export/embed.html?bbox=" + (longitude - 0.01) + "%2C" + (latitude - 0.01) + "%2C" + (longitude + 0.01) + "%2C" + (latitude + 0.01) + "&amp;layer=mapnik";
    document.getElementById("map").src = mapUrl;
  }
  
  
  function showError(error) {
    document.getElementById("map").src = ""; // Efface le contenu de l'iframe
    
    switch(error.code) {
        case error.PERMISSION_DENIED:
            document.getElementById("map-container").innerHTML = "L'utilisateur a refusé la demande de géolocalisation.";
            break;
        case error.POSITION_UNAVAILABLE:
            document.getElementById("map-container").innerHTML = "Les informations de localisation ne sont pas disponibles.";
            break;
        case error.TIMEOUT:
            document.getElementById("map-container").innerHTML = "La demande de géolocalisation a expiré.";
            break;
        case error.UNKNOWN_ERROR:
            document.getElementById("map-container").innerHTML = "Une erreur inconnue s'est produite.";
            break;
    }
  }
