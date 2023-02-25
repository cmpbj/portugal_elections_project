"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline
from elections_mlops_project.pipelines import preprocessing_data as pp
from elections_mlops_project.pipelines import feature_engineering as fe
from elections_mlops_project.pipelines import dct_model as dt

def register_pipelines() -> Dict[str, Pipeline]:
    
    pre_processing_pipeline = pp.create_pipeline()
    feature_engineer_pipeline = fe.create_pipeline()
    decision_tree_model_pipeline = dt.create_pipeline()
    
    return {
        "pp": pre_processing_pipeline,
        "fe": feature_engineer_pipeline,
        "dt": decision_tree_model_pipeline,
        "__default__": pre_processing_pipeline + feature_engineer_pipeline + decision_tree_model_pipeline }
