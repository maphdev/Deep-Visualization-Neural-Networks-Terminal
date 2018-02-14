import sys

from utils import *
from visualizations import *

def main(argv):

    check_number_arguments(argv,5, "Usage : <model : path> <layer : int> <filter : int or \"all\"> <saved output : name.png>")

    model = check_load_model(argv[1])
    layer = check_get_selected_layer(model, argv[2])
    filters = check_get_selected_filters(model, layer, argv[3])

    image_mod = maxout(model, layer, filters)

    save_image(image_mod, argv[4])
    
# Entree du programme
if __name__ == "__main__":
    main(sys.argv)


#choisir max_iter=?
