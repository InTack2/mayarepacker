# mayarepacker  

[![PyPI Versions](https://img.shields.io/pypi/v/mayarepacker.svg)](https://pypi.org/project/mayarepacker)
[![Downloads](https://pepy.tech/badge/mayarepacker)](https://pepy.tech/project/mayarepacker)
[![license](https://img.shields.io/pypi/l/mayarepacker)](https://pypi.org/project/mayarepacker)
[![Supported Versions](https://img.shields.io/pypi/pyversions/mayarepacker.svg)](https://pypi.org/project/mayarepacker)
[![pytest](https://codecov.io/gh/InTack2/mayarepacker/branch/master/graph/badge.svg)](https://codecov.io/gh/InTack2/mayarepacker)
[![code style](https://img.shields.io/badge/code%20style-flake8-000000.svg)](https://pypi.org/-project/flake8/)  

Maya の自動パッケージリローダ.

[README 英語版](https://github.com/InTack2/mayarepacker/blob/main//README.md)  

## Features
このリポジトリは、TechnicalArtistがMayaでツールを作成する際に、簡単にホットロードするための機能です。
モニタリングを開始すると、指定したフォルダ配下のpythonFileが更新されると、指定したPackageがリロードされます。 

[![Image from Gyazo](https://i.gyazo.com/b7d1c54e6e51d4092a16d5c8b9e36637.gif)](https://gyazo.com/b7d1c54e6e51d4092a16d5c8b9e36637)

It is also possible to manually reload at any time.  
[![Image from Gyazo](https://i.gyazo.com/ed5358930ec629c33af9e9cfce2c0d9e.gif)](https://gyazo.com/ed5358930ec629c33af9e9cfce2c0d9e)


## 導入方法
pipでインストールしてください。
`pip install mayarepacker`を実行

Mayaのコンソールで以下実行で起動できます。
適宜、シェルフに登録などしてご利用ください。
```python
import mayarepacker
mayarepacker.main()
```

## Usage
mayarepackerには下記の2つのモードがあります。
- 自動リロード
  - フォルダを指定し、そのフォルダ以下のPythonファイルに更新があった場合に指定パッケージをリロードする。
- 手動リロード
  - 指定パッケージをリロードする

### 手動リロード
- リロード対象を指定
- ボタンを押す

### 自動リロード
- 監視するフォルダを指定する
- 更新があった時のリロード対象を選択
- 監視を開始
- 更新等した時に自動で更新されている事を確認
- 監視を終了したい時はStopボタンを押すかツールを閉じる事で可能。

## サポート
〇・・動作確認済み
？・・未確認
| Maya Verison | Windows | Mac |  
| ------------ | ------- | --- |  
| 2018         | 〇      | 〇  |  
| 2019         | ？      | ？  |  
| 2020         | 〇      | 〇  |  
| 2022         | 〇      | 〇  |  