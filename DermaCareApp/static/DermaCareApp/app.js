
let counts=setInterval(updated);
let counts2 = setInterval(updated);
let counts3 = setInterval(updated);
let counts4 = setInterval(updated);
let val=0;
let val2 = 2000;
let val3 = 2000;
let val4 = 0;
function updated(){
    var count= document.getElementById("num1");
    var count2 = document.getElementById("num2");
    var count3 = document.getElementById("num3");
    var count4 = document.getElementById("num4");
    count.innerHTML=++val;
    count2.innerHTML =++val2;
    count3.innerHTML = ++val3;
    count4.innerHTML = ++val4;
    if(val===880)
    {
        clearInterval(counts);
    }

    if(val2 === 2200){
        clearInterval(counts2);
    }
    if(val3 === 2300){
        clearInterval(counts3);
    }

    if(val4 === 278){
        clearInterval(counts4);
    }
}


function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
  }
  
function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
  }




