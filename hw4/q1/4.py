# Function to format a student record line
def format_student_record(line):
    # Split the line into parts separated by tabs
    parts = line.split('\t')

    if len(parts) == 4:
        first_name = parts[0].capitalize()
        last_name = parts[1].capitalize()
        email = parts[2]
        phone_number = parts[3].strip()
        
        # Check if the phone number starts with '301-' or '301'
        if not phone_number.startswith('301'):
            # If not, add '301-' before the phone number
            phone_number = '301-' + phone_number
        
        # Format the line with the modified information
        formatted_line = f"{first_name} {last_name} {email} {phone_number}\n"
        
        return formatted_line
    else:
        # Return the line as is if it doesn't have the expected format
        return line

# Open the input file for reading
with open('students.txt', 'r') as input_file:
    # Read the lines from the input file
    lines = input_file.readlines()

# Open the output file for writing
with open('students2.txt', 'w') as output_file:
    # Process each line and write it to the output file
    for line in lines:
        formatted_line = format_student_record(line)
        output_file.write(formatted_line)

print("File 'students2.txt' has been created with the formatted data.")
