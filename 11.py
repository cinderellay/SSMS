'''
import json
import requests
import jsonpath
from jsonpath import jsonpath
'''
import pandas as pd
import numpy as np


def menu():
    print("\n===M E N U===")
    print("1 产品信息查询")
    print("2 产品信息维护")
    print("3 业务员信息查询")
    print("4 业务员信息维护")
    print("5 销售记录信息查询")
    print("6 销售记录信息维护")
    print("7 销售排名")
    print("0 保存并退出程序")
    print("=============")
def menu1():
    print("\n----menu1----")
    print("1 全部产品信息")
    print("2 根据产品编码查询")
    print("3 根据名称查询")
    print("0 返回主菜单")
    print("------------")
def menu2():
    print("\n----menu2----")
    print("1 产品入仓库")
    print("2 产品售出")
    print("3 批量导入产品信息")
    print("4 手动添加产品信息")
    print("5 删除产品信息")
    print("6 修改产品信息")
    print("0 返回主菜单")
    print("------------")
def menu3():
    print("\n----menu3----")
    print("1 全部业务员信息")
    print("2 根据工号查询")
    print("3 根据姓名查询")
    print("0 返回主菜单")
    print("------------")
def menu4():
    print("\n----menu4----")
    print("1 批量导入业务员信息")
    print("2 手工添加业务员信息")
    print("3 删除业务员信息")
    print("4 修改业务员信息")
    print("0 返回主菜单")
    print("------------")
def menu5():
    print("\n----menu5----")
    print("1 全部销售记录信息")
    print("2 组合查询")
    print("0 返回主菜单")
    print("------------")
def menu6():
    print("\n----menu6----")
    print("1 批量导入销售记录")
    print("2 手工添加销售记录")
    print("3 删除销售记录")
    print("4 修改销售记录")
    print("0 返回主菜单")
    print("------------")
def menu7():
    print("\n----menu7----")
    print("1 根据销售额对销售员的业绩进行排名")
    print("2 根据销售额对产品进行排名")
    print("0 返回主菜单")
    print("------------")
def seek(data, x, index):
    for i in data:
        if x == i[index]:
            return i
    return []
def vague_seek(data, x, index):
    result = data[0].reshape(1, len(data[0]))
    for i in data:
        for j in x:
            if j not in i[index]:
                break
        else:
            result = np.append(result, i.reshape(1, len(i)), axis=0)
    return np.delete(result, 0, axis=0)
def com_seek(record_data, time, sale, prod):
    result = record_data[0].reshape(1, len(record_data[0]))
    for i in record_data:
        if i[1] == time and i[2] == sale and i[3] == prod:
            result = np.append(result, i.reshape(1, len(i)), axis=0)
    return np.delete(result, 0, axis=0)
def index(data, x):
    for i in range(len(data)):
        if (data[i] == x).all():
            return i
    return -1
def show_product(x):
    if len(x.shape) == 1:
        print("产品编码：%s\t产品名称：%s\t销售指导价：%s\t库存量：%s\t\n" % (x[0], x[1], x[2], x[3]), end='')
    else:
        for xx in x:
            print("产品编码：%s\t产品名称：%s\t销售指导价：%s\t库存量：%s\t\n" % (xx[0], xx[1], xx[2], xx[3]), end='')
def show_saleman(x):
    if len(x.shape) == 1:
        print("工号：%s\t姓名：%s\t部门:%s\t级别：%s\t状态：%s\t\n" % (x[0], x[1], x[2], x[3], x[4]), end='')
    else:
        for xx in x:
            print("工号：%s\t姓名：%s\t部门:%s\t级别：%s\t状态：%s\t\n" % (xx[0], xx[1], xx[2], xx[3], xx[4]), end='')
def show_record(x):
    if len(x.shape) == 1:
        print("订单号：%s\t销售日期：%s\t销售员工号:%s\t产品编码：%s\t销售价格：%s\t销售数量：%s\t\n" % (x[0], x[1], x[2], x[3], x[4], x[5]), end='')
    else:
        for xx in x:
            print("订单号：%s\t销售日期：%s\t销售员工号:%s\t产品编码：%s\t销售价格：%s\t销售数量：%s\t\n" % (xx[0], xx[1], xx[2], xx[3], xx[4], xx[5]), end='')
