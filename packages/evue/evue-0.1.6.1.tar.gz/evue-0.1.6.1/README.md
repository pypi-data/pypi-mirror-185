# evue

> Evue is a high-performance gui framework base an html/css which can run on windows/linux/macos/web/ios/andriod/rtos! Write once, run everywhere!

See the [中文文档](https://github.com/scriptiot/evue/blob/master/README-zh.md) for Chinese readme.

## Features

![brief](https://github.com/scriptiot/evue/blob/master/doc/images/brief.png?raw=true)

+ Just python as you like 
+ multi-user for web
+ dark/light theme support
+ responsive support
+ ...

## Framework

+ Evue architecture 

> Evue is a high-performance gui framework base an html/css which is platform independence and ui engine independence!  

![evue](https://github.com/scriptiot/evue/blob/master/doc/images/evue.png?raw=true)


+ Evuecompiler architecture

> Evuecompiler is a compiler which compile evue file to python/javascript code!

![evuecompiler](https://github.com/scriptiot/evue/blob/master/doc/images/evuecompiler.png?raw=true)

+ Evue cross platfom
    + Evue for flutter (windows/linux/macos/web/ios/andriod)
    + Evue for lvgl（rtos on mcu like Asr3603/F1C100/F1C200/esp32/stm32/...）
> you can run evue on any platfom as you like!

+ Evue for all ui engine
    + Evue for flutter
    + Evue for lvgl
    + Evue for Qt
    + Evue for PySide2
    + ...
> you can compile evue to any ui code as you like!

## Installation
Use the package manager [pip](https://github.com/scriptiot/evue) to install evue.

```bash
pip install evue
```

or
```bash
git clone https://github.com/scriptiot/evue.git
cd evue
python setup.py install # also `pip install ."
```

## Getting started

+ [evue_website](https://github.com/scriptiot/evue/tree/master/examples/evue_website)

```python
cd examples
python evuebrowser.py ./evue_website/project.json
or
python evuebrowser.py ./evue_website/app.py
```

![evue_website](https://github.com/scriptiot/evue/tree/master/doc/images/evue_website.gif?raw=true)

+ [evue_login](https://github.com/scriptiot/evue/tree/master/examples/evue_login)

```python
cd examples
python evuebrowser.py ./evue_login/project.json
or
python evuebrowser.py ./evue_login/app.py
```

![evue_login](https://github.com/scriptiot/evue/tree/master/doc/images/evue_login.gif?raw=true)


## Evue Studio

> Evue Studio is a develop platform for evue developer to create/compile/deploy evue project!

![designer](https://github.com/scriptiot/evue/blob/master/doc/images/designer.png?raw=true)


[download latest evue studio](https://github.com/scriptiot/evue/releases/download/0.1.6.1/evuestudio-20230106211347-65b5a31.7z)

+ uncompress evuestudio-*.7z
+ double click `evuestudio.exe` 

## Evue for iot
> Evue for iot is a commercial product named `quicknode`, a tiny runtime of js engnine which can run on lots of mcu

![quicknode](https://github.com/scriptiot/evue/blob/master/doc/images/quicknode.gif?raw=true)

more info [what is quicknode](doc/EVUE%E4%BA%A7%E5%93%81%E4%BB%8B%E7%BB%8DPDF%E7%89%88.pdf)

[download quicknode](https://github.com/scriptiot/evue/releases/download/0.1.6/quicknode-qbc-20221215142421-693fbf88.zip)

+ uncompress quicknode-qbc-20221215142421-693fbf88.zip
+ double click `quicknode.bat` or `quicknode_chart.bat` 

[document](https://www.yuque.com/bytecode/eu1sci/ymto6i)

## how to compile evue to python code

![evue2py](https://github.com/scriptiot/evue/blob/master/doc/images/evue2py.gif?raw=true)

[how to compile evue to python code](https://github.com/scriptiot/evue/wiki/How-to-compile--evue-to--python-code%3F)

+ login in evue studio
+ switch to compile page
+ add project dir to watch
+ evue will be compiled to python code automatically when you change evue file

## Community

+ [Discussions](https://github.com/scriptiot/evue/discussions)
+ [Issues](https://github.com/scriptiot/evue/issues)


## Contribute to this wonderful project

+ `Welcome to contribute to this wonderful project no matter you are a community technical talent or designer talent, or product manager talent or community operation talent, your name will be one of evue contributors!`

+ `if you like evue, you can send email to [ding465398889@163.com], thanks!`


## Contact

> If there is a need for cooperation, please send email/wechat/QQ for more support!

+ Email : ding465398889@163.com
+ WeChat: dragondjf
> ![dragondjf](https://github.com/scriptiot/evue/blob/master/doc/images/dragondjf.jpg?raw=true)
+ Evue for IOT
> ![dragondjf](https://github.com/scriptiot/evue/blob/master/doc/images/QQ.jpg?raw=true)

## Salute

+ [evm](https://github.com/scriptiot/evm)
+ [lvgl](https://github.com/lvgl/lvgl)
+ [flet](https://github.com/flet-dev/flet)
+ [flutter](https://github.com/flutter/flutter)
