# ExpreLev  
This tutorial will introduce how to run ExpreLev to obtain TPM/CPM/FPKM.

### ExpreLev can be used to obtain TPM/CPM/FPKM based on raw read count matrices.  

#### usage: 
##### calculate the expression levels for genes based on reads mapped to gene body (e.g., PRO-seq) 
```ExpreLevGene [-h] -g GTF -i INPUT -d DEPTH -t TYPEID [-o OUT]```  
##### calculate the expression levels for genes based on reads mapped to gene exon (e.g., RNA-seq)
```ExpreLevExon [-h] -g GTF -i INPUT -d DEPTH -t TYPEID [-o OUT]```  
##### calculate the enrichment for epigenetic signals based on reads peak regions (e.g., ChIP-seq/ATAC-seq)
**the the first 3 columns of input file is chr,start,end**  
```ExpreLevEpi [-h] -i INPUT -d DEPTH -t TYPEID [-o OUT]```  
                     
optional arguments:  
|  |   |    |   |   |
|:----:|:-----:|:----:|:------:|:------:|  
| -h |  |--help|| show this help message and exit |
| -g |  --GTF | --gtf|GTF|standard GTF annotation file (https://www.gencodegenes.org/)|
| -i | --INPUT  | --input | INPUT |input file (raw read count matrices)  |  
| -d | --DEPTH  | --depth |DEPTH|the total mapped reads file|
| -o | --OUT    | --out |  OUT |name of output file  |


### Installation 
#### requirement for installation
python>=3.8  
numpy  
pandas  
argparse  
cooler   
h5py  
scipy.stats   
statsmodels.stats.multitest  

#### pip install ExpreLev==1.0.3
https://pypi.org/project/ExpreLev/1.0.3/
