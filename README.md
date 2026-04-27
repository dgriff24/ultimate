# ultimate

Ultimate is a stack-based esoteric programming language inspired by [BeeScript](https://esolangs.org/wiki/BeeScript).

| Instruction | Description |
| ------ | ------ |
| `CHILLY` | Push 0 onto the stack |
| `MATCH` | Duplicate the top value of the stack |
| `POINT` | Add 1 to the top value of the stack |
| `VIOLATION` | Pops A and then B from the stack and pushes B - A to the stack |
| `PULL` | Takes one character of input and pushes it's ascii code to the stack |
| `CHIRP` | Pop the top value of the stack and print it as an ascii character |
| `STALL` | Pop the top value of the stack and print it as an integer |
| `CHECK FEET n` | Pop the top of the stack. If it is zero, jump to the nth line |
| `FORCE HOME` | Pop the top of the stack and push it to the bottom |
| `FORCE AWAY` | Remove the bottom value of the stack and push it to the top |
| `BREAK` | Terminate program execution |


### Here are some examples of code inputs and outputs:

`python ultimate.py examples/reversestring.ulti` <br>
a<br>
s<br>
d<br>
f<br>
<br>
fdsa<br>

`python ultimate.py examples/cat.ulti` <br>
a<br>
a<br>

Note on `cat`: because it only accepts 1 character at a time, it can only print one character.

`python ultimate.py examples/repeater.ulti`<br>
a<br>
4<br>
aaaa<br>
