import os
import sys


def set_action_output(name: str, value: str):
    sys.stdout.write(f'::set-output name={name}::{value}\n')


def main():
    input_file = os.environ["INPUT_FILE"]

    with open(input_file, 'r') as f:
        print(f)

    x = f['version']
    print(x)
    x=x+1
    print(x)

    set_action_output('new-version', x)

    sys.exit(0)


if __name__ == "__main__":
    main()