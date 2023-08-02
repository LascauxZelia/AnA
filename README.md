# AnA
A short metagenomic assembly pipeline and gene annotation
This pipeline is designed to assemble raw metagenomic sequencing data using SPAdes software and then annotate the predicted genes from the assembly using Prodigal.  

## Prerequisites
Make sure to have the following software installed before running the pipeline:
- SPAdes (https://cab.spbu.ru/software/spades/)
- Prodigal (https://github.com/hyattpd/Prodigal)

You can create a conda environment and install them:
`conda install SPAdes`
`conda install prodigal`

## Installation
1. Clone this repository to your local system using the following command:
   `git clone `

## Usage
1. Your metagenomic sequencing files in FASTQ format are in a same `data` directory.
2. Execute the pipeline by running the main script `main.sh`:
  `bash main.sh`
Make sure that the scripts are authorised to run. If not, run : `chmod +x assemble.sh annotate.sh main.sh`  
The pipeline will perform the following steps:
- Assembly with SPAdes: The metagenomic sequences will be assembled to form contigs in the `assembly` directory.
- Annotation with Prodigal: Predicted genes from the assembly will be annotated into proteins in the `.faa` and `.ffn` files in the `annotations` directory.

The final results will be available in the `assembly` and `annotations` directories.

## License

Specify the license under which you want to share the code ( GNU GENERAL PUBLIC LICENSE, Version 3).

## Contact

If you have any questions or comments about the pipeline, feel free to contact me at [zelia.bontemps@imbim.uu.se](mailto:zelia.bontemps@imbim.uu.se).
