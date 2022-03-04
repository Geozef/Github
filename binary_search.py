import random

while 1:

    array = [random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9)]

    array = sorted(array)
    term = -1
    found = 0
    while found == 0:
        term = int(input(array))
        for i in array:
            if i == term:
                found = 1

    term_high = len(array) - 1
    term_low =  0
    term_mid = len(array)//2
    while array[term_mid] != term:
        if array[term_mid] > term:
            term_low = term_mid 
        else:
            term_high = term_mid
        term_mid = (term_high - term_low)//2
    print("Term is item", term_mid, "in list.")


