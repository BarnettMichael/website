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
            $(this).animate({height: '10vh'});
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

    $('.portfolio_project').hover(function() {
        $(this).find('.project_button').css('visibility', 'visible');
    }, function() {
        $(this).find('.project_button').css('visibility', 'hidden');
    });
});
