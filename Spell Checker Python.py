# Empty dictionary to load all words
speller = {}

# Load all words in speller
def load():
    my_dictionary = open("smalldict.txt", 'r')          # Open "smalldict.txt" in read mode to read all words in it
    # Add keys and values to speller
    for word in my_dictionary:
        word = word.lower()         # Convert all words to lowercase
        if word[0].lower() not in speller:      # If first letter of word is not in speller
            speller[word[0]] = []               # Initialise an empty list corresponding to each key

        speller[word[0]].append(word.rstrip('\n'))      # Append word after stripping off \n

    for element in speller:             # Print speller for ease and debugging
        print(element, speller[element])

    my_dictionary.close()           # Close dictionary


# For taking input paragraph and putting all words in a list
def input_para():
    
    para = input("Enter paragraph: ")       # Take input paragraph
    # Function call for Punctuation(string), defined later
    temp = Punctuation(para.lower())   # Convert para to lower, remove all punctuations, store in variable temp
    input_list = temp.split()       # Split the string into words (separated by space) and put in list
    return input_list               # Return the list of words in the input paragraph

# Our main spell checker program
def check(input_list):
    count=0         # To keep a count of misspelled words

    for word in input_list:         # Iterate through every input word
        if word in speller[word[0]]:        # If word found in speller
            print("correct")
        else:
            print("misspelt")
            count += 1              # Increment count of misspelt words

    print("Count of misspelt words: ", count)       # Print the count of misspelt words

# To remove all punctuations from input string
def Punctuation(string): 
  
    # String of all the possible punctuation marks 
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
  
    
    for x in string:        # Travel each character in input string.
        if x in punctuations:    # If that character is a punctuation 
            string = string.replace(x, "")      # Replace the punctuation character with empty character.
  
    # Print string without punctuation 
    return string

# Main function - good coding practice
def main():
    load()      # Load all words into speller
    input_list = input_para()       # Take input from user and store words in input_list
    check(input_list)           # Perform spell check on all the words
    

if __name__ == "__main__":          # Calling main function
    main()
