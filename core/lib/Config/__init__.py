import os
import json


def check_config(config_file=None):
    # 默认配置名
    if config_file is None:
        config_file = "config.json"

    # 检测配置文件是否存在
    if not is_config_file_exists(config_file):
        init_config_file(config_file)


def is_config_file_exists(config_file):
    if os.path.exists(config_file):
        return True
    else:
        return False


def init_config_file(config_file):
    config_content = {
        "proj_name": "Hsunr",
        "host": "127.0.1",
        "port": "5000"
    }
    json_object = json.dumps(config_content)
    with open(config_file, "w") as f:
        f.write(json_object)

def update_config_file(config_file,new_config):
    config_data = None
    with open(config_file, "r", encoding="utf-8") as f:
        config_data = json.load(f)
        config_data.update(new_config)

    with open(config_file, "w", encoding="utf-8") as f:
        json.dump(config_data, f)

def get_config(config_file=None):
    if config_file is None:
        config_file="config.json"
    with open(config_file, "r", encoding="utf-8") as f:
        config_data = json.load(f)
    return config_data
