const openBtn = document.querySelector(".open_btn");
const closeBtn = document.querySelector(".close_btn");
const myNav = document.querySelector("nav");
const navlinks = document.querySelectorAll(".nav_link")


openBtn.addEventListener("click",()=>{
    myNav.style.transform = "translate(0%)";
})
closeBtn.addEventListener("click",()=>{
    myNav.style.transform = "translate(100%)";
})


if (window.innerWidth <= 846){
    for (let links of navlinks ){
links.addEventListener("click", ()=>{
myNav.style.transform = "translate(100%)";
})
}
}