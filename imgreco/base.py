from fractions import Fraction

import numpy as np
from PIL import Image

from util.richlog import get_logger
from . import imgops
from . import resources
from . import util

logger = get_logger(__name__)


def get_back_my_build(img):
    """
    :returns: [0][1]
              [3][2]
    """
    aspect = Fraction(*img.size)
    vw, vh = util.get_vwvh(img)
    if aspect == Fraction(16, 9):
        return (np.array((72.266*vw, 81.528*vh)), np.array((88.750*vw, 81.528*vh)), np.array((88.750*vw, 92.500*vh)), np.array((72.266*vw, 92.500*vh)))
    else:
        # FIXME: implement with feature matching?
        raise NotImplementedError('unsupported aspect ratio')

# 点击基建主界面右上角的提示（以凸显一键收取）

def check_emergency_task(img):
    vw, vh = util.get_vwvh(img.size)
    #(1175, 71) + (56, 44) = (1231, 115)
    icon1 = img.crop((91.796 * vw, 9.861 * vh, 96.171 * vw , 15.972 * vh)).convert('RGB')
    icon2 = resources.load_image_cached('base/emergency.png', 'RGB')

    icon1, icon2 = imgops.uniform_size(icon1, icon2)
    mse = imgops.compare_mse(np.asarray(icon1), np.asarray(icon2))
    # print(mse, icon1.size)
    logger.logimage(icon1)
    logger.logtext('mse=%f' % mse)
    return mse < 2000

def check_room_clear(img):
    #查看是否有清空按钮
    vw, vh = util.get_vwvh(img.size)
    #(1150,6) + (97,48) = (1231, 115)
    icon1 = img.crop((89.843 * vw, 0.833 * vh, 97.421 * vw , 7.500 * vh)).convert('RGB')
    icon2 = resources.load_image_cached('base/clear.png', 'RGB')

    icon1, icon2 = imgops.uniform_size(icon1, icon2)
    mse = imgops.compare_mse(np.asarray(icon1), np.asarray(icon2))
    # print(mse, icon1.size)
    logger.logimage(icon1)
    logger.logtext('mse=%f' % mse)
    return mse < 2000

def check_room_commerical(img):
    #查看是否是贸易站
    vw, vh = util.get_vwvh(img.size)
    icon1 = img.crop((32.656*vw, 82.361*vh, 41.875*vw, 90.278*vh)).convert('RGB')
    icon2 = resources.load_image_cached('base/commerical.png', 'RGB')

    icon1, icon2 = imgops.uniform_size(icon1, icon2)
    mse = imgops.compare_mse(np.asarray(icon1), np.asarray(icon2))
    # print(mse, icon1.size)
    logger.logimage(icon1)
    logger.logtext('mse=%f' % mse)
    return mse < 2000

def check_room_battle_record(img):
    #查看是否是在造战斗记录的制造站
    vw, vh = util.get_vwvh(img.size)
    icon1 = img.crop((2.188*vw, 77.083*vh, 10.469*vw, 92.639*vh)).convert('RGB')
    icon2 = resources.load_image_cached('base/battle_record.png', 'RGB')

    icon1, icon2 = imgops.uniform_size(icon1, icon2)
    mse = imgops.compare_mse(np.asarray(icon1), np.asarray(icon2))
    # print(mse, icon1.size)
    logger.logimage(icon1)
    logger.logtext('mse=%f' % mse)
    return mse < 2000

def check_room_gold(img):
    #查看是否是在造赤金的制造站
    vw, vh = util.get_vwvh(img.size)
    icon1 = img.crop((2.188*vw, 77.083*vh, 10.469*vw, 92.639*vh)).convert('RGB')
    icon2 = resources.load_image_cached('base/gold.png', 'RGB')

    icon1, icon2 = imgops.uniform_size(icon1, icon2)
    mse = imgops.compare_mse(np.asarray(icon1), np.asarray(icon2))
    # print(mse, icon1.size)
    logger.logimage(icon1)
    logger.logtext('mse=%f' % mse)
    return mse < 2000

