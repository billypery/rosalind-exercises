"""This code receives 2 numbers: n = number of months, k = number of offspring pairs, and calculates the
total number of rabbits at month n (immortal Fibonacci rabbits)"""

n_k = open("n_k","r")
n_k = n_k.read()
n_k = n_k.split()
num_of_months = int(n_k[0])
num_of_pairs = int(n_k[1])

def get_total_rabbit_num(months,pairs):
    range_months = range(1,months+1)
    total_rabbit_for_each_month = {}
    for month in range_months:
        if month == 1 or month == 2:
            total_rabbit_for_each_month[month] = 1
        else:
            total_rabbit_for_each_month[month] = (pairs*total_rabbit_for_each_month[month-2])+ (total_rabbit_for_each_month[month-1])
    return total_rabbit_for_each_month

dict_of_months_and_rabbits = get_total_rabbit_num(num_of_months,num_of_pairs)

for k,v in dict_of_months_and_rabbits.items():
    print ("Month: %s" %k," Total pairs of rabbits: %s" %v)
