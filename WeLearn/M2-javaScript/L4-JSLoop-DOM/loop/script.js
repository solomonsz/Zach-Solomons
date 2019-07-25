/*

 for (let i =0; i <names.length; i++){
 console.log(names[i]);
}

names.forEach(name => {
  // run this function for each name in names
  console.log(name);
})
let sum = 0;
let numbers = [1,2,3,4,5,6,7,8,9,10]

const findTotal = ((item) => {
sum = sum + item;
});
numbers.forEach(findTotal)
console.log(sum);*/

const buttons =  document.querySelectorAll('button');
const box = document.querySelector('#box');

buttons.forEach((button) => {
  button.addEventListener('click', () => {
    const color = button.innerHTML;
    box.style.background = color;
  });
});
