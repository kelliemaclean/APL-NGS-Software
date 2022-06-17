'''
Delly is an integrated structural variant (SV) 
prediction method that can discover, genotype and visualize deletions,
tandem duplications, inversions and translocations at single-nucleotide
resolution in short-read massively parallel sequencing data.
It uses paired-ends, split-reads and read-depth to sensitively and 
accurately delineate genomic rearrangements throughout the genome.
Structural variants can be annotated using Delly-sansa and visualized 
using Delly-maze or Delly-suave.
https://github.com/dellytools/delly

delly call -x hg19.excl -o delly.bcf -g hg19.fa input.bam

bcftools view delly.bcf > delly.vcf

'''