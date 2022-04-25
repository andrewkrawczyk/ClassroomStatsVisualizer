$(function () {

    $('.js-create-student').click(function () {
        $.ajax({
            url: '/student/create/',
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $('#student-modal').modal('show');
            },
            success: function (data) {
                $('#student-modal .modal-content').html(data.html_form);
            }
        });
    });

    $('#student-modal').on('submit', '.js-student-create-form', function () {
        var form = $(this);
        $.ajax({
            url: form.attr('action'),
            data: form.serialize(),
            type: form.attr('method'),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $('#student-modal').modal('hide');
                } else {
                    $('#student-modal .modal-content').html(data.html_form);
                }
            }
        });
        return false;
    });
});