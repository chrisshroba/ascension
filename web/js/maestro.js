/**
 * Created by chrisshroba on 2/19/15.
 */

run_buttons = $(".run-button")

var oldActive;
function setActive(element) {
    if(oldActive!=undefined)
        oldActive.classList.remove("success");
    oldActive = element;
    element.classList.add("success");
}

for(var i = 0; i < run_buttons.length; i++){
   //do something to each div like
   run_buttons[i].onclick = function() {
       filename=(this.dataset["filename"]);
       $.get("/api/run_file/" + filename);
//       debugger;
       setActive(this.parentElement.parentElement);
   }
}

$("#kill-btn").click(
    function() {
        $.get("/api/killall");

    }
)
