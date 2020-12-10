import re

with open("input.txt", "r") as input_file:
    input_string = input_file.read()

input_list = input_string.split("\n\n")
passports = [item.replace("\n", " ").strip() for item in input_list]

mandatory_items = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

verify_pattern = re.compile(r"(byr:((200[0-2])|(19[2-9][0-9]{1}))|iyr:((2020)|(201[0-9]))|eyr:((2030)|(202[0-9]))|hgt:(((19[0-3])|(1[5-8][0-9]{1}))cm|((7[0-6])|(6[0-9])|(59))in)|hcl:#[0-9a-fA-F]{6}|ecl:(amb|blu|brn|gry|grn|hzl|oth)|pid:\d{9}$|cid:.*)")

def verify_passport_quick(passport):
    items = [item.split(":")[0] for item in passport.split(" ")]
    if set(mandatory_items).issubset(items):
        return True
    else:
        return False

def verify_passport(passport):
    if not verify_passport_quick(passport):
        return False
    items = passport.split(" ")
    for item in items:
        if not verify_pattern.match(item.strip()):
            print("{} hat nicht gematched. Passport: '{}'".format(item, passport))
            return False
    return True

correct_passport_count_quick = 0
correct_passport_count = 0
for passport in passports:
    if verify_passport_quick(passport):
        correct_passport_count_quick += 1
    if verify_passport(passport):
        correct_passport_count += 1

print("Laut Aufgabe 1 sind {} Passports " \
      "korrekt".format(correct_passport_count_quick))
print("Laut Aufgabe 2 sind {} Passports " \
      "korrekt".format(correct_passport_count))
