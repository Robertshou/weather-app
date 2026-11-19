# 天气查询小工具（Python）

一个基于 Python 的命令行天气查询小程序，输入城市名即可查看实时温度、天气、湿度和风速。
天气数据来自免费接口 [wttr.in](https://wttr.in/)，**无需申请 API Key**。

## 环境要求

- Python 3.8 及以上
- Windows / macOS / Linux 均可

## 安装依赖

```bash
pip install -r requirements.txt
```

## 运行

```bash
python weather.py
```

启动后按提示输入城市名（如 `天津`、`北京`、`Shanghai`），输入 `q` 退出。

## 功能说明

- 实时温度、天气状况、湿度、风速
- 支持连续查询多个城市
- 网络异常 / 城市名错误时有友好提示，不会直接崩溃

## 项目结构

```
weather-app/
├── weather.py        # 主程序
├── requirements.txt  # 依赖清单
├── .gitignore        # Git 忽略规则
└── README.md         # 项目说明
```

## 备注

- wttr.in 在国内网络下偶尔可能超时，多试几次即可；如长期不稳定，可替换为和风天气等国内接口。
- 本项目仅用于学习交流。
