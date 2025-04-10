# isONclust_analysis
This repository consists of the analysis scripts that were used during the isONclust3 study.


#Requirements
The analysis pipelines require several tools and python libraries to be installed in order to run.
Tools to be installed: 
1. `Minimap2`[LINK](https://github.com/lh3/minimap2)
2. `Samtools`[LINK](http://www.htslib.org/)
3. `isONclust`[LINK](https://github.com/ksahlin/isONclust)
4. `isONclust3`[LINK](https://github.com/aljpetri/isONclust3)
5. `Rattle`[LINK](https://github.com/comprna/RATTLE)
6. `GeLuster`[LINK](https://github.com/yutingsdu/GeLuster)

We ran isONclust3 using the official wrapper pipeline issued by ONT (pipeline-nanopore-denovo-isoforms)[LINK](https://github.com/nanoporetech/pipeline-nanopore-denovo-isoforms)

Python libraries to be installed:
1. `snakemake`
2. `pysam`
3. `scikit-learn`
4. `networkx`
 While snakemake is required to run the overall analysis pipeline, pysam and scikit-learn are needed for running the analysis scripts `compute_cluster_quality*.py`.
The structure of this repository is as follows: Evaluation consists of the actual analyses with each folder being one experiments. We used a wrapper bash script,submit_main_snakemake.sh,  to start jobs on our cluster using cluster specific resources as set in (cluster.json). The input folders and certain variables (e.g. k,w for the Different_k_w experiment), were set in cluster_config.json being the config file of the actual snakemake pipeline (located in snakefile).  

#Availability of the data
##Raw data
The datasets were downloaded using the following links:
[Drosophila](ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR358/005/ERR3588905/ERR3588905_1.fastq.gz), [SIRV](ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR358/003/ERR3588903/ERR3588903_1.fastq.gz), [ONT_human](https://www.ncbi.nlm.nih.gov/sra/DRX524696), [ALZ](https://downloads.pacbcloud.com/public/dataset/Alzheimer2019_IsoSeq/), [PB_human_SIRV](https://downloads.pacbcloud.com/public/dataset/UHRRisoseq2021/Intermediate-FullLengthReads/),[HG002](https://downloads.pacbcloud.com/public/dataset/Kinnex-full-length-RNA/DATA-Revio-HG002-1/2-FLNC/), [ONT_old](https://s3.amazonaws.com/nanopore-human-wgs/rna/fastq/Bham_Run1_20171115_1D.pass.dedup.fastq), [SIM](https://github.com/ksahlin/isONclust/blob/master/test/ccs.fastq.gz.part-ad)

##References
We downloaded the references used for this study from the following links:
[Human](https://github.com/marbl/CHM13), used for ONT_human, ALZ, HG002, SIM, merged with SIRV to yield the reference for PB_human_SIRV.<br />
[Drosophila](ftp://ftp.ensembl.org/pub/release-97/fasta/drosophila_melanogaster/dna/Drosophila_melanogaster.BDGP6.22.dna.toplevel.fa.gz)<br />
[SIRV](https://www.lexogen.com/wp-content/uploads/2018/08/SIRV_Set1_Lot00141_Sequences_170612a-ZIP.zip)

To be able to run the analysis pipelines on your machine please change the cluster related settings to according to your machines commands and change the input folders used by the snakemake pipeline (located in cluster_config.json) for each experimental pipeline you would like to run.
