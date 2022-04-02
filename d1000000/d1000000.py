from collections.abc import Iterable


# Solution
def parse_test_case(s):
    out = {
        'dices': int(s[0]),
        'sides': [int(i) for i in s[1].split()]
    }
    return out


def solve(data):
    dices = sorted(data['sides'])
    cur = 1
    for d in dices:
        if d >= cur:
            cur += 1
    return cur-1


# Utilities
class InputReader(Iterable):
    test_case_data = []

    def __init__(self, read_func, input_string=None):
        if input_string:
            self._read_input_string_file(read_func, input_string)
        else:
            self._read_input_string_std(read_func)

    def _read_input_string_file(self, read_func, input_string):
        num_test_cases = int(next(input_string))
        self.test_case_data = [read_func([next(input_string), next(input_string)])
                               for _ in range(num_test_cases)]
        assert len(self.test_case_data) == num_test_cases

    def _read_input_string_std(self, read_func):
        num_test_cases = int(input())
        self.test_case_data = [read_func([input(), input()])
                               for _ in range(num_test_cases)]
        assert len(self.test_case_data) == num_test_cases

    def __iter__(self):
        return iter(self.test_case_data)


def main():
    wrapped_string = None

    # For testing
    # import os
    # raw_input_string = "".join(open(f'{os.path.dirname(os.path.realpath(__file__))}/sample_input.txt', 'r').readlines())
    # from io import StringIO
    # wrapped_string = StringIO(raw_input_string)

    input_reader = InputReader(parse_test_case, wrapped_string)
    for test_case_idx, data in enumerate(input_reader):
        print(f"Case #{test_case_idx + 1}: {solve(data)}")


if __name__ == '__main__':
    main()
