from sklearn.datasets import load_breast_cancer
import pandas as pd
import numpy as np

df = load_breast_cancer(as_frame=True)
df.head()