$(document).ready(setup);

function setup(){
    parseForm();
}

var error = false;
//Parse form input
function parseForm(){
    $("#submitButton").click(function(){
        firstname = document.getElementById("firstname").value.toLowerCase();
        lastname = document.getElementById("lastname").value.toLowerCase();
        caseID = document.getElementById("caseID").value.toLowerCase();
        email = document.getElementById("email").value.toLowerCase();

        if (checkInput(firstname, lastname, caseID, email) == false){
          sendSellerInfo();
        }
    });
}

//Error checking for invalid input
function checkInput(firstname, lastname, caseID, email){
  if (name == ""){
    $("#lastnameErr").html("Please enter a last name<br>");
    error = true;
  }
  if (caseID == ""){
    $("#idErr").html("Please enter a valid case ID <br>");
    error = true;
  }
}

function sendSellerInfo(){
    $.getJSON($SCRIPT_ROOT + '/_add_seller_info', {
        name: name,
        id: id
      }, function(data) {
        $("#result").text(data.result);
      });
}
//Send data to python code
