# ExpreLev  
This tutorial will introduce how to run ExpreLev to obtain TPM/CPM/FPKM.

### ExpreLev can be used to obtain TPM/CPM/FPKM based on raw read count matrices.  

#### usage: 
```ExpreLev [-h] [-b] -I INPUTPATH -f FILENAME -d DISTANCE -r RESOLUTION -O OUTPATH -c CHRSIZE -o OUTFILE``` 


                     
optional arguments:  
|  |   |    |   |   |
|:----:|:-----:|:----:|:------:|:------:|  
| -h |  |--help|| show this help message and exit |
| -b ||  --balanced |   | contact matrix is iced or balanced |
| -I | INPUTPATH  | --inputpath | INPUTPATH |path of input file  |  
| -f | FILENAME   | --filename    | FILENAME |name of input file |
| -d | DISTANCE  | --distance |DISTANCE|the distance of distal chromation interactions|
| -r    |   RESOLUTION| --resolution | RESOLUTION| resolution of contact matrix  | 
| -O | OUTPATH    | --outpath |  OUTPATH |path of output file  |  
| -c | CHRSIZE    | --chrsize |  CHRSIZE |chromosome size file  |
| -o | OUTFILE    | --outfile |  OUTFILE |name of output file  |


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

#### pip install DLR-ICF==1.0.3
https://pypi.org/project/DLR-ICF/1.0.3/
