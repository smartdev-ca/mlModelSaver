import dill as pickle
import json

import os

from functools import partial
import numpy as np

def ensure_directory_exists(directory_path):
    """
    Ensure that the specified directory exists. If it doesn't, create it.

    Parameters:
    directory_path (str): The path of the directory to ensure exists.
    """
    os.makedirs(directory_path, exist_ok=True)


def check_file_exists(file_path):
    """
    Check if the specified file exists.

    Parameters:
    file_path (str): The path of the file to check.

    Returns:
    bool: True if the file exists, False otherwise.
    """
    if os.path.isfile(file_path):
        print(f"File '{file_path}' exists.")
        return True
    else:
        print(f"File '{file_path}' does not exist.")
        return False


supportedModels = {
    "sm.OLS": {
        "supported": True,
        "normalPredictorFunction": "predict"
    },
    "sm.Logit": {
        "supported": True,
        "normalPredictorFunction": "predict"
    },
    "sklearn.neighbors.KNeighborsClassifier": {
        "supported": True,
        "normalPredictorFunction": "predict_proba"
    },
    "sklearn.tree.DecisionTreeClassifier": {
        "supported": True,
        "normalPredictorFunction": "predict_proba"
    },
    "sklearn.tree.DecisionTreeRegressor": {
        "supported": True,
        "normalPredictorFunction": "predict"
    },
}

supportedDataType = {
    "int": {
        "supported": True
    },
    "float": {
        "supported": True
    },
    "binary":{
        "supported": True
    },
    "probebility":{
        "supported": True
    }
}

def default_transformer(x):
    return x


def mlModelSavePredict(self, df, typeOfPredict = 'normal'):
    dfAfterTransformation = self.mlModelSaverTransformer(df)
    output = []
    outputsName = self.mlModelSaverConfig.get("outputs", [{"name": "result"}])
    outputsName = [item["name"] for item in outputsName]
    modelType = self.mlModelSaverConfig['modelType']
    modelTypeConfig = supportedModels[modelType]
    if typeOfPredict == 'normal':
        results = getattr(self, modelTypeConfig['normalPredictorFunction'])(dfAfterTransformation)
        for  value in results:
            if isinstance(value, np.ndarray):
                res = {}
                for index, val in enumerate(value):
                    res[outputsName[index]] = val
                output.append(res)
            else:
                output.append({
                    outputsName[0]: value,
                })
        return output
    return output

class MlModelSaver:

    cachedModels = {}

    def __init__(self, config):
        self.baseRelativePath = config.get('baseRelativePath', '.')
        self.modelsFolder = f'{self.baseRelativePath}/{config.get('modelsFolder', '~~modelsFolder')}'
        ensure_directory_exists(self.modelsFolder)

    def listOfPickles(self):
        files = os.listdir(self.modelsFolder)
        picklesList = [file for file in files if file.endswith('.pkl')]
        return picklesList

    def listOfModels(self):
        picklesList = self.listOfPickles()
        modelsList = []
        for pickleFileName in picklesList:
            modelsList.append(pickleFileName.split(".pkl")[0])
        return modelsList



    def showSupportedModels(self):
        supported_keys = [key for key, value in supportedModels.items() if value.get('supported')]
        return supported_keys

    def loadModelByName(self, modelName):
        filename = f'{self.modelsFolder}/{modelName}.pkl'
        loaded_model = pickle.load(open(filename, 'rb'))
        self.cachedModels[loaded_model.mlModelSaverConfig.get("modelName")] = loaded_model
        return loaded_model

    def exportModel(self, model, config):
        transformer = config.get("transformer", default_transformer)
        model.mlModelSaverTransformer = transformer
        if "transformer" in config:
            del config["transformer"]
        model.mlModelSaverConfig = config
        isModelSupporter = supportedModels.get(
            config.get("modelType", ''),
            {}
        ).get("supported", False)
        if not isModelSupporter:
            raise ValueError(f'only {self.showSupportedModels()} are supported and {config.get("modelType", '')} is not supported')
        modelName = model.mlModelSaverConfig['modelName']
        model.mlModelSavePredict = partial(mlModelSavePredict, model)
        filename = f'{self.modelsFolder}/{modelName}.pkl'
        pickle.dump(model, open(filename, 'wb'))
        return self.loadModelByName(modelName)

    def getModel(self, modelName):
        model = self.cachedModels.get(modelName, None)
        if model != None:
            return model
        return self.loadModelByName(modelName)


