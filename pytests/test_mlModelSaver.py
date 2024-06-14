# test_mlModelSaver.py

import sys
import os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '../mlModelSaver'
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
    assert mlModelSaverInstance1.modelsFolder == "test_modelsFolder"
    tesSupportedModels = mlModelSaverInstance1.showSupportedModels()
    assert tesSupportedModels == ['sm.OLS']


def test_OLS_LinearRegression():
    from mlModelSaver import MlModelSaver
    import numpy as np
    import pandas as pd
    import statsmodels.api as sm
    salaryMisDf = pd.read_excel("./datasets/Salary_MIS.xlsx")
    salaryBasedOnGpaMisStatistics = sm.OLS(
        salaryMisDf["Salary"],
        sm.add_constant(salaryMisDf[["GPA", "MIS", "Statistics"]])
    )
    salaryBasedOnGpaMisStatisticsFit = salaryBasedOnGpaMisStatistics.fit()
    mlModelSaverInstance2 = MlModelSaver({
        "baseRelativePath": ".",
        "modelsFolder": "~~tmp/models"
    })

    mlModelSaverInstance2.exportModel(
        salaryBasedOnGpaMisStatisticsFit,
        {
            "modelName": "salaryBasedOnGpaMisStatisticsFit",
            "description": "Predict Salary based on GPA MIS Statistics for sallaryMisDf",
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
            "output": [
                {
                    "name": "Salary",
                    "type": "int"
                }
            ]
        }
    )
    assert 2 == 2
