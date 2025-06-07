# exercise 1

# first way

text = "AbbaBAaAb" 
countA = 0
countB = 0
for char in text:
    if char.lower() == 'a':
        countA += 1
    elif char == 'b':
        countB += 1
print("A and a:", countA)
print("b:", countB)

# second way

text = "AbbaBAaAb" 
countA = 0
countB = 0
for i in range(len(text)):
    if text[i] == 'a' or text[i] == 'A':
        countA += 1
    elif text[i] == 'b':
        countB += 1
print("A and a:", countA)
print("b:", countB)