#!/bin/sh
#SBATCH -A snic2022-5-592 
#SBATCH --time=5-00:00:00
#SBATCH -p core
#SBATCH -n 20
# Memory per node specification is in MB. It is optional. 
# The default limit is 3000MB per core.
#SBATCH --job-name="IsONformDrosophila"
#SBATCH --mail-user=alexander.petri@math.su.se
#SBATCH --mail-type=ALL

#conda init bash
set -o errexit

# --forcerun minimap2_align minimap2_map bwa_mem_align strobemap_align strobemap_map accelalign_align accelalign_map bowtie2_align
ml bioinfo-tools
ml snakemake/5.32.2
ml gcc/9.3.0
ml samtools
ml minimap2/2.28

snakemake --keep-going -j 999999 --configfile cluster_config.json --latency-wait 100 --verbose -n




