### haf    
    
    The http api auto test framework. 
    
[![Build Status](https://travis-ci.org/tsbxmw/haf.svg?branch=master)](https://travis-ci.org/tsbxmw/haf)


### new features


- based on ~~ pytest & allure~~ local test runner now

- support xlsx,json,yml,py easy cases

- report generate

- multy processes

- multy runner on different machine



### How to get it

> using pip to get it

```shell
   tsbxmw@ps# pip install haf --upgrade
```

> using git tool to get it

```bash
   tsbxmw@ps# git clone https://github.com/tsbxmw/haf
   tsbxmw@ps# cd haf
   tsbxmw@ps# python setup.py install
```


### How to run

- mkdir at testcases

```shell
    mkdir testcases
```

- create xlsx file with template in template

- move file.xlsx to testcases

- run 

```shell
    python -m haf --case=testcases
```


### FrameWork 

#### Design

![map](/doc/HAF-dev2.0.0.png)

#### Doc

[doc url](https://github.com/tsbxmw/haf/tree/dev-2.0.0/doc)

### Release Note

> version 1.1.6
* add argparse to make arg tool
* local runner to replace pytest (dev)
* testsuite support (dev)
* testresult support (dev)

> version 1.1.5
* add assertpy support

> version 1.1.3
* add assert_that func to Run to show more in allure

> version 1.1.1
* change to wheel 

> version 1.0.2
* upload to pypi

> version 0.5
* 增加 report allure 2.5 setup 支持
* 增加 report 的 发布

> version 0.4
* complete basic function with xlsx file 
* add python doc support at doc 