#!/bin/sh
#SBATCH -A naiss2024-5-55 
#SBATCH --time=1-00:00:00
#SBATCH -p shared
#SBATCH -n 20
#SBATCH -N 1
#SBATCH --job-name="SIRV_isonclust1"
#SBATCH --mail-user=alexander.petri@math.su.se
#SBATCH --mail-type=ALL

#conda init bash
set -o errexit

# --forcerun minimap2_align minimap2_map bwa_mem_align strobemap_align strobemap_map accelalign_align accelalign_map bowtie2_align


snakemake --keep-going -j 999999 --cluster "sbatch -A {cluster.account} -p {cluster.p} -n {cluster.n} -N {cluster.N}  -t {cluster.runtime} -J {cluster.jobname} --mail-type={cluster.mail_type} --mail-user={cluster.mail}" --cluster-config cluster.json --cluster-config cluster.json --configfile cluster_config.json --latency-wait 100 --verbose 


