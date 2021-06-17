introString = input("Enter your introduction")
characterCount = 0
# the last word will not be considered. so we set 1 as initial value
wordCount = 1
for character in introString:
    characterCount = characterCount + 1
    if (character==" "):
        wordCount = wordCount + 1
    if (character=="."):
        wordCount = wordCount + 1
print("Number of characters in introduction : ")
print(characterCount)
print("Number of words in introduction : ")
print(wordCount)