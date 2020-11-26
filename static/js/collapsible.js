function collapsibleToggle(a) {
    a.classList.toggle("active");
    var content = a.nextElementSibling;
    if (content.style.maxHeight){
      content.style.maxHeight = null;
    } else {
      content.style.maxHeight = content.scrollHeight + "px";
    }
  }