function navRespond(a) {
    a.classList.toggle("change");
    var x = document.getElementById("mob_nav");
    if (x.className === "mob_nav") {
      x.className += " responsive";
    } else {
      x.className = "mob_nav";
    }
  }