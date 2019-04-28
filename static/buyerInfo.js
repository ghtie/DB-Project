$(document).ready(setup);

function setup(){
    parseForm();
}

//Parse form input
function parseForm(){
    $("#submitButton").click(function(){
        name = document.getElementById("name").value.toLowerCase();
        checkInput(name);
    });
}

//Error checking for invalid input
function checkInput(name){
  if (name == ""){
    $("#nameErr").html("Please enter a Case ID<br>");
  }
}

//Send data to python code
