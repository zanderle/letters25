$(document).ready(function () {
    $('.form-submit').parent('.form-group').addClass('submit submit-not-active');
    $('.form-submit').each(function () {
        if ($(this).val() !== '') {
            $(this).parent('.form-group.submit').removeClass('submit-not-active').addClass('submit-filled-in');
        }
    });
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

    $('#letter-submission-form .submit-button').on('click', function(e) {
        e.preventDefault();
        var values = {};
        $.each($('#letter-submission-form').serializeArray(), function(i, field) {
            values[field.name] = field.value;
        });
        $('#submit-letter-modal').modal('show');
    });
    $('#letter-submission-form').on('submit', function() {
        $('#letter-submission-form input[type=submit]').hide();
        spinner = '<img src="/static/img/hourglass.gif" class="center-block" width="60px">'
        $('#letter-submission-form input[type=submit]').parent('div').append(spinner);
    });
});