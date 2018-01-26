$('.answers').click(function() {
    $(this).select();
}); // $('.answers').each(function() { ... });

$('#submit').click(function() {
    $(this).attr('data-toggle', 'modal')
    $(this).attr('data-target', '#message')
    var results = { name:null, answers:{} };
    var empty = null;
    $('.answers').each(function() {
        var id = $(this).attr('id');
        var value = $(this).val().trim();
        if (value === '' && !empty) {
            empty = id;
        } // if (value === '' && !empty)
        results.answers[id] = value;
    }); // $('.answers').each(function() { ... });
    if (empty) {
        $(this).attr('data-toggle', '')
        $(this).attr('data-target', '')
        $('#' + empty).attr('placeholder', 'This field shouldn\'t be empty');
        $('#' + empty).focus();
        return ;
    } // if (empty)
    results.name = $('#name').val().trim();
    $.ajax({
        url:        './',
        type:       'POST',
        data:       results,
        success: function(response) {
            $('#response').text(response.post_status)
        },
        error: function(xhr, errmsg, err) {
            $('#response').text(xhr.status + ': ' + xhr.responseText)
        }
      }); // $.ajax({ ... });
}); // $('#submit').click(function() { ... });

$('#message').on('show.bs.modal', function () {
    setTimeout(function(){
        $('#message').modal('hide');
    }, 3000);
}); // $('#message').on('show.bs.modal', function () { ... });
