var fullname= 'Raz Berejik '
console.log(fullname) ;

function validEmail(){
    let obj=document.getElementById('email');
    let emailOK=obj.checkValidity();
    if (emailOK) {
    document.getElementById('emailvaild').innerHTML= 'OK';
    alert(" email is valid");
    }
    else{
        document.getElementById('emailvaild').innerHTML= 'enter valid email';
    }

}
