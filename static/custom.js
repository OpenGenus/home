$(function () {
  $('a[href*="#"]:not([href="#"])').click(function (e) {
    var target = $(e.target.hash);

    if (target.length) {
      $('html, body').animate({
        scrollTop: target.offset().top
      }, 1000);

      return false;
    }
  });
});

//For faq accordion
$(document).ready(function(){
	$(".box").click(function(){
	  $(this).next().slideToggle("fast");
	  $(this).find('i').toggle();
	});

});
