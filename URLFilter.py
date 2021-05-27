import sys
import csv
original_stdout = sys.stdout
print("Copyright 2021 created by Rodger Ng Yong Fung")
types = input("Enter Type e.g.{simple|regex|wildcard}:")
action = input("Enter Action e.g.{block|allow|monitor|exempt}:")
with open('cmdoutput.txt', 'w') as f:
    sys.stdout = f
    print("config webfilter urlfilter ")
    print("edit 1")
    print("config entries")
    with open('blacklist.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count: int = 0
        for row in csv_reader:
            print("edit 0")
            print(f'set url {" ".join(row)}')
            print("set type " + types)
            print("set action " + action)
            print("next")
            print("end")
        line_count += 1
    sys.stdout = original_stdout