def manage(pd=None):
    products = pd.read_csv("product.csv")
    products = np.array(products)
    salemen = pd.read_csv("salemen.csv")
    salemen = np.array(salemen)
    records = pd.read_csv("records.csv")
    records = np.array(records)
    while 1:
        menu()
        x = int(input("请输入序号选择操作："))
        # 产品信息查询
        if x == 1:
            while 1:
                menu1()
                x = int(input("请输入序号选择操作："))
                # 输出全部产品信息
                if x == 1:
                    for i in products:
                        show_product(i)
                # 根据产品编码查询
                elif x == 2:
                    x = int(input("请输入要查询的产品编码："))
                    i = seek(products, x, 0)
                    if len(i) == 0:
                        print("请输入正确的产品编码！")
                    else:
                        show_product(i)
                # 根据名称查询
                elif x == 3:
                    x = input("请输入要查询的产品名称：")
                    i = vague_seek(products, x, 1)
                    if len(i) != 0:
                        show_product(i)
                    else:
                        print("没有这个产品！")
                elif x == 0:
                    break
                else:
                    print("请输入正确的序号！\n")
        # 产品信息维护
        elif x == 2:
            while 1:
                menu2()
                x = int(input("请输入序号选择操作："))
                # 产品入仓库
                if x == 1:
                    x = int(input("请输入要入库的产品的编码："))
                    y = int(input("请输入入库数量："))
                    if y <= 0:
                        print("入库数量必须大于0")
                        continue
                    i = seek(products, x, 0)
                    if len(i) == 0:
                        print("产品编码错误，入库失败！")
                    else:
                        i[3] += y
                        print("入库成功！")
                # 产品售出
                elif x == 2:
                    x = int(input("请输入要售出的产品的编码："))
                    y = int(input("请输入售出数量："))
                    if y <= 0:
                        print("出库数量必须大于0")
                        continue
                    i = seek(products, x, 0)
                    if len(i) == 0:
                        print("产品编码错误，出库失败！")
                    elif i[3] < y:
                        print("产品数量不够，出库失败！")
                    else:
                        i[3] -= y
                        print("出库成功！")
                # 批量导入产品信息
                elif x == 3:
                    x = input("请输入要导入的产品信息的文件地址（需为.csv文件，且第一行为产品属性名称，编码为utf-8）:")
                    f = np.array(pd.read_csv(x, encoding="utf8"))
                    for ff in f:
                        if len(seek(products, ff[0], 0)) == 0:
                            products = np.append(products, ff.reshape(1, len(ff)), axis=0)
                        else:
                            print("该产品编码已被占用，不导入！")
                            continue
                # 手动添加产品信息
                elif x == 4:
                    x = int(input("请输入要添加的产品的编码："))
                    if len(seek(products, x, 0)) != 0:
                        print("已存在该产品信息！")
                    else:
                        product = np.array(x, dtype=object)
                        product = np.append(product, input("请输入要添加的产品的名称："))
                        product = np.append(product, int(input("请输入要添加的产品的销售指导价：")))
                        product = np.append(product, int(input("请输入要添加的产品的数量：")))
                        products = np.append(products, product.reshape(1, len(product)), axis=0)
                        print("添加成功！")
                # 删除产品信息
                elif x == 5:
                    x = int(input("请输入要删除的产品的编码："))
                    i = seek(products, x, 0)
                    if len(i) == 0:
                        print("产品编码错误，删除失败！")
                    elif len(seek(records, x, 3)) != 0:
                        i[3] = 0
                        print("产品销售记录不为空，清空库存！")
                    else:
                        products = np.delete(products, index(products, i), axis=0)
                        print("删除成功！")
                # 修改产品信息
                elif x == 6:
                    x = int(input("请输入要修改的产品的编码："))
                    i = seek(products, x, 0)
                    if len(i) == 0:
                        print("产品编码错误，修改失败！")
                    else:
                        i[1] = input("请输入修改后的产品的名称：")
                        i[2] = int(input("请输入修改后的产品的销售指导价："))
                        i[3] = int(input("请输入修改后的产品的库存数量："))
                elif x == 0:
                    break
                else:
                    print("请输入正确的序号！\n")
        # 业务员信息查询
        elif x == 3:
            while 1:
                menu3()
                x = int(input("请输入序号选择操作："))
                # 全部业务员信息
                if x == 1:
                    for i in salemen:
                        show_saleman(i)
                # 根据工号查询
                elif x == 2:
                    x = int(input("请输入要查询的业务员的工号："))
                    i = seek(salemen, x, 0)
                    if len(i) == 0:
                        print("请输入正确的工号！")
                    else:
                        show_saleman(i)
                # 根据姓名查询
                elif x == 3:
                    x = input("请输入要查询的业务员的姓名：")
                    i = vague_seek(salemen, x, 1)
                    if len(i) != 0:
                        show_saleman(i)
                    else:
                        print("没有这个姓名的业务员！")
                elif x == 0:
                    break
                else:
                    print("请输入正确的序号！\n")
        # 业务员信息维护
        elif x == 4:
            while 1:
                menu4()
                x = int(input("请输入序号选择操作："))
                # 批量导入业务员信息
                if x == 1:
                    x = input("请输入要导入的业务员信息的文件地址（需为.csv文件，且第一行为业务员属性名称，编码为utf-8）:")
                    f = np.array(pd.read_csv(x, encoding="utf8"))
                    for ff in f:
                        if len(seek(salemen, ff[0], 0)) == 0:
                            salemen = np.append(salemen, ff.reshape(1, len(ff)), axis=0)
                        else:
                            print("该销售员工号已被占用，不导入！")
                            continue
                # 手工添加业务员信息
                elif x == 2:
                    x = int(input("请输入要添加的业务员的工号："))
                    if len(seek(salemen, x, 0)) != 0:
                        print("已存在该业务员信息！")
                    else:
                        man = np.array(x, dtype=object)
                        man = np.append(man, input("请输入要添加的业务员的姓名："))
                        man = np.append(man, int(input("请输入要添加的业务员所在部门：")))
                        man = np.append(man, int(input("请输入要添加的业务员级别：")))
                        man = np.append(man, input("请输入要添加的业务员状态："))
                        salemen = np.append(salemen, man.reshape(1, len(man)), axis=0)
                        print("添加成功！")
                # 删除业务员信息
                elif x == 3:
                    x = int(input("请输入要删除的业务员的工号："))
                    i = seek(salemen, x, 0)
                    if len(i) == 0:
                        print("业务员工号错误，删除失败！")
                    elif len(seek(records, x, 2)) != 0:
                        i[4] = "离职"
                        print("业务员有销售记录，将其设置为离职！")
                    else:
                        salemen = np.delete(salemen, index(salemen, i), axis=0)
                        print("删除成功！")
                # 修改业务员信息
                elif x == 4:
                    x = int(input("请输入要修改的业务员的工号："))
                    i = seek(salemen, x, 0)
                    if len(i) == 0:
                        print("业务员工号错误，修改失败！")
                    else:
                        i[1] = input("请输入修改后的业务员的姓名：")
                        i[2] = int(input("请输入修改后的业务员的部门："))
                        i[3] = int(input("请输入修改后的业务员的级别："))
                        i[4] = input("请输入修改后的业务员的状态：")
                elif x == 0:
                    break
                else:
                    print("请输入正确的序号！\n")
        # 销售记录信息查询
        elif x == 5:
            while 1:
                menu5()
                x = int(input("请输入序号选择操作："))
                # 全部销售记录信息
                if x == 1:
                    for i in records:
                        show_record(i)
                # 根据组合查询
                elif x == 2:
                    com_data = input("请输入组合(空格分隔)：")
                    c_data = com_data.split()
                    x = c_data[0]
                    y = int(c_data[1])
                    z = int(c_data[2])
                    i = com_seek(records, x, y, z)
                    if len(i) != 0:
                        show_record(i)
                    else:
                        print("没有这个日期的销售记录或没有这个业务员的销售记录！")
                elif x == 0:
                    break
                else:
                    print("请输入正确的序号！\n")
        # 销售记录信息维护
        elif x == 6:
            while 1:
                menu6()
                x = int(input("请输入序号选择操作："))
                # 批量导入销售记录
                if x == 1:
                    x = input("请输入要导入的销售记录的文件地址（需为.csv文件，且第一行为销售记录属性名称，编码为utf-8）:")
                    f = np.array(pd.read_csv(x, encoding="utf8"))
                    records = np.append(records, f, axis=0)
                # 手工添加销售记录
                elif x == 2:
                    x = int(input("请输入要添加的销售记录的订单号："))
                    if len(seek(records, x, 0)) != 0:
                        print("已存在该销售记录！")
                    else:
                        record = np.array(x, dtype=object)
                        record = np.append(record, input("请输入要添加的销售日期："))
                        temp = int(input("请输入要添加的销售员工号："))
                        i = seek(salemen, temp, 0)
                        if len(i) == 0:
                            print("没有找到该销售员！")
                            continue
                        elif i[4] == "离职":
                            print("该销售员离职了！")
                            continue
                        else:
                            record = np.append(record, temp)
                        temp = int(input("请输入要添加的产品编码："))
                        temp_product = seek(products, temp, 0)
                        if len(temp_product) != 0:
                            record = np.append(record, temp)
                        else:
                            print("没有找到该产品！")
                            continue
                        temp = int(input("请输入要添加的销售价格："))
                        if temp >= temp_product[2]:
                            record = np.append(record, temp)
                        else:
                            print("销售价格不能低于指导价格！")
                            continue
                        temp = int(input("请输入要添加的销售数量："))
                        if temp <= temp_product[3]:
                            temp_product[3] -= temp
                            record = np.append(record, temp)
                        else:
                            print("销售数量不能大于产品库存量！")
                            continue
                        records = np.append(records, record.reshape(1, len(record)), axis=0)
                        print("添加成功！")
                # 删除销售记录
                elif x == 3:
                    x = int(input("请输入要删除的销售记录的订单号："))
                    i = seek(records, x, 0)
                    if len(i) == 0:
                        print("订单号错误，删除失败！")
                    else:
                        records = np.delete(records, index(records, i), axis=0)
                        j = seek(products, i[3], 0)
                        j[3] += i[5]
                        print("删除成功！")
                # 修改销售记录
                elif x == 4:
                    x = int(input("请输入要修改的销售记录的订单号："))
                    i = seek(records, x, 0)
                    if len(i) == 0:
                        print("订单号错误，修改失败！")
                    else:
                        i[1] = input("请输入修改后的销售日期：")
                        i[2] = int(input("请输入修改后的销售员工号："))
                        i[3] = int(input("请输入修改后的产品编码："))
                        i[4] = int(input("请输入修改后销售价格："))
                        i[5] = int(input("请输入修改后的销售数量："))
                elif x == 0:
                    break
                else:
                    print("请输入正确的序号！\n")
        # 销售排名
        elif x == 7:
            while 1:
                menu7()
                x = int(input("请输入序号选择操作："))
                # 根据销售额对销售员的业绩进行排名
                if x == 1:
                    order_man = np.array([["销售员工号", "销售额"]], dtype=object)
                    for man in salemen:
                        sales_volume = 0
                        for i in records:
                            if man[0] == i[2]:
                                sales_volume += i[4]*i[5]
                        order_man = np.append(order_man, [[man[0], sales_volume]], axis=0)
                    order_man = np.delete(order_man, 0, axis=0)
                    order_man = order_man[np.argsort(-order_man[:, 1])]
                    print(order_man)
                # 根据销售额对产品进行排名
                if x == 2:
                    order_product = np.array([["产品编号", "销售额"]], dtype=object)
                    for pro in products:
                        sales_volume = 0
                        for i in records:
                            if pro[0] == i[3]:
                                sales_volume += i[4] * i[5]
                        order_product = np.append(order_product, [[pro[0], sales_volume]], axis=0)
                    order_product = np.delete(order_product, 0, axis=0)
                    order_product = order_product[np.argsort(-order_product[:, 1])]
                    print(order_product)
                if x == 0:
                    break
        # 保存并退出程序
        elif x == 0:
            products = np.insert(products, 0, np.array([["产品编码", "产品名称", "销售指导价", "库存量"]]), axis=0)
            pd.DataFrame(products).to_csv("product.csv", header=0, index=0)
            salemen = np.insert(salemen, 0, np.array([["工号", "姓名", "部门", "级别", "状态"]]), axis=0)
            pd.DataFrame(salemen).to_csv("salemen.csv", header=0, index=0)
            records = np.insert(records, 0, np.array([["订单号", "销售日期", "销售员工", "产品编码", "销售价格", "销售数量"]]), axis=0)
            pd.DataFrame(records).to_csv("records.csv", header=0, index=0)
            break
        else:
            print("请输入正确的序号！\n")
manage(pd)

