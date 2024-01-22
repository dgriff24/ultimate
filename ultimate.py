import sys

lines = []
try:
   fileName = sys.argv[1]
   file = open(fileName)
   lines = file.read().split("\n")
   file.close()
except Exception as e:
   print(f"Error while opening file:\n{e}")
   sys.exit(0)

stack = []
pc = 0

def err(str):
   print("\n" + str + f" at line {pc}")
   sys.exit(0)

def pop(index = -1):
   if len(stack) < 1:
      err("Error: Stack underflow")
   return stack.pop(index)

while pc >= 0 and pc < len(lines):
   parts = lines[pc].split(" ")
   instr = parts[0]
   if instr == "CHILLY":
      stack.append(0)
   elif instr == "POINT":
      a = pop()
      stack.append(a+1)
   elif instr == "MATCH":
      a = pop()
      stack.append(a)
      stack.append(a)
   elif instr == "CHIRP":
      print(chr(pop()), end="", flush=True)
   elif instr == "STALL":
      print(int(pop()), end="", flush=True)
   elif instr == "VIOLATION":
      a = pop()
      b = pop()
      stack.append(b - a)
   elif instr == "CHECK":
      a = pop()
      if len(parts) < 3 or parts[1] != "FEET":
         err("Error: Expected instruction argument for CHECK FEET")
      try:
         line = int(parts[2]) - 1 # - 1 because list indexes start at 0
         if a == 0:
            pc = line - 1 # - 1 again because we're incrementing pc each instruction
      except:
         err("Error: Invalid instruction argument for FLY")
   elif instr == "FORCE":
      if len(parts) < 2:
         err("Error: Expected to specify FORCE")
      if parts[1] == 'AWAY':
         a = pop(0)
         stack.append(a)
      elif parts[1] == 'HOME':
         a = pop()
         stack.insert(0, a)
   elif instr == "CALL":
      try:
         stack.append(ord(input("")[0]))   
      except IndexError:
         stack.append(0)
   elif instr == 'BREAK':
      break
   pc += 1

print('')