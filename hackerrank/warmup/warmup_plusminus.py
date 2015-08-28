# Enter your code here. Read input from STDIN. Print output to STDOUT

array_size = int(raw_input())

array = map(int, raw_input().split())

def is_positive(x):
    return x > 0

positive_elts = filter(is_positive, array)

def is_negative(x):
    return x < 0

negative_elts = filter(is_negative, array)

def is_zero(x):
    return x == 0

zero_elts = filter(is_zero, array)

print float(len(positive_elts))/array_size
print float(len(negative_elts))/array_size
print float(len(zero_elts))/array_size