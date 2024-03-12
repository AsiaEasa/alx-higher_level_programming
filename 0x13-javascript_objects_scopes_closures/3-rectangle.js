#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print = () => {
    let m = 0;
    while (m < this.height) {
      let Xshape = '';
      let n = 0;
      while (n < this.width) {
        Xshape += 'X';
        n++;
      }
      console.log(Xshape);
      m++;
    }
  };
};
