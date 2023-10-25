# drnet
DRNet: Efficient Few-Shot Learning Model for Regenerating Restricted-Access Area Maps

## Requirements

```
python==3.7 
numpy==1.18.5 
keras==2.4.3 
tensorflow==2.3.0 
matplotlib==3.3.0
scikit-image==0.16.2 
tqdm==4.45.0
```

## How to use

Train a new model with your map (in the image folder).
```
python DRnet/main.py --gpu --config config/roomA.json

--gpu                       Activates GPU acceleration for training
--config                    Path to config file in json format

```
./DRnet/sripts/eval_single_category.sh




