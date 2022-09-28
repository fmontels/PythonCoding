"""Read the pickle file from the pickle path."""
import pickle


def open_pickle(pickle_path):
    """Open the pickle file from pickle_path."""
    with open(pickle_path, 'rb') as file:
        pickle_obj = pickle.load(file)

    return pickle_obj

def print_pickle(pickle_obj):
    """Show the pictures and print their names."""
    for i, img in enumerate(pickle_obj['img']):
        title = pickle_obj['img_filename'][i].split('/')[-1]
        img.show(
            title=title,
        )
        print(title)


if __name__ == "__main__":
    PICKLE_PATH = r'datasets/pickle/Images.pickle'
    pickle_object = open_pickle(PICKLE_PATH)
    print_pickle(pickle_object)
