(function ($) {
	"use strict";


      // Sticky Menu
      $(window).on('scroll',function() {
          var scroll = $(window).scrollTop();
          if (scroll >= 10) {
              $(".header-area").addClass("sticky");
          } else {
              $(".header-area").removeClass("sticky");
          }
      });

      //Type js
      var element = $(".element");
        $(function () {
            element.typed({
                strings: ["AWESOME", "amazing"],
                typeSpeed: 250,
                loop: true,
            });
        });


      // Smooth scroll
      $(function() {
        $('a[href*="#"]:not([data-toggle="tab"])').on('click', function() {
         if (location.pathname.replace(/^\//, '') === this.pathname.replace(/^\//, '') && location.hostname === this.hostname) {
             var target = $(this.hash);
             var headerH = '70' ;
             target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
             if (target.length) {
                 $('html, body').animate({
                     scrollTop: target.offset().top - headerH + "px"
                 }, 1000);
                 return false;
             }
         }
       });
     });



      // Magnific Popup gallery
      $('.popup-gallery').magnificPopup({
      delegate: 'a', // child items selector, by clicking on it popup will open
      gallery: {
        enabled: true
      },
      type: 'image'
      // other options
      });
      

      //Mixitup
      $('.work-mixi').mixItUp();


      // Slicknav
      $('#traffic-menu').slicknav({
    
       prependTo:'#mobile-menu-wrap'

      });



      // Counter
/*     $('.counter').counterUp({
          delay: 10,
          time: 1000
      });*/

     

      // Contact Form
      
      // Get the form.
      var form = $('#contact-form');

      // Get the messages div.
      var formMessages = $('.form-message');

      // Set up an event listener for the contact form.
      $(form).on('submit',function(e) {
        // Stop the browser from submitting the form.
        e.preventDefault();

        // Serialize the form data.
        var formData = $(form).serialize();

        // Submit the form using AJAX.
        $.ajax({
          type: 'POST',
          url: $(form).attr('action'),
          data: formData
        })
        .done(function(response) {
          // Make sure that the formMessages div has the 'success' class.
          $(formMessages).removeClass('error');
          $(formMessages).addClass('success');

          // Set the message text.
          $(formMessages).text(response);

          // Clear the form.
          $('#contact-form input,#contact-form textarea').val('');
        })
        .fail(function(data) {
          // Make sure that the formMessages div has the 'error' class.
          $(formMessages).removeClass('success');
          $(formMessages).addClass('error');

          // Set the message text.
          if (data.responseText !== '') {
            $(formMessages).text(data.responseText);
          } else {
            $(formMessages).text('Oops! An error occured. Message could not be sent.');
          }
        });
      });


    jQuery(window).on('load',function(){
            //wow
            new WOW().init();
            window.wow = new WOW(
                {
                  boxClass:     'wow',      // default
                  animateClass: 'animated', // default
                  mobile:       true,       // default
                  live:         true,        // default
                  offset: 100
                }
            )
            window.wow.init();

        
    });


}(jQuery));	