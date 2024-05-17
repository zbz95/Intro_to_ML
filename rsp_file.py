import pandas as pd
import numpy as np

def count_rsp(df, mrp = 3000, malyi_sotr = 100, malyi_dohod = 300000, 
              micro_sotr = 15, micro_dohod = 30000,
              krupnyi_sotr = 250, krupnyi_dohod = 3000000):
    
    df['СГД'] = df['СГД'].astype(np.float64)
    df['СГЧС'] = df['СГЧС'].astype(np.float64)
    

    krupnyi = df.loc[(df['СГЧС']>krupnyi_sotr) | (df['СГД']>krupnyi_dohod*mrp)]
    
    malyi = df.loc[(df['СГЧС']<=malyi_sotr) & (df['СГД']<=malyi_dohod*mrp)]
    micro = malyi.loc[(malyi['СГЧС']<=micro_sotr) | (malyi['СГД']<=micro_dohod*mrp)]
    
    kr_ma_xin = list(krupnyi['XIN']) + list(malyi['XIN'])
    
    srednii = df.loc[~df['XIN'].isin(kr_ma_xin)]
    
    
    krupnyi = pd.concat([krupnyi, srednii.loc[srednii['LICENSE'].notna()]])
    srednii = srednii.loc[srednii['LICENSE'].isna()]
    
    srednii = pd.concat([srednii, malyi.loc[malyi['LICENSE'].notna()]])
    malyi = malyi.loc[malyi['LICENSE'].isna()]
    micro = micro.loc[micro['LICENSE'].isna()]
    
    krupnyi.to_csv('krupnyi.csv', index=False)
    srednii.to_csv('srednii.csv', index=False)
    
    kr = len(krupnyi)
    kr_nekom = len(krupnyi.loc[krupnyi['Priznak']=='Некоммерческая организация'])
    
    sr = len(srednii)
    sr_nekom = len(srednii.loc[srednii['Priznak']=='Некоммерческая организация'])
    
    micro_xin = list(micro['XIN'])
    malyi = malyi.loc[~malyi['XIN'].isin(micro_xin)]
    
    ma = len(malyi)
    ma_nekom = len(malyi.loc[malyi['Priznak']=='Некоммерческая организация'])
    
    mi = len(micro)
    mi_nekom = len(micro.loc[micro['Priznak']=='Некоммерческая организация'])
    
    
    
    print(f'Крупных: {kr}. Коммерческих крупных: {kr-kr_nekom}. Некоммерческих крупных: {kr_nekom}.')
    print(f'Средних: {sr}. Коммерческих средних: {sr-sr_nekom}. Некоммерческих средних: {sr_nekom}.')
    print(f'Малых: {ma}. Коммерческих малых: {ma-ma_nekom}. Некоммерческих малых: {ma_nekom}.')
    print(f'Микро: {mi}. Коммерческих микро: {mi-mi_nekom}. Некоммерческих микро: {mi_nekom}.')

    