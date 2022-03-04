def fibo_thingy(terms):
    outer_count = terms
    num = 0
    num1 = 0
    num2 = 1
    while outer_count != 0:
        num2 = num + num2
        num = num1
        num1 = num2
        print(num2)
        outer_count -= 1
       
fibo_thingy(int(input()))
