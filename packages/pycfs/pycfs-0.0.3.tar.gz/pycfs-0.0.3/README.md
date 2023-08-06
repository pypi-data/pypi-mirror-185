# PyCFS : Automatization and optimization interface library for Trelis and CFS


<!-- Badges -->

[![PyPI Version][pypi-image]][pypi-url]

[pypi-image]: https://img.shields.io/pypi/v/pycfs
[pypi-url]: https://pypi.org/project/pycfs/

<!-- Documentation  -->

## Installation - non developers : 
**PyCFS** can now be installed and updated directly with `pip`. If you don't have a python distribution installed we recommend you to first install an anaconda distribution of python and set up an environment with **Python 3.9**. To do this follow these steps : 

- Download and install anaconda python distribution (miniconda is also fine)
- Open your command prompt (anaconda prompt on windows/bash on linux)
- Create a new environment with : `conda create --name simenv python=3.9`
- Switch to new environment with : `conda activate simenv`
- Make sure that the next time you are using the library you switch to the `simenv` environment.

Then you can proceede with the package install. 

If using anaconda python distribution, run :  
```bash
python -m pip install pycfs
```

else if using system python then run : 
```bash
pip3 install pycfs
```

To upgrade to a newer version of the software just run : 
```bash
python -m pip install --upgrade pycfs
```

## Installation - developers :

To install the package make sure you're in the same directory as the **setup.py** file. If you are 
using an anaconda distribution just run : 
```
$ python -m pip install -r requirements.txt
$ python -m pip install -e .
```
the `-e` flag applies the changes you make while developing directly to the package so that you can easily test it while developing in this source directory.

If you are using a direct python installation run : 
```
pip3 install -r requirements.txt
pip3 install -e .
```
This will install the required packages and then the *pycfs* package itself.

## Developer notes : 

### Build and update : 

```bash
# building the new release : 
python -m build

# upload to pypi (assuming that in dist only new build): 
python -m twine upload --skip-existing dist/*
```

## Command line tool :

There is also a command line tool which allows the automatic setup generation for your projects. After installing *PyCFS* to your system this tool will be available automatically. To check it out and get the help information just type : 
```bash
pycfs --help
```

To generate a project run : 

```bash
pycfs newsim my_cool_project 
```

This will generate a folder structure and template files for you to fill with your simulation files. Additionally one can specify the path to *CFS* on your machine as well as the alias for the used *mesher* as shown in the help page.

## Example : Local usage

In the *example_local* folder an example is presented on how to use the package to automate the 
changing of model parameters, geometry and mesh parameters as well as simulation parameters. 

The main idea is to define a *PyCfs* object which needs : 

- `project_name` : name of the project - must be the same as the associated *xml* file.
- `cfs_path` : location of CFS installation (for example on RK03 it is '/share/programs/Devel/CFS_BIN/build_opt')
- `trelis_params` : these are the names of the trelis params as they are defined in the journal file.
- `init_params` : a set of initial parameters for the model to run a first setup pass.


## Example : Remote usage (ssh and vscode) 

In the case that one is using a remote machine to run and/or develop on that machine a nice solution is to use __[VS Code](https://code.visualstudio.com/)__ and install the __[Remote SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh)__ extension. This allows one to browse, edit and run code on the remote machine within the local VS Code window. To set up a connection after installing the necessary extension it is straight forward, in the lower left corner a small icon will appear. Click on the icon and a window at the top center of the screen will appear. Listing some of the choices : 

- `Remote SSH: Connect Current Window to Host...`
- `Remote SSH: Connect to Host...`
- ...

You can choose the first option if no new window should be opened. A guide on what is needed will be shown and after putting in all of the information it will be saved for later usage. 

A very nice point about this approach is that it is possible to even run **jupyter notebooks** inside of the *VS Code* windows. This is usefull if any analysis of the data with plots or some prototyping is needed. 

If one is inclined to use **jupyter notebooks** in the browser environment please refer to this __[tutorial](https://ljvmiranda921.github.io/notebook/2018/01/31/running-a-jupyter-notebook/)__ on how to set up the ssh connection and ports to do this. It is quite easy but the approach with VS Code is much nicer in general. 