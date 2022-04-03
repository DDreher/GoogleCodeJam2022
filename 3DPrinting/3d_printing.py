from collections.abc import Iterable

# Constants
REQUIRED_VAL = 1e6
NUM_COLORS = 4
RESULT_IMPOSSIBLE = "IMPOSSIBLE"


# Solution
def parse_test_case(s):
    out = {'c': [], 'm': [], 'y': [], 'k': []}

    def append(tokens):
        out['c'].append(int(tokens[0]))
        out['m'].append(int(tokens[1]))
        out['y'].append(int(tokens[2]))
        out['k'].append(int(tokens[3]))

    # printer 0
    append(s[0].split())
    # printer 1
    append(s[1].split())
    # printer 2
    append(s[2].split())
    return out


def solve(data):
    min_values = [min(data['c']), min(data['m']), min(data['y']), min(data['k'])]
    sum_min_values = sum(min_values)

    if sum_min_values < REQUIRED_VAL:
        # If even the minima don't suffice, then we can't solve
        return RESULT_IMPOSSIBLE

    out_values = [0, 0, 0, 0]
    ink_required = REQUIRED_VAL
    for i in range(NUM_COLORS):
        out_values[i] = min(min_values[i], ink_required)
        ink_required -= out_values[i]

    assert(ink_required == 0)
    return " ".join(str(int(v)) for v in out_values)


# Utilities
class InputReader(Iterable):
    test_case_data = []

    def __init__(self, read_func, input_string=None):
        if input_string:
            self.read_input_string_from_file(read_func, input_string)
        else:
            self.read_input_string_from_stdin(read_func)

    def read_input_string_from_file(self, read_func, input_string):
        num_test_cases = int(next(input_string))
        self.test_case_data = [read_func([next(input_string), next(input_string), next(input_string)])
                               for _ in range(num_test_cases)]
        assert len(self.test_case_data) == num_test_cases

    def read_input_string_from_stdin(self, read_func):
        num_test_cases = int(input())
        self.test_case_data = [read_func([input(), input(), input()])
                               for _ in range(num_test_cases)]
        assert len(self.test_case_data) == num_test_cases

    def __iter__(self):
        return iter(self.test_case_data)


def main():
    wrapped_string = None

    # For testing - Uncomment to read from file
    # import os
    # raw_input_string = "".join(open(f'{os.path.dirname(os.path.realpath(__file__))}/sample_input.txt', 'r').readlines())
    # from io import StringIO
    # wrapped_string = StringIO(raw_input_string)

    input_reader = InputReader(parse_test_case, wrapped_string)
    for test_case_idx, data in enumerate(input_reader):
        print(f"Case #{test_case_idx + 1}: {solve(data)}")


if __name__ == '__main__':
    main()
