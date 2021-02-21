anyWord = input("Enter any one word to get some interesting details:")

charLength = len(anyWord)
print("The Total Characters for your word is:", charLength)

count = 0
for letter in anyWord:
    if (letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u'):
        count += 1
print("Total count of vowels in your word is:", count)

