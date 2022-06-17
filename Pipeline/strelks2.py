'''
Strelka2 is a fast and accurate small variant caller optimized for
analysis of germline variation in small cohorts and somatic variation
in tumor/normal sample pairs. The germline caller employs an efficient
tiered haplotype model to improve accuracy and provide read-backed phasing,
adaptively selecting between assembly and a faster alignment-based haplotyping
approach at each variant locus. The germline caller also analyzes input sequencing
data using a mixture-model indel error estimation method to improve robustness to
indel noise. The somatic calling model improves on the original Strelka method
for liquid and late-stage tumor analysis by accounting for possible tumor cell
contamination in the normal sample. A final empirical variant re-scoring step
using random forest models trained on various call quality features has been
added to both callers to further improve precision.
https://github.com/Illumina/strelka
'''
