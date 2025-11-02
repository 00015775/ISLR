# config.py
import os

# ----------------------------------------------------------------------
# 1. GLOBAL SETTINGS
# ----------------------------------------------------------------------
DATA_ROOT = "./Data_Numpy_Arrays_RSL_UzSL"        
VIDEO_DEVICE = 1                                  
FRAME_WIDTH, FRAME_HEIGHT = 1280, 720
FPS = 30
FRAMES_PER_REP = 60  # fixed length per repetition
COUNTDOWN_SECONDS = 5

# ----------------------------------------------------------------------
# 2. INITIAL SIGN-WORD LIST (you can add more later)
# ----------------------------------------------------------------------
DEFAULT_SIGNS = [
    "nima", "eshitish", "salom", "rahmat", "yaxshi"
]

# ----------------------------------------------------------------------
# 3. MEDIA-PIPE SETTINGS
# ----------------------------------------------------------------------
MP_CONFIDENCE = 0.6
POSE_REMOVE_IDX = [0,1,2,3,4,5,6,7,8,9,10,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]
POSE_KEEP_CONNECTIONS = frozenset([(11,12),(11,13),(12,14),(13,15),(14,16)])

