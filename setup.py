from setuptools import setup, find_packages

setup(
    name='mlModelSaver',
    version='1.0.29',
    packages=find_packages(),
    description='Make life easier for saving and serving ML models',
    long_description=open('DOCS.md').read(),  # Assumes you have a README.md file
    long_description_content_type='text/markdown',  # Specify the format of the long description
    author='Jason Jafari',
    author_email='me@jasonjafari.com',
    url='https://github.com/smartdev-ca/mlModelSaver',  # URL to your package repository
    classifiers=[
       'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'License :: OSI Approved :: MIT License',  # Correct classifier for the MIT License
        'Programming Language :: Python :: 3.12',
    ],
    keywords='machine learning model saving serving',  # Keywords for your package
    install_requires=[
        'numpy>=1.26.4',
        'pandas>=2.2.2',
        'scikit-learn>=1.5.0',
        'statsmodels>=0.14.2',
        'matplotlib>=3.9.0',
        'dill>=0.3.8',
    ],
    project_urls={  # Optional
        'Documentation': 'https://github.com/smartdev-ca/mlModelSaver/blob/main/DOCS.md',
        'Source': 'https://github.com/smartdev-ca/mlModelSaver',
        'Tracker': 'https://github.com/smartdev-ca/mlModelSaver/issues',
    },
)
