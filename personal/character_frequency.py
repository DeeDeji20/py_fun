character = "success"

def check_occurrence_of_character(word):
    count = 0
    for character in word:
        if character == "s":
            count += 1
    print(count)
check_occurrence_of_character(character)    