from kedro.pipeline import Pipeline, node
from .nodes import training_election_model


def create_pipeline():
    return Pipeline(
        [
            node(func=training_election_model, inputs="final_data", outputs="model_Election", name="training_model"),
        ],
        tags=["training_model"]
    )
