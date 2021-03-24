# Deep-SKIE---USCAP

This repository includes the codes used to generate the results for the Deep-SKIE pipeline mentioned in the paper [Improving the accuracy of gastrointestinal neuroendocrine tumor grading with deep learning](https://www.nature.com/articles/s41598-020-67880-z)

## Generation of training set
SKIE was used to generate the following classes of each hot-spot sized tile (500 x 500 µm) obtained via non-overlapping sliding window technique from double-immunostained WSIs (synaptophysin and Ki-67):
- Class 0 : >70% background
- Class 1 : <20 % tumor
- Class 2 : Tumor grade 1
- Class 3 : Tumor grade 2
The subsequent counterparts of H&E and Ki-67 only WSIs were trained to generate "Model_he" and "Model_Ki67".

## Training the models

### Model_syn:

Inception V3 was used to train all models mentioned here (10 epochs, batch size 32). Model_syn is the model trained on synaptophysin-Ki67 double immunostained images.
The code `TrainModel_syn.py` should be run in order to train the model again. 


### Model_he:

Model_he is the model trained on H&E-stained images. The code `TrainModel_he.py` should be run in order to train the model again.


### Model_Ki67:

Model_Ki67 is the model trained on Ki67-hematoxylin-stained images. The code `TrainModel_Ki67.py` should be run in order to train the model again. 


## Testing the models

Modify `Test_all_models.py` to specify the test folder and the model (.h5 file) to be used for testing. The results will be saved in a csv file as two columns : filenames and predictions.  

## Display heat-map of predictions

The code `csvToMask.py` (within `Display_results` folder) reads the saved csv file to generate a dictionary of filenames to predictions. These filenames are then used to find the location of the hot-spot sized tile within the WSI and the predicted class names for each tile is used to generate a heatmap.

