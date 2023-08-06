from importlib.resources import files

import numpy as np
import pandas as pd

cookies = """
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN;q=0.8
Cache-Control: max-age=0
Connection: keep-alive
Cookie: cookiesession1=678B287ESTV0234567898901234AFCF1; SL_G_WPT_TO=zh; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1
Host: www.edu.cn
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Sec-GPC: 1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36
"""

votes = '''
#接龙
投票接龙
1. 房号+姓名+反对/赞成/弃权
2. 100 神仆  赞成
3. 184朱良 赞成
4. 118号 反对
5. 97号 弃权
6. 62号(不能退钱就赞成，可以退钱就算了，不想烦)
7. 174号 赞成
8. 86-海鱼 反对（1来历尴尬；2过于破旧，维修维护成本未知，建议及时止损。如果无法退款，已花的费用众筹算我一份）
9. 223 九凤 赞同
10. 126一郑桂华 赞同
11. 247   大卫林  赞同
12. 128号孙伟 弃权（照顾个别业主，可以放到不显眼处）
13. 禾亮188 赞同
14. 168茅 赞同
15. 229   亚梅   赞同
16. 109－21赞同
17. 233林 赞同 （为了照顾少数人位置重新协商）
18. 129号 赞同
19. 136号 赞成
20. Xing 31号 赞同 希望小区越来越好，支持所有正能量的行为！
21. 120号 赞成（位置为照顾个别人想法，可以协商）
22. 42号ringing 反对，和小区建筑风格不符
23. 245号 赞成
24. 83小宝 反对
25. 3号 反对
26. 242 赞成、英雄不问出处，正能压邪！
27. 瑞华1号 赞成
28. 108-301 赞同
29. 227赞成
30. 224严，赞同！墓区边的房子都买了，还怕这个！就算从风水讲，墓区的东西面还是好风水。原先比当今小区还要乱的时候，就有热心的业主捐了五六块镜子，放在转角处，改善小区道路行车安全，经过几届业委会和全体正常交物业管理费业主的共同努力，小区面貌已有较大的改善，愿意为小区建设奉献的行为理应得到鼓励和支持！
31. 青青翠竹 赞同
32. 青青翠竹 赞同88号   南赞同
33. 南88 赞同
34. 78-安妮 弃权（既然已经来了后续协商更新外观或者位置就行）
35. 139-常 赞同
36. 143徐  赞同
37. 157号 赞同
38. 19-rongying 反对，和小区风格不搭
39. 106- 赞同 喜欢马车 无论来自哪里都喜欢
40. 62号叶师傅 赞同
41. 241～赵永 弃权（出发点是好的，但随意性强，没有遵循小区基本的议事规则，没有事先征询大多数业主意见。）
42. 127-凌耀初 赞同！（由于马儿和马车锈烂严重，希望好好修补。另，来历也确实是有点尴尬，建议修复时颜色重新考虑）。通过这件事情如能形成小区的议事规则，如能形成网络投票的新机制，那将大大提高业主大会和业委会的决策效率，那是一件大好事！我们小区急需做的大事还有不少～
43. 108-402陈 弃权（不论结果怎么样，至少体现了办事透明度和业主参与度，是好事。）
44. 110-401可可 赞成（本来就是业委会牵头做的事情，也是为了改善小区环境，如果每样小事都需要全体业主投票，业主们就太累了）
45. 72号 赞同
46. 76号 赞同
47. 华爷140 弃权
48. 74号陆 赞同
49. 185-麻辣面 弃权
50. 202号王焱 赞成
51. 61-芊茉 赞同
52. 151田 赞同
53. 21-夏 赞同
54. 117 赞同
55. 9号 弃权  虽然参加了众筹，但是的确不知道还有那么多邻居没有进新群，不知道众筹这个事；虽然初心是为了美丽家园做出贡献，但的确不知道青博馆大门开在海湾园内；虽然放在海湾园里的东西肯定不会全是祭品（比如园区办公室的办公用品、摆设等等），但他的确是海湾园里出来的；虽然我不信邪，但的确有人会觉得这个晦气。
56. 115-402 赞同 心中为阳处处阳，心中为阴处处阴，心灵纯洁一点就不会有那么多的事情了
57. 静80 反对放在大门口，可以改个地方放吗？听说是海湾园里出来的的确会让人觉得晦气。
58. 艺嘉 赞同
59. 114-402 赞同
60. 219号戴  赞同。
61. 8-陈 赞同（既来之则安之）
62. 172杰 赞同（是饰品非祭品）
63. 148号艺嘉 赞成
64. 152CQ 赞成
65. 211号 赞成
66. 10-嘟嘟爸 赞成
67. 135 反对。这种材质注定了保养翻新不会只有一次，这一次大家众筹了那么下次呢？如果不翻新，那么一到小区门口就会感到这个小区的破败，如果翻新，那么钱从哪里出？因为不赞同，所以后续费用也不愿意承担。桃花岛上的亭子想要翻新我看大家都想选一劳永逸的材质，为什么在小区门口要放一个需要反复翻新的？
68. 178-冰姐 赞成，小区要做成一件事太难了
69. 217  赞同
70. 15洪虹 弃权
71. 55号 赞成
认知的差异性产生了多样性的思想碰撞现象，我思故我在
72. 105号301  赞成
73. 84-wang 弃权
'''


