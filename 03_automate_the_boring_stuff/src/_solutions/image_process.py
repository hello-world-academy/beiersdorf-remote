def image_process(img):
    '''
    Function to apply a series of image processing and enhancement steps on an image
    : img: a PIL image object
    : return: a copy of a processed/enhanced PIL image object
    '''
    # crop
    img = image_crop(img, ratio=2/3)
    # rotate
    theta = 180
    img = img.rotate(angle=theta)
    # gray scale
    enhancer = ImageEnhance.Color(img)
    img = enhancer.enhance(0)
    return img.copy() # returns a copy