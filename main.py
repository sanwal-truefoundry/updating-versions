import os
import sys


def set_action_output(name: str, value: str):
    sys.stdout.write(f'::set-output name={name}::{value}\n')


def main():
    input_file = os.environ["INPUT_FILE"]

    with open(input_file, 'r') as f:
        data = f.readlines()
        print(data[2])
        y = data[2]
        print(y[-1])

    print(y[-1])
    x=y[-1]+1
    print(y)

    set_action_output('new-version', y)

    sys.exit(0)


if __name__ == "__main__":
    main()