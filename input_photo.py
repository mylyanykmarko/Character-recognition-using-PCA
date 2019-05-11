from dataset_handler import read_img
import numpy as np


# Extract pixels from inpuyed photo and return them as list
def img_to_vector(path):
    # read image, returns list of lists
    img_matrix = read_img(path)
    # Concatenate all this list into one
    np_vector = np.concatenate(img_matrix)
    img_vector = [i for i in np_vector]
    return img_vector


# Transforms vector into mean deviation form
def to_deviation_form(vector, mean):
    for i in range(len(vector)):
        vector[i] -= mean[i]
    return vector


# Project photo at evc`s space
def project_photo(photo, evcs):
    projected_photo = []
    for i in evcs:
        projected_photo.append(np.inner(i, photo))
    return projected_photo
