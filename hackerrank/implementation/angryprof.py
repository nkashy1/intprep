def decision(n, k, arrivals):
    def pleasing(time):
        if time <= 0:
            return True
        return False

    if len(filter(pleasing, arrivals)) < k:
        return 'YES'
    return 'NO'

def run_case():
    parameters = map(int, raw_input().split())
    arrivals = map(int, raw_input().split())
    print decision(parameters[0], parameters[1], arrivals)

def run():
    cases = int(raw_input())
    for _ in range(cases):
        run_case()

run()