def check_room_power(img):
    #查看是否是发电站
    vw, vh = util.get_vwvh(img.size)
    icon1 = img.crop((0.859*vw, 84.583*vh, 10.469*vw, 96.250*vh)).convert('RGB')
    icon2 = resources.load_image_cached('base/power.png', 'RGB')

    icon1, icon2 = imgops.uniform_size(icon1, icon2)
    mse = imgops.compare_mse(np.asarray(icon1), np.asarray(icon2))
    # print(mse, icon1.size)
    logger.logimage(icon1)
    logger.logtext('mse=%f' % mse)
    return mse < 2000


def get_room_clear(img):
    #清空房间
    aspect = Fraction(*img.size)
    vw, vh = util.get_vwvh(img)
    if aspect == Fraction(16, 9):
        return (91.016*vw, 1.389*vh, 96.875*vw, 6.667*vh)
    else:
        # FIXME: implement with feature matching?
        raise NotImplementedError('unsupported aspect ratio')
def get_staff_info(img):
    """
    :returns: 
    
    """
    #进驻信息:(30, 250), (120, 340)
    aspect = Fraction(*img.size)
    vw, vh = util.get_vwvh(img)
    if aspect == Fraction(16, 9):
        return (2.343*vw, 34.722*vh, 16.666*vw, 47.222*vh)
    else:
        # FIXME: implement with feature matching?
        raise NotImplementedError('unsupported aspect ratio')

def get_room_current(img):
    #进驻信息:(870, 108), (1200, 200)
    aspect = Fraction(*img.size)
    vw, vh = util.get_vwvh(img)
    if aspect == Fraction(16, 9):
        return (73.047*vw, 13.472*vh, 90.859*vw, 25.556*vh)
    else:
        # FIXME: implement with feature matching?
        raise NotImplementedError('unsupported aspect ratio')

def get_my_build_task(img):
    """
    :returns: [0][1]
              [3][2]
    """
    aspect = Fraction(*img.size)
    vw, vh = util.get_vwvh(img)
    if aspect == Fraction(16, 9):
        return (np.array((92.031*vw, 10.417*vh)), np.array((99.688*vw, 10.417*vh)), np.array((99.688*vw, 15.417*vh)), np.array((92.031*vw, 15.417*vh)))
    else:
        # FIXME: implement with feature matching?
        raise NotImplementedError('unsupported aspect ratio')

def get_my_build_task_emergency(img):
    """
    :returns: [0][1]
              [3][2]
    """
    #(119, 162)/720
    aspect = Fraction(*img.size)
    vw, vh = util.get_vwvh(img)
    if aspect == Fraction(16, 9):
        return (np.array((92.031*vw, 16.520*vh)), np.array((99.688*vw, 16.520*vh)), np.array((99.688*vw, 22.500*vh)), np.array((92.031*vw, 22.500*vh)))
    else:
        # FIXME: implement with feature matching?
        raise NotImplementedError('unsupported aspect ratio')

# 一键收取制造站的物品
def get_my_build_task_clear(img):
    """
    :returns: [0][1]
              [3][2]
    """
    aspect = Fraction(*img.size)
    vw, vh = util.get_vwvh(img)
    if aspect == Fraction(16, 9):
        return (np.array((12.500*vw, 91.667*vh)), np.array((16.797*vw, 91.667*vh)), np.array((16.797*vw, 98.472*vh)), np.array((12.500*vw, 98.472*vh)))
    else:
        # FIXME: implement with feature matching?
        raise NotImplementedError('unsupported aspect ratio')

def get_base_med(img, i):
    """
    :returns: the i^th dorm pos
    """

    
    aspect = Fraction(*img.size)
    vw, vh = util.get_vwvh(img)
    if aspect == Fraction(16, 9):
        return (60.937*vw, (38.888 + i*10000.0/720.0)*vh, 70.312*vw, (47.222 + i*10000.0/720.0)*vh)
    else:
        # FIXME: implement with feature matching?
        raise NotImplementedError('unsupported aspect ratio')

