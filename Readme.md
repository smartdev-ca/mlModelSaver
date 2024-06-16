# mlModelSaver

## Project page in pypi
[mlModelSaver](https://pypi.org/project/mlModelSaver/)
## [Tutorial youtube](https://www.youtube.com/watch?v=fchTlNk2P8s)
## [Documentation](https://pypi.org/project/mlModelSaver/)

## How to install virtualenv

```
pip install virtualenv
```

## Use vireualevn
```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## if you install new dependency run this command and commit your code
```
pip freeze > requirements.txt
```

## for instalation in local
```
pip install -e .
```


## build project
```
python setup.py sdist bdist_wheel
```

## Push project
```
twine upload dist/*
```

## Run Jupyter notebooks
```
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
jupyter notebook \
        --notebook-dir="./notebooks" \
        --ip=0.0.0.0 --port=3225
```