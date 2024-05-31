# Function to reverse a string
def reverse_string(input_string):
    return input_string[::-1]

# Main function
if __name__ == "__main__":
    # Input string
    input_string = input("Enter a string to reverse: ")
    
    # Reverse the string
    reversed_string = reverse_string(input_string)
    
    # Print the reversed string
    print("Reversed string:", reversed_string)
