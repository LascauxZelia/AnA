#!/usr/bin/env python3

import argparse
import os
import subprocess

def assemble(input_dir1, input_dir2, output_dir, num_threads=4, min_contig_length=500, k_min=21, k_max=101, step_size=10):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Perform metagenomic assembly with MegaHit for each paired-end read file
    for r1_file in os.listdir(input_dir1):
        if r1_file.endswith(".fastq"):
            r1_base = os.path.splitext(r1_file)[0]
            r2_file = os.path.join(input_dir2, f"{r1_base}_R2.fastq")
            output_subdir = os.path.join(output_dir, f"{r1_base}_megahit_output")

            # Run MegaHit command
            cmd = [
                "megahit",
                "-1", os.path.join(input_dir1, r1_file),
                "-2", r2_file,
                "-o", output_subdir,
                "--num-cpu-threads", str(num_threads),
                "--min-contig-len", str(min_contig_length),
                "--k-min", str(k_min),
                "--k-max", str(k_max),
                "--k-step", str(step_size)
            ]

            subprocess.run(cmd)

def main():
    parser = argparse.ArgumentParser(description="Metagenomic Assembly with MegaHit")
    parser.add_argument("-i1", "--input-dir1", required=True, help="Input directory for R1 FASTQ files")
    parser.add_argument("-i2", "--input-dir2", required=True, help="Input directory for R2 FASTQ files")
    parser.add_argument("-o", "--output-dir", required=True, help="Output directory for assembly results")
    parser.add_argument("--num-threads", type=int, default=4, help="Number of threads for assembly (default: 4)")
    parser.add_argument("--min-contig-len", type=int, default=500, help="Minimum contig length to be reported (default: 500)")
    parser.add_argument("--k-min", type=int, default=21, help="Minimum value of k for the final assembly (default: 21)")
    parser.add_argument("--k-max", type=int, default=101, help="Maximum value of k for the final assembly (default: 101)")
    parser.add_argument("--step-size", type=int, default=10, help="Step size for incrementing k during assembly (default: 10)")

    args = parser.parse_args()

    assemble(args.input_dir1, args.input_dir2, args.output_dir, args.num_threads, args.min_contig_len, args.k_min, args.k_max, args.step_size)

if __name__ == "__main__":
    main()
