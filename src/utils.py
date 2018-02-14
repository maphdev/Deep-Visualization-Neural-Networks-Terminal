import os, sys

from keras import backend as K
from keras.models import load_model

from vis.visualization import get_num_filters
from vis.utils import utils

import matplotlib.image as mpimg

# Verifie si le nombre d'arguments est respecte, renvoie l'usage si ce n'est pas le cas
def check_number_arguments(argv, nb, usage):
    if len(argv) != nb:
        print(usage)
        sys.exit(1)

# Verifie la validite du chemin du model passe en parametre et renvoie le modele s'il existe
def check_load_model(path):
    if os.path.exists(path):
        return load_model(path)
    else:
        print("The path for the model doesn't exist.")
        sys.exit(1)

# Verifie la validite du chemin de l'image passe en parametre et renvoie l'image
def check_load_image(model, path):
    if os.path.exists(path):
        if K.image_data_format() == 'channels_first':
            image =  utils.load_img(path, target_size=(int(model.input.shape[2]), int(model.input.shape[3])))
            image = image.reshape(model.input.shape[1], model.input.shape[2], model.input.shape[3])
        elif K.image_data_format() == 'channels_last':
            image =  utils.load_img(path, target_size=(int(model.input.shape[1]), int(model.input.shape[2])))
            image = image.reshape(model.input.shape[1], model.input.shape[2], model.input.shape[3])
        return image
    else:
        print("The path for the image doesn't exist.")
        sys.exit(1)

# Verifie la validite du layer passe en argument (0:nb-1) et renvoie le layer s'il existe
def check_get_selected_layer(model, layer):
    numberOfLayers = len(model.layers)
    if int(layer) in range(0, numberOfLayers):
        return int(layer)
    else:
        print("There is no such layer.")
        sys.exit(1)

# Verifie la validite du filter passe en argument (0:nb-1) et renvoie le filter s'il existe
def check_get_selected_filters(model, layer, filters):
    if filters == "all":
        return None;
    elif int(filters) in range(0, get_num_filters(model.layers[layer])):
        return int(filters)
    else:
        print("There is no such filter.")
        sys.exit(1)

# Applique des modifications aux layers du modele afin de creer un nouveau graphe
def apply_modifications(model, custom_objects=None):
    model_path = 'tmp.h5'
    try:
        model.save(model_path)
        return load_model(model_path, custom_objects=custom_objects)
    finally:
        os.remove(model_path)

# Sauvegarder une image
def save_image(image, name):
    mpimg.imsave(name, image)
