// alert("hello");
var gamePattern = [];
var buttonColours = ["red", "blue", "green", "yellow"];
function nextSequence() {
  var randomNumber = Math.random();
  randomNumber *= 3;
  randomNumber = Math.floor(randomNumber) + 1;
  return randomNumber;
}
var randomChosenColour = buttonColours[nextSequence()];
gamePattern.push(randomChosenColour);
$(document).ready(() => {
  setInterval(() => {
    $("#" + randomChosenColour).fadeIn();
    $("#" + randomChosenColour).fadeOut();
  }, 300);
});

console.log("sounds/" + randomChosenColour + ".mp3");
var x = new Audio("sounds/" + randomChosenColour + ".mp3");
x.play();
