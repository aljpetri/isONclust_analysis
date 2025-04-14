# isONclust_analysis
This repository consists of the analysis scripts that were used during the isONclust3 study as well as the results we obtained during our study.


# Table of contents
1. [Structure of the repository](#structure)
2. [Requirements](#requirements)
3. [Running the analysis scripts](#run_analyses)
4. [Availability of the data](#data_avail)
      1. [Rawdata](#raw)
      2. [References](#refs)
## Structure of the repository<a name="structure"></a>  
The repository contains the following folders: <br />
+[Evaluation](Evaluation) contains the evaluation scripts used for each experiment <br />
+[Results_Submitted](Results_Submitted) contains the results we obtained for the publication of the isONclust3 study ( doi: https://doi.org/10.1101/2024.10.29.620862 )<br />
+[isONclust2](isONclust2) contains the script run for the analysis of isONclust2 (seperate due to isONclust2 requiring its own wrapper script)<br />

## Requirements<a name="requirements"></a>

The analysis pipelines require several tools and python libraries to be installed in order to run.
Tools to be installed: 
1. `Minimap2`[LINK](https://github.com/lh3/minimap2)
2. `Samtools`[LINK](http://www.htslib.org/)
3. `isONclust`[LINK](https://github.com/ksahlin/isONclust)
4. `isONclust3`[LINK](https://github.com/aljpetri/isONclust3)
5. `Rattle`[LINK](https://github.com/comprna/RATTLE)
6. `GeLuster`[LINK](https://github.com/yutingsdu/GeLuster)

We ran isONclust2 using the official wrapper pipeline issued by ONT (pipeline-nanopore-denovo-isoforms)[LINK](https://github.com/nanoporetech/pipeline-nanopore-denovo-isoforms)

In addition, the following Python packages to be installed with ``pip install X`` for package `X` are

1. `snakemake`
2. `pysam`
3. `scikit-learn`
4. `networkx`

# Running the analysis scripts <a name="run_analyses"></a>
   
While snakemake is required to run the overall analysis pipeline, pysam and scikit-learn are needed for running the analysis scripts `compute_cluster_quality*.py`.
The structure of this repository is as follows: Evaluation consists of the actual analyses with each folder being one experiments. We used a wrapper bash script,submit_main_snakemake.sh, to start jobs on our cluster using cluster specific resources as set in (cluster.json). The input folders and certain variables (e.g. k,w for the Different_k_w experiment), were set in cluster_config.json, being the config file of the actual snakemake pipeline (located in snakefile). 

The experiments in the paper are separated into different snakemake pipelines. We ran each experiment pipeline on our high-performance cluster as: ``sbatch submit_main_snakemake.sh`` ( where `submit_main_snakemake.sh` is a shell script found in the respective evaluation folder [here](https://github.com/aljpetri/isONclust_analysis/tree/main/Evaluation) ). <br />

To run the `submit_main_snakemake.sh` shell script on your cluster in a slurm environment, please update the cluster parameters as satisfied by your cluster.


## Availability of the data<a name="data_avail"></a>

### Raw data<a name="raw"></a>

The datasets were downloaded using the following links:<br />
[Drosophila](https://www.ebi.ac.uk/ena/browser/view/PRJEB34849), [SIRV](https://www.ebi.ac.uk/ena/browser/view/PRJEB34849), [ONT_human](https://www.ncbi.nlm.nih.gov/sra/DRX524696), [ALZ](https://downloads.pacbcloud.com/public/dataset/Alzheimer2019_IsoSeq/), [PB_human_SIRV](https://downloads.pacbcloud.com/public/dataset/UHRRisoseq2021/Intermediate-FullLengthReads/), [HG002](https://downloads.pacbcloud.com/public/dataset/Kinnex-full-length-RNA/DATA-Revio-HG002-1/2-FLNC/), [ONT_old](https://s3.amazonaws.com/nanopore-human-wgs/rna/fastq/Bham_Run1_20171115_1D.pass.dedup.fastq), [SIM-500k (ccs.fastq.gz.part-aa-ad)](https://github.com/ksahlin/isONclust/tree/master/test)

### References<a name="refs"></a>

We downloaded the references used for this study from the following links: <br />
-[Human reference (CHM13)](https://github.com/marbl/CHM13): Used for ONT_human, ALZ, HG002 and SIM. <br />
-Drosophila reference: ftp://ftp.ensembl.org/pub/release-97/fasta/drosophila_melanogaster/dna/Drosophila_melanogaster.BDGP6.22.dna.toplevel.fa.gz <br />
-[SIRV](https://www.lexogen.com/wp-content/uploads/2018/08/SIRV_Set1_Lot00141_Sequences_170612a-ZIP.zip): Used for SIRV. <br />

For PB_human_SIRV we merged SIRV with Human as reference.



