if($(window).width() < 800) {
        $('.navbar .nav_menu_button .button_image').attr('src', '../static/img/menu_dark_medium.png');
        }
else {
    $('.navbar .nav_menu_button .button_image').attr('src', '../static/img/menu_dark.png');
        }

$(document).ready(function() {

    $('a[href^="#"]').on('click', function (e) {
        e.preventDefault();

        var target = this.hash;
        var $target = $(target);

        $('html, body').stop().animate({
            'scrollTop': $target.offset().top
            }, 750, 'swing');
        });

    $('.navbar').click(function() {
        if ($(this).hasClass('expanded')){
            $(this).animate({height: '85px'});
            }
        else {
            $(this).animate({height: '115vh'});
            }
        $(this).toggleClass('expanded');
        $('.navbar .Title').toggleClass('expanded');
        $('.navbar .Cv_Button').toggleClass('expanded');
        $('.navbar .Projects_Menu').toggleClass('expanded');
        $('.navbar .nav_options').toggleClass('expanded');
        $('.navbar .nav_menu_button').toggleClass('expanded');
        });

    $('.navbar').hover(function() {

        if ($(window).width() < 800) {
            $('.navbar .nav_menu_button .button_image').attr('src', '../static/img/menu_light_medium.png');
        }
        else {
            $('.navbar .nav_menu_button .button_image').attr('src', '../static/img/menu_light.png');
        }
    }, function() {
        if ($(window).width() < 800) {
            $('.navbar .nav_menu_button .button_image').attr('src', '../static/img/menu_dark_medium.png');
        }
        else {
            $('.navbar .nav_menu_button .button_image').attr('src', '../static/img/menu_dark.png');
        }
    });

    var index = 0;
    var delay = 2250;
    var fade = 400;
    var index_max = $(".spacer--content li").length -1;

	function cycleSpacer(){
	        $(".spacer--content li:eq(" + index + ")")
	            .animate({"opacity" : "1"}, fade)
	            .animate({"opacity" : "1"}, delay)
	            .animate({"opacity" : "0"}, fade, function(){
	                (index == index_max) ? index=0 : index++;
	                    cycleSpacer();
	                });
	         };

	 cycleSpacer();

    $('.portfolio_project').hover(function() {
        $(this).find('.project_button').css('visibility', 'visible');
    }, function() {
        $(this).find('.project_button').css('visibility', 'hidden');
    });

    $('.modal_button').hover(function() {
        $(this).find('.modal_title').css('color', 'rgb(51, 122, 183)')
    }, function() {
        $(this).find('.modal_title').css('color', 'rgb(255, 255, 255)')
    });
});
