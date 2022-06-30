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

    l = len(y)
    print(int(y[l-5:l-3]))
    x=str(int(y[l-5:l-3])+1)
    print(x)
    z = y[9:12]+x
    print(z)

    set_action_output('new-version', z)+

    sys.exit(0)


if __name__ == "__main__":
    main()