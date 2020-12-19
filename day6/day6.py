with open("input.txt", "r") as input_file:
	input_string = input_file.read()

input_list = input_string.split("\n\n")
input_list = [line.split("\n") for line in input_list]

sum_counts_different = 0
sum_counts_same = 0

for group in input_list:
	result_set = set()
	set_list = list()
	for answer in group:
		temp_set = set()
		for char in answer:
			result_set.add(char)
			temp_set.add(char)
		set_list.append(temp_set)
	
	sum_counts_different += len(result_set)
	sum_counts_same += len(set.intersection(*set_list))

print("Teil 1: Summe der unterschiedlichen Antworten: {}".format(sum_counts_different))
print("Teil 2: Summe der gleichen Antworten: {}".format(sum_counts_same))