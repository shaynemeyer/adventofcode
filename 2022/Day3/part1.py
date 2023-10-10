
file = open("test.txt", "r")

for line in file:
  firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
  print(firstpart, secondpart)

