#!/bin/bash

# Default values for MegaHit options
min_contig_length=500
k_min=21
k_max=101
step_size=10

# Parse command-line arguments
while [[ $# -gt 0 ]]; do
    key="$1"

    case $key in
        -i|--input-dir)
        input_dir="$2"
        shift # past argument
        shift # past value
        ;;
        -o|--output-dir)
        output_dir="$2"
        shift # past argument
        shift # past value
        ;;
        --num-threads)
        num_threads="$2"
        shift # past argument
        shift # past value
        ;;
        --min-contig-len)
        min_contig_length="$2"
        shift # past argument
        shift # past value
        ;;
        --k-min)
        k_min="$2"
        shift # past argument
        shift # past value
        ;;
        --k-max)
        k_max="$2"
        shift # past argument
        shift # past value
        ;;
        --step-size)
        step_size="$2"
        shift # past argument
        shift # past value
        ;;
        *)    # unknown option
        echo "Unknown option: $key"
        exit 1
        ;;
    esac
done

# Create the output directory if it doesn't exist
mkdir -p $output_dir

for file in $input_dir/*.fastq; do
    base=$(basename $file .fastq)
    megahit -r $file -o $output_dir/${base}_megahit_output \
            --num-cpu-threads ${num_threads:-4} \
            --min-contig-len ${min_contig_length:-$min_contig_length} \
            --k-min ${k_min:-$k_min} \
            --k-max ${k_max:-$k_max} \
            --k-step ${step_size:-$step_size}
done
