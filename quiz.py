def main() :
scores = readFloats()

if len(scores) > 1 :
removeMinimum(scores)
removeMinimum(scores)
total = sum(scores)
print("Final score:", total)
else :
print("At least two scores are required.")

def readFloats() :
# Create an empty list.
values = []
# Read the input values into a list.
print("Please enter values, Q to quit:")
userInput = input("")
while userInput.upper() != "Q" :
values.append(float(userInput))
userInput = input("")
return values

def removeMinimum(values) :
smallestPosition = 0
for i in range(1, len(values)) :
if values[i] < values[smallestPosition] :
smallestPosition = i
values.pop(smallestPosition)
# yessss Start the program now
main()
