# test_mlModelSaver.py

import sys
import os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..'
        )
    )
)


def test_ensureCLassInstance():
    from mlModelSaver import MlModelSaver
    mlModelSaverInstance1 = MlModelSaver({
        "baseRelativePath": "test_baseRelativePath",
        "modelsFolder": "test_modelsFolder"
    })
    assert mlModelSaverInstance1.baseRelativePath == "test_baseRelativePath"
    assert mlModelSaverInstance1.modelsFolder == "test_baseRelativePath/test_modelsFolder"
    tesSupportedModels = mlModelSaverInstance1.showSupportedModels()
    assert tesSupportedModels == ['sm.OLS', 'sm.Logit']


def test_OLS_LinearRegression():
    from mlModelSaver import MlModelSaver
    import numpy as np
    import pandas as pd
    import statsmodels.api as sm
    from helpers import add_constant_column
    salaryMisDf = pd.read_excel("./datasets/Salary_MIS.xlsx")
    salaryBasedOnGpaMisStatistics = sm.OLS(
        salaryMisDf["Salary"],
        add_constant_column(salaryMisDf[["GPA", "MIS", "Statistics"]])
    )
    salaryBasedOnGpaMisStatisticsFit = salaryBasedOnGpaMisStatistics.fit()
    mlModelSaverInstance2 = MlModelSaver({
        "baseRelativePath": ".",
        "modelsFolder": "~~tmp/testModels"
    })



    loadedModel = mlModelSaverInstance2.exportModel(
        salaryBasedOnGpaMisStatisticsFit,
        {
            "modelName": "salaryBasedOnGpaMisStatistics",
            "description": "Predict Salary based on GPA MIS Statistics for salaryMisDf",
            "modelType": "sm.OLS",
            "inputs": [
                {
                    "name": "GPA",
                    "type": "float",
                },
                {
                    "name": "MIS",
                    "type": "binary"
                },
                {
                    "name": "Statistics",
                    "type": "binary"
                }
            ],
            "transformer": add_constant_column,
            "outputs": [
                {
                    "name": "Salary",
                    "type": "int"
                }
            ]
        }
    )
    from mlModelSaver import check_file_exists
    assert check_file_exists("./~~tmp/testModels/salaryBasedOnGpaMisStatistics.pkl") == True
    testData = salaryMisDf[["GPA", "MIS", "Statistics"]].iloc[0:2]
    predictedValueWithLoadedModel = loadedModel.mlModelSavePredict(testData, 'normal')
    assert  predictedValueWithLoadedModel == [{'Salary': 73.9924679451542}, {'Salary': 69.55525482441558}]
    assert list(mlModelSaverInstance2.cachedModels.keys()) == ['salaryBasedOnGpaMisStatistics']
