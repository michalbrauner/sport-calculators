$( document ).ready(function() {

    $('#calculator-running form').on('submit', function(e) {
        e.preventDefault();

        $.post($(this).attr('action'), $(this).serialize(), function(response) {
            console.log(response);
        });

        return false;

    });
});
