#!/usr/bin/node
const SquareP = require('./5-square');

module.exports = class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let m = 0;
    while (m < this.height) {
      let X = '';
      let n = 0;
      while (n < this.width) {
        X += 'X';
        n++;
      }
      console.log(X);
      m++;
    }
  }
}
