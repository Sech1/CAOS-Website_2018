<!--Validation JS-->
var isValid = false;

function regCheck(object, errorMsg, errorMsg2, regEx) {
    var valid = false;
    if (!object.checkValidity()) {
        //if invalid set error section to display error
        errorSection.innerHTML += errorMsg;
        //set test bool to false
        valid = false;
    } else if (!object.value.match(regEx)) {
        errorSection.innerHTML += errorMsg2;
        valid = false;
    } else {
        // else set to true
        valid = true;
        //reset error
    }
    return valid;
}

function validate() {

    var alpha = /^[A-Za-z]+$/;
    var email =
        /^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$/;

    var inpObj = document.getElementById('id_first');
    var lastObj = document.getElementById('id_last');
    var emailObj = document.getElementById('id_email');

    var firstValid = false;
    var lastValid = false;
    var emailValid = false;

    var errorSection = document.getElementById('errorSection')
    errorSection.innerHTML = '';

    var firstEmpty = '<span style="color:red">Enter first name.</span><br>';
    var firstInvalid = '<span style="color:red">Enter valid first name.</span><br>';
    var lastEmpty = '<span style="color:red">Enter last name.</span><br>';
    var lastInvalid = '<span style="color:red">Enter valid last name.</span><br>';
    var emailEmpty = '<span style="color:red">Enter valid email.</span><br>';

    //     ---------FIRST NAME VALIDITY CHECK---------
    //Check validity of first name
    firstValid = regCheck(inpObj, firstEmpty, firstInvalid, alpha);
    //     ---------FIRST NAME VALIDITY CHECK ENDS---------


    //     ---------LAST NAME VALIDITY CHECK---------
    //Check validity of last name
    lastValid = regCheck(lastObj, lastEmpty, lastInvalid, alpha);
    //     ---------LAST NAME VALIDITY CHECK ENDS---------


    //     ---------EMAIL VALIDITY CHECK---------
    //check validity of email input (is it an email address)
    emailValid = regCheck(emailObj, emailEmpty, emailEmpty, email);
//     ---------EMAIL VALIDITY CHECK ENDS---------

//     ---------FINAL VALIDITY CHECK---------
//If all required fields are filled then set isValid to true and allow to form to submit
    if ((firstValid && lastValid && emailValid)) {
        //set isValid to true
        isValid = true;
    }
    return isValid;
}