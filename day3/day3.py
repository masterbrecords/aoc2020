with open("input.txt", "r") as input_file:
    input_list = input_file.readlines()

input_list = list(map(str.strip, input_list))


def check_for_tree(input_string, position):
    relative_position = position % len(input_string)
    if input_string[relative_position] == "#":
        return True
    else:
        return False


def check_slope(slope_v, slope_h):
    h_pos = 0
    trees = 0
    for v_pos, line in enumerate(input_list):
        if (v_pos % slope_v == 0):
            if check_for_tree(line, h_pos):
                trees = trees + 1
            h_pos += slope_h
    return trees


print("Anzahl der Bäume in Teil 1: {}".format(check_slope(1, 3)))

slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]

product = 1
for slope in slopes:
    product *= check_slope(*slope)

print("Produkt der Bäume in Teil 2: {}".format(product))
