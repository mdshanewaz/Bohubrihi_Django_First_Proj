// Aside Start
const nav = document.querySelector(".nav"),
    navList = nav.querySelectorAll("li"),
    totalNavList = navList.length,
    allSection = document.querySelectorAll("section"),
    totalSection = allSection.length;

for(let i=0; i<totalNavList; i++){
    const a = navList[i].querySelector("a");
    a.addEventListener("click", function(){

        removeBackSection();

        for(let j=0; j<totalNavList; j++){
            if(navList[j].querySelector("a").classList.contains("active")){
                addBackSection(j);
            }
            navList[j].querySelector("a").classList.remove("active");
        }
        this.classList.add("active");
        showSection(this);
        if(window.innerWidth < 1200){
            asideSectionTogglerBtn();
            for(i=0; i<totalSection; i++){
                allSection[i].classList.remove("stop-scrolling");
                darkblackshadow[i].style.display = "none";
            }
        }
    });
}

function removeBackSection(){
    for(let i=0; i<totalSection; i++){
        allSection[i].classList.remove("back-section");
    }
}

function addBackSection(num){
    allSection[num].classList.add("back-section");
}

function showSection(element){
    for(let i=0; i<totalSection; i++){
        allSection[i].classList.remove("active");
    }

    const target = element.getAttribute("href").split("#")[1];
    document.querySelector("#" + target).classList.add("active");
}

function updateNav(element){
    for(let i =0; i<totalNavList; i++){
        navList[i].querySelector("a").classList.remove("active");
        const target = element.getAttribute("href").split("#")[1];
        if(target === navList[i].querySelector("a").getAttribute("href").split("#")[1]){
            navList[i].querySelector("a").classList.add("active");
        }
    }
}

document.querySelector(".more-me").addEventListener("click", function(){
    const sectionIndex = this.getAttribute("data-section-index");
    console.log(sectionIndex);
    showSection(this);
    updateNav(this);
    removeBackSection();
    addBackSection(sectionIndex);
});

document.querySelector(".hire-me").addEventListener("click", function(){
    const sectionIndex = this.getAttribute("data-section-index");
    showSection(this);
    updateNav(this);
    removeBackSection();
    addBackSection(sectionIndex);
});

const mainContent = document.querySelector(".main-content"),
    navTogglerBtn = document.querySelector(".nav-toggler"),
    aside = document.querySelector(".aside");
    darkblackshadow = document.querySelectorAll(".dark-black-shadow")

mainContent.addEventListener("click", (e) =>{
    if(navTogglerBtn.classList.contains("open") && aside.classList.contains("open")){
        aside.classList.remove("open");
        navTogglerBtn.classList.remove("open");

        for(i=0; i<totalSection; i++){
            allSection[i].classList.remove("stop-scrolling");
            darkblackshadow[i].style.display = "none";
        }
    };

    const card = ".card-box"
    const isClosest = e.target.closest(card);
    if(!isClosest && (cardBox.style.display = "block")){
        cardBox.style.display = "none";
        cardModal.style.display = "none";
    };
});

navTogglerBtn.addEventListener("click", () => {
    asideSectionTogglerBtn();
    fixedPosition();

    if(cardBox.style.display = "block"){
        cardBox.style.display = "none";
        cardModal.style.display = "none";
    }

    for(j=0; j<totalmodalList; j++){
        if(modal[j].style.display = "block"){
            modal[j].style.display = "none";
        };
    };
});

function asideSectionTogglerBtn(){
    aside.classList.toggle("open");
    navTogglerBtn.classList.toggle("open");
}

function fixedPosition(){
    for(i=0; i<totalSection; i++){
        if(navTogglerBtn.classList.contains("open") && aside.classList.contains("open")){
            allSection[i].classList.add("stop-scrolling");
            darkblackshadow[i].style.display = "block";
        }
        else{
            allSection[i].classList.remove("stop-scrolling");
            darkblackshadow[i].style.display = "none";
        }
    }
}
// Aside End

// Logo Start
// Light and Dark mode
var DaybrandNight = document.querySelector("#brand"); 
var sun = document.querySelector("#sun");
sun.style.display = "none";
var moon = document.querySelector("#moon");
document.body.classList.toggle("dark");

DaybrandNight.onclick = function(){
    document.body.classList.toggle("dark");
    if(sun.style.display === "none"){
        moon.style.display = "none";
        sun.style.display = "block";
    } else{
        sun.style.display = "none";
        moon.style.display = "block";
    }
};
// Logo End

// Home Start
var typed = new Typed(".typing",{
    strings: ["", "Software Engineer", "Web Designer", "Web Developer", "Data Scientist", "Cyber Security Specialist"],
    typeSpeed: 100,
    BackSpeed: 60,
    loop: true
});
// Home End

// About Start
const aboutSec = document.querySelector(".about");
const progressContainer = document.querySelectorAll(".progress");
const progressIn = document.querySelectorAll(".progress-in");
const skillPercentage = document.querySelectorAll(".skill-percent");



let setPercentage = setInterval(() =>{
    if(aboutSec.classList.contains("active")){
        for(i=0; i<progressContainer.length; i++){
            progressIn[i].style.width = progressContainer[i].getAttribute("data-percentage") + "%";
            skillPercentage[i].innerText = progressContainer[i].getAttribute("data-percentage") + "%";
            skillPercentage[i].style.left = progressContainer[i].getAttribute("data-percentage") + "%";
        } 
    } 
}
)
// About End

// Project Start
// Project filterable image hover effect start  
let list = document.querySelectorAll('.list');
let projectItem = document.querySelectorAll('.project-item');

