from keras.models import load_model
import pandas as pd
import random
import warnings
warnings.filterwarnings('ignore')

class rl:
    def __init__(self, dataDf):
        self.dataDf = dataDf

    def dp(self):
        lstmLoad = load_model('./lstm.hdf5')
        result = lstmLoad.predict(self.dataDf)
        return int(result[0][0])
        # ranNum = random.randrange(0,2)
        # return ranNum
