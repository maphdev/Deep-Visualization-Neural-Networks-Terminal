import sys

from utils import *
from visualizations import *

def main(argv):

    check_number_arguments(argv, 6, "Usage : <model : path> <image : path> <layer : int> <filter : int or \"all\"> <saved output : name.png>")

    model = check_load_model(argv[1])
    image = check_load_image(model, argv[2])
    layer = check_get_selected_layer(model, argv[3])
    filters = check_get_selected_filters(model, layer, argv[4])

    image_mod = reason(model, image, layer, filters)

    save_image(image_mod, argv[5])
    
# Entree du programme
if __name__ == "__main__":
    main(sys.argv)
