#!/usr/bin/python
import re

fold_name = "D:\\_WorkSpace_\\80_NewSLIM\\10_S&M\\#AppSupport\\2014\\201407\\20140728_01_storage_io_performance_issue\\"
in_file_name = "iostat_20140728.log"
out_file_name = "iostat_20140728.log.analysis.by.python.txt"

in_file = open(fold_name+in_file_name, "r")
out_file = open(fold_name+out_file_name, "w")

#line = in_file.readline()

for line in in_file:
	#match datetime
	match = re.match(r'.*PM.*', line)
	if match:
		datetime = line
		continue
	#match title
	match = re.match(r'^Device:.*', line)
	if match:
		out_file.write(line[0:-1] + "\tdatetime\n")
		continue
	#match data
	match = re.match(r'.*sd[hijkl].*|^dm-2.*', line)
	if match:
		out_file.write(line[0:-1] + "\t" + datetime)
		continue

in_file.close()
out_file.close()