var signin_btn = document.querySelector('#submit');
var email = document.querySelector('#email');
var password = document.querySelector('#pass');
// hooking up the buttons and inputs 


signin_btn.addEventListener('click', () => {
    var email_value = email.value;
    var pass = sha256(password.value);
    // getting the email and the password(encoded)

    var xhr = new XMLHttpRequest();
    var form = new FormData();
    // creating objects of formdata and xhr 

    form.append('email', email_value);
    form.append('pass', pass);
    // appending the value of email and password to the formdata 

    xhr.open('POST', '/check_login');
    // connecting to the server 
    xhr.send(form);
    // sending the data 
    xhr.addEventListener('load', () => {
        var response = xhr.response;
        // getting the response 

        if (response == "success") {
            location.href = '/';
        } else {
            if (response == 'not found') {
                alert("check your email again");
            } else {
                alert("Check your password again");
                location.reload();
            }
            // handling the response 
        }
    });
});