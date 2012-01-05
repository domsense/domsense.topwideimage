$(document).ready(function(){

    $('.slideshow-enabled ul.tabs').tabs('div.wideimage', {
        // enable "cross-fading" effect
        effect: 'fade',
        fadeInSpeed: 500,
        fadeOutSpeed: 500,

        // start from the beginning after the last tab
        rotate: true,

    // use the slideshow plugin. It accepts its own configuration
    }).slideshow({
        autoplay: true,
        interval: 4000,
    });

});