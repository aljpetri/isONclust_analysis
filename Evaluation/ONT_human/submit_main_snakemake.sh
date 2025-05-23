#!/bin/sh
#SBATCH -A naiss2024-5-55 
#SBATCH --time=1-00:00:00
#SBATCH -p shared
#SBATCH -n 20
#SBATCH -N 1
#SBATCH --job-name="ONT_human_analysis"
#SBATCH --mail-user=alexander.petri@math.su.se
#SBATCH --mail-type=ALL

#conda init bash
set -o errexit


ml bioinfo-tools
ml snakemake/5.30.1
ml gcc/9.3.0
ml samtools
ml minimap2/2.28
ml pysam/0.15.3-python3.7.2
ml scikit-learn/0.22.1

snakemake --keep-going -j 999999 --cluster "sbatch -A {cluster.account} -p {cluster.p} -n {cluster.n} -N {cluster.N}  -t {cluster.runtime} -J {cluster.jobname} --mail-type={cluster.mail_type} --mail-user={cluster.mail}" --cluster-config cluster.json --cluster-config cluster.json --configfile cluster_config.json --latency-wait 100 --verbose 




