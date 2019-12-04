## Project directory structure
```
├── README.md          Add some info about your project here
├── data               Your data files (ignored in version control) and datasets specifications lives here
│   ├── processed      Do not ever modify your raw data, do your preprocessing and store the final files here
│   ├── cache          Downloaded raw data files lives here
│   └── raw            Do not download any files here
│       ├── dataset1   
│       │   └── .toml  Specifications for downloading data
│       ├── dataset2
│       │   └── .csv   Actual dataset with links to binaries like images, audio files, etc... Use git-lfs if this file gets big enough
│       └── dataset3   
│           └── .json  Actual dataset with links to binaries like images, audio files, etc... Use git-lfs if this file gets big enough
├── logs               Your model training logs live here, so model training could be monitored by TensorBoard
├── notebooks          Your notebooks live here and their name indicate the order they should be ran. i.e. 01-explore-... and 02-clean-...
├── src                Your python files live here
│   ├── __init__.py
│   └── utils
│       ├── __init__.py
│       └── utils.py   
├── scripts            Your shell scripts that perform various tasks live here 
│   └── cleanup.sh     Clear your cached data, logs, etc...
└── weights
```


## Using virtual environments
Conda or pipenv come pre-installed for easy quick use.

### Create a new environment
First you need to change your current directory to the one where you want your environment config to be tracked.
If you want to use pipenv, initalize your environment by calling `pipenv lock` and if you want to use conda, run `conda create --name YOUR_ENV_NAME python=3.7 -y`.

### Make Jupyter aware of the new environment
If you are using conda, just install `ipykernel` inside your new environment `conda install -n ENV_NAME ipykernel`

Otherwise if you are using `pipenv`, `virtualenv`, etc... install `ipykernel` in your new environment `pip install ipykernel`. And then  `python -m ipykernel install --user --name=ENV_NAME`.

### Remove unused kernels
First to find all the available kernel specs `jupyter kernelspec list` and then you can run `jupyter kernelspec remove KERNAL_NAME`

# Access Kaggle datasets
First you need to install kaggle cli `pip install kaggle --upgrade` and then generate an API key by going to https://www.kaggle.com/<username>/account and select 'Create API Token'
```
export KAGGLE_USERNAME=username
export KAGGLE_KEY=xxxxxxxxx
```
