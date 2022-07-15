import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta


## filter for value val in column col in dataframe df 
def filter_(df, col, val):
    return df.loc[df[col] == val]

## filter on multiple columns for a single value per column - dictionary of {column:value} pairs
def filter_more_cols(df, dict: dict):
    cols = list(dict.keys())
    vals = list(dict.values())
    length = len(dict)

    x = filter_(df, cols[0], vals[0])
    if length == 1:
        return x
    if length > 1:
        for i in range(1, length):
            x = filter_(x, cols[i], vals[i])
        return x

def filter_more_values(df, col, val: list, neg = False):
    '''filter single column col from dataframe df for multiple values val - can retain or remove specified values
    neg: if True the specified values val will be removed
    '''
    length = len(val)

    if neg == False:
        val1 = df.loc[df[col] == val[0]]
        if length == 1:
            return val1
        else:
            input = []
            input.append(val1)
            for i in range(1, length):
                val2 = df.loc[df[col] == val[i]]
                input.append(val2)
            outputFalse = pd.concat(input)
            return outputFalse

    elif neg == True:
        val1 = df.loc[df[col] != val[0]]
        if length == 1:
            return val1
        else:
            for i in range(1, length):
                val1 = val1.loc[val1[col] != val[i]]
        return val1

def date_delta(date:any, date_format, delta):
    if type(date) == str:
        date = datetime.strptime(date, date_format)
    past_date = date - relativedelta(months=delta)
    past_date = past_date.strftime(date_format)
    return past_date

def month_list(start, end, format):
    return pd.date_range(start, end, freq='MS').strftime(format).tolist()