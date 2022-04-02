from collections.abc import Iterable

def parse_test_case(s):
    tokens = s.split()
    r = int(tokens[0])
    c = int(tokens[1])
    return {"rows": r, "cols": c}


# Solution
def solve(data):
    rows = data["rows"]
    cols = data["cols"]

    if rows <= 0:
        return
    if cols <= 0:
        return

    s = ""

    # Print first row
    for c in range(cols):
        if c == 0:
            s += '..+'
        else:
            s += '-+'
    s += '\n'

    for r in range(rows):
        # print middle
        if r == 0:
            # First row is special (dots!)
            for c in range(cols):
                if c == 0:
                    s += '.'
                s += '.|'
        else:
            # For other rows use regular pipes
            for c in range(cols):
                if c == 0:
                    s += '|'
                s += '.|'
        s += '\n'

        # print bottom
        for c in range(cols):
            if c == 0:
                s += '+'
            s += '-+'
        s += '\n'
    return s


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
        self.test_case_data = [read_func(next(input_string)) for _ in range(num_test_cases)]
        assert len(self.test_case_data) == num_test_cases

    def _read_input_string_std(self, read_func):
        num_test_cases = int(input())
        self.test_case_data = [read_func(input()) for _ in range(num_test_cases)]
        assert len(self.test_case_data) == num_test_cases

    def __iter__(self):
        return iter(self.test_case_data)


def main():
    wrapped_string = None

    # For testing
    # import os
    # from io import StringIO
    # raw_input_string = "".join(open(f'{os.path.dirname(os.path.realpath(__file__))}/sample_input.txt', 'r').readlines())
    # wrapped_string = StringIO(raw_input_string)

    input_reader = InputReader(parse_test_case, wrapped_string)
    for test_case_idx, data in enumerate(input_reader):
        print(f"Case #{test_case_idx + 1}:")
        print(solve(data))


if __name__ == "__main__":
    main()
