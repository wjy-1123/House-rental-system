from house_service import add_house, delete_house, update_house, query_house

def print_menu():
    """打印控制台菜单"""
    print("\n===== 房屋出租系统 V1.0 =====")
    print("1. 新增房源")
    print("2. 删除房源")
    print("3. 修改房源")
    print("4. 查询房源")
    print("5. 退出系统")
    print("============================")

def main():
    """主程序入口"""
    while True:
        print_menu()
        choice = input("请输入操作编号（1-5）：")
        # 1. 新增房源
        if choice == "1":
            print("\n----- 新增房源 -----")
            address = input("请输入房源地址：")
            try:
                price = float(input("请输入租金（元/月）："))
                area = float(input("请输入面积（㎡）："))
            except ValueError:
                print("错误：租金/面积必须是数字！")
                continue
            house_type = input("请输入户型（如：一居室、两居室）：")
            add_house(address, price, area, house_type)
        # 2. 删除房源
        elif choice == "2":
            print("\n----- 删除房源 -----")
            try:
                house_id = int(input("请输入要删除的房源ID："))
                delete_house(house_id)
            except ValueError:
                print("错误：房源ID必须是整数！")
        # 3. 修改房源
        elif choice == "3":
            print("\n----- 修改房源 -----")
            try:
                house_id = int(input("请输入要修改的房源ID："))
                # 收集要修改的字段
                new_info = {}
                address = input("请输入新地址（不修改按回车）：")
                if address:
                    new_info["address"] = address
                price_input = input("请输入新租金（不修改按回车）：")
                if price_input:
                    try:
                        new_info["price"] = float(price_input)
                    except ValueError:
                        print("错误：租金必须是数字！")
                        continue
                area_input = input("请输入新面积（不修改按回车）：")
                if area_input:
                    try:
                        new_info["area"] = float(area_input)
                    except ValueError:
                        print("错误：面积必须是数字！")
                        continue
                house_type = input("请输入新户型（不修改按回车）：")
                if house_type:
                    new_info["house_type"] = house_type
                # 调用修改函数
                if new_info:
                    update_house(house_id, new_info)
                else:
                    print("未输入任何修改内容！")
            except ValueError:
                print("错误：房源ID必须是整数！")
        # 4. 查询房源
        elif choice == "4":
            print("\n----- 查询房源 -----")
            print("查询条件类型：1-ID  2-地址  3-租金  4-户型")
            cond_choice = input("请输入条件类型编号（1-4）：")
            cond_type_map = {"1": "id", "2": "address", "3": "price", "4": "house_type"}
            if cond_choice not in cond_type_map:
                print("错误：无效的条件类型！")
                continue
            condition_type = cond_type_map[cond_choice]
            condition_value = input(f"请输入{condition_type}查询值：")
            # 执行查询
            result = query_house(condition_type, condition_value)
            # 展示结果
            if result:
                print("\n查询结果：")
                for house in result:
                    print(f"ID：{house['id']} | 地址：{house['address']} | 租金：{house['price']}元/月 | 面积：{house['area']}㎡ | 户型：{house['house_type']}")
            else:
                print("未找到符合条件的房源！")
        # 5. 退出系统
        elif choice == "5":
            print("感谢使用房屋出租系统，再见！")
            break
        # 无效输入
        else:
            print("错误：请输入1-5之间的有效编号！")

if __name__ == "__main__":
    main()
