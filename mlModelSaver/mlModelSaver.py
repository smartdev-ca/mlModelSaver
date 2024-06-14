import pickle
import json

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

class MlModelSaver:

    def __init__(self, config):
        self.baseRelativePath = config.get('baseRelativePath', '.')
        self.modelsFolder = config.get('modelsFolder', '~~modelsFolder')

    def showSupportedModels(self):
        supported_keys = [key for key, value in supportedModels.items() if value.get('supported')]
        return supported_keys

    def exportModel(self, model, config):
        model.mlModelSaverConfig = config
        isModelSupporter = supportedModels.get(
            config.get("modelType", ''),
            {}
        ).get("supported", False)
        if not isModelSupporter:
            raise ValueError(f'only {self.showSupportedModels()} are supported and {config.get("modelType", '')} is not supported')
        print(model.mlModelSaverConfig)
        # modelName = config['modelName']
        # modelsConfig[modelName] = {}
        # modelsConfig[modelName]['name'] = modelName
        # model = config['model']
        # inputs = config['inputs']
        # output = config['output']
        # transformers = config.get('transformers', [])
        # description = config['description']
        # modelsConfig[modelName]['description'] = description
        # modelsConfig[modelName]['inputs'] = inputs
        # if len(transformers) > 0:
        #     modelsConfig[modelName]['transformers'] = transformers
        # modelsConfig[modelName]['output'] = output
        # modelType = config.get('modelType', '')
        # modelsConfig[modelName]['modelType'] = modelType
        # if hasattr(model, 'customMetrics'):
        #     customMetrics = model.customMetrics
        #     modelsConfig[modelName]['customMetrics'] = customMetrics
        # else:
        #     pass
        # filename = f'{baseRelativePath}/models/{modelName}'
        # pickle.dump(model, open(filename, 'wb'))
        # with open(f'{baseRelativePath}/models/configs.json', "w") as outputFile:
        #     json.dump(modelsConfig, outputFile, indent = 4)

        # loaded_model = pickle.load(open(filename, 'rb'))
        # return loaded_model