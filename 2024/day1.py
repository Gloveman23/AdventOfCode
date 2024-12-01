import math

if __name__ == '__main__':
    file = open("input.txt")
    lines = file.readlines()
    list1 = []
    list2 = []
    for line in lines:
        e1, e2 = line.split('   ')
        list1.append(int(e1))
        list2.append(int(e2))
    list1.sort()
    list2.sort()
    diffs = [abs(list1[x] - list2[x]) for x in range(len(list1))]
    total = sum(diffs)
    print(f'Total difference: {total}')
    
    total2 = 0
    for num in list1:
        count = 0
        count = list2.count(num)
        total2 += num * count
        
    print(f'Similarity score: {total2}')