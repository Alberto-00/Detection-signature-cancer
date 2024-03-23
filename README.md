# Leveraging gene expression and genomic varation for cancer prediction using one-shot learning
The Cancer Genome Atlas (TCGA), a cancer genomics reference program, has molecularly characterized more than 20,000 primary cancer samples and paired normal samples covering 33 types of cancer.
This joint effort between the NCI and the National Human Genome Research Institute began in 2006. In the twelve years since, TCGA has generated more than 2.5 petabytes of genomic, epigenomic, transcriptomic, and proteomics. These data have led to improvements in the ability to diagnose, treat and prevent cancer by helping to establish the importance of cancer genomics.

## Contribution of this work
During the experimental process, the size of the dataset used was significantly increased in order to improve the diversity and representativeness of the data. This adjustment allowed the model to learn from a wider variety of examples, improving its generalization. In addition, adjustments were made to both models involved in this study, both the classification model and the Siamese-type model. A key element of the optimization was the implementation of the use of custom weights. This strategy allowed different weights to be assigned to different instances of the dataset based on the amount of samples present. Finally, a specification was introduced regarding the types of mutations, this allowed for greater precision in the analysis of genetic information. Numerous studies aimed at identifying a distinctive genomic signature for different types of cancer are being conducted in the current research landscape.

## Requirements (tested)

| Module               | Version |
|----------------------|---------|
| tensorflow           | 2.15.0  |
| torch                | 2.1.2   |
| cuda                 | 12.2    |

To install tensorflow follow this guide: <a href="https://blog.tensorflow.org/2023/11/whats-new-in-tensorflow-2-15.html">link</a><br>
To install and set up cuda and cudnn follow this guide:
<ul>
  <li><a href="https://medium.com/@yulin_li/how-to-update-cuda-and-cudnn-on-ubuntu-18-04-4bfb762cf0b8">install cuda - cudnn on Ubuntu</a></li>
  <li><a href="https://developer.nvidia.com/cuda-12-2-0-download-archive?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=22.04&target_type=deb_local">Cuda 12.2</a></li>
  <li><a href="https://developer.nvidia.com/rdp/cudnn-archive">cuDNN</a></li>
</ul>

## Related work
For more information about our research project access the paper here: <a href="https://github.com/Alberto-00/Detection-signature-cancer/blob/main/exam/Bioinformatica_Paper_CancerDetection.pdf">our paper</a><br>
To view the other papers that have contributed to the cancer research study and on which we have commented follow this link: <a href="https://github.com/Alberto-00/Detection-signature-cancer/tree/main/papers">other papers</a><br>

## Technical informations - main.py
In this section we introduce technical informations and installing guides!

### Download Dataset
<ul>
  <li>Download from Google Drive all the files in the folder <code>Dataset</code>: <a href="https://drive.google.com/drive/folders/1sE_4XjG516zfMvnWwfQ3gR5h7_4NlvjL?usp=sharing">LINK</a>;</li>
  <li>Files should be downloaded within a folder with the name <code>dataset</code>;</li>
  <li>Copy the dataset folder and paste it inside the project in this way: <code>/Detection-signature-cancer/code/dataset</code></li>
</ul>

### Config Path
In this script there are some path that we are going to describe now:<br>

Dataset
<ol style="list-style-type: numbers;">
  <li><code>dataset_path</code>: the dataset that we want to use (<code>SNP_DEL_INS_CNA_mutations_and_variants</code> has two);</li>
  <li><code>encoded_path</code>: the encoded of the dataset;</li>
</ol>

Classification
<ol style="list-style-type: numbers;">  
  <li><code>model_path</code>: where the model will be saved or uploaded;</li>
  <li><code>risultati_classification</code>: results of the classification;</li>
</ol>

Siamese
<ol style="list-style-type: numbers;">  
  <li><code>siamese_path</code>: where the model of the siamese network will be saved or uploaded;</li>
  <li><code>risultati_siamese</code>: results of the siamese network;</li>
</ol>
<br><br>

If you want to change the dataset to use either <code>0030</code> or <code>0005</code> (read the paper for the meanings) you only 
need to edit the string containing <code>0030</code> or <code>0005</code> and replace it with one of the two.

For example:
```
dataset_path = ("dataset/data_mrna/SNP_DEL_INS_CNA_mutations_and_variants/"
                    "data_mrna_v2_seq_rsem_trasposto_normalizzato_deviazione_0030_dataPatient_mutations_and_variants.csv")      
```

Becomes

```
dataset_path = ("dataset/data_mrna/SNP_DEL_INS_CNA_mutations_and_variants/"
                    "data_mrna_v2_seq_rsem_trasposto_normalizzato_deviazione_0005_dataPatient_mutations_and_variants.csv")      
```

<br>

Or
```
model_path = "models/0030/classification/espressione_genomica_con_varianti_2LAYER/"
```

Becomes

```
model_path = "models/0005/classification/espressione_genomica_con_varianti_2LAYER/"
```

### Boolean Variables
Always in the <code>main.py</code> script you can set some variables:

<ul>
  <li><code>only_variant = False</code>: if you use the dataset that contains only variations in gene mutations set this on <code>True</code>;</li>
  <li><code>data_encoded = False</code>: allows to generate the encoded of the dataset (if this is the first time you run the code leave the default value) 
    <ul>
      <li><code>False</code>: encoded to be generated;</li>
      <li><code>True</code>code>: load an encoded;</li>
    </ul>
  </li>
  <li><code>classification = True</code>: run the classification;</li>
  <li><code>siamese_net = True</code>: run the siamese network;</li>
  <li><code>siamese_variants = True</code>: if you use the dataset that contains the variations in gene mutations set this on <code>True</code>;</li>
</ul>
<br>

The Siamese Network can only be launched if it has a classification model already trained and saved. In the project the classification model has already been trained. 
If you want to use the models in this project and not start experimenting again set the parameters in this way (example for <code>0030</code> dataset):
```
only_variant = False
data_encoded = True
classification = False
siamese_net = True
siamese_variants = True
```

To run the project run the <code>main.py</code> script.

## Author & Contacts 

| Name | Description |
| --- | --- |
| <p dir="auto"><strong>Alberto Montefusco</strong> |<br>Developer - <a href="https://github.com/Alberto-00">Alberto-00</a></p><p dir="auto">Email - <a href="mailto:a.montefusco28@studenti.unisa.it">a.montefusco28@studenti.unisa.it</a></p><p dir="auto">LinkedIn - <a href="https://www.linkedin.com/in/alberto-montefusco">Alberto Montefusco</a></p><p dir="auto">My WebSite - <a href="https://alberto-00.github.io/">alberto-00.github.io</a></p><br>|
| <p dir="auto"><strong>Alessandro Macaro</strong> |<br>Developer   - <a href="https://github.com/mtolkien">mtolkien</a></p><p dir="auto">Email - <a href="mailto:a.macaro@studenti.unisa.it">a.macaro@studenti.unisa.it</a></p><p dir="auto">LinkedIn - <a href="https://www.linkedin.com/in/alessandro-macaro-391b7a214/">Alessandro Macaro</a></p><br>|
