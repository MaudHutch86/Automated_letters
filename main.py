# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("Input/Names/invited_names.txt") as names:
    names = names.readlines()
    print(names)
with open("Input/letters/starting_letter.txt") as letter:
    letter_contents = letter.read()
    for n in names:
        strip_name = n.strip()
        changed_letter = letter_contents.replace("[name],", f"{n},")
        with open(f"./Output/ReadyToSend/letter_for_{strip_name}.txt", mode="w") as i:
            i.write(changed_letter)
