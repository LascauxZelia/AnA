#!/usr/bin/env python

## Libraries 
import sys
import shutil
from os import system
import os.path
from pathlib import Path 

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
fastq_dir = os.path.join(path)+ '/' + input_dir

assembly_dir = "assembly"
os.makedirs(assembly_dir, exist_ok=True)

annotation_dir = "annotations"
os.makedirs(annotation_dir, exist_ok=True)

for filename in os.listdir(fastq_dir):
    print(filename)
    seq_name = filename[:-9]
    input_file = os.path.join(fastq_dir, filename)
    output_dir_megahit = os.path.join(assembly_dir, seq_name + '_megahit')
    #Megahit command
    megahit_command = f"megahit -t {cpu} --min-contig-len {min_contig_len} --k-step {kstep} --k-min {kmin} -o {output_dir_megahit} -r {input_file}"
    #Execute megahit command
    os.system(megahit_command)

    #Prodigal command
    output_dir_prodigal = os.path.join(annotation_dir, seq_name + '_prodigal')
    os.makedirs(output_dir_prodigal, exist_ok=True)
    prodigal_command = prodigal_command = f"prodigal -a {seq_name}_proteins.faa -d {seq_name}_genes.fas -i {output_dir_megahit}/final.contigs.fa -m -p meta -o  {seq_name}_prodigal_output.txt "
    os.system(prodigal_command)
    # Move Prodigal output files to the annotation directory
    shutil.move(f"{seq_name}_proteins.faa", os.path.join(output_dir_prodigal, f"{seq_name}_proteins.faa"))
    shutil.move(f"{seq_name}_genes.fas", os.path.join(output_dir_prodigal, f"{seq_name}_genes.fas"))
    shutil.move(f"{seq_name}_prodigal_output.txt", os.path.join(output_dir_prodigal, f"{seq_name}_prodigal_output.txt"))
