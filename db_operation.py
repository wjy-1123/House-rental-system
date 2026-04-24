import json
import os

# 定义数据文件路径
DATA_FILE = "./data/houses.json"

def init_db():
    """
    初始化数据文件：如果houses.json不存在，创建并写入空列表
    空间复杂度：O(1)（仅创建空文件）
    """
    # 确保data文件夹存在
    os.makedirs("./data", exist_ok=True)
    # 如果文件不存在，创建并写入空列表
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump([], f, ensure_ascii=False, indent=4)

def read_houses():
    """
    读取所有房源数据
    时间复杂度：O(n)（n为房源数，JSON解析耗时与数据量正相关）
    空间复杂度：O(n)（存储所有房源数据）
    return: 房源列表（每个元素是字典）
    """
    init_db()  # 先确保文件存在
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def write_houses(houses):
    """
    写入房源数据到JSON文件
    时间复杂度：O(n)（n为房源数，JSON序列化耗时与数据量正相关）
    空间复杂度：O(1)（仅写入操作，无额外存储）
    param houses: 要写入的房源列表
    """
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(houses, f, ensure_ascii=False, indent=4)
