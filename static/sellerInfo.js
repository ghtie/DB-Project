$(document).ready(setup);

function setup(){
    parseForm();
}

var error = false;
var name = "";
var email = "";
//Parse form input
function parseForm(){
    $("#submitButton").click(function(){
        name = document.getElementById("name").value.toLowerCase();
        caseID = document.getElementById("caseID").value.toLowerCase();

        if (checkInput(name, caseID) == false){
          sendSellerInfo();
        }
    });
}

//Error checking for invalid input
function checkInput(name, caseID){
  if (name == ""){
    $("#nameErr").html("Please enter a name<br>");
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
