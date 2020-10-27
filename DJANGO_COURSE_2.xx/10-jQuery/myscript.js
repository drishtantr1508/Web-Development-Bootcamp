$('h1').click(function(){
  console.log("there was a click")
  $(this).css('color','red')
  $(this).text("red")
})
$('input').eq(0).keypress(function(event){
  if (event.which===13){
    $('input').eq(1).click()
    console.log("submit button is clicked");
  }
})
function click_submit(){

}
