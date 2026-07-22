import pandas as pd
import io

def load_csv(file):
    content = file.file.read()
    return pd.read_csv(io.BytesIO(content))
