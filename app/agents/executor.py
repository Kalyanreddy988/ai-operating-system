import pandas as pd
from app.tools.mltools import train_model

def execute(file, goal):
    df = pd.read_csv(file.file)

    # auto select last column as target
    target_col = df.columns[-1]

    return train_model(df, target_col)
