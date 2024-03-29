
def palindrome(pass_string):
    print(pass_string)
    temp_list = []
    temp_list = pass_string.split()
    print(temp_list)
    count = 0
    for element in temp_list:
        if element.lower() == element.lower()[::-1]:
            count += 1
    print("The number of palindrome words are : ", count)

palindrome("asa aua def radar Awasare")

