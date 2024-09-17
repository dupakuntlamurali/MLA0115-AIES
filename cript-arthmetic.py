from itertools import permutations

def word_to_number(word, mapping):
    return int(''.join(str(mapping[letter]) for letter in word))

def is_solution(words, result, perm):
    letters = set(''.join(words) + result)
    if len(letters) > 10:
        return False
    mapping = dict(zip(letters, perm))
    word_sum = sum(word_to_number(word, mapping) for word in words)
    result_number = word_to_number(result, mapping)
    return word_sum == result_number

def solve_cryptarithmetic(words, result):
    letters = set(''.join(words) + result)
    if len(letters) > 10:
        return "No solution, too many letters."
    for perm in permutations(range(10), len(letters)):
        if is_solution(words, result, perm):
            mapping = dict(zip(letters, perm))
            return mapping
    return "No solution."

def print_solution(words, result, solution):
    print(f"{' + '.join(words)} = {result}")
    if isinstance(solution, dict):
        for letter, digit in solution.items():
            print(f"{letter} = {digit}")
    else:
        print(solution)

words = ['SEND', 'MORE']
result = 'MONEY'

solution = solve_cryptarithmetic(words, result)
print_solution(words, result, solution)
