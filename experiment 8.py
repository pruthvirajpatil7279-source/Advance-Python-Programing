# Open the input file in read mode
with open("input.txt", "r") as infile:
    lines = infile.readlines()          # read all lines into a list

# Count the number of lines
print("Total number of lines:", len(lines))

# Extract the first two lines
first_two = lines[:2]
print("First two lines:")
for line in first_two:
    print(line.strip())

# Write the extracted lines to a new file
with open("output.txt", "w") as outfile:
    outfile.writelines(first_two)

print("Extracted lines written to output.txt")