# Open the input file for reading and the output file for writing
with open('class_scores.txt', 'r') as input_file, open('scores2.txt', 'w') as output_file:
    for line in input_file:
        # Split each line into a username and a test score
        parts = line.split()
        if len(parts) == 2:
            username, score_str = parts
            try:
                # Convert the score to an integer and add 5
                score = int(score_str) + 5
                # Write the username and the new score to the output file
                output_file.write(f"{username} {score}\n")
            except ValueError:
                print(f"Skipping invalid line: {line.strip()}")

print("Scores have been updated and written to 'scores2.txt'.")
