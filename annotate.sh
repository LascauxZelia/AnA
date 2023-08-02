#!/bin/bash

# Default values for Prodigal options
min_gene_length=150
metagenomic_mode=true
single_stranded=false
p_value=1e-5

# Parse command-line arguments
while [[ $# -gt 0 ]]; do
    key="$1"

    case $key in
        -i|--input-dir)
        input_dir="$2"
        shift # past argument
        shift # past value
        ;;
        --min-gene-len)
        min_gene_length="$2"
        shift # past argument
        shift # past value
        ;;
        --metagenomic-mode)
        metagenomic_mode="$2"
        shift # past argument
        shift # past value
        ;;
        --single-stranded)
        single_stranded="$2"
        shift # past argument
        shift # past value
        ;;
        --p-value)
        p_value="$2"
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

for file in $input_dir/*.fasta; do
    base=$(basename $file .fasta)
    prodigal -i $file -d $output_dir/${base}.faa -a $output_dir/${base}.ffn \
             -m ${metagenomic_mode:-$metagenomic_mode} \
             -s ${single_stranded:-$single_stranded} \
             -p meta -f gff \
             -c -m -g ${min_gene_length:-$min_gene_length} \
             -p ${p_value:-$p_value}
done
