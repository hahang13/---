import pandas as pd
import numpy as np
import datetime as dt
import time
import warnings
warnings.filterwarnings('ignore')

import timeCh
import databased
import subpub64bit
import jipyo
import newslabel
import datahap
import reinforcementLearning

# 최소 0.28% 이상 오른 상태에서 팔아야 수익이 난다.

# dayAndTime = timeCh.timeChange(timeNow).timeDay()
# print(dayAndTime[1])
# print(type(int(print(dayAndTime[1]))))

stockNameList = ['루닛']
stockCodeList = ['328130']
database = ['34.64.50.135','root','P@ssw0rd6388','stockdata']

jong = []
actions = []
lock = False

while True:
    timeNow = dt.datetime.now()
    # timeNow = dt.datetime(2023,7,5,14,55)
    if 1520 >= timeNow.hour * 100 + timeNow.minute >= 900:
        lock = False
        
        subpub64bit.dataSubPub().sub()
        
        getStockData = databased.database(stockCodeList, stockNameList, database, timeNow).download()

        jipyoDf = jipyo.jipyoCreate(getStockData[1], timeNow).create()
        newsScore = newslabel.newslabel(getStockData[2]).labeling()
        hapDf = datahap.dataHap(getStockData[0], jipyoDf, newsScore).hap()
        hapDf.drop(['종목코드','종목명','날짜'], axis=1, inplace=True)

        actionResult = reinforcementLearning.rl(hapDf).dp()

        jong.append(str(hapDf['종가']))
        actions.append(actionResult)

        subpub64bit.dataSubPub().pub(actionResult)

        timeNow = dt.datetime.now()
        print('[시스템]:'+str(timeNow.hour)+'시 '+str(timeNow.minute + 1)+'분이 되기 기다리는 중...')
        secondLeft = 60 - int(timeNow.second)
        time.sleep(secondLeft)
    else:
        if lock == False:
            lock = True
            rewardDf = pd.DataFrame({
                '환경':jong,
                '행동':actions
            })
            rewardDf.to_csv('./rewardList.csv', encoding='euc-kr')

        print('[시스템]:현재 주식 거래 가능한 시간이 아닙니다. 현재시간 : '+str(timeNow.hour)+'시 '+str(timeNow.minute)+'분')
        time.sleep(1)
        continue
