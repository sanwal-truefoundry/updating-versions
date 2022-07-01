import os
import sys


def set_action_output(name: str, value: str):
    sys.stdout.write(f'::set-output name={name}::{value}\n')


def main():
    first_input_file = os.environ["INPUT_FILE-1"]
    second_input_file = os.environ["INPUT_FILE-2"]
    third_input_file = os.environ["INPUT_FILE-3"]

    with open(first_input_file, 'r') as f1:
        data1 = f1.readlines()
        y1 = data1[5]

    print(y1)
    l1 = len(y1)
    x1=str(int(y1[l1-3:l1-1])+1)
    print(x1)
    z1 = y1[9:13]+x1

    with open(second_input_file, 'r') as f2:
        data2 = f2.readlines()
        y2 = data2[2]

    print(y2)
    l2 = len(y2)
    x2=str(int(y2[l2-3:l2-1])+1)
    print(x2)
    z2 = y2[9:13]+x2

    with open(third_input_file, 'r') as f3:
        data3 = f3.readlines()
        y3 = data3[2]

    print(y3)
    l3 = len(y3)
    x3 = str(int(y3[l3-3:l3-1])+1)
    print(x3)
    z3 = y3[9:13]+x3

    set_action_output('new-version-1', z1)
    set_action_output('new-version-2', z2)
    set_action_output('new-version-3', z3)

    sys.exit(0)


if __name__ == "__main__":
    main()