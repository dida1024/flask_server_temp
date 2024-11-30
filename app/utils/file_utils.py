# 文件工具类

import os
import uuid

from app.config import Config

def create_temp_file(suffix: str = ".pcm"):
    temp_dir = Config.TEMP_PATH
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    return os.path.join(temp_dir, f"{uuid.uuid4()}{suffix}")

def delete_temp_file(path: str):
    if os.path.exists(path):
        os.remove(path)

# 创建下载文件
def create_download_file(suffix: str = ".pcm"):
    # 创建下载文件夹
    download_dir = Config.DOWNLOAD_PATH
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    # 文件名
    file_name = f"{uuid.uuid4()}{suffix}"
    file_path = os.path.join(download_dir, file_name)
    
    download_url = f"{Config.DOWNLOAD_URL}{file_name}"
    
    return file_path, download_url

# 从指定目录中查找文件
def find_file(file_name: str):
    # 获取当前文件所在目录的上两级目录（ai_tran_server）
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    # 直接在 ai_tran_server 目录下的 download 文件夹中查找
    download_dir = os.path.join(base_dir, 'download')
    file_path = os.path.join(download_dir, file_name)
    print(f"查找文件: {file_path}")
    print(f"文件是否存在: {os.path.exists(file_path)}")  # 添加调试信息
    if os.path.exists(file_path):
        return file_path
    return None
