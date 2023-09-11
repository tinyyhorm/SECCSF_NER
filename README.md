# SECCSF_NER
SECCSF aims to improve the performance of named entity recognition models under low resource conditions by combining Chinese Glaphs with Chinese semantics.
# Dependencies
transformers==2.2.2  
botocore==1.23.26  
urllib3==1.26.8  
pytorch-crf  
torch==1.5.1  
torchvision==0.6.1  
scikit-learn==0.22.1  
# DataSet
We give a lightweight EPIC dataset as an example. In the path of DataSet/0.25/, where is a 1/4 EPIC training dataset. The training dataset encapsulates a dictionary in npz format, where 'words' and 'labels' are used as keys to store the original text and label data. The validation set is stored in the path of DataSet/Test/.
# Performance
The following confusion matrices are the average performance of the four baseline models (BiLSTM-CRF\XLM-R-BiLSTM-CRF\RoBERTa-BiLSTM-CRF\SECCSF-BiLSTM-CRF) when 10 random seeds are  set into the training dataset and the validation dataset.
|The Confusion Matrices of Four Baselines|BiLSTM-CRF|XLM-R-BiLSTM-CRF|RoBERTa-BiLSTM-CRF|SECCSF-BiLSTM-CRF|
|:----:|:----:|:----:|:----:|:----:|
|||||
