import pickle
import json

import os

from functools import partial

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
        "supported": True
    }
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
    }
}

def default_transformer(x):
    return x


def mlModelSavePredict(self, df, typeOfPredict = 'normal'):
    dfAfterTransformation = self.mlModelSaverTransformer(df)
    output = []
    outputsName = self.mlModelSaverConfig.get("outputs", [{"name": "result"}])
    outputsName = [item["name"] for item in outputsName]
    if typeOfPredict == 'normal':
        results = self.predict(dfAfterTransformation)
        for  value in results:
            output.append({
                outputsName[0]: value,
            })
        return output

class MlModelSaver:

    cachedModels = {}

    def __init__(self, config):
        self.baseRelativePath = config.get('baseRelativePath', '.')
        self.modelsFolder = f'{self.baseRelativePath}/{config.get('modelsFolder', '~~modelsFolder')}'
        ensure_directory_exists(self.modelsFolder)



    def showSupportedModels(self):
        supported_keys = [key for key, value in supportedModels.items() if value.get('supported')]
        return supported_keys

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
        loaded_model = pickle.load(open(filename, 'rb'))
        self.cachedModels[loaded_model.mlModelSaverConfig.get("modelName")] = loaded_model
        return loaded_model
