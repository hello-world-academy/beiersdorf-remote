def image_crop(img, ratio=0.5):
    '''
    Function crop a PIL image object by a given ratio from 0 to 1.
    : img: PIL image object
    : ratio: float between 0 and 1
    : returns: a cropped PIL image object
    '''
    assert ratio > 0, print("Warning: Ratio shall be greater than 0")
    assert ratio <= 1, print("Warning: Ratio shall be lower than 1")
    center = (img.width // 2, img.height //2)
    upper_left_x = center[0] - center[0] * ratio
    upper_left_y = center[1] - center[1] * ratio
    lower_right_x = center[0] + center[0] * ratio
    lower_right_y = center[1] + center[1] * ratio
    return img.crop(box=(upper_left_x, upper_left_y, lower_right_x, lower_right_y))
