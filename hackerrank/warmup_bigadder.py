# Enter your code here. Read input from STDIN. Print output to STDOUT
def longify(int_as_string):
    return long(int_as_string)

def add(x, y):
    return x + y

array_size = int(raw_input()) # Who cares?
result = reduce(add, map(longify, raw_input().split()))

print result