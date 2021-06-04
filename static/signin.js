var signin_btn = document.querySelector('#submit');
var email = document.querySelector('#email');
var password = document.querySelector('#pass');


signin_btn.addEventListener('click', () => {
    var email_value = email.value;
    var pass = sha256(password.value);

    var xhr = new XMLHttpRequest();
    var form = new FormData();

    form.append('email', email_value);
    form.append('pass', pass);

    xhr.open('POST', '/check_login');
    xhr.send(form);
    xhr.addEventListener('load', () => {
        var response = xhr.response;

        if (response == "success") {
            location.href = '/';
        } else {
            if (response == 'not found') {
                alert("check your email again");
            } else {
                alert("Check your password again");
                location.reload();
            }

        }
    });
});