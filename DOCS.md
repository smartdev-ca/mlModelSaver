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

In this example, we demonstrate how to use **mlModelSaver** to export a simple linear regression model based on a notebook from [ml_models_deployments](https://github.com/jafarijason/ml_models_deployments).

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

testData = [
    {
        "Temperature": 42,
        "Advertising": 15,
        "Discount": 5
    }
]

# Create a DataFrame from the dictionary
testDf = pd.DataFrame(testData)

# this will be your model without export
modelPredictSaleByTemperatureAdvertisingDiscountFit.predict( add_constant_column(testDf)

# result 0    19590.46727 \n dtype: float64

# this will be result of predict with exported model
loadedModel.mlModelSavePredict(testDf)
#result [{'Sales': 19590.467270313893}]

```

## Supported Models

Current supported models by **mlModelSaver**:

```python
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
}



## Next Steps

- [-] **Support More Models** **WIP**: Extend **mlModelSaver** to support various types of models beyond simple linear regression, such as decision trees, neural networks, and ensemble methods.

- [-] **Additional Examples**: Provide diverse examples demonstrating the use of **mlModelSaver** with different machine learning models and data preprocessing techniques.

- [] **Video Tutorial**: Create a comprehensive video tutorial demonstrating how to train models, use **mlModelSaver** for saving and deployment, and integrate with popular frameworks like Flask and FastAPI.

- [] **Save Models to S3**: Implement functionality to save models directly to Amazon S3 for scalable and reliable storage, ensuring robust deployment in cloud environments.


### Support More Models

Expand **mlModelSaver** to handle a variety of machine learning models beyond simple linear regression. Example models could include decision trees, support vector machines, and deep learning models. Ensure that each model type integrates seamlessly with **mlModelSaver**'s saving and deployment functionalities.

### Save Models to S3

Enhance **mlModelSaver** to include options for saving models directly to Amazon S3. This feature ensures that models are stored securely and can be accessed from any location, facilitating deployment across distributed systems and cloud environments.

### Additional Examples

Include a range of examples demonstrating **mlModelSaver**'s capabilities across different use cases. Examples should cover various scenarios such as regression, classification, and time series forecasting. Provide clear instructions and code snippets for each example, showcasing how to prepare data, train models, and deploy them using **mlModelSaver**.

### Video Tutorial

Produce a video tutorial that guides users through the entire process of using **mlModelSaver**. The tutorial should include steps for training a model, integrating with **mlModelSaver** for saving and loading, and deploying the model using popular web frameworks like Flask or FastAPI. Emphasize best practices and common pitfalls to help users maximize efficiency and reliability in their machine learning projects.

These next steps will enhance **mlModelSaver**'s usability and scalability, enabling users to leverage advanced machine learning models effectively in production environments.

