from setuptools import setup, find_packages

setup(
    name='mlModelSaver',
    version='1.0.7',
    packages=find_packages(),
    description='Make life easier for saving and serving ML models',
    long_description=open('README.md').read(),  # Assumes you have a README.md file
    long_description_content_type='text/markdown',  # Specify the format of the long description
    author='Jason Jafari',
    author_email='me@jasonjafari.com',
    url='https://github.com/smartdev-ca/mlModelSaver',  # URL to your package repository
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'License :: MIT License',  # Specify your license
        'Programming Language :: Python :: 3.9 or above',
    ],
    keywords='machine learning model saving serving',  # Keywords for your package
    install_requires=[
        # List of dependencies, e.g.:
        # 'numpy>=1.18.0',
        # 'scikit-learn>=0.22.0',
    ],
    project_urls={  # Optional
        'Documentation': 'https://github.com/smartdev-ca/mlModelSaver/wiki',
        'Source': 'https://github.com/smartdev-ca/mlModelSaver',
        'Tracker': 'https://github.com/smartdev-ca/mlModelSaver/issues',
    },
)
