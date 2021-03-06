import logging

import cv2 as cv
import numpy as np
from PIL import Image

from . import imgops, util
from . import resources

from resources.imgreco import map_vectors

logger = logging.getLogger('imgreco.map')


def recognize_map(img, partition):
    logger.debug('recognizing in partition %s', partition)
    anchors = map_vectors.map_anchors[partition]
    scale = img.height / 720
    img = imgops.scale_to_height(img.convert('RGB'), 720)
    imgmat = np.asarray(img)
    match_results = [(anchor, *imgops.match_template(imgmat, resources.load_image_cached('maps/%s/%s.png' % (partition, anchor), 'RGB')))
                     for anchor in anchors]
    logger.debug('anchor match results: %s', repr(match_results))
    use_anchor = max(match_results, key=lambda x: x[2])
    if use_anchor[2] < 0.9:
        return None
    logger.debug('use anchor: %s', repr(use_anchor))
    bias = np.asarray(use_anchor[1], dtype=np.int32) - map_vectors.stage_maps[partition][use_anchor[0]]
    logger.debug('bias: %s', bias)
    result = {name: (pos + bias) * scale for name, pos in map_vectors.stage_maps[partition].items()}
    return result


def recognize_daily_menu(img, partition):
    logger.debug('recognizing daily menu in partition %s', partition)
    names = [x[:-4] for x in resources.get_entries('maps/' + partition)[1]]
    scale = img.height / 720
    img = imgops.scale_to_height(img.convert('RGB'), 720)
    imgmat = np.asarray(img)
    match_results = [(name, *imgops.match_template(imgmat, resources.load_image_cached('maps/%s/%s.png' % (partition, name), 'RGB'), method=cv.TM_SQDIFF_NORMED))
                     for name in names]
    logger.debug('%s', match_results)
    result = {name: (np.asarray(pos) * scale, conf) for name, pos, conf in match_results if conf < 0.08}
    return result


def get_daily_menu_entry(viewport, daily_type):
    vw, vh = util.get_vwvh(viewport)
    if daily_type == 'material':
        return (23.472*vh, 86.667*vh, 41.111*vh, 96.944*vh)
    elif daily_type == 'soc':
        return (44.583*vh, 86.667*vh, 62.083*vh, 96.944*vh)
    elif daily_type == 'event':
        return (110.417*vh, 87.222*vh, 125.000*vh, 96.389*vh)
    else:
        raise KeyError(daily_type)

def get_event_entry(viewport, event_type):
    #活动中再点击一次才进入关卡选择界面
    vw, vh = util.get_vwvh(viewport)
    if event_type == 'MB':
        return (100*vw-31.944*vh, 15.972*vh, 100*vw-9.306*vh, 27.500*vh)
    elif event_type == 'WR':
        return (87.437*vw, 61.556*vh, 93.687*vw, 90.778*vh)
    else:
        raise KeyError(event_type)
if __name__ == '__main__':
    import sys
    import pprint
    pprint.pprint(globals()[sys.argv[1]](Image.open(sys.argv[2]), sys.argv[3]))
