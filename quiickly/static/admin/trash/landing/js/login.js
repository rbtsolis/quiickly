function login(username,password)
{
               var data = {'email': 'userdemo@gmail.com','password': 'userdemo'};
               var csrftoken = getCookie('csrftoken');

               function csrfSafeMethod(method)
               {
                    // these HTTP methods do not require CSRF protection
                    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
               }

               //This method add the csrftoken to the headers of the POST Request
                $.ajaxSetup({
                    headers: { "X-CSRFToken": csrftoken }
                });

                // This other method send all the POST Request via AJAX
                $.ajax({
                    data: data,
                    url: "/login/",
                    type: "POST",
                    beforeSend: function(){
                    },
                    success: function(response)
                    {
                        console.log(response);
                    },
                    error: function(){
                    }
                });
}

//This function get the value of the cookie csrftoken generated for Django and return the value
function getCookie(name)
{
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
