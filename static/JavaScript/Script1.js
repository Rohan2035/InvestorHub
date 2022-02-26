"use strict";

let x, s;
x = document.querySelectorAll(".box");

if (x.length == 0) {
  let head = document.querySelector('#heading-display-all');
  console.log(head);
  head.innerHTML = 'No Posts Added';

} else {

  for (let i = 0; i < x.length; i ++) {
    s = `${x[i].textContent}`;
    x[i].innerHTML = s.slice(0, 150) + '...';
  }

}


function deleteFunc (e) {

  console.log(e.parentNode.id);
  let parent_id = e.parentNode.id;
  let del = document.querySelector(`#${parent_id}`);
  del.submit();

}

function editFunc () {
  let e = document.querySelector('.edit');
  e.submit();
}


