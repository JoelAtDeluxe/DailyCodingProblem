import json


def solution_1(l):
    # inefficient. Retrieves the product several times over. O(n2)
    rtn = []

    if l is None:
        return rtn

    list_length = len(l)
    for i in range(list_length):
        first_half, _ = product(l[0:i])
        second_half, _ = product(l[i + 1: list_length])
        rtn.append(first_half * second_half)

    return rtn


def solution_2_with_div(l):
    # More efficient. Goes through the array twice, providing constant time
    rtn = []
    if l is None:
        return rtn

    total, zero_count = product(l, skip_zeros=True)
    if zero_count > 1:
        return [0 for i in range(len(l))]

    for i in range(len(l)):
        if l[i] == 0:
            rtn.append(total)
        elif zero_count == 1:
            rtn.append(0)
        else:
            rtn.append(int(total/l[i]))
    return rtn


# def solution_3_no_div(l):
#     if l in (None, []):
#         return []

#     if len(l) == 1:
#         return [1]
    
#     total, zero_count = product(l[1:])  # skip the first element
#     rtn = [1 for i in range(len(l))]
#     for idx, num in enumerate(rtn):
#         if idx == 0:
#             rtn[0] = total
#         else:
#             rtn[idx] = 


def product(some_list, skip_zeros=False):
    list_product = 1
    zero_count = 0
    for item in some_list:
        if item == 0:
            zero_count += 1
            if skip_zeros:
                continue
        list_product = list_product * item
    return list_product, zero_count


def load_tests(file_path='tests.json'):
    with open(file_path) as fh:
        return json.load(fh)


def mainline():
    data = load_tests()
    tests = data.get('tests')
    
    solutions = [solution_1, solution_2_with_div]

    for solution_index, solution_func in enumerate(solutions):
        print(f"Solution {solution_index}")
        for idx, test in enumerate(tests):
            actual = solution_func(test.get('data'))
            if actual != test.get('expected'):
                print(f'\tfor test {idx + 1} I expected: {test.get("expected")} but got: {actual}')
            else:
                print(f'\tTest {idx + 1} passed!')


if __name__ == "__main__":
    mainline()
