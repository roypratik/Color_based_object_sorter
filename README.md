An object sorter based on color. Primarily we are using blue,green and red objects to distinguish images of the objects. We are using transfer learning on several pretrained models to compare the metrics of each of them.

Dataset:
Self-generated pictures.
Augmentation of the captured images.
Dataset from kaggle:
https://www.kaggle.com/ayanzadeh93/color-classification 


Installation commands:

git clone https://github.com/roypratik/Color_based_object_sorter.git

cd Color_based_object_sorter

Create (and activate) a new environment, named deep-learning with Python 3.6. If prompted to proceed with the install (Proceed [y]/n) type y.

Linux or Mac:
conda create -n deep-learning-neural python=3.6
source activate deep-learning

Windows:
conda create --name deep-learning-neural python=3.6
activate deep-learning

Install PyTorch and torchvision; this should install the latest version of PyTorch.

Linux or Mac:
conda install pytorch torchvision -c pytorch 

Windows:
conda install pytorch -c pytorch
pip install torchvision

Install a few required pip packages, which are specified in the requirements text file (including OpenCV).

pip install -r requirements.txt

jupyter notebook
