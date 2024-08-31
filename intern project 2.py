def count_words(text):
    """
    This function takes a string input and returns the number of words in it.
    Words are defined as sequences of characters separated by spaces.
    """
                                                                     # Strip any leading/trailing whitespace and split the text into words
    words = text.strip().split()

                                                                    # Return the length of the resulting list, which is the word count
    return len(words)

def main():
    """
    Main function to execute the word counting program.
    Handles user input and displays the word count.
    """
    print("Welcome to the Word Counter Program!")
    
                                                                        # Get user input
    user_input = input("Please enter a sentence or paragraph: ")
    
                                                                        # Error handling for empty input
    if not user_input.strip():
        print("Error: No text entered. Please try again.")
        return
    
                                                                        # Count the words using the count_words function
    word_count = count_words(user_input)
    
                                                                         # Display the result
    print(f"The total number of words is: {word_count}")

if __name__ == "__main__":
    main()
