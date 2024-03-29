# Define the function
def palindrome(string_1):
    print("Input string is:", string_1)
    count = 0
    listOfWords = string_1.split(" ")
    print("All the words in list format:", listOfWords)
    for element in listOfWords:
        if element.lower() == element.lower()[::-1]:  # Compare each word, not the whole string
            count += 1
    print("Number of palindrome words:", count)

# Call the function with a string
palindrome("madam and radar are examples of palindrome words")