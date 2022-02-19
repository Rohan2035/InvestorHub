"use strict";

// Card-text modification
let x, s;
x = document.querySelectorAll(".box");

for (let i = 0; i < x.length; i ++) {
  s = `${x[i].textContent}`;
  x[i].innerHTML = s.slice(0, 150) + '...';
}