N = int(input())
K = int(input())
i = 0
count_fives = 0
count_evens = 0
divisible_by_three = N%3==0
if divisible_by_three:
    while N>=10**i:
        digit = (N%(10**(i+1)))//(10**i)
        if digit%2==0:
            count_evens += 1
        if digit == 5:
            count_fives += 1
        i += 1
else:
    while N>=10**i:
        digit = (N%(10**(i+1)))//(10**i)
        if digit == 5:
            count_fives += 1
        i += 1

choose_2_i=i*(i-1)/2

def prob_last_five(k):
    if k==0:
        if N%5==0:
            return 1
        else:
            return 0
    a = (prob_last_five(k-1) * (choose_2_i - i) + count_fives + 0.0)/choose_2_i
    return a

def prob_last_even(k):
    if k==0:
        if N%2==0:
            return 1
        else:
            return 0
    a = (prob_last_even(k-1) * (choose_2_i - i) + count_evens + 0.0)/choose_2_i
    return a

