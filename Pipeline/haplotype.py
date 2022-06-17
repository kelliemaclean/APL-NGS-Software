'''
The HaplotypeCaller is capable of calling SNPs and indels simultaneously 
via local de-novo assembly of haplotypes in an active region.
In other words, whenever the program encounters a region showing signs
of variation, it discards the existing mapping information and completely
reassembles the reads in that region. This allows the HaplotypeCaller to be
more accurate when calling regions that are traditionally difficult to call,
for example when they contain different types of variants close to each other.
It also makes the HaplotypeCaller much better at calling indels than
position-based callers like UnifiedGenotyper.
https://gatk.broadinstitute.org/hc/en-us/articles/360037225632-HaplotypeCaller

'''

import os
cmd = (
    "gatk --java-options "-Xmx4g" HaplotypeCaller -R hg_38.fasta -I input.bam -O output.g.vcf.gz -ERC GVCF
)

os.popen(cmd)