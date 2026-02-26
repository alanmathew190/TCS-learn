const inc = document.getElementById("inc");
const dec = document.getElementById("dec");
const res = document.getElementById("res");
const save = document.getElementById("save");
load()
let count = 10
 document.getElementById("count").innerHTML = count;
// Add EventListener to btn
// btn.addEventListener("click", () => {
//   document.getElementById("txt").innerHTML.fontcolor=blue
//   // var name = window.prompt("Enter value")
//   // console.log(name);
//   // document.getElementById("txt").innerHTML="Your Name is "+name
// });

function update() {
  document.getElementById("count").innerHTML = count;
}
inc.addEventListener("click", () => {
    count+=1
update()
})

dec.addEventListener("mouseover", () => {
    if (count > 0) {
        count--
        update()
    }
})

save.addEventListener('click',() => {
    localStorage.setItem("count",count)
})

function load() {
  let count = localStorage.getItem("count");
 document.getElementById("count").innerHTML = count;
}
res.addEventListener("click", () => {
  count=0
  update();
});





