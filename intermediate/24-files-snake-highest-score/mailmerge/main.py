#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"

with open("./Input/Letters/starting_letter.txt") as file_letter:
    content = file_letter.read()

with open("./Input/Names/invited_names.txt") as file:
    lines = file.readlines()
    for line in lines:
        new_letter = content.replace(PLACEHOLDER, line.strip())
        with open(f"./Output/ReadyToSend/letter_for_{line.strip()}.txt", "w") as file_letter_for:
            file_letter_for.write(new_letter)
