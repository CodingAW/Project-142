import pandas as pd
import numpy as np

df = pd.read_csv("articles.csv")
df = df.sort_values(['total_events'], ascending=[False])

output = df[["title", "url","total_events"]].head(20).values.tolist()
# print(output)