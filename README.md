# AnA
A short metagenomic assembly pipeline and gene annotation
This pipeline is designed to assemble raw metagenomic sequencing data using Megahit software and then annotate the predicted genes from the assembly using Prodigal.  

## Software information
Make sure to have the following software installed before running the pipeline:
- Megahit (https://github.com/voutcn/megahit)
- Prodigal (https://github.com/hyattpd/Prodigal)

## Installation
1. Clone this repository to your local system using the following command:
   `git clone https://github.com/LascauxZelia/AnA.git`
   
2. You can directly create the AnA conda environment with this command line:  
`conda env create -f env.yml`  
And then activate the environment :  
`conda activate AnA`  

Or you can manually create a conda environment and install the following packages:  
`conda install -c bioconda megahit`  
`conda install -c bioconda prodigal`

## Usage
1. Your metagenomic sequencing files in FASTQ format are in a same directory (for now, only merge files).
2. Customize MegaHit and Prodigal options (if needed) in the `main.sh` script:

   - MegaHit options:
     - `min_contig_length`: The minimum contig length to be reported. Default value is 500.
     - `k_min`: The minimum value of k (k-mer size) for the final assembly. Default value is 21.
     - `k_max`: The maximum value of k for the final assembly. Default value is 101.
     - `step_size`: The step size for incrementing k during assembly. Default value is 10.

   - Prodigal options:
     - `min_gene_length`: The minimum gene length to be reported. Default value is 150.
     - `metagenomic_mode`: Enable metagenomic mode for gene prediction. Default value is true.
     - `single_stranded`: Enable single-stranded mode for gene prediction. Default value is false.
     - `p_value`: The p-value threshold for gene prediction. Default value is 1e-5.  
       
3. Execute the pipeline by running the `main.sh` script:

```bash
bash main.sh \
  -i data \
  -o results \
  --num-threads 8 \
  --min-contig-len 1000 \
  --k-min 31 \
  --k-max 121 \
  --step-size 20 \
  --min-gene-len 100 \
  --metagenomic-mode false \
  --single-stranded true \
  --p-value 1e-3
```

Make sure that the scripts are authorised to run. If not, run : `chmod +x assemble.sh annotate.sh main.sh`  

The pipeline will perform the following steps:  
- Assembly with Megahit: The metagenomic sequences will be assembled to form contigs in the `assembly` directory.
- Annotation with Prodigal: Predicted genes from the assembly will be annotated into proteins in the `.faa` and `.ffn` files in the `annotations` directory.

The final results will be available in the `assembly` and `annotations` directories.

## License

Specify the license under which you want to share the code ( GNU GENERAL PUBLIC LICENSE, Version 3).

## Contact

If you have any questions or comments about the pipeline, feel free to contact me at [zelia.bontemps@imbim.uu.se](mailto:zelia.bontemps@imbim.uu.se).
