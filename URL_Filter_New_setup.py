f = open("WebFilterScript.txt", "w")
#f.write("Created by Rodger Ng Yong Fung\n")
setId = input ("Enter id e.g.{1}:")
setname = input ("Set Name:")
settype = input ("Enter Type e.g.{simple|regex|wildcard}:") 
setaction = input ("Enter Action e.g.{block|allow|monitor|exempt}:") 
import csv
f.write("config webfilter urlfilter\n ")
f.write ("edit " + setId + "\n")
f.write ("set name " + setname +"\n")
f.write ("config entries\n")
with open('blacklist.csv') as csv_file: #open a file name blacklist.csv
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader: #read all the lines of a file 
        line_count == 0
        f.write  ("edit 0\n")
        f.write  (f'set url {" ".join(row)}\n') #write url name
        f.write  ("set type " + settype + "\n")
        f.write  ("set action " + setaction +"\n")
        f.write  ("set status enable\n")
        f.write  ("next\n")
        f.write  ("end\n")
        line_count += 1
f.close()
