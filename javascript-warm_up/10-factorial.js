#!/usr/bin/node
const a = parseInt(process.argv[2]);

function factorial (a) {
  let product = 1;
  for (let i = 1; i <= a; i++) {
    product *= i;
  }
  console.log(product);
}

factorial(a);
