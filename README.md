# Sudoku Solver
This project uses backtracking (https://en.wikipedia.org/wiki/Backtracking) to solve 9*9 Sudoku. <br>

- sudoku.py - Solves a sudoku board and prints the solution. The sudoku problem needs to be specified at the top of the script. You can change it to solve a problem of your choice.
- sudoku_gui.py - Includes GUI (built with pygame).
- outputs - This folder consists a few demo videos. Some of these videos show backtracking working in real time. 

<b>Postscript - </b> <br>
- I am working to include OCR to this project to allow for direct image inputs of sudoku problems (even from newspaper and magazines).
  I tried using a digit classifier that I built with my own feed forward neural net framework, but it was messing up a few digits every time.
  A convolutional neural net will work much better for this application. I am looking forward to adding that next.
