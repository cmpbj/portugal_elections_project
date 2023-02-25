import pandas as pd
import numpy as np
from kedro.pipeline import node
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def training_election_model(final_data: pd.DataFrame) -> DecisionTreeRegressor:
    # Split the dataset into feature matrix (x) and target variable (y)
    x = final_data.drop(columns=['FinalMandates'])
    y = final_data[['FinalMandates']]

    # Standardize the feature matrix using StandardScaler
    sc = StandardScaler()
    x_std = sc.fit_transform(x)
    df_x = pd.DataFrame(x_std, columns=x.columns)

    # Split the standardized data into training and testing sets
    x_train, x_test, y_train, y_test = train_test_split(df_x, y, test_size=0.3, random_state=123)

    # Train a DecisionTreeRegressor using GridSearchCV to find the best hyperparameters
    model = DecisionTreeRegressor()
    parameters = {'criterion': ['squared_error'], 'max_depth': np.arange(2, 11)}

    clf = GridSearchCV(model, parameters, cv=5)
    clf.fit(df_x, y)

    # Get the best parameters found by GridSearchCV
    best_params = clf.best_params_

    # Fit a DecisionTreeRegressor with the best hyperparameters
    model = DecisionTreeRegressor(max_depth=best_params['max_depth'], criterion=best_params['criterion'])
    model.fit(x_train, y_train)

    return model
dct_model_node = node(
    func = training_election_model,
    inputs="final_data",
    outputs="model_Election",
    name="dct_model"
)