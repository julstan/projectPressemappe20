/* collapse Bootstrap hat das hier ersetzt :^)
var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
}
*/


// Scroll Indicator

window.onscroll = function() {myFunction()};

function myFunction() {
  let winScroll = document.body.scrollTop || document.documentElement.scrollTop;
  let height = document.body.scrollHeight - window.innerHeight;
  let scrolled = document.getElementById("myBar").style.width;
  if (height !== 0) {
    scrolled = (winScroll / height) * 100;
  }

  document.getElementById("myBar").style.width = scrolled + "%";
}

// Pfeile



