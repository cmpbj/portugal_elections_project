import pandas as pd
from sklearn.preprocessing import LabelEncoder
from typing import Any, Dict
from kedro.pipeline import node


def preprocess_data(raw_data: pd.DataFrame) -> pd.DataFrame:
    encoded_data = raw_data.copy()
    object_columns = list(encoded_data.select_dtypes(include=['object']).columns)
    encoder = LabelEncoder()
    for col in object_columns:
        encoded_data[col] = encoder.fit_transform(encoded_data[col])
    return encoded_data


preprocess_data_node = node(
    preprocess_data,
    inputs="raw_data",
    outputs="encoded_data",
    name="preprocess_data_node"
)


