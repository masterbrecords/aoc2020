import re

with open("input.txt", "r") as input_file:
    input_list = input_file.readlines()

input_list = [line.strip() for line in input_list]


def check_password(first_position, second_position, letter, password):
    i = 0
    if password[int(first_position) - 1] == letter:
        i = i + 1
    if password[int(second_position) - 1] == letter:
        i = i + 1
    if i == 1:
        return True
        print("Passwort {} stimmt".format(password))
    else:
        return False


regex = re.compile("(\d+)-(\d+) (\w): (\w+)")


def interpret_line(input_string):
    matches = regex.search(input_string)
    if matches:
        return matches.groups()
    else:
        return False


correct_passwords = 0
for item in input_list:
    if check_password(*interpret_line(item)):
        correct_passwords = correct_passwords + 1
print(correct_passwords)
