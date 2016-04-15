
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


function register()
{
    var avatar = "data:image/png;base64,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";

    /*
    var data = {
        'display_name' : 'Demo AJAX', 'password' : 'ajax12345', 'email' : 'demo@ajax.com',
        'avatar' : avatar, 'phone' : '50688164043',
        'address_name' : 'casa', 'address' : 'Calle #3 calí',
        'os' : 'android', 'latitude' : '17.25655', 'longitude' : '-12.52456'
    }
    */

    var latitude = 40.75793;
    var longitude = -72.98551;

    var data = {

    "name": "somename",
    "email": "some@some.com",
    "avatar": "data:image/gif;base64,R0lGODlhEAAQAMQAAORHHOVSKudfOulrSOp3WOyDZu6QdvCchPGolfO0o/XBs/fNwfjZ0frl3/zy7////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAkAABAALAAAAAAQABAAAAVVICSOZGlCQAosJ6mu7fiyZeKqNKToQGDsM8hBADgUXoGAiqhSvp5QAnQKGIgUhwFUYLCVDFCrKUE1lBavAViFIDlTImbKC5Gm2hB0SlBCBMQiB0UjIQA7",
    "phone": '506896055',
    "address.name": "some",
    "address.address": "some address",
    "address.latitude": latitude,
    "address.longitude": longitude,
    "os": "Android"
    }

    //This method add the csrftoken to the headers of the POST Request
    $.ajaxSetup({
        headers: { "X-CSRFToken": getCookie("csrftoken") }
    });

    $.ajax({
        data: data,
        url: "/api/v1/users/",
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
