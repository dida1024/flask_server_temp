# FLASK_SERVER_TEMP

## 🌌 引子
> "创造是一种热情，而不是一种工作。" -艾萨克·阿西莫夫

![version](https://img.shields.io/badge/version-1.0-blue)
![python](https://img.shields.io/badge/python-3.10-green)
![license](https://img.shields.io/badge/license-MIT-orange)

FLASK_SERVER_TEMP 是一个快速创建Flask后端服务的模板，旨在帮助开发者快速搭建项目框架。

## 🚀 特性

- 基于Flask的轻量级后端服务
- 集成MongoDB数据库支持
- JWT认证机制
- Swagger API文档自动生成
- 数据验证和序列化

## 📦 依赖

主要依赖：

- [Python](https://www.python.org/downloads/) (3.10)
- [Flask](https://flask.palletsprojects.com/) (3.0.3)
- [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/) (4.6.0)
- [Flask-PyMongo](https://flask-pymongo.readthedocs.io/) (2.3.0)
- [pymongo](https://pymongo.readthedocs.io/) (4.10.1)
- [flasgger](https://github.com/flasgger/flasgger) (0.9.7.1)
- [marshmallow](https://marshmallow.readthedocs.io/) (3.23.0)

完整的依赖列表请查看 `requirements.txt` 文件。

## 🛠️ 安装

1. 克隆仓库：
   ```
   git clone https://github.com/dida1024/FLASK_SERVER_TEMP.git
   cd FLASK_SERVER_TEMP
   ```

2. 创建并激活虚拟环境：
   ```
   python -m venv venv
   source venv/bin/activate  # 在Windows上使用 venv\Scripts\activate
   ```

3. 安装依赖：
   ```
   pip install -r requirements.txt
   ```

## 🚀 使用方法

1. 运行应用：
   ```
   flask run
   ```

2. 在浏览器中访问 `http://localhost:5000` 。

## 🤝 贡献

欢迎贡献代码、报告问题或提出新功能建议！请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解更多信息。

## 📄 许可证

本项目采用 MIT 许可证。详情请查看 [LICENSE](LICENSE) 文件。