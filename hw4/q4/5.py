# Define the input and output file names
input_file_name = "input.txt"
output_file_name = "output.txt"

# Function to find the longest word from a list of words
def find_longest_word(words):
    if not words:
        return None
    return max(words, key=len)

# Read the contents of the input file
with open(input_file_name, "r") as input_file:
    text = input_file.read()

# Split the contents into words
words = text.split()

# Find the longest word
longest_word = find_longest_word(words)

# Write the longest word to the output file
with open(output_file_name, "w") as output_file:
    output_file.write(longest_word)

print(f"The longest word '{longest_word}' has been written to '{output_file_name}'.")
