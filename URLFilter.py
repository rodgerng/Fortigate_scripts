print ("Copyright 2021 created by Rodger Ng Yong Fung")
settype = input ("Enter Type e.g.{simple|regex|wildcard}:") 
setaction = input ("Enter Action e.g.{block|allow|monitor|exempt}:") 
import csv
print ("config webfilter urlfilter ")
print ("edit 1")
print ("config entries")
with open('blacklist.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        line_count == 0
        print   ("edit 0")
        print   (f'set url {" ".join(row)}')
        print   ("set type " + settype)
        print   ("set action " + setaction)
        print   ("next")
        print   ("end")
        line_count += 1
