function accept(){
    var delCookieDiv = document.querySelector(".cookies");
    delCookieDiv.remove();
}

function changeTemp(unit) {
    //creates an array and the array contains all the elements in .tempNum and for every array we'll traverse to see what to do if its F or C and will 
    var tempArr = document.querySelectorAll(".tempNum");
    console.log(tempArr);
    for (var i =0; i<tempArr.length;i++){
        var temp = parseFloat(tempArr[i].innerText);
        if(unit ==="F"){
            temp = ((temp* 9/5) +32);
        }
        else{
            temp = ((temp-32)*(5/9));
        }
        tempArr[i].innerText = Math.round(temp);
    }
}