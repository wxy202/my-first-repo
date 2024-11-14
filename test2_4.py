def solve_chicken_rabbit(heads, feet):
    # 检查脚数是否可能
    if feet % 2 != 0 or feet < heads * 2 or feet > heads * 4:
        return "Data Error"

        # 计算兔子的数量
    rabbits = (feet - heads * 2) / 2

    # 如果计算出的兔子数量不是整数，则无解
    if not rabbits.is_integer():
        return "Data Error"

        # 计算鸡的数量
    chickens = heads - int(rabbits)

    # 返回结果
    return f"鸡{chickens}只，兔子{int(rabbits)}只"


# 读取输入
input_str = input("请输入头数,脚数：")
try:
    heads, feet = map(int, input_str.split(','))
    result = solve_chicken_rabbit(heads, feet)
    print(result)
except ValueError:
    print("输入错误，请输入有效的数字。")