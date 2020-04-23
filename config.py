##
# COMMON CONFIG
##

# PASCAL VOC
CLASSES = ['Aeroplane', 'Bicycle', 'Bird', 'Boat', 'Bottle',
           'Bus', 'Car', 'Cat', 'Chair', 'Cow', 'Diningtable',
           'Dog', 'Horse', 'Motorbike', 'Person', 'Pottedplant',
           'Sheep', 'Sofa', 'Train', 'Tvmonitor']

INPUT_SHAPE = (300, 300, 3)

WEIGHTS = 'weights_SSD300.hdf5'


##
# PREDICT CONFIG
##


##
# TRAIN CONFIG
##
BBOX_PKL = "prior_boxes_ssd300.pkl"
DATA_PKL = "VOC2007.pkl"
# DATA_PKL = "gt_pascal.pkl"

PATH_PREFIX = "./VOCdevkit/VOC2007/JPEGImages/"

TRAIN_VAL_SPLIT = 0.8
