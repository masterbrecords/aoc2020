with open("input.txt", "r") as input_file:
    input_list = input_file.readlines()

input_list = [line.strip() for line in input_list]

def calc_binary(input_string, positive_char, char_count):
    result = 0
    i = char_count - 1
    for char in input_string:
        if char == positive_char:
            result += 2**i
        i -= 1
    return result

def calc_row(input_string):
    return calc_binary(input_string, "B", 7)

def calc_column(input_string):
    return calc_binary(input_string, "R", 3)

def calc_seat_id(boarding_pass):
    row = calc_row(boarding_pass[0:7])
    column = calc_column(boarding_pass[7:10])
    return row * 8 + column

result_list = [calc_seat_id(boarding_pass) for boarding_pass in input_list]

print("Teil 1: Höchste Seat ID: {}".format(max(result_list)))

result_list.sort()

last_item = min(result_list) - 1
for pass_id in result_list:
    if pass_id - last_item > 1:
        print("Teil 2: Fehlende Seat ID: {}".format(pass_id - 1))
    last_item = pass_id

