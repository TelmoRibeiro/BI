def count_letters(s):
    counter = 0
    for character in s:
        if character.isalpha():
            counter += 1
    print("#letters: " + str(counter))

def main():
    s = "HelloWorld"
    count_letters(s)

main()