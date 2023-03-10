from kedro.pipeline import Pipeline, node
from .nodes import preprocess_data


def create_pipeline():
    return Pipeline(
        [
            node(func=preprocess_data, inputs="raw_data", outputs="preprocessed_data", name="preprocess_data"),
        ],
        tags=["preprocessing"]
    )
