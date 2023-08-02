#!/bin/bash

# Default values for MegaHit options
min_contig_length=500
k_min=21
k_max=101
step_size=10

# Default values for Prodigal options
min_gene_length=150
metagenomic_mode=true
single_stranded=false
p_value=1e-5

# Parse command-line arguments for MegaHit and Prodigal options
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

# Call the assemble.sh script with provided arguments
bash assemble.sh \
  -i ${input_dir:-data} \
  -o ${output_dir:-assembly} \
  --num-threads ${num_threads:-4} \
  --min-contig-len ${min_contig_length:-$min_contig_length} \
  --k-min ${k_min:-$k_min} \
  --k-max ${k_max:-$k_max} \
  --step-size ${step_size:-$step_size}

# Call the annotate.sh script with provided arguments
bash annotate.sh \
  -i ${output_dir:-assembly} \
  --min-gene-len ${min_gene_length:-$min_gene_length} \
  --metagenomic-mode ${metagenomic_mode:-$metagenomic_mode} \
  --single-stranded ${single_stranded:-$single_stranded} \
  --p-value ${p_value:-$p_value}
