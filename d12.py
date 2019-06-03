from collections import defaultdict



def main():
    with open("puzzleInputs/12.txt") as file:
        inp = file.readlines()
    init_str = to_num(inp[0].split(":")[1].strip())
    init_str_len = len(init_str)

    max_generations = 50000000000
    slice_size = 5
    padding = (slice_size - 1) * "0"
    pot_states = padding + init_str + padding

    rules = defaultdict(lambda: "0")
    for rule_str in inp[1:]:
        rule, result = [s.strip() for s in rule_str.split(" => ")]
        rules[to_index(rule)] = to_num(result)
    
    # 50bil will never complete, inspected loop and noticed that after 
    # 124 generations the sum always increase by 88. 
    # Cut the loop short here, and sum up any remaining generations later
    gens_processed = 0
    for gen in range(min(125, max_generations)):
        new_states = []
        for start_index in range(0, len(pot_states) + 1 - slice_size):
            asdf = pot_states[start_index : start_index + slice_size]
            new_states.append(rules[to_index(asdf)])
        pot_states = padding + "".join(new_states) + padding
        gens_processed += 1
        
        # Part 1
        if (gens_processed == 20):
            print(calc_pot_sum(pot_states, init_str_len))
    
    # Part 2
    pot_sum = calc_pot_sum(pot_states, init_str_len)
    pot_sum += 88 * max(0, max_generations - gens_processed)
    print(pot_sum)


conversion = str.maketrans({"#":"1", ".":"0"})
def to_num(s):
    return s.translate(conversion)

def to_index(s):
    return int(to_num(s), 2)

def calc_pot_sum(pot_states, init_size):
    offset = (len(pot_states) - init_size) // 2
    return sum([(ind - offset) * int(val) for ind, val in enumerate(pot_states)])

if __name__ == "__main__":
    main()
