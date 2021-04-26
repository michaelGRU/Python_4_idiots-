/*main functions*/
//jQuery UI to make a DIV draggble
$( function() {
    $( ".parent").draggable();
   
     $( ".stringParent").draggable();
     $( ".javaParent").draggable();
     $( ".chaosParent").draggable();
   

} );


// this is the tab in about me section(2) 
//https://www.w3schools.com/howto/howto_js_vertical_tabs.asp
//put this on top otherwise it might mess up the form
function switchEd(evt, edulvl) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(edulvl).style.display = "block";
    evt.currentTarget.className += " active";
}
document.getElementById("defaultOpen").click();




//smooth scroll for any div element from one id to another 
$("#projects").click(function() {
    $('html, body').animate({
        scrollTop: $("#ss3").offset().top
    }, 2000);
});

//blink 
$('.blink').each(function() {
    var elem = $(this);
    elem.fadeOut(100)
        .fadeIn(100)
        .fadeOut(100)
        .fadeIn(100)
        .fadeOut(100)
        .fadeIn(100);
});

function setTimer(){
    var timeleft = 10;
    var downloadTimer = setInterval(function(){
        timeleft--;
        document.getElementById("countdowntimer").textContent = timeleft;
        if(timeleft <= 0)
            clearInterval(downloadTimer);
    },1000);



}
setTimeout(setTimer, 16000);




//main typewriter content
function getUserInput(element){
    var _NSAKEY; //used for cryptography
    var userInput = document.getElementById("userInput").value;
    if (event.keyCode==13) { //user hits enter key
        //clear the screen
        document.getElementById("p1").setAttribute("hidden",true);
        document.getElementById("p2").setAttribute("hidden",true);
        document.getElementById("p3").setAttribute("hidden",true);
        document.getElementById("p4").setAttribute("hidden",true);
        document.getElementById("p5").setAttribute("hidden",true);
        document.getElementById("p6").setAttribute("hidden",true);
        document.getElementById("p7").setAttribute("hidden",true);


        //check userInput 
        //        var letters = /^[A-Za-z]+$/;
        //        if(element.value.match(letters)){
        var d = new Date();

        var i = 0;
        var txt = 'LOADING...' + d.toLocaleString();
        var speed = 50;

        function typeWriter() {
            if (i < txt.length) {
                document.getElementById("output1").innerHTML += txt.charAt(i);
                i++;
                setTimeout(typeWriter, speed);
            }
        }
        typeWriter();
        var firstLetter = userInput.charAt(0);
        var capIt = firstLetter.toUpperCase();
        var name = capIt + userInput.substring(1);
        
        var i2 = 0;
        var txt2 = name + ', my job is to help you find your way around the site. The top navigation bar ';
        var speed2 = 50;
        var stopWatch = 4800;

        function typeWriter2() {
            if (i2 < txt2.length) {
                document.getElementById("output2").innerHTML += txt2.charAt(i2);
                i2++;
                setTimeout(typeWriter2, speed2);
            }

        }

        setTimeout(typeWriter2,stopWatch);
        var i3 = 0;
        var txt3 = 'will lead you to the place you want. I\'d recommend you to check out ABOUT ME section first.';
        var speed3 = 50;

        function typeWriter3() {
            if (i3 < txt3.length) {
                document.getElementById("output3").innerHTML += txt3.charAt(i3);
                i3++;
                setTimeout(typeWriter3, speed3);
            }

        }

        setTimeout(typeWriter3,stopWatch*2);
        var i4 = 0;
        var txt4 = 'I hope you will find something interesting.';
        var speed4 = 50;

        function typeWriter4() {
            if (i4 < txt4.length) {
                document.getElementById("output4").innerHTML += txt4.charAt(i4);
                i4++;
                setTimeout(typeWriter4, speed4);
            }

        }

        setTimeout(typeWriter4,stopWatch*3);



    }



    //    }
}

//smooth scroll; 
//an alternative way would be to use the html build in function, 
// html{scroll-behavior:smooth}
//https://www.w3schools.com/howto/howto_css_smooth_scroll.asp
//however, the html version doesnt work on some browsers
$(document).ready(function(){
    $("a").on('click', function(event) {
        if (this.hash !== "") {
            event.preventDefault();
            var hash = this.hash;
            $('html, body').animate({
                scrollTop: $(hash).offset().top
            }, 800, function(){
                window.location.hash = hash;
            });
        } 
    });
});


//$(function () {
//    $(document).scroll(function () {
//        var $nav = $(".navbar");
//        $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
//    });
//});
//
//




