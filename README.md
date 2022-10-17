# SSMS
Data Analysis Course Project

# <center>实验:开发一个单机版销售管理系统

<center>姓名：张笑一


<center>学号：JL21010001


</center>

### 问题描述

* 背景描述。
  某公司有N名业务员（N<100，人员数量是变动的），销售M种产品（M<1000，数量变动），公司需要跟踪记录每名销售员的销售业绩和每种产品的销售情况。并能够通过销售分析菜单完成下列任务：搜索某个业务员的销售记录，搜索某种产品的销售记录，按销售额对销售员的业绩进行排名，按销售额对产品的业绩进行排名，等等。基于这些需求，需要一个单机版销售管理系统，由一个管理员运行和管理，对业务员、产品和销售记录等信息进行管理维护。

* 数据描述。
  系统需要处理的主要信息有：业务员（工号（唯一），姓名（不唯一），部门，级别，状态）， 产品（产品编码（唯一），产品名称，销售指导价，库存量），销售记录（订单号（唯一），销售日期，销售员工号，产品编码，销售价格，销售数量）。系统至少需要跟踪这些信息，为了程序处理的需要，可以增加额外的数据。

* 功能描述。
  系统至少需要具有下列功能：
  （1） 批量从文件（csv或xlsx格式）导入业务员、产品、销售记录数据；
  （2） 手工添加产品信息、修改已有产品的信息、更新产品库存、删除产品条目（或库存清零）；
  （3） 手工添加业务员信息、修改业务员信息、删除业务员信息（或离职）；
  （4） 手工添加销售记录、修改销售记录、删除销售记录；
  （5） 根据工号或姓名查询展示业务员信息；分页列表显示所有业务员信息；
  （6） 根据产品编码或产品名称（模糊）查询展示产品信息；分页列表显示所有产品信息；
  （7） 根据日期、业务员或产品组合查询销售记录及汇总数据；
  （8） 按照销售额对销售员的业绩进行排名（从高到低），按销售额对产品进行排名（从高到低）；
  （9） 从菜单选择退出系统时，自动保存所有的数据到备份文件（格式自选）；
  （10） 系统恢复功能，从备份文件中导入所有数据。

* 业务逻辑约束。
  在业务处理中，需要满足以下逻辑：
  （1）销售价格默认为指导价格，不能低于指导价格；
  （2）添加销售记录时，对应的业务员和产品必须存在，库存不为零，且业务员状态为在职；
  （3）删除产品时，若该产品的销售记录不为空，则只能将其库存清零，而不能删除该商品的基本信息；
  （4）删除业务员时，若该业务员的销售记录不为空，则只能将其状态设置为“离职”，而不能删除该业务员的基本信息；
  （5）增加一条销售记录时，销售量不能超过当前库存量，增加销售记录后，需要将库存量相应减少；
  （6）产品价格、销售量等数据不能为负数。
  若不满足以上逻辑，系统需要提示错误，并将错误信息写入日志（error.log)，格式和内容自定，但不能中断程序的执行。不满足的逻辑的修改和删除请求将被拒绝。


### 需求分析

（1）能完成产品基本信息的维护：即各实体的基本信息的增、删、改。

（2）能完成产品基本信息的查询。

（3）能完成业务员基本信息的维护：即各实体的基本信息的增、删、改。

（4）能完成业务员基本信息的查询。

（5）能完成销售记录基本信息的维护：即各实体的基本信息的增、删、改。

（6）能完成销售记录基本信息的查询。

（7）进行销售排名

~~~ mermaid
graph TB;
a(menu)-->a1("1 产品信息查询")
a(menu)-->a2("2 产品信息维护")
a(menu)-->a3("3 业务员信息查询")
a(menu)-->a4("4 业务员信息维护")
a(menu)-->a5("5 销售记录信息查询")
a(menu)-->a6("6 销售记录信息维护")
a(menu)-->a7("7 销售排名")
a(menu)-->a8("0 保存并退出程序")
~~~



### 概要设计

~~~ python
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
~~~



```mermaid
graph TB;
A(产品信息查询)-->a1("1 全部产品信息")
A(产品信息查询)-->a2("2 根据产品编码查询")
A(产品信息查询)-->a3("3 根据名称查询")
A(产品信息查询)-->a4("0 返回主菜单")
```

~~~ mermaid
graph TB;
B(产品信息维护)-->B1("1 产品入仓库")
B(产品信息维护)-->B2("2 产品售出")
B(产品信息维护)-->B3("3 批量导入产品信息")
B(产品信息维护)-->B4("4 手动添加产品信息")
B(产品信息维护)-->B5("5 删除产品信息")
B(产品信息维护)-->B6("6 修改产品信息")
B(产品信息维护)-->B7("0 返回主菜单")
~~~

