function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$(document).ready(function() {
    $(".js-like-question").on("click", function() {
        var $this = $(this);
        $.ajax({
            url: "/like_question/",
            method: "POST",
            dataType: "json",
            data: {
                "question_id": $this.data("question_id"),
                "csrfmiddlewaretoken": getCookie("csrftoken")
            }
        }).done(function(data) {
            console.log(data);
            location.reload();
        });
        return false;
    });
});


$(document).ready(function() {
    $(".js-dislike-question").on("click", function() {
        var $this = $(this);
        $.ajax({
            url: "/dislike_question/",
            method: "POST",
            dataType: "json",
            data: {
                "question_id": $this.data("question_id"),
                "csrfmiddlewaretoken": getCookie("csrftoken")
            }
        }).done(function(data) {
            console.log(data);
            location.reload();
        });
        return false;
    });
});
