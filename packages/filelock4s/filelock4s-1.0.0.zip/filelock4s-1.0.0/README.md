# filelock4s - single shared lock pool manage by filelock.

![image](https://img.shields.io/badge/made_in-china-ff2121.svg)
[![image](https://img.shields.io/pypi/v/filelock4s.svg)](https://pypi.org/project/filelock4s/)
[![image](https://img.shields.io/pypi/l/filelock4s.svg)](https://pypi.org/project/filelock4s/)

## About
基于filelock实现的单个共享锁数据文件的锁池管理.

## Requirements
- Python3.9

## Install
通过pip命令安装：
```shell
pip install filelock4s
```
或者通过下载源码包或clone代码至本地，然后通过如下命令安装：
```shell
python setup.py install
```

## Example
```python
from filelock4s.user_pool import UserPool

with UserPool("user.data").acquire_to_add_current_user():
    pass
```
