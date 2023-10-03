def create_pattern_dict(pattern):
    pattern_dict = {}
    for index, char in enumerate(pattern):
        if char != '*':
            pattern_dict[index] = char
    return pattern_dict


def match_patterns(user_pattern, string_list):
    user_pattern_dict = create_pattern_dict(user_pattern)
    matching_strings = []

    for string in string_list:
        if len(user_pattern) != len(string):
            continue  # Skip strings with different lengths

        match = True
        for index, char in user_pattern_dict.items():
            if string[index] != char:
                match = False
                break

        if match:
            matching_strings.append(string)

    return matching_strings


# Given list of strings
L = ['aabaabac', 'cabaabca', 'aaabbcba', 'aabacbab', 'acababba']

# Input from the user
user_pattern = input("Enter a pattern with '*' as placeholders: ")

matching_strings = match_patterns(user_pattern, L)

if matching_strings:
    print("Matching strings:", matching_strings)
else:
    print("No matching strings found.")
