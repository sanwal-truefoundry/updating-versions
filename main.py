import os
import sys


def set_action_output(name: str, value: str):
    sys.stdout.write(f'::set-output name={name}::{value}\n')


def main():
    input_file = os.environ["INPUT_FILE"]

    with open(input_file, 'r') as f:
        data = f.readlines()
        print(data[2])
        print(data[2][-1])

    x = 4
    print(x)
    x=x+1
    print(x)

    set_action_output('new-version', x)

    sys.exit(0)


if __name__ == "__main__":
    main()