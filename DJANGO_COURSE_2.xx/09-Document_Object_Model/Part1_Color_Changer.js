// Alright so we've discussed the way you can grab html elements, let's
// see how we can interact with them in Javascript!

// Type this into your console:

// Grab the Header with h1
var header = document.querySelector("h1")
var p=document.querySelector("#click")
var t=document.querySelector("#text")
var headone=document.querySelector("#one")
var headtwo=document.querySelector("#two")
var headthree=document.querySelector("#three")
// Then you can interface with the object.

// Interface with the style.
//You will see a ton of options show up!
header.style.color = 'red'

headtwo.addEventListener("mouseover",function(){
  //headtwo.textContent="Mouse currently over"
  headtwo.style.color="blue"
})
headtwo.addEventListener("mouseout",function(){
//headtwo.textContent="This is header 2"
headtwo.style.color="black"
})
 headthree.addEventListener("click",function(){
   headthree.textContent="i am clicked"
 })
// Now let's connect it to the script to
// change it once every second to a random color!

// Random Color Function:

// http://stackoverflow.com/questions/1484506/random-color-generator-in-javascript
function getRandomColor(){
  var letters = "0123456789ABCDEF";
  var color = '#';
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random()*16)];
  }
  return color
}

// Simple function for clarity
function changeHeaderColor(){
  colorInput = getRandomColor()
  header.style.color = colorInput;

}
function change_text_color(){
  clinput=getRandomColor()
  p.style.color= clinput;
  alert("i am clicked")
}
// Now perform the action over intervals (milliseocnds):
setInterval("changeHeaderColor()",500);
// setInterval("change_text_color()",300);
p.addEventListener("click",change_text_color)

// function to execute enter button as send button.

t.addEventListener("keyup",function(event){
  if (event.keyCode === 13) {
      event.preventDefault();
       p.click()
  }
})




// headone.addEventListener("mouseover",hoverin(headone))
