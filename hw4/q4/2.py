def letter_to_position(letter):
    if 'a' <= letter <= 'z':
        return ord(letter) - ord('a') + 1
    elif 'A' <= letter <= 'Z':
        return ord(letter) - ord('A') + 1
    else:
        return None

def replace_letters_with_position(text):
    result = []
    for char in text:
        position = letter_to_position(char)
        if position is not None:
            result.append(str(position))
    return ' '.join(result)

# Input string
input_text = "We have a lot of rain in June."

# Replace letters with their positions
output_text = replace_letters_with_position(input_text)

# Print the result
print(output_text)
