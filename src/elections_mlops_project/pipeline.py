from typing import Dict

from kedro.pipeline import Pipeline
import pipelines.preprocessing_data as pp

def create_pipelines(**kwargs) -> Dict[str, Pipeline]:
    pp_pipeline = pp.create_pipeline()
    return {
        "de": pp_pipeline,
        "__default__": Pipeline([])
    }
