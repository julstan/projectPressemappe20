
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


function scrollUp() {
    // window.scrollBy(0, -window.innerHeight);
    window.scrollBy(0, -10000);
}

function scrollDown() {
    window.scrollBy(0, 10000);
}
