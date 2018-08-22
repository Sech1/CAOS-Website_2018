<!--Validation JS-->
var isValid = false;

function validate() {

    var alpha = /^[A-Za-z]+$/;

    var firstValid = false;
    var lastValid = false;
    var emailValid = false;

    var inpObj = document.getElementById('id_first');
    var lastObj = document.getElementById('id_last');
    var emailObj = document.getElementById('id_email');

    document.getElementById('errorSection').innerHTML += '';

    //     ---------FIRST NAME VALIDITY CHECK---------
    //Check validity of first name
    if (!inpObj.checkValidity()) {
        //if no name is entered change placeholder
        inpObj.setAttribute("placeholder", "Required Field - Please enter first name");
        //display error
        document.getElementById('errorSection').innerHTML += '<span style="color:red">Enter first name.</span><br>';
        //set bool to false so form will not submit
        firstValid = false;
    } else if (!inpObj.value.match(alpha)) {
        //display error if user enters non-accepted characters
        inpObj.setAttribute("placeholder", "Please only use alpha numeric characters");
        //display error for entering an invalid first name
        document.getElementById('errorSection').innerHTML += '<span style="color:red">Enter valid first name.</span><br>';
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
        //if no name is entered change placeholder
        lastObj.setAttribute("placeholder", "Required Field - Please enter last name");
        //set error field to error
        document.getElementById('errorSection').innerHTML += '<span style="color:red">Enter last name.</span><br>';
        //set bool so form will not submit
        lastValid = false;
    } else if (!lastObj.value.match(alpha)) {
        //if user enters non-alpha chars change placeholder
        inpObj.setAttribute("placeholder", "Please only use alpha numeric characters");
        //display error in error field if non-alpha characters are used
        document.getElementById('errorSection').innerHTML += '<span style="color:red">Enter valid last name.</span><br>';
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
        //check if email is valid - if not set placeholder to hint
        emailObj.setAttribute("placeholder", "Required Field - Please enter email");
        //if invalid set error section to display error
        document.getElementById('errorSection').innerHTML = '<span style="color:red">Enter valid email.</span><br>';
        //set test bool to false
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