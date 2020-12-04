from fractions import Fraction

import numpy as np
from PIL import Image

from util.richlog import get_logger
from . import imgops
from . import resources
from . import util

logger = get_logger(__name__)


def get_friend_corners(img):
    """
    :returns: [0][1]
              [3][2]
    """
    aspect = Fraction(*img.size)
    vw, vh = util.get_vwvh(img)
    if aspect == Fraction(16, 9):
        return (np.array((22.734*vw, 76.667*vh)), np.array((33.203*vw, 76.667*vh)), np.array((33.203*vw, 82.083*vh)), np.array((22.734*vw, 82.083*vh)))
    else:
        return [x[0] for x in imgops.find_homography(resources.load_image_cached('main/friends.png', 'L'), img)]
       
def get_friend_list(img):
    """
    :returns: [0][1]
              [3][2]
    """
    aspect = Fraction(*img.size)
    vw, vh = util.get_vwvh(img)
    if aspect == Fraction(16, 9):
        return (np.array((1.484*vw, 25.694*vh)), np.array((16.797*vw, 25.694*vh)), np.array((16.797*vw, 36.111*vh)), np.array((1.484*vw, 36.111*vh)))
    else:
        # FIXME: implement with feature matching?
        raise NotImplementedError('unsupported aspect ratio')
        
def get_friend_build(img):
    """
    :returns: [0][1]
              [3][2]
    """
    aspect = Fraction(*img.size)
    vw, vh = util.get_vwvh(img)
    if aspect == Fraction(16, 9):
        return (np.array((74.065*vw, 17.134*vh)), np.array((79.967*vw, 17.134*vh)), np.array((79.967*vw, 28.065*vh)), np.array((74.065*vw, 28.065*vh)))
    else:
        # FIXME: implement with feature matching?
        raise NotImplementedError('unsupported aspect ratio')
        
def get_next_friend_build(img):
    """
    :returns: [0][1]
              [3][2]
    """
    aspect = Fraction(*img.size)
    vw, vh = util.get_vwvh(img)
    if aspect == Fraction(16, 9):
        return (np.array((85.625*vw, 79.444*vh)), np.array((99.531*vw, 79.444*vh)), np.array((99.531*vw, 93.750*vh)), np.array((85.625*vw, 93.750*vh)))
    else:
        # FIXME: implement with feature matching?
        raise NotImplementedError('unsupported aspect ratio')

def get_store(img):
    aspect = Fraction(*img.size)
    vw, vh = util.get_vwvh(img)
    if aspect == Fraction(16, 9):
        return (60.000*vw, 60.278*vh, 70.703*vw, 71.806*vh)
    else:
        # FIXME: implement with feature matching?
        raise NotImplementedError('unsupported aspect ratio')

def get_creditstore(img):
    aspect = Fraction(*img.size)
    vw, vh = util.get_vwvh(img)
    if aspect == Fraction(16, 9):
        return (85.859*vw, 11.389*vh, 97.734*vw, 17.778*vh)
    else:
        # FIXME: implement with feature matching?
        raise NotImplementedError('unsupported aspect ratio')

def get_creditstore_credit(img):
    aspect = Fraction(*img.size)
    vw, vh = util.get_vwvh(img)
    if aspect == Fraction(16, 9):
        return (75.703*vw, 3.611*vh, 83.203*vw, 7.361*vh)
    else:
        # FIXME: implement with feature matching?
        raise NotImplementedError('unsupported aspect ratio')

def get_creditstore_ith_good(img, i, j):
    # return the pos of i^th good
    aspect = Fraction(*img.size)
    vw, vh = util.get_vwvh(img)
    if aspect == Fraction(16, 9):
        return ((5.391 + 19.766*i)*vw, (29.167 + 35.139*j)*vh, (17.891 + 19.766*i)*vw, (45.417 + 35.139*j)*vh)
    else:
        # FIXME: implement with feature matching?
        raise NotImplementedError('unsupported aspect ratio')

def get_creditstore_good_buy(img):
    aspect = Fraction(*img.size)
    vw, vh = util.get_vwvh(img)
    if aspect == Fraction(16, 9):
        return (65.000*vw, 77.639*vh, 78.594*vw, 83.750*vh)
    else:
        # FIXME: implement with feature matching?
        raise NotImplementedError('unsupported aspect ratio')

def check_unenough_credit(img):
    vw, vh = util.get_vwvh(img.size)
    icon1 = img.crop((81.016*vw, 11.389*vh, 97.734*vw, 19.583*vh)).convert('RGB')
    icon2 = resources.load_image_cached('credit/unenough_credit.png', 'RGB')

    icon1, icon2 = imgops.uniform_size(icon1, icon2)
    mse = imgops.compare_mse(np.asarray(icon1), np.asarray(icon2))
    # print(mse, icon1.size)
    logger.logimage(icon1)
    logger.logtext('mse=%f' % mse)
    return mse < 2000


def get_metting_room(img):
    aspect = Fraction(*img.size)
    vw, vh = util.get_vwvh(img)
    if aspect == Fraction(16, 9):
        return 
    else:
        # FIXME: implement with feature matching?
        raise NotImplementedError('unsupported aspect ratio')

def get_clue_daily(img):
    aspect = Fraction(*img.size)
    vw, vh = util.get_vwvh(img)
    if aspect == Fraction(16, 9):
        return 
    else:
        # FIXME: implement with feature matching?
        raise NotImplementedError('unsupported aspect ratio')

def get_clue_daily_receive(img):
    aspect = Fraction(*img.size)
    vw, vh = util.get_vwvh(img)
    if aspect == Fraction(16, 9):
        return 
    else:
        # FIXME: implement with feature matching?
        raise NotImplementedError('unsupported aspect ratio')

def get_clue_friend(img):
    aspect = Fraction(*img.size)
    vw, vh = util.get_vwvh(img)
    if aspect == Fraction(16, 9):
        return 
    else:
        # FIXME: implement with feature matching?
        raise NotImplementedError('unsupported aspect ratio')

def check_clue_friend(img):
    return 1