import pandas as pd
import numpy as np

def count_rsp(df_clean, mrp = 3000, malyi_sotr = 100, malyi_dohod = 300000, 
              micro_sotr = 15, micro_dohod = 30000,
              krupnyi_sotr = 250, krupnyi_dohod = 3000000):
    
    df_clean['СГД'] = df_clean['СГД'].astype(np.float64)
    df_clean['СГЧС'] = df_clean['СГЧС'].astype(np.float64)
    
    krupnyi = df_clean.loc[(df_clean['СГЧС']>krupnyi_sotr) | (df_clean['СГД']>krupnyi_dohod*mrp)]
    malyi = df_clean.loc[(df_clean['СГЧС']<=malyi_sotr) & (df_clean['СГД']<=malyi_dohod*mrp)]
    
    micro = malyi.loc[(malyi['СГЧС']<=micro_sotr) | (malyi['СГД']<=micro_dohod*mrp)]
    
    print(f'Субъектов крупного предпринимательства = {len(krupnyi)}')
    print(f'Субъектов среднего предпринимательства = {len(df_clean) - len(krupnyi) - len(malyi)}')
    print(f'Субъектов малого предпринимательства = {len(malyi)+476100}, из них субъектов микро предпринимательства {len(micro)+476100}')
    
    
def count_rsp_sotr(df_clean, malyi_sotr = 100, 
              micro_sotr = 15, krupnyi_sotr = 250):
    
    df_clean['СГЧС'] = df_clean['СГЧС'].astype(np.float64)
    
    krupnyi = df_clean.loc[(df_clean['СГЧС']>krupnyi_sotr)]
    malyi = df_clean.loc[(df_clean['СГЧС']<=malyi_sotr)]
    
    micro = malyi.loc[(malyi['СГЧС']<=micro_sotr)]
    
    print(f'Субъектов крупного предпринимательства = {len(krupnyi)}')
    print(f'Субъектов среднего предпринимательства = {len(df_clean) - len(krupnyi) - len(malyi)}')
    print(f'Субъектов малого предпринимательства = {len(malyi)}, из них субъектов микро предпринимательства {len(micro)}')
    
    
def count_rsp_dohod(df_clean, mrp = 3000,  malyi_dohod = 300000, 
                    micro_dohod = 30000, krupnyi_dohod = 3000000):
    
    df_clean['СГД'] = df_clean['СГД'].astype(np.float64)
    
    krupnyi = df_clean.loc[(df_clean['СГД']>krupnyi_dohod*mrp)]
    malyi = df_clean.loc[(df_clean['СГД']<=malyi_dohod*mrp)]
    
    micro = malyi.loc[(malyi['СГД']<=micro_dohod*mrp)]
    
    print(f'Субъектов крупного предпринимательства = {len(krupnyi)}')
    print(f'Субъектов среднего предпринимательства = {len(df_clean) - len(krupnyi) - len(malyi)}')
    print(f'Субъектов малого предпринимательства = {len(malyi)+476100}, из них субъектов микро предпринимательства {len(micro)+476100}')