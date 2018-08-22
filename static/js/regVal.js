<!--Validation JS-->
var isValid = false;

function validate() {

    var alpha = /^[A-Za-z]+$/;
    var email =
        /^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$/;

    var firstValid = false;
    var lastValid = false;
    var emailValid = false;

    var inpObj = document.getElementById('id_first');
    var lastObj = document.getElementById('id_last');
    var emailObj = document.getElementById('id_email');

    var errorSection = document.getElementById('errorSection')
    errorSection.innerHTML = '';

    //     ---------FIRST NAME VALIDITY CHECK---------
    //Check validity of first name
    if (!inpObj.checkValidity()) {
        //display error
        errorSection.innerHTML += '<span style="color:red">Enter first name.</span><br>';
        //set bool to false so form will not submit
        firstValid = false;
    } else if (!inpObj.value.match(alpha)) {
        //display error for entering an invalid first name
        errorSection.innerHTML += '<span style="color:red">Enter valid first name.</span><br>';
        //set bool to false so form will not submit
        firstValid = false;
    } else {
        //set true so form will submit
        firstValid = true;
        //remove error
    }
    //     ---------FIRST NAME VALIDITY CHECK ENDS---------


    //     ---------LAST NAME VALIDITY CHECK---------
    //Check validity of last name
    if (!lastObj.checkValidity()) {
        //set error field to error
        errorSection.innerHTML += '<span style="color:red">Enter last name.</span><br>';
        //set bool so form will not submit
        lastValid = false;
    } else if (!lastObj.value.match(alpha)) {
        //display error in error field if non-alpha characters are used
        errorSection.innerHTML += '<span style="color:red">Enter valid last name.</span><br>';
        //set bool to false to form will not submit
        lastValid = false;
    } else {
        //if all is valid set bool to true so form will submit
        lastValid = true;
        //clear error field
    }
    //     ---------LAST NAME VALIDITY CHECK ENDS---------


    //     ---------EMAIL VALIDITY CHECK---------
    //check validity of email input (is it an email address)
    if (!emailObj.checkValidity()) {
        //if invalid set error section to display error
        errorSection.innerHTML += '<span style="color:red">Enter valid email.</span><br>';
        //set test bool to false
        emailValid = false;
    } else if (!emailObj.value.match(email)) {
        errorSection.innerHTML += '<span style="color:red">Enter valid email.</span><br>';
        emailValid = false;
    } else {
        // else set to true
        emailValid = true;
        //reset error
    }
//     ---------EMAIL VALIDITY CHECK ENDS---------

//     ---------FINAL VALIDITY CHECK---------
//If all required fields are filled then set isValid to true and allow to form to submit
    if ((firstValid && lastValid && emailValid)) {
        //set isValid to true
        isValid = true;
    }

    return isValid;
}