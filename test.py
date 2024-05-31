import os

def reverse_string(s):
    if not s:
        raise ValueError("No input string provided")
    return s[::-1]

if __name__ == "__main__":
    input_string = os.getenv('INPUT_STRING')
    if input_string is None:
        print("Error: INPUT_STRING environment variable not set")
        exit(1)
    
    print(f"Original string: {input_string}")
    print(f"Reversed string: {reverse_string(input_string)}")