~~~ mermaid
graph TB;
C("业务员信息查询")-->c1("1 全部业务员信息")
C("业务员信息查询")-->c2("2 根据工号查询")
C("业务员信息查询")-->c3("3 根据姓名查询")
C("业务员信息查询")-->c4("0 返回主菜单")
~~~

~~~ mermaid
graph TB;
D("业务员信息维护")-->d1("1 批量导入业务员信息")
D("业务员信息维护")-->d2("2 手工添加业务员信息")
D("业务员信息维护")-->d3("3 删除业务员信息")
D("业务员信息维护")-->d4("4 修改业务员信息")
D("业务员信息维护")-->d5("0 返回主菜单")
~~~

~~~ mermaid
graph TB;
E("销售记录信息查询")-->e2("1 全部销售记录信息")
E("销售记录信息查询")-->e3("2 组合查询")
E("销售记录信息查询")-->e5("0 返回主菜单")
~~~

~~~ mermaid
graph TB;
F("销售记录信息维护")-->f1("1 批量导入销售记录")
F("销售记录信息维护")-->f2("2 手工添加销售记录")
F("销售记录信息维护")-->f3("3 删除销售记录")
F("销售记录信息维护")-->f4("4 修改销售记录")
F("销售记录信息维护")-->f5("0 返回主菜单")
~~~

~~~ mermaid
graph TB;
~~~

~~~ mermaid
graph TB;
G("销售排名")-->g1("1 根据销售额对销售员的业绩进行排名")
G("销售排名")-->g2("2 根据销售额对产品进行排名")
G("销售排名")-->g3("0 返回主菜单")
~~~



###  详细设计

**data为文件:products.csv;records.csv;salemen.csv,根据提供的数据x，利用文件的索引index进行搜寻。**

~~~ python
def seek(data, x, index):
    for i in data:
        if x == i[index]:
            return i
    return []
~~~

**根据名称模糊查询**

~~~ python
def vague_seek(data, x, index):
    result = data[0].reshape(1, len(data[0]))
    for i in data:
        for j in x:
            if j not in i[index]:
                break
        else:
            result = np.append(result, i.reshape(1, len(i)), axis=0)
    return np.delete(result, 0, axis=0)
~~~

**组合查询的函数**

~~~ python
def com_seek(record_data, time, sale, prod):
    result = record_data[0].reshape(1, len(record_data[0]))
    for i in record_data:
        if i[1] == time and i[2] == sale and i[3] == prod:
            result = np.append(result, i.reshape(1, len(i)), axis=0)
    return np.delete(result, 0, axis=0)
~~~

**索引**

~~~ python
def index(data, x):
    for i in range(len(data)):
        if (data[i] == x).all():
            return i
    return -1
~~~

**展示产品、业务员、销售记录有关的信息**

~~~ python
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
~~~

主要类的结构设计

产品的属性：产品编码、产品名称、销售指导价、库存量

业务员的属性：工号、姓名、部门、级别、状态

销售记录的属性：订单号、销售日期、销售员工号、产品编码、销售价格、销售数量

**manage实现菜单的功能**

一.产品信息查询

1.输出全部产品信息

```python
if x == 1:
    for i in products:
        show_product(i)
```

2.根据产品编码查询

```python
elif x == 2:
    x = int(input("请输入要查询的产品编码："))
    i = seek(products, x, 0)
    if len(i) == 0:
        print("请输入正确的产品编码！")
    else:
        show_product(i)
```

3.根据名称查询

```python
                elif x == 3:
                    x = input("请输入要查询的产品名称：")
                    i = vague_seek(products, x, 1)
                    if len(i) != 0:
                        show_product(i)
                    else:
                        print("没有这个产品！")
```

二.产品信息维护

1.产品入仓库

```python
if x == 1:
    x = int(input("请输入要入库的产品的编码："))
    y = int(input("请输入入库数量："))
    if y <= 0:
        print("入库数量必须大于0")
        break
    i = seek(products, x, 0)
    if len(i) == 0:
        print("产品编码错误，入库失败！")
    else:
        i[3] += y
        print("入库成功！")
```

2.产品售出

```python
elif x == 2:
    x = int(input("请输入要售出的产品的编码："))
    y = int(input("请输入售出数量："))
    if y <= 0:
        print("出库数量必须大于0")
        break
    i = seek(products, x, 0)
    if len(i) == 0:
        print("产品编码错误，出库失败！")
    elif i[3] < y:
        print("产品数量不够，出库失败！")
    else:
        i[3] -= y
        print("出库成功！")
```

