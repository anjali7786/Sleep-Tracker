// console.log("hello");
// const timer = `  <div class="time">
// <label for="appt" class="bt fs-5">Enter your Bedtime:</label>
// &nbsp;
// <input type="time" class="appt1" name="appt" min="00:00" max="23:59" required>
// </div>
// <div class="time">
// <label for="appt" class="wt fs-5">Enter Wakeup time:</label>
// &nbsp;
//   <input type="time" class="appt2" name="appt" min="00:00" max="23:59" required>
// </div>
// </br>`;
// document.querySelector("#icon1").addEventListener("click", function(){
//     document.querySelector("#icon1").insertAdjacentHTML("beforebegin", timer);
//     // console.log("click");
// })
// document.querySelector("#icon2").addEventListener("click", function(){
//     document.querySelector("#icon2").insertAdjacentHTML("beforebegin", timer);
//     // console.log("click");
// })


const imgdiv=`<div class="overlay"></div>`;
document.querySelector(".container1").insertAdjacentHTML("afterend",imgdiv);
const overlay=document.querySelector(".overlay");

//Set for every picture
let imgclick1= document.querySelectorAll(".box1 img")[0];
let img1=`<img src="../Static/Images/Motivational-img/Zoomed/31 (1).jpg">`;
imgclick1.addEventListener("click", function (){
  overlay.insertAdjacentHTML("afterbegin",img1);
  overlay.style.visibility="visible";
})


//To remove overlay
overlay.addEventListener("click", function (){
  overlay.style.visibility="hidden";
  document.querySelector(".overlay img").remove();
})
