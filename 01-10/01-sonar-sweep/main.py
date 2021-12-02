import sys
from typing import List


def run(input_file: str) -> None:
    def count_increments(measurements: List[int]):
        result = 0
        for i, measure in enumerate(measurements):
            if measure > measurements[i - 1]:
                result += 1

        return result

    with open(input_file) as buffer:
        input_data = buffer.read()
        measurements = list(map(int, input_data.splitlines()))

    print(count_increments(measurements))


if __name__ == "__main__":
    try:
        input_file = sys.argv[1]
        run(input_file)
    except IndexError:
        print(f"Usage: python3 {__file__} <input_file>")
        sys.exit(1)
