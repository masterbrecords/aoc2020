import re

with open("input.txt", "r") as input_file:
    input_list = input_file.readlines()

input_list = [rule.strip() for rule in input_list]


class Bag:
    def __init__(self, color: str, count: int = 1):
        self.color = color
        self.count = count

    def __repr__(self):
        return f"{self.count} {self.color} bags"


class Rule:
    def __init__(self, color: str, allowed_bag_list: list):
        self.color = color
        self.allowed_bag_list = allowed_bag_list

    def __repr__(self):
        return f"{self.color} bag contains {self.allowed_bag_list}"


rule_list = list()
expression = re.compile("(?:(\d*) (\w* \w*) (?:bags|bag)(?:, |\.))")
for line in input_list:
    split = line.split(" bags contain ")
    rule_color = split[0]
    bag_list = list()
    for item in expression.findall(split[1]):
        bag_list.append(Bag(item[1], int(item[0])))

    rule_list.append(Rule(rule_color, bag_list))


def get_rule(color: str):
    for rule in rule_list:
        if rule.color == color:
            return rule
    return None


def check_for_nested_bag(rule: Rule, search_color: str):
    result = False
    for bag in rule.allowed_bag_list:
        if bag.color == search_color:
            # print(f"Regel {rule} erlaubt {search_color} direkt")
            return True
        else:
            # print(f"Regel {rule} erlaubt nicht direkt {search_color}")
            result = check_for_nested_bag(get_rule(bag.color), search_color)
            if result:
                return True
    # print(f"Regel {rule} erlaubt keine weiteren Bags")
    return result


rule_count = 0
for rule in rule_list:
    if check_for_nested_bag(rule, "shiny gold"):
        rule_count += 1

print(f"Teil 1: shiny gold wird von {rule_count} Regeln erlaubt")


def calc_contained_bags(rule: Rule):
    if len(rule.allowed_bag_list) == 0:
        return 0
    else:
        contained_count = 0
        for bag in rule.allowed_bag_list:
            contained_count += bag.count
            contained_count += calc_contained_bags(
                get_rule(bag.color)) * bag.count
        return contained_count


print("Teil 2: shiny gold muss "
      f"{calc_contained_bags(get_rule('shiny gold'))} "
      "bags enthalten")