def get_dorm_ok(img):
    aspect = Fraction(*img.size)
    vw, vh = util.get_vwvh(img)
    if aspect == Fraction(16, 9):
        return (87.109*vw, 91.528*vh, 96.406*vw, 96.528*vh)
    else:
        # FIXME: implement with feature matching?
        raise NotImplementedError('unsupported aspect ratio')

def check_staff_blue(img, i):
    aspect = Fraction(*img.size)
    vw, vh = util.get_vwvh(img)
    # 小trick:123倒过来安排，使得办公室和发电站都是效率最高的优先。
    if aspect == Fraction(16, 9):
        if i == 2:
            x = (39.453*vw, 10.417*vh, 42.422*vw, 10.972*vh)
        elif i == 1:
            x = (39.453*vw, 87.778*vh, 42.422*vw, 88.333*vh)
        elif i == 0:
            x = (47.031*vw, 10.417*vh, 50.000*vw, 10.972*vh)
        elif i == 3:
            x = (47.031*vw, 87.778*vh, 50.000*vw, 88.333*vh)
        elif i == 4:
            x = (57.422*vw, 10.417*vh, 60.391*vw, 10.972*vh)
    else:
        # FIXME: implement with feature matching?
        raise NotImplementedError('unsupported aspect ratio')
    icon1 = img.crop(x).convert('RGB')
    icon2 = resources.load_image_cached('base/blue.png', 'RGB')

    icon1, icon2 = imgops.uniform_size(icon1, icon2)
    mse = imgops.compare_mse(np.asarray(icon1), np.asarray(icon2))
    # print(mse, icon1.size)
    logger.logimage(icon1)
    logger.logtext('mse=%f' % mse)
    return mse < 2000

def get_staff_numi(img, i):
    aspect = Fraction(*img.size)
    vw, vh = util.get_vwvh(img)
    if aspect == Fraction(16, 9):
        if i == 2:
            return (34.688*vw, 20.556*vh, 41.250*vw, 42.639*vh)
        elif i == 1:
            return (33.906*vw, 52.917*vh, 41.094*vw, 71.667*vh)
        elif i == 0:
            return (45.234*vw, 20.556*vh, 52.109*vw, 42.639*vh)
        elif i == 3:
            return (45.859*vw, 52.917*vh, 52.578*vw, 71.667*vh)
        elif i == 4:
            return (57.031*vw, 20.556*vh, 63.438*vw, 42.639*vh)
    else:
        # FIXME: implement with feature matching?
        raise NotImplementedError('unsupported aspect ratio')

def get_base_left(img, i, j):
    aspect = Fraction(*img.size)
    vw, vh = util.get_vwvh(img)
    posx1 = [0.703, 15.469, 31.797]
    posx2 = [3.203, 19.219, 35.703]
    posy1 = [40.417, 52.639, 66.944]
    posy2 = [46.667, 61.250, 76.111]
    if aspect == Fraction(16, 9):
        return (posx1[j]*vw, posy1[i]*vh, posx2[j]*vw, posy2[i]*vh)
    else:
        # FIXME: implement with feature matching?
        raise NotImplementedError('unsupported aspect ratio')

def get_base_right(img, i):
    aspect = Fraction(*img.size)
    vw, vh = util.get_vwvh(img)

    if aspect == Fraction(16, 9):
        if i == 0:
            return (91.719*vw, 24.306*vh, 96.797*vw, 31.389*vh)
        elif i == 1:
            return (96.797*vw, 52.500*vh, 99.375*vw, 60.139*vh)
    else:
        # FIXME: implement with feature matching?
        raise NotImplementedError('unsupported aspect ratio')

def get_base_top(img):
    aspect = Fraction(*img.size)
    vw, vh = util.get_vwvh(img)

    if aspect == Fraction(16, 9):
        return (54.375*vw, 11.111*vh, 75.781*vw, 27.361*vh)
    else:
        # FIXME: implement with feature matching?
        raise NotImplementedError('unsupported aspect ratio')
