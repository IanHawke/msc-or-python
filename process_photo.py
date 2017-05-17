from skimage import io, transform, util

def process_photo(filename, size=(8,8)):
    """
    Returns a greyscale version of an image of a given size. If the original
    image has a different aspect ratio to the target size, the image will
    first be cropped before being resized to prevent it getting distorted.

    Parameters
    ----------
    filename : string
        name of image file (including path)
    size : int tuple
        size that we want input image to be rescaled to
    """
    # read photo as greyscale
    photo = io.imread(filename, as_grey=True)

    # crop photo so it's the correct ratio
    if photo.shape[0] / photo.shape[1] > size[0] / size[1]:
        crop_amount = int(0.5 * photo.shape[0] * (photo.shape[0] / photo.shape[1] - size[0] / size[1]))
        small_photo = util.crop(photo, ((crop_amount, crop_amount), (0,0)))
    else:
        crop_amount = int(0.5 * photo.shape[1] * (photo.shape[1] / photo.shape[0] - size[1] / size[0]))
        small_photo = util.crop(photo, ((0,0), (crop_amount, crop_amount)))

    # now resize the photo
    small_photo = transform.resize(small_photo, size)

    return small_photo
