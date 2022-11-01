setInterval( function() {
    var seconds = new Date().getSeconds();
    var minutes = new Date().getMinutes();
    var hours = new Date().getHours();
    if (hours > 12){
        hours -= 12;
    }
    minutes = minutes * 60;
    hours = hours * 3600;    
    var secDegree = seconds * 6 + 180;
    var minDegree = ((minutes + seconds) / 10) + 180;
    var hourDegree = ((hours + minutes + seconds) / 120) + 180;
    var secondsHand = document.querySelector("#seconds");
    secondsHand.style.transform = "rotate("+secDegree+"deg)";
    var minutesHand = document.querySelector("#minutes");
    minutesHand.style.transform = "rotate("+minDegree+"deg)";
    var hourHand = document.querySelector("#hour");
    hourHand.style.transform = "rotate("+hourDegree+"deg)";
  }, 1000);