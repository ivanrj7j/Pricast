const signup = document.querySelector('#signup');
// hooking up the signup button 

signup.addEventListener('click', () => {
    let name = document.querySelector('#name').value;
    // hooking up the name 
    let email = document.querySelector('#email').value;
    // hooking up the email  
    let password = sha256(document.querySelector('#password').value);
    // getting and encrypting the password 

    const xhr = new XMLHttpRequest();
    const data = new FormData();
    // creating the XMLHttpRequest and FormData Object 

    data.append('name', name);
    data.append('email', email);
    data.append('pass', password);
    // appending the data 

    xhr.open('POST', '/add_member');
    // connecting to the register 
    xhr.send(data);
    // sending the data to backend 
    xhr.addEventListener('load', ()=>{
        let response = xhr.response;
        if (response == 'o') {
            window.open('/');
        }
        else{
            if(response == 't'){
                alert("Email is already taken");
                location.reload()
            }else{
                alert("Something went wrong");
                location.reload()
            }
        }
    });
});
