import sys


def run(input_file: str) -> None:
    with open(input_file) as buffer:
        input_data = buffer.read()
        instructions = input_data.splitlines()

    position = {
        'horizontal': 0,
        'vertical': 0
    }

    instruction_map = {
        'forward': {
            'direction': 'horizontal',
            'operator': lambda x, y: x + y
        },
        'down': {
            'direction': 'vertical',
            'operator': lambda x, y: x + y
        },
        'up': {
            'direction': 'vertical',
            'operator': lambda x, y: x - y
        }
    }

    for inst in instructions:
        instruction_direction, steps = inst.split()

        instruction = instruction_map[instruction_direction]
        direction, operation = instruction['direction'], instruction['operator']
        position[direction] = operation(position[direction], int(steps))

    print(position['horizontal'] * position['vertical'])


if __name__ == "__main__":
    try:
        input_file = sys.argv[1]
        run(input_file)
    except IndexError:
        print("Usage: python3 {__file__} <input_file>")
        sys.exit(1)
