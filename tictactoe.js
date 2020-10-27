var td=document.querySelectorAll("td")
var restart=document.querySelector("#b")
function clearboard(){
  for (var i=0;i<=8;i++){
    if (td[i].textContent==='X'||td[i].textContent==='O'){
      td[i].textContent=''
    }
  }
}
for (var i=0;i<=8;i++){
  console.log(td[i]);
}
restart.addEventListener('click',clearboard)

// function input_x(){
//
//
//   }
// }
for (var j=0;j<=8;j++){
  td[j].addEventListener('dblclick',function(){
    if (this.textContent===''||this.textContent==='X'){
      this.textContent='O'
    }
  }
)
}

for (var i=0;i<=8;i++){
  td[i].addEventListener('click',function(){
    if (this.textContent===''){
      this.textContent='X'
    }
  }
)
}
