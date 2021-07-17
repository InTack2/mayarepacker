# mayarepacker  

[![PyPI Versions](https://img.shields.io/pypi/v/mayarepacker.svg)](https://pypi.org/project/mayarepacker)
[![Downloads](https://pepy.tech/badge/mayarepacker)](https://pepy.tech/project/mayarepacker)
[![license](https://img.shields.io/pypi/l/mayarepacker)](https://pypi.org/project/mayarepacker)
[![Supported Versions](https://img.shields.io/pypi/pyversions/mayarepacker.svg)](https://pypi.org/project/mayarepacker)
[![pytest](https://codecov.io/gh/InTack2/mayarepacker/branch/master/graph/badge.svg)](https://codecov.io/gh/InTack2/mayarepacker)
[![code style](https://img.shields.io/badge/code%20style-flake8-000000.svg)](https://pypi.org/-project/flake8/)  

Automatic package reloader for Maya.

## Features
This repository is a feature that makes it easy to hot-load their tools when they create them in Maya.  
When monitoring is started, the specified Packge will be reloaded when the pythonFile under the specified folder is updated.  
![AutoReload.git](https://github.com/InTack2/mayarepacker/blob/main/images/AutoReload.gif)

It is also possible to manually reload at any time.  
![ManualReload.git](https://github.com/InTack2/mayarepacker/blob/main/images/ManualReload.gif)

## How to install
Install it with pip.
Run `pip install mayarepacker`.

You can start it by running the following in the Maya console.
Register it on the shelf and use it as needed.
``` python
import mayarepacker
mayarepacker.main()
```

## Usage
There are two modes of mayarepacker
- Automatic reload
  - Specify a folder and mayarepacker will reload the specified package when there is an update to the Python files under that folder.
- Manual reload
  - Reloads the specified package.

### Manual Reload
- Specify the reload target
- Click the reload button.

### Auto Reload
- Specify the folder to monitor
- Select the target to reload when there is an update
- Start monitoring
- Confirm that the file is automatically updated when it is updated.
- If you want to stop the monitoring, you can click the Stop button or close the tool.
