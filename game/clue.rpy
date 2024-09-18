define clue_1 = Character("{b}线索一：淳谷若夜所说的“那帮人”，指的究竟是谁呢？\n{/b}")
define clue_2 = Character("{b}线索二：根据柳香的劲爆消息，三山代公司有见不得人的黑产，真实性有待商榷。\n{/b}")
define clue_3 = Character("{b}线索三：淳谷若夜讨厌番茄。\n{/b}")
define clue_4 = Character("{b}线索四：淳谷若夜的母亲凯瑟琳是个外国人。\n{/b}")
define clue_5 = Character("{b}线索五：淳谷若夜有一个带有密码的笔记本，密码未知。\n{/b}")
define xiansuo_1 = 0
define xiansuo_2 = 0
define xiansuo_3 = 0
define xiansuo_4 = 0
define xiansuo_5 = 0

screen clue():
    frame:
        xcenter 0.5
        ycenter 0.5
        xsize 1280
        ysize 720
        viewport:
            xinitial 0.0
            yinitial 0.0
            scrollbars "vertical"
            mousewheel True
            draggable True
            pagekeys True
            side_yfill True
            vbox:
                text "{color=#ff0000}{b}这里是游戏时收集的线索，请合理使用它们。（退出该界面重进可以刷新）{/color}{/b}\n\n\n"
                if xiansuo_1 == 1:
                    text "[clue_1]"
                if xiansuo_2 == 1:
                    text "[clue_2]"
                if xiansuo_3 == 1:
                    text "[clue_3]"
                if xiansuo_4 == 1:
                    text "[clue_4]"
                if xiansuo_5 == 1:
                    text "[clue_5]"
                textbutton _("退出") action Return("clue")
