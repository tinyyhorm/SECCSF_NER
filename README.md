# SECCSF_NER
SECCSF aims to improve the performance of named entity recognition models under low resource conditions by combining Chinese character structure with Chinese semantics.
# Dependencies
transformers==2.2.2  
botocore==1.23.26  
urllib3==1.26.8  
pytorch-crf  
torch==1.5.1  
torchvision==0.6.1  
scikit-learn==0.22.1  
# DataSet
We give a lightweight EPIC dataset as an example. Under the DataSet/0.25/, there is a 1/4 EPIC training dataset. The data encapsulates a dictionary in npz format, where 'words' and 'labels' are used as keys to store the original text and label data. The validation set is stored in the DataSet/Test/.
