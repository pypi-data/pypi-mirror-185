# Beat Python Readme

The package contains several function to make analysis easier. Several function included in the packages are:
- Connection to Presto
- API connection to S3
- API connection to google
- Visualisation

There are pre-requisite to connect to google as described here:

# Instalation
Since the package will consist of geo related package so installing gdal is necessary (be patient, takes time)
```
brew install gdal
```
Install the sakudata package
```
pip install /path/to/project --upgrade --upgrade-strategy eager
```


# How to update the wheels

Install pipreqs
```
pip install pipreqs
```
Inside the project folder, run this command
```
pipreqs /path/to/project --force
```
Create the distribution file
```
python -m build
```