def create_name(name='姓名', rows=40):
    xm = [
        '赵钱孙李周吴郑王冯陈褚蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏窦章苏潘葛奚范彭郎鲁韦昌马苗方俞任袁柳',
        "群平风华正茂仁义礼智媛强天霸红和丽平世莉界中华正义伟岸茂盛繁圆一懿贵妃彭习嬴政韦近荣群智慧睿兴平风清扬自成世民嬴旺品网红丽文天学与翔斌霸学花文教学忠谋书"
    ]
    x = np.random.choice(list(xm[0]), (rows, 1))
    m = np.random.choice(list(xm[1]), (rows, 2))
    nm = np.hstack((x, m))
    df = pd.DataFrame(nm)
    df[2] = df[2].apply(lambda x: ('', x)[np.random.randint(0, 2)])
    dff = pd.DataFrame()
    dff[name] = df[0] + df[1] + df[2]

    return dff[name]


def create_columns(column_list, value_list, rows=40):
    size = (rows, len(column_list))
    if type(value_list[0]) == int and len(value_list) == 2:
        return pd.DataFrame(np.random.randint(*value_list, size=size), columns=column_list)
    else:
        return pd.DataFrame(np.random.choice(value_list, size=size), columns=column_list)


def generate_df(rows=40):
    return pd.concat([
        pd.DataFrame(data=range(220151000, 220151000 + rows), columns=['考号']),
        create_name('姓名', rows),
        create_columns(['性别'], ['男', '女'], rows),
        # create_columns(['邮编'], [171019, 200234], rows),
        create_columns(['学校'], ['清华大学', '北京大学', '复旦大学', '上海师大', '上海交大'], rows),
        create_columns(['班级'], ['计算机科学与技术', '人工智能', '数据科学'], rows),
        create_columns(['英语', '政治', '线代', '概率'], [20, 100], rows),
        create_columns(['高数', '专业课', '表达能力', '面试'], [30, 150], rows)],

        axis=1)


def generate_sr(v='英语', i='姓名', rows=40):
    dd = generate_df(rows)
    return pd.Series(data=dd[v].values.tolist(), index=dd[i], name="学生成绩")


def load(name):
    from importlib.resources import files

    data_file = files('pet.data').joinpath(f'{name}.xlsx')
    return pd.read_excel(data_file)


def load_data(file_name):
    data_file = files('pet.data').joinpath(f'{file_name}')

    if file_name.split('.')[-1] == 'xlsx':
        return pd.read_excel(data_file)

    elif file_name.split('.')[-1] == 'txt':
        return open(data_file, encoding="UTF-8").read()

    elif file_name.split('.')[-1] == 'csv':
        return pd.read_csv(data_file)

    else:
        return eval(file_name)


def download_textbook1():
    import os, shutil
    from importlib.resources import files
    dst = os.path.join(os.path.expanduser("~"), 'Desktop') + '\\Python与数据分析及可视化教学案例'
    src = files('pet.textbook1')
    print('Please wait....')
    shutil.copytree(src, dst, dirs_exist_ok=True)
    print('done!!')
    os.system(f"start explorer {dst}")


if __name__ == '__main__':
    # dd=generate_df(10)
    # dff=dd.set_index('姓名')
    # s=dff['英语']
    print(generate_df())

    # ss=pd.Series(data=dd['英语'].values.tolist(),index=dd['姓名'],name="学生成绩")
    # print(ss)

    print(generate_sr(rows=10))
    print(load_data('tyjhzz.txt'))
