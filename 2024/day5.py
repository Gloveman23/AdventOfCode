if __name__ == "__main__":
    file = open("input.txt")
    lines = file.readlines()
    rules = []
    updates = []
    mode = False
    for line in lines:
        if line == '\n':
            mode = True
            continue
        if mode:
            updates.append([int(a) for a in line.split(',')])
        else:
            rules.append(tuple(int(a) for a in line.split("|")))
    total = 0
    incorrect_updates = []
    for update in updates:
        correct = True
        for rule in rules:
            if not correct:
                break
            if any(i not in update for i in rule):
                continue
            else:
                for i in range(len(update)):
                    if update[i] == rule[0]:
                        break
                    elif update[i] == rule[1]:
                        correct = False
                        break
        if correct:
            index = 0.5*(len(update) - 1)
            total += update[int(index)]
        else:
            incorrect_updates.append(update)

    total2 = 0
    for update in incorrect_updates:
        active_rules = [rule for rule in rules if all(a in update for a in rule)]
        changes = True
        while changes:
            changes = False
            for i in range(0, len(update)-1):
                first = update[i]
                second = update[i+1]
                if any(first == b and second == a for (a,b) in active_rules):
                    update[i] = second
                    update[i+1] = first
                    changes = True
        total2 += update[int(0.5*(len(update)-1))]

    print(f"Part 1: {total}")
    print(f"Part 2: {total2}")
