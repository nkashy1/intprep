# The number up to which we should count.
N = int(raw_input())

if N < 1:
    raise ValueError("Argument should be a positive integer.")

for i in range(1, N+1):
    special_output = []
    if i%3 == 0:
        special_output.append("Fizz")
    if i%5 == 0:
        special_output.append("Buzz")

    if len(special_output) > 0:
        print ' '.join(special_output)
    else:
        print i
