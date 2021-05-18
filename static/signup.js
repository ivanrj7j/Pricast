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
});
