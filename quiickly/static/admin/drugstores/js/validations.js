
function getId(id) {
    let selector = document.getElementById(id);
    return selector;
}

function ajax(type,url,body,headers)
{
    let ajax = new XMLHttpRequest();
    ajax.onreadystatechange = function(response) {
        if (ajax.readyState == 4 && ajax.status == 200)
        {
            return response;
        }
        return "The server doesn't acept the request";
    };

    ajax.open(type, url, true);

    headers.forEach(function(header) {
        ajax.setRequestHeader(header.header_name, header.header_value);
    });

    /*
    let data = new FormData();

    for (let key in body)
    {
        data.append(key, body[key]);
    }
    */

    if (type == "POST")
    {
        ajax.send(body);
    }
    else
    {
        ajax.send();
    }
}

var login_click    = getId("submit-login").addEventListener("click", validate_login);
var email_enter    = getId("input-email").addEventListener("keypress", enter_submit);
var password_enter = getId("input-password").addEventListener("keypress", enter_submit);

// This event each enter and call validate_login to validate this
function enter_submit()
{
    if(event.keyCode == 13){
        validate_login();
    }
}

function validate_login()
{
    let email_filter = /[\w-\.]{1,25}@([\w-]{2,25}\.)*([\w-]{2,}\.)[\w-]{2,4}/;
    let email    = getId("input-email");
    let email_value = email.value;
    let password = getId("input-password");
    let password_value = password.value;
    let notification_box = getId("notification-box");
    email_value = email_value.replace(/\s\s+/g, ' ');

    console.log("entró");

    if(email_filter.test(email_value) && !email_value.startsWith(" "))
    {
        email.classList.remove("input-error");
        notification_box.classList.remove("box-error");
        notification_box.innerText = "";

        if(isNaN(password_value) && !password_value.startsWith(" "))
        {
            password.classList.remove("input-error");
            notification_box.classList.remove("box-error");
            notification_box.innerText = "";
            login(email_value,password_value);
        }
        else
        {
            password.classList.add("input-error");
            notification_box.innerText = "contraseña mal escrito";
            notification_box.classList.add("box-error");
        }
    }
    else
    {
        email.classList.add("input-error");
        notification_box.innerText = "Correo mal escrito";
        notification_box.classList.add("box-error");
    }
}


/*
function login(email,password)
{
    let data = { "email" : email, "password" : password};

    let headers = [
        {"header_name" : "X-CSRFToken", "header_value" : getCookie("csrftoken") },
        {"header_name" : "Content-Type", "header_value" : 'application/json' },
        {"header_name" : "X-Requested-With", "header_value" : 'XMLHttpRequest' }
    ];

    let ajax_response = ajax("POST","/login/",data,headers);

    console.log(ajax_response);
}
*/



function login(email,password)
{
    let data = { "email" : email, "password" : password }

    //This method add the csrftoken to the headers of the POST Request
    $.ajaxSetup({
        headers: { "X-CSRFToken": getCookie("csrftoken") }
    });

    $.ajax({
        data: data,
        url: "/login/",
        type: "POST",
        beforeSend: function()
        {
        },
        success: function(response)
        {
            var response = JSON.parse(response);

            console.log(response)

            if(response.status_login == 'success')
            {
                window.location.assign("/droguerias/")
            }
            else if(response.status_login == 'error')
            {
            }
            else
            {
            }
        },
        error: function()
        {
        }
    });
}


//This function get the value of the cookie csrftoken generated for Django and return the value
function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i=0; i<ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1);
        if (c.indexOf(name) == 0) return c.substring(name.length,c.length);
    }
    return "";
}
