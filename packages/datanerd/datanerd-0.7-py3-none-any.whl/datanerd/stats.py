import pandas as pd
import numpy as np

def stats(df):
    
    df_stats=pd.DataFrame()

    df_stats=df.describe(percentiles=[.1,.2,.25,.3,.4,.5,.6,.7,.75,.8,.9,.95,.99]).T

    dfMissing=((df.isna().sum()/len(df))*100).to_frame('%ofMissingValues')

    num_columns = df.select_dtypes(exclude=['object']).columns
    cat_columns = df.select_dtypes(['object']).columns

    dfNonZero=df[num_columns].apply(lambda x: 100 * ((x > 0) & (x.notnull())).mean()).to_frame("%ofNonZeroValues")

    dfUnique=df.apply(lambda x: x.nunique(dropna=False), axis=0).to_frame("#ofUniqueValues")


    FinalDF=pd.concat([df_stats,dfMissing,dfNonZero,dfUnique],ignore_index=False,axis=1)

    return FinalDF