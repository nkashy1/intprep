def run(word):
    L = len(word)

    def character_filter(c):
        def f(x):
            if x > c:
                return True
            return False
        return f

    def replacement_index(i):
        if i < L - 1:
            candidates = filter(character_filter(word[i]), word[i+1:])
            if len(candidates) == 0:
                return None
            replacement = min(candidates)
            return i + 1 + word[i+1:].find(replacement)
        return None

    result = "no answer"

    for i in range(L-2,-1,-1):
        j = replacement_index(i)
        if j is not None:
            word_as_list = list(word)
            temp = word_as_list[j]
            word_as_list[j] = word_as_list[i]
            word_as_list[i] = temp
            result = ''.join(word_as_list[:(i+1)] + sorted(word_as_list[(i+1):]))
            break

    print result

num_words = int(raw_input())
for _ in range(num_words):
    run(raw_input())
