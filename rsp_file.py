import numpy as np
import pandas as pd

def count_rsp(data, mrp = 3000, malyi_sotr = 100, malyi_dohod = 300000, 
              micro_sotr = 15, micro_dohod = 30000,
              krupnyi_sotr = 250, krupnyi_dohod = 3000000):
    
    df = data.copy()
    df_num = df.loc[~((df['Доходы'].isin(['Нет данных по доходам за 2022г', 'Нет данных по доходам', '-'])) | (df['Сотрудники'].isin(['Нет данных по сотрудникам', '-'])))].copy()
    df_nonnum = df.loc[((df['Доходы'].isin(['Нет данных по доходам за 2022г', 'Нет данных по доходам', '-'])) | (df['Сотрудники'].isin(['Нет данных по сотрудникам', '-'])))].copy()
    df_num['Доходы'] = df_num['Доходы'].astype(np.float64)
    df_num['Сотрудники'] = df_num['Сотрудники'].astype(np.float64)
    
    df_num['Категория'] = None
    df_num.loc[(df_num['Сотрудники']>krupnyi_sotr) | (df_num['Доходы']>krupnyi_dohod*mrp), 'Категория'] = 'Крупное предпринимательство'
    df_num.loc[(df_num['Сотрудники']<=malyi_sotr) & (df_num['Доходы']<=malyi_dohod*mrp), 'Категория'] = 'Малое предпринимательство'
    df_num.loc[(((df_num['Сотрудники']<=micro_sotr) | (df_num['Доходы']<=micro_dohod*mrp)) & (df_num['Категория']== 'Малое предпринимательство')), 'Категория'] = 'Микро предпринимательство'
    df_num['Категория'].fillna('Среднее предпринимательство', inplace=True)
    
    df_num.loc[(df_num['Лицензия']!='-') & (df_num['Категория'].isin(['Малое предпринимательство', 'Микро предпринимательство'])), 'Категория'] = 'Среднее предпринимательство'
    
    df = pd.concat([df_num, df_nonnum])
    
    df.loc[df['Категория']=='Крупное предпринимательство'].to_excel('krupnyi.xlsx', index=False)
    df.loc[df['Категория']=='Среднее предпринимательство'].to_excel('srednii.xlsx', index=False)
    df.loc[df['Категория']=='Нет данных'].to_excel('net_dannyh.xlsx', index=False)
    df.loc[df['Категория']=='Нет данных за 2022г'].to_excel('net_dannyh_2022.xlsx', index=False)

    print(df['Категория'].value_counts())

def count_rsp_sotr(data, malyi_sotr = 100, micro_sotr = 15, krupnyi_sotr = 250):
    
    df = data.copy()
    df_num = df.loc[~(df['Сотрудники'].isin(['Нет данных по сотрудникам', '-']))].copy()
    df_nonnum = df.loc[df['Сотрудники'].isin(['Нет данных по сотрудникам', '-'])].copy()
    df_num['Сотрудники'] = df_num['Сотрудники'].astype(np.float64)
    
    df_num['Категория'] = None
    df_num.loc[df_num['Сотрудники']>krupnyi_sotr, 'Категория'] = 'Крупное предпринимательство'
    df_num.loc[df_num['Сотрудники']<=malyi_sotr, 'Категория'] = 'Малое предпринимательство'
    df_num.loc[((df_num['Сотрудники']<=micro_sotr) & (df_num['Категория']== 'Малое предпринимательство')), 'Категория'] = 'Микро предпринимательство'
    df_num['Категория'].fillna('Среднее предпринимательство', inplace=True)
    
    df_num.loc[(df_num['Лицензия']!='-') & (df_num['Категория'].isin(['Малое предпринимательство', 'Микро предпринимательство'])), 'Категория'] = 'Среднее предпринимательство'
    
    df = pd.concat([df_num, df_nonnum])
    
    df.loc[df['Категория']=='Крупное предпринимательство'].to_excel('krupnyi.xlsx', index=False)
    df.loc[df['Категория']=='Среднее предпринимательство'].to_excel('srednii.xlsx', index=False)
    df.loc[df['Категория']=='Нет данных'].to_excel('net_dannyh.xlsx', index=False)
    df.loc[df['Категория']=='Нет данных за 2022г'].to_excel('net_dannyh_2022.xlsx', index=False)

    print(df['Категория'].value_counts())

    