letters = ["A", "E", "G", "I", "O", "S", "T"]
numbers = ["4", "3", "6", "1", "0", "5", "7"]
#user_input = input("Try a word! ") 
user_input = "TEA"

count = 0

while count < len(user_input):
    #print(user_input[count])
    letter = user_input[count]
    letter_add_to_translation = ""
    internal_count = 0 
    while internal_count < len(letters):
        letter_to_convert = letters[internal_count]
        #print(letter_to_convert)
        if letter == letter_to_convert:
            print("WE HAVE A MATCH")
            print(numbers[internal_count])
        internal_count += 1
    count += 1