# example usage: python3 script.py "../BabelStream/build/" "omp-stream_gcc" "double" 

import sys
import subprocess
import csv
import numpy as np
from math import sqrt
from scipy import stats

prefix         = sys.argv[1]       
application    = sys.argv[2]
datatype       = sys.argv[3]

if datatype == "float":
  data_size_bytes = 4
  options         = ["--csv", "--numtimes", "2", "--float"]
else:
  data_size_bytes = 8
  options         = ["--csv", "--numtimes", "2"]

if len(sys.argv) > 4:
  options += ["--arraysize", sys.argv[4]]

function_names = {0: "copy", 1: "mul", 2: "add", 3: "triad", 4: "dot"}
n_measurements   = 100
n_functions      = len(function_names)
confidence_level = 0.95
data_size_bytes  = 8

data = np.empty((n_functions,n_measurements))

for i in range(n_measurements):
  res = subprocess.check_output([prefix + application] + options,text=True)
  rows = res.split("\n")
  for j in range(len(rows)):
    if rows[j].startswith("function,"):
       csv_row_start = j+1
       break
  for j in range(n_functions):
    data[j][i] = float((rows[csv_row_start+j].split(","))[5])
    
array_size = float((rows[csv_row_start].split(","))[2])
n_bytes = [array_size*(data_size_bytes * 2)] * 2 + [array_size*(data_size_bytes * 3)] * 2 + [array_size*(data_size_bytes * 2)]
means = [np.mean(data[j]) for j in range(n_functions)]
stds  = [np.std(data[j])  for j in range(n_functions)]
cis   = [stats.norm.interval(confidence_level, loc=means[j], scale=stds[j]/sqrt(n_measurements)) for j in range(n_functions)]

with open(application+".csv", "w") as csv_file:
   csv_writer = csv.writer(csv_file)
   csv_writer.writerow(["function", "bandwidth [B/s]", "avg. execution time [s]", "CI start [s]", "CI end [s]"])
   for j in range(n_functions):
     csv_writer.writerow([function_names[j],
     			  n_bytes[j] / means[j],
     			  means[j],
     			  cis[j][0],
     			  cis[j][1]
                          ])
