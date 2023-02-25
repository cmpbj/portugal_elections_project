from kedro.pipeline import Pipeline, node
from .nodes import feature_eng


def create_pipeline():
    return Pipeline(
        [
            node(func=feature_eng, inputs="preprocessed_data", outputs=["X_train", "X_test", "y_train", "y_test", "final_data"], name="feature_eng"),
        ],
        tags=["feature"]
    )

