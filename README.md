----------

__This project has since been updated to offer a web interface to simplify its use. Minor bugs have also been fixed. You can find this updated project [here](https://github.com/maphdev/Deep_Visualization_Neural_Networks_Web_app).__

----------

# Deep Visualization Neural Networks

Programmation project carried out as part of the Master's degree in Computer Science at the University of Bordeaux.

The main purpose is to offer an easy way to visualize convolutional neural networks, through two visualizations types described in the [paper](https://vadl2017.github.io/paper/vadl_0100-paper.pdf) of G. Strezoski et al. : Reason and MaxOut.

Visualizations are implemented with Keras, a high-level neural networks API written in Python and capable of running on top of Tensorflow, and Keras-vis, a high-level toolkit for visualizing and debugging trained keras neural networks models.

## Requirements :

The components below are required in order to use the visualizations.
- [Python3](https://www.python.org/downloads/)
- [Tensorflow](https://www.tensorflow.org/install/)
- [H5PY](http://docs.h5py.org/en/latest/build.html)
- [Keras](https://keras.io/)
- [Keras-vis](https://raghakot.github.io/keras-vis/)

## How to use the visualizations in terminal :

- Reason :
```bash
  python ./src/reason.py <model : path/name_model.h5> <image : path/name_image.jpg> <layer : int> <filter : int or "all"> <saved output : name.jpg>
```
- Maxout :
```bash
  python ./src/maxout.py <model : path/name_model.h5> <layer : int> <filter : int or "all"> <max_iter : int> <saved output : name.jpg>
```
## Load deep learning models with pre-trained weights

If you want to quickly experiment or you don't have any trained model available, you can easily load a model with weights pre-trained on ImageNet :

```bash
  python ./src/generate_models.py <name_1> <name_2> ...
```
Three models are available with this command :

- "VGG16" : a 22-layers network trained on ImageNet, with a default input size of 224x224.
- "ResNet50" : a 175-layers network trained on ImageNet, with a default input size of 224x224.
- "NASNetLarge" : a 1021-layers network trained on ImageNet, with a default input size of 331x331.

Models loaded with this command are generated in the "models" directory.
