"use strict";

let x, s;
x = document.querySelectorAll(".box");

if (x.length == 0) {
  let head = document.querySelector('#heading-display-all');
  head.innerHTML = 'No Posts Added';

} else {

  for (let i = 0; i < x.length; i ++) {
    s = `${x[i].textContent}`;
    x[i].innerHTML = s.slice(0, 150) + '...';
  }

}


function deleteFunc (e) {

  let parent_id = e.parentNode.id;
  let del = document.querySelector(`#${parent_id}`);
  del.submit();

}

function editFunc (e) {
  
  let parent_id = e.parentNode.id;
  let edit = document.querySelector(`#${parent_id}`);
  
  edit.submit();
  
}


