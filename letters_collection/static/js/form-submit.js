$(document).ready(function () {
    $('.form-submit').parent('.form-group').addClass('submit submit-not-active');
    $('.form-submit').focus(function () {
        $(this).parent('.form-group.submit').removeClass('submit-not-active').addClass('submit-active');
    });
    $('.form-submit').blur(function () {
        $(this).parent('.form-group.submit').removeClass('submit-active').addClass('submit-not-active');        
        if ($(this).val() !== '') {
            $(this).parent('.form-group.submit').removeClass('submit-not-active').addClass('submit-filled-in');
        } else {
            $(this).parent('.form-group.submit').removeClass('submit-filled-in').addClass('submit-not-active');
        }
    });
});