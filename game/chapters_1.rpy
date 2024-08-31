label chapters_1:
    play music "Tr6_CITRUS.wav"
    scene shatanbaitian
    with dissolve
    """
    {b}这是一个阳光明媚的周末，我也结束了一周的工作，来这里好好散步休息。{/b}

    {b}呼吸一下略带腥味的海风，享受一下悦耳的浪声。{/b}

    {b}舒坦！{/b}
    """
    "{b}来到这个城市这么久，还是头一次这么轻松惬意。{/b}"
    "{b}不因为别的，主要是因为我被解雇了。{/b}"
    "{b}那个傻缺老板在周末这么美好的时间通知我滚蛋。{/b}"
    "{b}好在那家伙有点人性，赔偿金没有少付，那我也没必要和他死磕。{/b}"
    "{b}趁着这个机会，好好去外面逛逛。{/b}"
    sakura "{b}鸠山前辈？{/b}"
    show sakurab at center
    with dissolve
    sakura "{b}真的是你啊。{/b}"
    hisaki "{b}你是？{/b}"
    "{b}眼前这个人有点眼熟，但又有点想不起来了。{/b}"
    sakura "{b}立山樱，那个是我。{/b}"
    hisaki "{b}哦，想起来了。{/b}"
    "{b}这个女孩曾经接受过我们公司的援助。{/b}"
    "{b}当时她是身患重病来着。{/b}"
    "{b}这么多年过去了，看样子她的身体恢复的不错。{/b}"
    sakura "{b}当时还没谢谢你，现在可以好好感谢一下，当时你的话对我很有帮助！{/b}"
    hisaki "{b}没什么，那都是我应该做的。{/b}"
    "{b}她说的是当时我胡编的心灵鸡汤吗？{/b}"
    "{b}那可太离谱了，\n自己还趁着没旁人狠狠倒了一波心灵垃圾。{/b}"
    "{b}那种连心灵鸡汤都不算的东西，这可真没必要感谢了。{/b}"
    hide sakurab
    show sakurac at center
    sakura "{b}特别是那句，“保持对生活的热爱，天使会赠与你爱的信件”。\n我到现在还记得！{/b}"
    hisaki "{b}那句啊......{/b}"
    "{b}那句纯属当时中二病犯了胡编的，拿来糊弄小孩子刚好。{/b}"
    "{b}也只有当时的自己才觉得振奋。{/b}"
    "{b}现在只觉得这句很粪。{/b}"
    hisaki "{b}其实那些记不记无所谓，对了，你现在身体怎么样了？{/b}"
    sakura "{b}恢复的还不错，现在单独出门没有问题了。{/b}"
    hisaki "{b}那就好。{/b}"
    "{b}现在还记得，当时她躺在病床上只能睁着眼睛，\n已经不能动弹，能恢复过来也算个奇迹。{/b}"
    "{b}快五年了吧。{/b}"
    "{b}想到这里我就有点恍惚感。{/b}"
    hide sakurac
    show sakurab at center
    sakura "{b}鸠山前辈？{/b}"
    sakura "{b}你是不是身体有点不舒服？{/b}"
    hisaki "{b}有吗？{/b}"
    $ _dismiss_pause = False
    scene black
    with Fade(2.5,0.0,2.5)
    $ _dismiss_pause = True
    stop music
    sakura "{b}鸠山前辈？{/b}"
    sakura "{b}能听到我说话吗？{/b}"
    "{b}......{/b}"
    play sound "<from 10 to 26>bibi.mp3"
    "{b}{color=#f00}病人生命体征已消失。{/b}{/color}"
    "{b}我......\n死了？{/b}"
    window hide
    $ _dismiss_pause = False
    $ quick_menu = False
    show text "{font=SourceHanSansLite.ttf}{size=+50}{color=#fff}Yuki Soffd制作。{/font}{/size}{/color}" 
    with Fade(1,0.0,1)
    with Pause(2)
    scene biaoti 
    with Fade(1,0.0,1)
    with Pause(2)
    $ _dismiss_pause = True
    $ quick_menu = True
    jump chapters_2

