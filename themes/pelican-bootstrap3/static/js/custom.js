$(document).ready(function () {
  window.onscroll = function () {
    changeNavBackground();
  };

  var hamburgerIcon = $(".icon-bar");
  hamburgerIcon.click(function () {
    console.log("hamburger clicked");
  });

  $(".search-articles").focus(function () {
    $(this).removeClass("highlight");
    $(this).css("border-bottom, 2px solid #fff");
  });
});

// Get the offset position of the navbar
var sticky = $("#header").offsetTop;

// Add background to Navigation when scrolling
function changeNavBackground() {
  var $nav = $(".navbar-fixed-top");
  $nav.toggleClass("scrolled", $(this).scrollTop() > $nav.height());
}
