from mrcnn.config import Config
from .constants import *

class Urban3dOptimalRGBD(Config):
    """Configuration for training on MS COCO.
    Derives from the base Config class and overrides values specific
    to the COCO dataset.
    """
    # Give the configuration a recognizable name
    NAME = "urban3d_optimal_rgbd"

    BACKBONE = 'resnet50'

    # We use a GPU with 12GB memory, which can fit two images.
    # Adjust down if you use a smaller GPU.
    IMAGES_PER_GPU = GLOB_IMAGES_PER_GPU

    # Uncomment to train on 8 GPUs (default is 1)
    GPU_COUNT = 1

    # Number of classes (including background)
    NUM_CLASSES = 1 + 1  # background + building footprints

    BATCH_SIZE = GLOB_BATCH_SIZE

    # Number of training steps per epoch
    STEPS_PER_EPOCH = 128

    # Skip detections with < 80% confidence
    DETECTION_MIN_CONFIDENCE = GLOB_DETECTION_MIN_CONFIDENCE

    WORKING_SIZE = GLOB_IMAGE_SIZE
    IMAGE_MIN_DIM = WORKING_SIZE
    IMAGE_MAX_DIM = WORKING_SIZE

    TRAIN_ROIS_PER_IMAGE = 100
    MAX_GT_INSTANCES = 50

    # Random crops of size IMAGE_MAX_DIM
    IMAGE_RESIZE_MODE = "crop"

    LEARNING_RATE = 0.001
    LEARNING_RATES = [LEARNING_RATE, LEARNING_RATE / 10]
    LEARNING_LAYERS = ["heads", "all"]
    LEARNING_EPOCHS = [5, 50]

    IMAGE_TYPE = "RGBD"
    IMAGE_CHANNEL_COUNT = 4
    MEAN_PIXEL = 4
    TRAIN_CONV1 = True

    EXT_USE_AUGMENTATION = GLOB_USE_AUGMENTATION


class Urban3dOptimalRGBDInference(Urban3dOptimalRGBD):
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1