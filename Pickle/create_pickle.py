"""Test for the creation of a pickle file based on images."""
import pickle
import os
from PIL import Image


def load_images(file_path):
    """Load image from file_path."""
    file_ext = r'.jpg'
    img_path_list = [
        os.path.join(file_path, _)
        for _ in os.listdir(file_path)
        if _.endswith(file_ext)
        ]
    img = [
        Image.open(imPath)
        for imPath in img_path_list
        ]
    return dict(
        [
            ('img_filename', img_path_list),
            ('img', img),
        ]
    )

def images_to_pickle(
        images_dict,
        pickle_destination,
        ):
    """Create the pickle file."""
    if not os.path.exists(pickle_destination):
        os.makedirs(pickle_destination)

    with open(pickle_destination + 'Images.pickle', 'wb') as file:
        pickle.dump(images_dict, file)

    print('Pickle create at '+str(pickle_destination))


if __name__ == "__main__":
    FILE_PATH = r'datasets/img/'
    PICKLE_DESTINATION = r'datasets/pickle/'
    images = load_images(FILE_PATH)
    images_to_pickle(images, PICKLE_DESTINATION)
