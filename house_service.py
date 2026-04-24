from db_operation import read_houses, write_houses


def get_next_house_id():
    """
    生成下一个房源ID（保证ID唯一）
    时间复杂度：O(n)（遍历所有房源找最大ID）
    return: 下一个可用的ID（整数）
    """
    houses = read_houses()
    if not houses:
        return 1  # 无房源时，第一个ID为1
    # 找到最大ID，加1作为新ID
    max_id = max(house["id"] for house in houses)
    return max_id + 1


def add_house(address, price, area, house_type):
    """
    新增房源（线性表的尾部插入操作）
    时间复杂度：O(n)（read/write各O(n)，整体O(n)）
    空间复杂度：O(n)（存储所有房源数据）
    param address: 房源地址（字符串）
    param price: 租金（整数/浮点数）
    param area: 面积（整数/浮点数）
    param house_type: 户型（字符串，如"一居室"）
    return: 新增成功返回True，失败返回False
    """
    # 基础数据校验（非空+数值合法性）
    if not address or not house_type:
        print("错误：地址和户型不能为空！")
        return False
    if not isinstance(price, (int, float)) or price <= 0:
        print("错误：租金必须是正数！")
        return False
    if not isinstance(area, (int, float)) or area <= 0:
        print("错误：面积必须是正数！")
        return False

    # 构建新房源字典（线性表的元素）
    new_house = {
        "id": get_next_house_id(),
        "address": address,
        "price": price,
        "area": area,
        "house_type": house_type
    }

    # 读取现有房源（线性表），新增元素（尾部插入）
    houses = read_houses()
    houses.append(new_house)  # 线性表append操作，时间复杂度O(1)

    # 写入文件
    write_houses(houses)
    print(f"房源新增成功！房源ID：{new_house['id']}")
    return True


def delete_house(house_id):
    """
    删除房源（线性表的指定位置删除操作）
    时间复杂度：O(n)（遍历找ID+写入文件，整体O(n)）
    空间复杂度：O(n)（存储所有房源数据）
    param house_id: 要删除的房源ID（整数）
    return: 删除成功返回True，失败返回False
    """
    houses = read_houses()
    # 遍历线性表，找到对应ID的房源
    for index, house in enumerate(houses):
        if house["id"] == house_id:
            del houses[index]  # 线性表删除操作，时间复杂度O(n)（后续元素前移）
            write_houses(houses)
            print(f"房源ID {house_id} 删除成功！")
            return True
    print(f"错误：未找到房源ID {house_id}！")
    return False


def update_house(house_id, new_info):
    """
    修改房源信息（线性表的指定元素更新操作）
    时间复杂度：O(n)（遍历找ID+写入文件，整体O(n)）
    空间复杂度：O(n)（存储所有房源数据）
    param house_id: 要修改的房源ID（整数）
    param new_info: 要修改的字段字典（如{"price": 5500, "area": 85}）
    return: 修改成功返回True，失败返回False
    """
    houses = read_houses()
    # 遍历线性表，找到对应ID的房源
    for house in houses:
        if house["id"] == house_id:
            # 仅更新传入的有效字段
            for key, value in new_info.items():
                if key in ["address", "price", "area", "house_type"]:
                    # 校验数值字段合法性
                    if key in ["price", "area"]:
                        if not isinstance(value, (int, float)) or value <= 0:
                            print(f"错误：{key}必须是正数！")
                            return False
                    house[key] = value
            write_houses(houses)
            print(f"房源ID {house_id} 修改成功！")
            return True
    print(f"错误：未找到房源ID {house_id}！")
    return False


def query_house(condition_type, condition_value):
    """
    查询房源（线性表的遍历筛选操作）
    时间复杂度：O(n)（遍历所有房源，n为房源数）
    空间复杂度：O(k)（k为符合条件的房源数，最坏O(n)）
    param condition_type: 查询条件类型（"id"/"address"/"price"/"house_type"）
    param condition_value: 查询条件值
    return: 符合条件的房源列表
    """
    houses = read_houses()
    result = []
    # 按条件遍历筛选
    for house in houses:
        # 处理ID查询（整数匹配）
        if condition_type == "id":
            if house["id"] == int(condition_value):
                result.append(house)
        # 处理地址查询（模糊匹配）
        elif condition_type == "address":
            if condition_value in house["address"]:
                result.append(house)
        # 处理户型查询（精确匹配）
        elif condition_type == "house_type":
            if house["house_type"] == condition_value:
                result.append(house)
        # 处理租金查询（数值匹配，示例：查询等于该价格的房源）
        elif condition_type == "price":
            if house["price"] == float(condition_value):
                result.append(house)
        else:
            print("错误：不支持的查询条件类型！")
            return []
    return result
