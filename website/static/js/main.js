$(document).ready(function() {

    if($(window).width() < 800) {
        $('.navbar .nav_menu_button .button_image').attr('src', '../static/img/menu_dark_medium.png');
        }

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

    /*$('.portfolio_project').hover(function() {
        $(this).css('width', '+=10px');
        $(this).css('height', '+=10px');
        $('.project_background', this).css('margin-top', '+=5px');
        $('.project_background', this).css('margin-left', '+=5px');
    }, function() {
        $(this).css('width', '-=10px');
        $(this).css('height', '-=10px');
        $('.project_background', this).css('margin-top', '-=5px');
        $('.project_background', this).css('margin-left', '-=5px');
    });*/

    /*$('.Cv_Button a div, .Score_Predictor a div').hover(function() {
        $(this).css('font-size', '+=2px');
        $(this).css('color', '#006767');
        $(this).css('background-color', '#003636');
    }, function() {
        $(this).css('font-size', '-=2px');
        $(this).css('color', '#003636');
        $(this).css('background-color', '#3E7F7F');
    });

    $('.Projects_Menu').hover(function() {
        $(this).css('font-size', '+=1px');
        $(this).css('color', '#006767');
        $(this).css('background-color', '#003636');
        $('.Projects_List').finish().slideDown('medium');
        }, function() {
        $(this).css('font-size', '-=1px');
        $(this).css('color', '#003636');
        $(this).css('background-color', '#3E7F7F');
        $('.Projects_List').finish().slideUp('slow');
    });

    $('.Project').hover(function() {
        $(this).css('font-size', '+=1px');
        $(this).css('color', '#006767');
        $(this).css('background-color', '#003636');
        }, function() {
        $(this).css('font-size', '-=1px');
        $(this).css('color', '#003636');
        $(this).css('background-color', '#3E7F7F');});*/
});
