import redis
import pandas as pd

address = redis.Redis(host='localhost', port=6379, db=0)

dataDf = pd.read_csv('../stock/루닛 지표 수정.csv', encoding='euc-kr')

address.set('column', str(dataDf.columns.values))
address.set('value', str(dataDf[-1:].values))

address.set('column', '컬럼입니다.')
address.set('value', '데이터입니다.')