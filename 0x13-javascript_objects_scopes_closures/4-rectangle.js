#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(Number(w)) && w > 0 && Number.isInteger(h) && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i, j, line;
    for (i = 0; i < this.height; i++) {
      line = '';
      for (j = 0; j < this.width; j++) {
        line += 'X';
      }
      console.log(line);
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    [this.width, this.height] = [this.width * 2, this.height * 2];
  }
}
module.exports = Rectangle;