3.批量导入产品信息

```python
elif x == 3:
    x = input("请输入要导入的产品信息的文件地址（需为.csv文件，且第一行为产品属性名称，编码为utf-8）:")
    f = np.array(pd.read_csv(x, encoding="utf8"))
    for ff in f:
        if len(seek(products, ff[0], 0)) == 0:
            products = np.append(products, ff.reshape(1, len(ff)), axis=0)
        else:
            print("该产品编码已被占用，不导入！")
            continue
```

4.手动添加产品信息

```python
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
```

5.删除产品信息

```python
elif x == 5:
    x = int(input("请输入要删除的产品的编码："))
    i = seek(products, x, 0)
    if len(i) == 0:
        print("产品编码错误，删除失败！")
    elif len(seek(records, x, 0)) != 0:
        i[3] = 0
        print("产品销售记录不为空，清空库存！")
    else:
        products = np.delete(products, index(products, i), axis=0)
        print("删除成功！")
```

6.修改产品信息

~~~ python
                elif x == 6:
                    x = int(input("请输入要修改的产品的编码："))
                    i = seek(products, x, 0)
                    if len(i) == 0:
                        print("产品编码错误，修改失败！")
                    else:
                        i[1] = input("请输入修改后的产品的名称：")
                        i[2] = int(input("请输入修改后的产品的销售指导价："))
                        i[3] = int(input("请输入修改后的产品的库存数量："))
~~~

三、业务员信息查询

1.全部业务员信息

~~~ python
                if x == 1:
                    for i in salemen:
                        show_saleman(i)
~~~

2.根据工号查询

~~~ python
                elif x == 2:
                    x = int(input("请输入要查询的业务员的工号："))
                    i = seek(salemen, x, 0)
                    if len(i) == 0:
                        print("请输入正确的工号！")
                    else:
                        show_saleman(i)
~~~

3.根据姓名查询

~~~ python
                elif x == 3:
                    x = input("请输入要查询的业务员的姓名：")
                    i = vague_seek(salemen, x, 1)
                    if len(i) != 0:
                        show_saleman(i)
                    else:
                        print("没有这个姓名的业务员！")
~~~

四、业务员信息维护

1.批量导入业务员信息

~~~ python
                if x == 1:
                    x = input("请输入要导入的业务员信息的文件地址（需为.csv文件，且第一行为业务员属性名称，编码为utf-8）:")
                    f = np.array(pd.read_csv(x, encoding="utf8"))
                    for ff in f:
                        if len(seek(salemen, ff[0], 0)) == 0:
                            salemen = np.append(salemen, ff.reshape(1, len(ff)), axis=0)
                        else:
                            print("该销售员工号已被占用，不导入！")
                            continue
~~~

2.手工添加业务员信息

~~~ python
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
~~~

3.删除业务员的信息

~~~ python
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
~~~

4.修改业务员的信息

~~~ python
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
~~~

五、销售记录信息查询

1.全部销售记录信息

~~~ python
                if x == 1:
                    for i in records:
                        show_record(i)
~~~

2.根据组合查询

~~~ python
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
~~~

六、销售记录信息维护

1.批量导入销售记录

~~~ python
                if x == 1:
                    x = input("请输入要导入的销售记录的文件地址（需为.csv文件，且第一行为销售记录属性名称，编码为utf-8）:")
                    f = np.array(pd.read_csv(x, encoding="utf8"))
                    records = np.append(records, f, axis=0)
~~~

2.手工添加销售记录

~~~ python
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
~~~

3.删除销售记录

~~~ python
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
~~~

4.修改销售记录

~~~ python
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
~~~

七、销售排名

1.根据销售额对销售员的业绩进行排名

~~~ python
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
~~~

2.根据销售额对产品进行排名

~~~ python
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
~~~

八、保存并退出程序

~~~  python
        elif x == 0:
            products = np.insert(products, 0, np.array([["产品编码", "产品名称", "销售指导价", "库存量"]]), axis=0)
            pd.DataFrame(products).to_csv("product.csv", header=0, index=0)
            salemen = np.insert(salemen, 0, np.array([["工号", "姓名", "部门", "级别", "状态"]]), axis=0)
            pd.DataFrame(salemen).to_csv("salemen.csv", header=0, index=0)
            records = np.insert(records, 0, np.array([["订单号", "销售日期", "销售员工", "产品编码", "销售价格", "销售数量"]]), axis=0)
            pd.DataFrame(records).to_csv("records.csv", header=0, index=0)
            break
~~~

###  调试分析及其测试结果

调试成功


