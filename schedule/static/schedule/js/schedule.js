coursePicker = $('#course-picker1');
newButton = $('#new');
deleteButton = $('#delete');

$(document).ready(function () {
    coursePicker.show();
    getSubjectAreas();
    // $('select#subject-area-select').change(function() {
    //     let subjectArea = $(this).children('option:selected').val();
    //
    //     return $.ajax({
    //        url: '/api/'
    //     });
    // });
});

newButton.click(function () {
    coursePicker.clone().insertAfter(coursePicker);
});

function getSubjectAreas() {
    return $.ajax({
        url: '/api/subject-area',
        success: function (result) {
            for (let sa of result.results) {
                $('select#subject-area-select').append(new Option(sa.short + ' - ' + sa.long, sa.short));
            }
        }
    });
}
