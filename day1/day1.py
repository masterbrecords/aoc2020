input = []
with open("input.txt") as input_file:
    input = input_file.readlines()

input = [int(line.strip()) for line in input]

for number1 in input:
    for number2 in input:
        sum_result = number1 + number2
        if sum_result == 2020:
            print(number1 * number2)
            break
    else:
        continue
    break


for number1 in input:
    for number2 in input:
        for number3 in input:
            sum_result = number1 + number2 + number3
            if sum_result == 2020:
                print(number1 * number2 * number3)
                break
