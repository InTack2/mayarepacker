# mayarepacker  

[![PyPI Versions](https://img.shields.io/pypi/v/mayarepacker.svg)](https://pypi.org/project/mayarepacker)
[![Downloads](https://pepy.tech/badge/mayarepacker)](https://pepy.tech/project/mayarepacker)
[![license](https://img.shields.io/pypi/l/mayarepacker)](https://pypi.org/project/mayarepacker)
[![Supported Versions](https://img.shields.io/pypi/pyversions/mayarepacker.svg)](https://pypi.org/project/mayarepacker)
[![pytest](https://codecov.io/gh/InTack2/mayarepacker/branch/master/graph/badge.svg)](https://codecov.io/gh/InTack2/mayarepacker)
[![code style](https://img.shields.io/badge/code%20style-flake8-000000.svg)](https://pypi.org/-project/flake8/)  

Automatic package reloader for Maya.  
[README Japanese version](https://github.com/InTack2/mayarepacker/blob/main//README_jp.md)  

## Features
This repository is a feature that makes it easy to hot-load their tools when they create them in Maya.  
When monitoring is started, the specified Package will be reloaded when the pythonFile under the specified folder is updated.  
[![Image from Gyazo](https://i.gyazo.com/b7d1c54e6e51d4092a16d5c8b9e36637.gif)](https://gyazo.com/b7d1c54e6e51d4092a16d5c8b9e36637)

It is also possible to manually reload at any time.  
[![Image from Gyazo](https://i.gyazo.com/ed5358930ec629c33af9e9cfce2c0d9e.gif)](https://gyazo.com/ed5358930ec629c33af9e9cfce2c0d9e)

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

## Support
〇・・confirmed operation.  
？・・Not tested.  
| Maya Verison | Windows | Mac |
| ------------ | ------- | --- |
| 2018         | 〇      | ？  |
| 2019         | ？      | ？  |
| 2020         | 〇      | 〇  |
| 2022         | 〇      | ？  |

## release

- 1.0.2
  - Fixed an issue that prevented Maya2018 from starting properly due to QStringModel.

- 1.0.0
  - Initial release.