for(let i = 0; i<list.length; i++){
    list[i].addEventListener('click', function(){
        for(let j = 0; j<list.length; j++){
            list[j].classList.remove('active');
        }
        this.classList.add('active');
        let dataFilter = this.getAttribute('data-filter');

        for(let k = 0; k<projectItem.length; k++){
            projectItem[k].classList.remove('active');
            projectItem[k].classList.add('hidden');

            if(projectItem[k].getAttribute('data-item') == dataFilter || dataFilter == "all"){
                projectItem[k].classList.remove('hidden');
                projectItem[k].classList.add('active');
            }
         }
    })
}

// Image on click effect start
const modal = document.querySelectorAll(".modal"),
    totalmodalList = modal.length,
    zoom = document.querySelectorAll(".zoom"),
    img = document.querySelectorAll(".myImg"),
    modalImg = document.querySelectorAll(".modal-content"),
    captionText = document.querySelectorAll(".caption-alt"),
    close = document.querySelectorAll("#close");

for(let i=0; i<totalmodalList; i++){
    zoom[i].onclick = function(){    
        modal[i].style.display = "block";
        modalImg[i].src = img[i].src;
        captionText[i].innerHTML = img[i].alt;
        modal[i].style.zIndex = "10000";      
    }

    close[i].onclick = function(){ 
        modal[i].style.display = "none";
    }

    modal[i].onclick = function(e){
        const modlalimg = ".modal-content";
        const isClosest = e.target.closest(modlalimg);
        if (!isClosest && (modal[i].style.display = "block")){
            modal[i].style.display = "none";
        } 
    }
}
// Image on click effect end
// Project filterable image hover effect End
// Project End

// Service Start
// Service review start
const slide = document.querySelector(".container-row-1");
const rightbtn = document.querySelector(".btn-r"); 
const leftbtn = document.querySelector(".btn-l");
const slideWidth = document.querySelector(".row-1-col").offsetWidth;

rightbtn.addEventListener("click", function(){
    slide.scrollLeft += slideWidth;
});

leftbtn.addEventListener("click", function(){
    slide.scrollLeft -= slideWidth;
});

// Service review end
// Service circle progress start 1
var circleProgress = document.querySelectorAll("#service-circle"),
progressValue = document.querySelectorAll("#progress-value");
const serviceSec = document.querySelector(".service");

let progressStartvalue1 = 0,
progressEndvalue1 = 105,
speed1 = 50;

let progress1 = setInterval(() => {
    if(serviceSec.classList.contains("active")){
        
        progressStartvalue1++;

        progressValue[0].textContent = `${progressStartvalue1*2}↑`
        circleProgress[0].style.background = `conic-gradient(var(--skin-color) ${progressStartvalue1 * 3.6}deg, #fff 0deg)`

        if(progressStartvalue1 == progressEndvalue1){
            clearInterval(progress1);
        }
    }
}, speed1);
// Service circle progress bar end 1

// Service circle progress start 2
let progressStartvalue2 = 0;
let progressEndvalue2 = 13;
let speed2 = 400;

let progress2 = setInterval(() => {
    if(serviceSec.classList.contains("active")){
        
        progressStartvalue2++;

        progressValue[1].textContent = `${progressStartvalue2}>`
        circleProgress[1].style.background = `conic-gradient(var(--skin-color) ${progressStartvalue2*8 * 3.6}deg, #fff 0deg)`

        if(progressStartvalue2 == progressEndvalue2){
            clearInterval(progress2);
        }
    }
}, speed2);
// Service circle progress bar end 2

// Service circle progress start 3
let progressStartvalue3 = 0;
let progressEndvalue3 = 19;
let speed3 = 250;

let progress3 = setInterval(() => {
    if(serviceSec.classList.contains("active")){

        progressStartvalue3++;

        progressValue[2].textContent = `${progressStartvalue3}+`
        circleProgress[2].style.background = `conic-gradient(var(--skin-color) ${progressStartvalue3*5.5 * 3.6}deg, #fff 0deg)`

        if(progressStartvalue3 == progressEndvalue3){
            clearInterval(progress3);
        }
    }
}, speed3);
// Service circle progress bar end 3

// Service circle progress start 4
let progressStartvalue4 = 0;
let progressEndvalue4 = 100;


let progress4 = setInterval(() => {
    if(serviceSec.classList.contains("active")){
        
        progressStartvalue4++;

        progressValue[3].textContent = `${progressStartvalue4}%`
        circleProgress[3].style.background = `conic-gradient(var(--skin-color) ${progressStartvalue4 * 3.6}deg, #fff 0deg)`

        if(progressStartvalue4 == progressEndvalue4){
            clearInterval(progress4);
        }
    }
}, speed1);
// Service circle progress bar end 4
// Service End

// Contact Start
function sendMail(){
    var params = {
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        subject: document.getElementById("subject").value,
        message: document.getElementById("message").value
    };
    
    const serviceID = "service_pn3e4zh";
    const templateID = "template_23jn0lq";
    
    emailjs.send(serviceID, templateID, params).then((res) =>{
        document.getElementById("name").value = "";
        document.getElementById("email").value = "";
        document.getElementById("subject").value = "";
        document.getElementById("message").value = "";
        cardBox.style.display = "block";
        cardModal.style.display = "block";
        console.log(send);
    })
    .catch((err) => console.log(err));
}

// Contact form pop-up button
var cardBox = document.getElementById("cardBox");
var cardModal = document.getElementsByClassName("cardModal")[0];
var closeBtn = document.getElementsByClassName("close-btn")[0];

closeBtn.onclick = function(){
    cardBox.style.display = "none";
    cardModal.style.display = "none";
}
// Contact End