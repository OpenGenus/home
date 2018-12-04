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

  //For searchbox in school list and intern list page
  $( "#search-button" ).click(function() {
    if( $( '#search-query' ).val() == "" ){
      $( '#search-query' ).css('border', '1px solid red');
      return false;
    }
    var page = $(this).data( "page" );
    window.location = '/' + page + '/search/' + $( "#search-query" ).val();
  });
  $('#search-query').keydown(function(event){
    $( '#search-query' ).css('border', 'unset');
    var keyCode = (event.keyCode ? event.keyCode : event.which);
    if (keyCode == 13) {
        $('#search-button').trigger('click');
    }
  });
});
