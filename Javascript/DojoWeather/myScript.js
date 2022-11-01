function loading(element) {
    alert('Loading weather report...');
}

function chooseType(element){
    var celsius;
    var fahrenheit;
    if (element.value == '°F')
    {
        console.log(1);
        var temp=document.querySelectorAll("#temp");
        var fahrenheit=[];
        var celsius=[];
        for (var i=0; i<temp.length; i++){
            celsius[i] = temp[i].innerHTML;
            celsius[i] = celsius[i].substring(0,celsius[i].length-1);
            fahrenheit[i] = convertCtoF(celsius[i]);
            temp[i].innerHTML = fahrenheit[i] + "°";
        }
    }
    else if (element.value == '°C')
    {
        console.log(2);
        var temp=document.querySelectorAll("#temp");
        var fahrenheit=[];
        var celsius=[];
        for (var i=0; i<temp.length; i++){
            fahrenheit[i] = temp[i].innerHTML;
            fahrenheit[i] = fahrenheit[i].substring(0,fahrenheit[i].length-1);
            celsius[i] = convertFtoC(fahrenheit[i]);
            temp[i].innerHTML = celsius[i] + "°";
        }
    }
}

function convertFtoC(temp){
    temp = Math.round((temp - 32) * 5 / 9);
    return temp;
}

function convertCtoF(temp){
    temp = Math.round((temp * 9 / 5) + 32);
    return temp;
}

function closeMessage(element){
    removeFadeOut(element, 2000);
}

function removeFadeOut( el, speed ) {
    var seconds = speed/1000;
    el.style.transition = "opacity "+seconds+"s ease";
    el.style.opacity = 0;
    setTimeout(function() {
        el.remove();
    }, speed);
}