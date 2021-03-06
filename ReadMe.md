# HAF    

    支持多种测试的高可用测试框架

[![Build Status](https://travis-ci.org/hautof/haf.svg?branch=master)](https://travis-ci.org/hautof/haf)
[![Documentation Status](https://readthedocs.org/projects/haf/badge/?version=latest)](https://haf.readthedocs.io/en/latest/?badge=latest)
[![PyPI](https://img.shields.io/pypi/v/haf.svg)](https://img.shields.io/pypi/v/haf.svg) [![GitHub release](https://img.shields.io/github/release/hautof/haf.svg)](https://img.shields.io/github/release/hautof/haf.svg)
                

![all](https://raw.githubusercontent.com/tsbxmw/haf/master/docs/show/all.gif)


# 安装

## 使用 pip 直接安装

```shell
   tsbxmw@ps# pip install haf --upgrade
```

## 使用 git 下载源码安装

```bash
   tsbxmw@ps# git clone https://github.com/tsbxmw/haf
   tsbxmw@ps# cd haf
   tsbxmw@ps# python setup.py install
```


# 如何运行例子

## 1，使用 `init` 命令 或者 `git` 获取源码例子

```bash
    python -m haf init
```

或者

```bash
    git clone https://github.com/tsbxmw/haf-sample
```

## 2, 例子提供了 `api` 和 `web-ui` 的测试用例

### 运行 `api` 用例

```bash
    python -m haf run -c=config.json
```

### 运行 `web ui` 测试用例

```bash
    python -m haf run -c=config-web.json
```

## 3, 可以在 `data` 文件夹下找到 `index.html`，作为默认的 html 报告

    使用 `chrome` 或者其他浏览器打开即可。

# 其他内容

| 快速开始 | 例子 | pypi 主页 | 文档主页 |
|---|---|---|---|
| [开始](https://github.com/tsbxmw/haf/wiki/Quick-Start) | [haf-sample](https://github.com/hautof/haf-sample) | [pypi](https://pypi.org/project/haf/) | [doc](https://haf-doc.readthedocs.io/en/dev-2.1.0/) |


# 插件

| id | 插件名称 | 插件版本 | github 主页|
|---|---|---|---|
| 1 | haf api server | [![PyPI](https://img.shields.io/pypi/v/hafapiserver.svg)](https://img.shields.io/pypi/v/hafapiserver.svg) | [haf webserver](https://github.com/hautof/haf-plugin-webserver) |
| 2 | haf sql publish | [![PyPI](https://img.shields.io/pypi/v/hafsqlpublish.svg)](https://img.shields.io/pypi/v/hafsqlpublish.svg) | [haf sqlpublish](https://github.com/hautof/haf-plugin-sqlpublish) |


# 如何运行自定义的用例

## 可以本地运行所以的用例

### 所有的进程在本地模式下都是在本机存在的

- `--bus-server(-bs)` 参数不适用时便是本地模式

### 修改 `testcases` 中的 `config.json` 文件，用来运行自己的用例

- 修改 `log_path` 和 `report_path` 和 `case_path` 3 个字段为自己默认的地址，分别为 日志路径、报告路径、用例路径。
- 可以删除 `config->run->sql_publish` 字段，如果不需要将数据上传到数据库。

```json
    {
      "config":{
        "name": "test",
        "debug" : false,
        "bus_server_port": 8801,
        "run": {
          "sql_publish": {
            "id": 1,
            "sql_name": "upload",
            "publish": true,
            "host": "192.168.0.200",
            "port": 3306,
            "username": "root",
            "password": "root",
            "database": "haf_publish",
            "protocol": "mysql"
          },
          "log": {
            "log_path": "./data"
          },
          "bus": {
            "only": false,
            "host": "",
            "port": "",
            "auth_key": ""
          },
          "report": {
            "report_path": "./data/report.html",
            "report_template": "base",
            "report_export_path": "email"
          },
          "case": [
            {
              "case_path": "./testcases/test.xlsx"
            },
            {
              "case_path": "./testcases/test2.json"
            },
            {
              "case_path": "./testcases/test1.xlsx"
            },
            {
              "case_path": "./testcases/test3.yml"
            }
          ],
          "runner":{
            "only": false,
            "count": 4
          },
          "loader": {
            "only": false
          },
          "recorder": {
            "only": false
          },
          "web_server": {
            "host": "",
            "port": "",
            "run": true
          }
        }
      }
    }
```

### 可以使用 `testcases` 中提供的默认例子创建新的用例

- 创建 `xlsx/py/json/yaml` 格式的用例
- 也可以使用 `haf-sample` 中的例子

### 运行

#### 使用 `config` 配置运行 测试

```shell
    python -m haf run -c=./testcases/config.json
```

#### 使用 参数 运行测试

```shell
    python -m haf run -case=./testcases/test.xlsx,./testcases/test2.json -ld=./data -rh=true -rod=./data/report.html
```

# 测试报告


![report](https://raw.githubusercontent.com/tsbxmw/haf/master/docs/show/report.gif)



# 如何运行 app-ui 测试用例

- 更改 `config.json` 中的 `report` 字段，增加 `report_template` 子字段， 使用 `base_app` 为模板

```json
    "run": {
        "type": "app"  # change type to app

        "report": {
            "report_template": "base_app",  # change report_template to base_app
            "report_path": "./data/report.html"
        }
    }
```

![report-app](https://raw.githubusercontent.com/tsbxmw/haf/master/docs/show/report-app.gif)


# 运行 web-ui 测试用例

- 更改 `config.json` 中的 `report` 字段，增加 `report_template` 子字段， 使用 `base_web` 为模板


```json
    "run": {
        "type": "web"  # change type to web

        "report": {
            "report_template": "base_web",  # change report_template to base_web
            "report_path": "./data/report.html"
        }
    }
```

![report-app](https://raw.githubusercontent.com/tsbxmw/haf/master/docs/show/webui.gif)



# haf 例子

> https://github.com/hautof/haf-sample


# 其他的命令行参数

- 使用多个 runner 增加运行速度， `runner-count`

```shell
    python -m haf run -rc=4
```

- 启动 web-server，提供可视化过程，`web-server` 

```shell
    python -m haf run -ws=true
```

- 只启动 `loader/runner/bus/recorder` 中的某个

```shell
    # only loader
    python -m haf run -ol=true
    # only bus
    python -m haf run -ob=true
    # only runner
    python -m haf run -or=true
    # only recorder
    python -m haf run -ore=true
```

- 使用自定义的报告模板

```json
    "report": {
        "report_template": "base_app"
    }
```

- 使用插件将数据发送到 数据库

```json
    "sql_publish": {
        "id": 1,
        "sql_name": "upload",
        "publish": true,
        "host": "192.168.0.200",
        "port": 3306,
        "username": "root",
        "password": "root",
        "database": "haf_publish",
        "protocol": "mysql"
    }
```

![sql](https://raw.githubusercontent.com/tsbxmw/haf/master/docs/png/haf-publish.png)


### 其他支持

```bash
    tsbx# pip install hafweb -U
```


```python
    python -m hafweb -ss=root:root@localhost:3306@haf_publish -p=8081
```

- 默认页面

   http://localhost:8081/

- index page
   
   http://localhost:8081/index
   
- today page

   http://localhost:8081/today
   
- others support looking at hafweb project


### web api server suport

- get loader infos

```bash
    http://localhost:8888/loader
```

- get runner infos

```bash
    http://localhost:8888/runner
```

- get result infos

```bash
    http://localhost:8888/result
```

- get report infos

```bash
    http://localhost:8888/report
    http://localhost:8888/report-app
```

### FrameWork 

#### Design

![map](https://raw.githubusercontent.com/tsbxmw/haf/master/docs/png/HAF-2.0.0.png)

### Doc

> [doc url](https://github.com/tsbxmw/haf/blob/master/docs/design.md)

> [read the doc](https://haf-doc.readthedocs.io/en/dev-2.2.0/)

> [wiki home](https://github.com/tsbxmw/haf/wiki)

> [Quick Start](https://github.com/tsbxmw/haf/wiki/Quick-Start)

### Release Note

[release note](https://github.com/tsbxmw/haf/blob/master/docs/releasenote.md)

### new features

- now support app-ui/web-ui cases and generate report

- support mysql result publish

- based on local test runners

- support xlsx,json,yml,py cases

- report generate with html-template

- multi-processes on different machines

- multi-runners

- web-server support restful api based on flask

- only mode : loader/runner/recorder/webserver/bus/logger support