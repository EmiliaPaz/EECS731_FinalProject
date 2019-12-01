import pandas as pd

assessor_data = pd.read_csv('assessor.csv')
assessor_data = assessor_data.apply(lambda x: x.astype(str).str.lower())

assessor_data = df.apply(lambda x: x.astype(str).str.lower())