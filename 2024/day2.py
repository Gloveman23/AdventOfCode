def test_this(report2):
    ALL_GOOD = True
    ALL_UP = True
    ALL_DOWN = True
    levels = [int(level) for level in report2]
    steps = [(levels[t+1]-levels[t]) for t in range(len(levels)-1)]
    for step in steps:
        if (s := abs(step)) < 1 or s >= 4:
            ALL_GOOD = False
        if step > 0:
            ALL_DOWN = False
        if step < 0:
            ALL_UP = False
    return ALL_GOOD and (ALL_UP or ALL_DOWN)


if __name__ == "__main__":
    file = open("input.txt")
    reports = file.readlines()
    reports = [a.removesuffix('\n').split(" ") for a in reports]
    safe = 0
    semisafe = 0
    reports3 = reports.copy()
    for report in reports:
        gut = test_this(report)
        if gut:
            safe += 1
            semisafe += 1
            reports3.remove(report)
    test_reports = [[report.copy() for i in range(len(report))] for report in reports3]
    for test_report_group in test_reports:
        gut = False
        i = 0
        for test_report in test_report_group:
            test_report = test_report[:i] + test_report[i+1:]
            gut = (b := test_this(test_report)) or gut
            i += 1
            if gut:
                break
        if gut:
            semisafe += 1

    print(f"Part 1: {safe}")
    print(f"Part 2: {semisafe}")
