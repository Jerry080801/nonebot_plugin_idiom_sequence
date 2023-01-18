<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-idiom-sequence

_✨ NoneBot 防撤回插件 ✨_


<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/A-kirami/nonebot-plugin-namelist.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-namelist">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-namelist.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">

</div>


## 📖 介绍

抄/修改自 https://github.com/wsdtl/nonebot_plugin_Idiom 的成语接龙
跨群, 多人游戏的特点能够让一个接龙活跃下去


## 💿 安装

<details>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-idiom-sequence

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-idiom-sequence
</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-idiom-sequence
</details>
<details>
<summary>poetry</summary>

    poetry nonebot-plugin-idiom-sequence
</details>
<details>
<summary>conda</summary>

    conda install nonebot-plugin-idiom-sequence
</details>

打开 nonebot2 项目的 `bot.py` 文件, 在其中写入

    nonebot.load_plugin('nonebot_plugin_idiom_sequence')

</details>


## 🎉 使用
### 指令表
| 指令 | 说明 |
|:-----:|:----:|
| 成语接龙|开始游戏 |
| 接/我接/接龙/j + 成语|接龙 |
| 结束接龙 |结束游戏 |
