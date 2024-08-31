# 定义全局变量
default mylist = [] # 用于存放输入的元素
default true_num = '' # 正确答案
default max_num = 0 # 最大输入数量

init -1 python:
    # 向列表中添加元素（用于显示列表元素）
    def show_list(list, myinput):
        # 如果列表中存在'错误'或'正确'，则清空列表
        if ('错误' or '正确') in list:
            list.clear()
        
        list.append(myinput)
        
        # 限制列表元素数量
        if len(list) > max_num:
            list.pop()
        else:
            pass

    # 撤回列表中的最后一个元素
    def remove_last_element(list):
        if list:
            list.pop()
        else:
            pass

    # 清空列表中的所有元素
    def list_clear(list):
        list.clear()

    # 判断列表中的元素（答案）是否正确
    def list_decide(list):
        # 使用join函数将列表转换为字符串方便比较
        mystr = ''.join(list)

        # 判断答案是否正确
        if mystr == true_num:
            list.clear()
            list.append('正确')
            # 可以使用return返回原先的label，但这里为了演示效果，没有使用return
        else:
            list.clear()
            list.append('错误')

screen lock_ceshi_15():

    # 使用meun保证能替换掉屏幕中的其他菜单
    tag menu

    # 使用join函数将列表转换为字符串
    $ mystr = ''.join(mylist)

    # 显示列表中的元素
    if mylist:
        button:
            background "#ffffff"
            xycenter (0.5, 0.2)
            hbox:
                for i in mylist:
                    text '{color=#000000}[i]'

    # 各类按键
    vbox:
        xycenter (0.5, 0.5)
        spacing 10
        if mylist != []:
            hbox:
                spacing 11
                button:
                    xysize (117, 75)
                    background "#9dc874"
                    hover_background "#c7eda4"
                    text '确定' xycenter (0.5,0.5)
                    # 调用函数list_decide，传入列表mylist作为参数
                    action Function(list_decide, list=mylist)
                button:
                    xysize (117, 75)
                    background "#c87474"
                    hover_background "#eda4a4"
                    text '清除' xycenter (0.5,0.5)
                    # 调用函数list_clear，传入列表mylist作为参数
                    action Function(list_clear, list=mylist)
        else:
            hbox:
                spacing 9
                button:
                    xysize (118, 75)
                    background "#00000000"
                button:
                    xysize (118, 75)
                    background "#00000000"
        
        # 多出10个像素高度的空白，用于美观
        null height 10

        hbox:
            spacing 10
            button:
                xysize (75, 75)
                background "#7491c8"
                hover_background "#abc1e9"
                text '1' xycenter (0.5,0.5)
                # 调用函数show_list，传入列表mylist和输入值作为参数
                action Function(show_list, list=mylist, myinput='1')
            button:
                xysize (75, 75)
                background "#7491c8"
                hover_background "#abc1e9"
                text '2' xycenter (0.5,0.5)
                action Function(show_list, list=mylist, myinput='2')
            button:
                xysize (75, 75)
                background "#7491c8"
                hover_background "#abc1e9"
                text '3' xycenter (0.5,0.5)
                action Function(show_list, list=mylist, myinput='3')
        
        hbox:
            spacing 10
            button:
                xysize (75, 75)
                background "#7491c8"
                hover_background "#abc1e9"
                text '4' xycenter (0.5,0.5)
                action Function(show_list, list=mylist, myinput='4')
            button:
                xysize (75, 75)
                background "#7491c8"
                hover_background "#abc1e9"
                text '5' xycenter (0.5,0.5)
                action Function(show_list, list=mylist, myinput='5')
            button:
                xysize (75, 75)
                background "#7491c8"
                hover_background "#abc1e9"
                text '6' xycenter (0.5,0.5)
                action Function(show_list, list=mylist, myinput='6')
        
        hbox:
            spacing 10
            button:
                xysize (75, 75)
                background "#7491c8"
                hover_background "#abc1e9"
                text '7' xycenter (0.5,0.5)
                action Function(show_list, list=mylist, myinput='7')
            button:
                xysize (75, 75)
                background "#7491c8"
                hover_background "#abc1e9"
                text '8' xycenter (0.5,0.5)
                action Function(show_list, list=mylist, myinput='8')
            button:
                xysize (75, 75)
                background "#7491c8"
                hover_background "#abc1e9"
                text '9' xycenter (0.5,0.5)
                action Function(show_list, list=mylist, myinput='9')

        hbox:
            spacing 10
            button:
                xysize (75, 75)
                background "#7491c8"
                hover_background "#abc1e9"
                text '回退' xycenter (0.5,0.5)
                # 调用函数remove_last_element，传入列表mylist作为参数
                action Function(remove_last_element, list=mylist)
            button:
                xysize (75, 75)
                background "#7491c8"
                hover_background "#abc1e9"
                text '0' xycenter (0.5,0.5)
                action Function(show_list, list=mylist, myinput='0')
            button:
                xysize (75, 75)
                background "#ff0505"
                hover_background "#ff9797"
                text '退出' xycenter (0.5,0.5)
                action Return()
        if '正确' in mylist:
            button:
                xysize (245, 75)
                background "#05ff16"
                hover_background "#a2fcb7"
                text '进入' xycenter (0.5,0.5)
                action Start("lock")


# 启动界面
label ceshi_15:
    $ true_num = '012345'
    $ max_num = 6
    call screen lock_ceshi_15