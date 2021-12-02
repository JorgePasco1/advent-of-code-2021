import sys


def run(input_file: str) -> None:
    with open(input_file) as buffer:
        input_data = buffer.read()


if __name__ == "__main__":
    try:
        input_file = sys.argv[1]
        run(input_file)
    except IndexError:
        print("Usage: python3 {__file__} <input_file>")
        sys.exit(1)
