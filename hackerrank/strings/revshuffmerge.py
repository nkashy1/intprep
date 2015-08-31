def run(revshuffmerged):
    length = len(revshuffmerged)
    revshuffmergedreversed = revshuffmerged[::-1]
    index = {}
    for i in range(length):
        try:
            index[revshuffmergedreversed[i]].append(i)
        except KeyError:
            index[revshuffmergedreversed[i]] = [i]

    frequencies = {c: len(locations)/2 for (c, locations) in index.items()}
    characters = sorted(frequencies.keys())

    current = []
    current_count = {c: 0 for c in characters}

    def concern(c):
        if current_count[c] < frequencies[c]:
            return True
        return False

    def admissible(k):
        for c in characters:
            if not (len([i for i in index[c] if i >= k]) >= frequencies[c] - current_count[c]):
                return False
        return True

    remaining_characters = sorted(filter(concern, characters))

    def construct(position, previous=None):
        for c in remaining_characters:
            i = min([j for j in index[c] if j >= position])
            if admissible(i):
                current.append(c)
                current_count[c] += 1
                if current_count[c] == frequencies[c]:
                    remaining_characters.remove(c)
                return i+1

    current_position = 0
    while len(current) < length/2:
        current_position = construct(current_position)

    print ''.join(current)

run(raw_input())