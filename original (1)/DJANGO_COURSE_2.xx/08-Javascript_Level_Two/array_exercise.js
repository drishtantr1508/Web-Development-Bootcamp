if(prompt("Would you like to start the roster web app? y/n")==='y'){
  running=true
}else{
  running=false
}
array=[]
while (running){
      var option=prompt("Type in 'add', 'remove','display' or 'quit' to perform  name action.")
      if (option==="add"){
        array.push(prompt("Type in the name you want to add."))
      }else if (option==="remove") {
        array.splice(array.indexOf(prompt("Type in the name you want to remove.")),1)
      }else if (option==="display"){
        console.log(array)
      }else if (option==="quit") {
        running=false
      }else{
        running=true
      }
}
alert("Thanks for using the webpage rooster.")
