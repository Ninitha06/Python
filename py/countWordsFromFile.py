def countWords():
    wordCount = 0
    fileName = input("Enter your file name : - ")
    file = open(fileName, "r")

    for f in file:
        words = f.split()
        wordCount = wordCount + len(words)

    print("Number of words : - ")
    print(wordCount)
# Splitting the words in the file

countWords()