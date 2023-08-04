#!/usr/bin/env python

## Libraries 
import csv
import sys
import shutil
from os import system
import os.path
from pathlib import Path 
import pandas

# debug
from pprint import pprint

try:
    input_dir = sys.argv[1]
    cpu = sys.argv[2]
    min_contig_len = sys.argv[3]
    kstep = sys.argv[4]
    kmin = sys.argv[5]
except IndexError: 
    print('Warning!\nNumber of threads not specified!\nUsing 20 threads...')
    cpu = '20'
    print('Warning!\nMinimum contig lenght not specified!\nDefault 1000...')
    min_contig_len = '1000'
    print('Warning!\nk step not specified!\nDefault 10...')
    kstep = '10'
    print('Warning!\nK min not specified!\nDefault 21...')
    kmin = '21'

path = os.getcwd()
fastq_dir = os.path.join(path) + input_dir

print(fastq_dir)

for filename in os.listdir(fastq_dir):
    print(filename)
    seq_name = filename[:-9]
    input_file = os.path.join(fastq_dir, filename)
    output_dir_megahit = seq_name + '_megahit'
    #Megahit command
    megahit_command = f"megahit -t {cpu} --min-contig-len {min_contig_len} --k-step {kstep} --k-min {kmin} -o {output_dir_megahit} -r {input_file}"
    #Execute megahit command
    os.system(megahit_command)
