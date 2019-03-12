import time
from ops import *
from utils import *

class Resnet(object):
    def __init__(self, sess, args):
        self.model_name = 'Resnet'
        self.sess = sess

        self.checkpoint_dir = args.checkpoint_dir
        self.dataset_dir = args.dataset_dir
        self.res_n = args.res_n
        self.epoch = args.epoch
        self.batch_size = args.batch_size
        self.iteration = len(self.train_x)//self.batch_size

        self.init_lr = args.lr


