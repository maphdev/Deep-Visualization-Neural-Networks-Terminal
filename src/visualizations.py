from keras import activations
from vis.visualization import visualize_cam, visualize_activation, overlay
from vis.input_modifiers import Jitter
from utils import *

# Visualisation Reason
def reason(model, image, layer, filters):
    # Changer l'activation softmax par linear
    model.layers[layer].activation = activations.linear
    model = apply_modifications(model)
    
    grads = visualize_cam(model, layer, filter_indices=filters, backprop_modifier="guided", grad_modifier=None, seed_input=image)
    grads = overlay(grads, image)
    return grads

# Visualisation MaxOut
def maxout(model, layer, filters):
    # Changer l'activation softmax par linear
    model.layers[layer].activation = activations.linear
    model = apply_modifications(model)

    act = visualize_activation(model, layer, filter_indices=filters, tv_weight=1., lp_norm_weight=0., verbose=True, input_modifiers=[Jitter(16)])
    return act
