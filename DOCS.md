# mlModelSaver documentation


Introducing **[mlModelSaver](https://pypi.org/project/mlModelSaver/)** – a streamlined Python module designed for data scientists and developers who seek a straightforward solution for model saving and serving.

While numerous tools are available for training machine learning models, many lightweight statistical models lack simple, efficient saving mechanisms. Existing enterprise solutions like MLflow are robust but come with considerable complexity. Based on my experience, I saw the need for an abstract model registry concept that simplifies this process.

**[mlModelSaver](https://github.com/smartdev-ca/mlModelSaver)** fills this gap, offering an intuitive way to save machine learning models and transformers. It facilitates seamless integration with frameworks like FastAPI ([Examples](https://github.com/jafarijason/ml_models_deployments)), Flask, and Django, enabling easy deployment and serving of models in production environments. Empower your machine learning workflow with **mlModelSaver** – the easy and efficient tool for model management.

## Installation

You can install **mlModelSaver** via pip:

```bash
pip install mlModelSaver
```


# mlModelSaver Example: Simple Linear Regression

In this example, we demonstrate how to use **mlModelSaver** to export a simple linear regression model based on a notebook from [ml_models_deployments](https://github.com/jafarijason/ml_models_deployments/blob/master/notebooks/001.ipynb).

### Example Description

This example builds a simple linear regression model to predict sales based on temperature, advertising, and discount factors. Once the model is fitted and satisfactory, **mlModelSaver** allows you to easily save and deploy the model for use in production environments.

### Example Code - notebook available [here](https://github.com/jafarijason/ml_models_deployments/blob/master/notebooks/001.ipynb)


```python
def add_constant_columnTransformer(df):
    # example transformer
    df_with_const = df.copy()
    df_with_const.insert(0, 'const', 1)
    return df_with_const

# Export the model using MlModelSaver
loadedModel = mlModelSaverInstance.exportModel(
    simpleLinearRegressionFittedModel, # the models is fitted and ready for usage
    {
        "modelName": "modelPredictSaleByTemperatureAdvertisingDiscountFit",
        "description": "Example model predicting sales based on temperature, advertising, and discount.",
        "modelType": "sm.OLS",  # Example model type (replace with actual type)
        "inputs": [
            {"name": "Temperature", "type": "float"},
            {"name": "Advertising", "type": "float"},
            {"name": "Discount", "type": "float"}
        ],
        "transformer": add_constant_columnTransformer,  # Use your transformation function here
        "outputs": [
            {
                "name": "Sales",
                "type": "float"
            }
        ]
    }
)
```
