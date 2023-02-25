import pandas as pd
import numpy as np
from scipy.stats import zscore
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.model_selection import train_test_split
from kedro.io import DataCatalog, MemoryDataSet
from kedro.pipeline import node
from typing import Any, Dict


def feature_eng(preprocessed_data: pd.DataFrame) -> pd.DataFrame:
    X_train, X_test, y_train, y_test = train_test_split(
        preprocessed_data.drop(['FinalMandates'], axis=1),
        preprocessed_data['FinalMandates'],
        test_size=0.3,
        random_state=123
    )

    selector = SelectKBest(f_classif, k=10)
    selector.fit(X_train, y_train)
    X_new = selector.transform(X_train)

    features = X_train.columns[selector.get_support()]
    final_data = preprocessed_data[np.concatenate([features, ['FinalMandates', 'time', 'territoryName', 'Party']])]

    z = np.abs(zscore(final_data))
    threshold = 3
    filtered_entries= (z < threshold).all(axis=1)
    final_data_ = final_data[filtered_entries]

    return X_train, X_test, y_train, y_test, final_data_


feature_eng_node = node(
    func = feature_eng,
    inputs="preprocessed_data",
    outputs=["X_train", "X_test", "y_train", "y_test", "final_data"],
    name="feature_eng"
)
