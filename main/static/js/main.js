function checkSize(){
    if ($(window).width() < 1120) {
        $("#wrapper").addClass("toggled");
        $(".menu-toggle").css("display","block");

    }

    else {
        $("#wrapper").removeClass("toggled");
        $(".menu-toggle").css("display","none");
    }

};

$(document).ready(function(){
    $('#page-content').fadeIn(300);
    $('.sidebar-nav a').each(function() {
      linklocation = this.href + '/';
      pageurl = window.location.href;
      if (linklocation === pageurl) {
         $(this).addClass('active');
        }
    });
    checkSize();

});

$(window).resize(checkSize);



$('.sidebar-nav a').click(function(e) {
	e.preventDefault();
	linklocation = this.href + '/';
	pageurl = window.location.href;
  if (linklocation === pageurl) {

  }

  else {
      $("#page-content").fadeOut(300, redirectPage);
  };

  function redirectPage() {
      var stop = linklocation.lastIndexOf('/')
      window.location = linklocation.substr(0,stop);
  };

});


