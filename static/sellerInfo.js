$(document).ready(setup);

function setup(){
    parseForm();
}

//Parse form input
function parseForm(){
    $("#submitButton").click(function(){
        firstname = document.getElementById("firstname").value.toLowerCase();
        lastname = document.getElementById("lastname").value.toLowerCase();
        caseID = document.getElementById("caseID").value.toLowerCase();
        email = document.getElementById("email").value.toLowerCase();
        checkInput(firstname, lastname, caseID, email);
    });
}

//Error checking for invalid input
function checkInput(firstname, lastname, caseID, email){
  if (firstname == ""){
    $("#firstnameErr").html("Please enter a first name<br>");
  }
  if (lastname == ""){
    $("#lastnameErr").html("Please enter a last name<br>");
  }
  if (caseID == ""){
    $("#idErr").html("Please enter a valid case ID <br>");
  }
  if (email == ""){
    $("#emailErr").html("Please enter a valid email<br>");
  }
}

//Send data to python code
