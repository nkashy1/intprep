def run(height):
    def level(i):
        return ' '*(height - i - 1) + '#'*(i + 1)

    levels = map(level, range(height))
    print "\n".join(levels)

height = int(raw_input())
run(height)