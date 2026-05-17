let count = 0;

function increase() {
  count++;
  console.log(count);
}

function decrease() {
  count--;
  console.log(count);
}

increase(); // 1
increase(); // 2
decrease(); // 1