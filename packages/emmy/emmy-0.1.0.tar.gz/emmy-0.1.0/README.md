
# Emmy
A very hard esolang named after Emmy Noether.

## Install
To install emmy, make sure you have pip installed (if not run `python -m ensurepip --upgrade`). Then, run `pip install emmy` in the terminal.

## Run code:
1. Save code as .emy
2. Do python3 -m emmy.everything.emmy "/path/to/file.emy" "input (optional)"

## List of commands
```
    Hex  : Opname, Description
    '1a' : 'rol', Rotates stack to the left
    'f6' : 'ror', Rotates stack to the right
    'ff' : 'ils', Starts an integer literal
    'a9' : 'ile', Ends an integer literal
    'ed' : 'icr', Pops value from stack, adds one, and then pushes it back to the stack
    '0e' : 'dcr', Pops value from stack, subtracts one, and then pushes it back to the stack
    '6a' : 'wls', Starts a while loop
    'c5' : 'wle', Ends a while loop
    'be' : 'acc', Adds one to the accumulator
    '8e' : 'dcc', Subtracts one from the accumulator
    '98' : 'ast', Pushes the accumulator to stack.
    '1b' : 'cst', Clears the stack.
    '5d' : 'inp', Pushes all of input to stack.
    '04' : 'out', Pops something, then prints it. If the popped item is a number, print chr(a). Otherwise, print a as it is.
    '13' : 'xor', Pops a, pops b, xors them
    'e3' : 'pls', Pops a, pops b, adds them
    '2a' : 'mns', Pops a, pops b, subtracts them
    '11' : 'num', Pops a, prints it as a number
    'c7' : 'rnd', Push a random bit onto the stack.
    'c4' : 'xpl', BOOM
    'ee' : 'emy', Pushes "Emmy" onto the stack
    '12' : 'bob', Pushes "bob" onto the stack
    '14' : 'hwd', Pushes "Hello, world!" onto the stack.
    'bb' : 'gds', Pushes "Graindstone" onto the stack
    'f5' : 'nin', Pushes input as a number onto stack.
```