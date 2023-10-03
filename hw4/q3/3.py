# Specify the names of the input files
file1_name = "file1.txt"
file2_name = "file2.txt"

# Specify the name of the output file
output_file_name = "combined_output.txt"

# Open the input files and the output file
with open(file1_name, "r") as file1, open(file2_name, "r") as file2, open(output_file_name, "w") as output_file:
    # Read lines from both files simultaneously
    lines_file1 = file1.readlines()
    lines_file2 = file2.readlines()

    # Determine the length of the shorter file
    min_length = min(len(lines_file1), len(lines_file2))

    # Combine lines from both files and write to the output file
    for i in range(min_length):
        combined_line = f"{lines_file1[i].strip()} {lines_file2[i].strip()}\n"
        output_file.write(combined_line)

print(f"Combined lines from '{file1_name}' and '{file2_name}' into '{output_file_name}'.")
