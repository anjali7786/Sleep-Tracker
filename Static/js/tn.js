// console.log("hello");
const timer = `  <div class="time">
<label for="appt" class="bt fs-5">Enter your Bedtime:</label>
&nbsp;
<input type="time" class="appt1" name="appt" min="00:00" max="23:59" required>
</div>
<div class="time">
<label for="appt" class="wt fs-5">Enter Wakeup time:</label>
&nbsp;
  <input type="time" class="appt2" name="appt" min="00:00" max="23:59" required>
</div>
</br>`;
document.querySelector("#icon1").addEventListener("click", function(){
    document.querySelector("#icon1").insertAdjacentHTML("beforebegin", timer);
    // console.log("click");
})
document.querySelector("#icon2").addEventListener("click", function(){
    document.querySelector("#icon2").insertAdjacentHTML("beforebegin", timer);
    // console.log("click");
})