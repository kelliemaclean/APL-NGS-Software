'''
Manta calls structural variants (SVs) and indels from mapped
paired-end sequencing reads. It is optimized for analysis of
germline variation in small sets of individuals and somatic variation
in tumor/normal sample pairs. Manta discovers, assembles and scores
large-scale SVs, medium-sized indels and large insertions within a
single efficient workflow. The method is designed for rapid analysis
on standard compute hardware: NA12878 at 50x genomic coverage is analyzed
in less than 20 minutes on a 20 core server, and most WGS tumor/normal
analyses can be completed within 2 hours. Manta combines paired and split-read
evidence during SV discovery and scoring to improve accuracy, but
does not require split-reads or successful breakpoint assemblies to
report a variant in cases where there is strong evidence otherwise.
It provides scoring models for germline variants in small sets of diploid
samples and somatic variants in matched tumor/normal sample pairs.
There is experimental support for analysis of unmatched tumor samples as well.
Manta accepts input read mappings from BAM or CRAM files and reports all SV 
and indel inferences in VCF 4.1 format. 
https://github.com/Illumina/manta
'''
