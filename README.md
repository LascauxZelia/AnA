# AnA
A short automatic metagenomic Assembly aNd gene Annotation pipeline
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
   `<input_dir>`, you need to put the name of your directory here. This directory must be in `AnA/`.   
2. Customize MegaHit and Prodigal options (if needed) in the `main.sh` script:

   - MegaHit options:
     - `min_contig_length`: The minimum contig length to be reported. Default value is 1000.
     - `k_min`: The minimum value of k (k-mer size) for the final assembly. Default value is 21.
     - `k_step`: increment of kmer size of each iteration (<= 28), must be even number. Default value is 20
     - `cpu`: Number of threads. Default value is 20.

   - Prodigal options:
     - `m`: Enable metagenomic mode for gene prediction. Default value is true.
       
3. Execute the pipeline by running the `main.py` script:

```bash
python main.py <input_dir> <cpu> <min_contig_len> <kstep> <kmin>
```
For example: If my merged reads are in a directory called 'data' I can run the following command :

```bash
python main.py data
```

Make sure that the scripts are authorised to run. If not, run : `chmod +x main.py`  

The pipeline will perform the following steps:  
- Assembly with Megahit: The metagenomic sequences will be assembled to form contigs in the `assembly/{seq_name}_megahit/` directory.
- Annotation with Prodigal: Predicted genes from the assembly will be annotated into proteins in the `.faa` and `.ffn` files in the `annotations` directory.

The final results will be available in the `assembly` and `annotations` directories.

## License

Specify the license under which you want to share the code (GNU GENERAL PUBLIC LICENSE, Version 3).

## Contact

If you have any questions or comments about the pipeline (or need to add more options), feel free to contact me at [zelia.bontemps@imbim.uu.se](mailto:zelia.bontemps@imbim.uu.se).
