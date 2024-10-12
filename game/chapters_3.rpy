label chapters_3:
    $ _dismiss_pause = True
    $ quick_menu = True
    scene hefengjiamendeng
    with moveintop
    play music "Tr4_PORTMERIA_LOOP.wav"
    show ryukab at center
    with dissolve
    ryuka "想不到素山小姐的手艺可真是不错。"
    ryuka "都有点吃撑了。"
    ryuka "住在这里会不会胖十斤啊？"
    hisaki "你倒是注意一点啊。"
    hisaki "我们是客人，注意一下礼节问题。"
    ryuka "但是真的好吃啊。"
    ryuka "素山小姐的番茄料理是我的神！"
    ryuka "下次一定要向她拜师学艺。"
    hisaki "唉，你真是......"
    ryuka "怎么了，这有什么问题吗？"
    hisaki "没问题，非常合理。"
    ryuka "那不就好了。"
    hide ryukab
    show ryukaa at center
    ryuka "话说，若夜那孩子没来吃饭呢。"
    hisaki "应该是看到我们也在，没来吧。"
    hisaki "那孩子还是有点怕生的。"
    ryuka "也对哦。"
    hisaki "天色不早了，去睡觉吧。"
    ryuka "这个点吗？有点早吧。"
    hisaki "不早了，是该睡了。"
    ryuka "好吧。"
    hide ryukaa
    with dissolve
    stop music
    scene hefenglangdeng
    with dissolve
    play music "ouxi_out.mp3"
    "柳香的房间与我的房间在不同的地方。"
    "我去我的房间需要路过这里。"
    wakayo "可恶啊！"
    "这个声音……"
    "我循着声音轻声走过去。"
    "这是若夜的房间吧。"
    menu:
        "默默在门口偷听":
            "我静静地听着房里的动静。"
            "随后我听到了“咣当”的一声，好像是有什么坚硬的东西掉在了地板上。"
            "紧接着我听到一阵脚步声。"
            "她要开门了，还是快点离开吧。"
        "当做没听到，回自己房间":
            "这孩子在发脾气吗？"
            "也许晚上没吃饭也是因为这个原因。"
            "又或者是自己的到来惹到她了。"
            "这些都要查啊。"
        "敲门，询问情况":
            "咯咯。"
            "我敲了敲门。"
            wakayo "谁啊？"
            hisaki "是我。你没事吧。"
            show wakayo1 at center
            with dissolve
            wakayo "没事。"
            hisaki "你这明显不是没事的样子。"
            wakayo "这……"
            wakayo "唉……"
            hide wakayo1
            show wakayo6 at center
            wakayo "其实也没什么。"
            wakayo "只是晚饭有番茄罢了。"
            hisaki "就因为这个？"
            wakayo "这可是非常重要的。"
            wakayo "我讨厌番茄。"
            $ xiansuo_3 = 1
            hisaki "哦，我懂。"
            hisaki "挑食是吧。"
            wakayo "这可不是挑食。"
            hisaki "行行行，你说的都对。"
            hide wakayo6
            show wakayo1 at center
            stop music
            play music "tenshinoyume.mp3"
            wakayo "我有一件事想问问你。"
            hisaki "什么事？"
            wakayo "人死之后，真的就不会有消息了吗？"
            hisaki "你为什么突然这么问？"
            "这孩子果然还是没有走出来吗？"
            hide wakayo1
            show wakayo2 at center
            wakayo "我想妈妈了。"
            hisaki "听我说。"
            hisaki "人类活在这个世界上是必然要死的，区别就是早与晚。"
            hisaki "但是呢，他们也在这个世界上留下了许多美好的事。"
            wakayo "妈妈也是吗？"
            hisaki "当然。"
            hisaki "总有一天，你会找到的。"
            hide wakayo2
            with dissolve
            stop music
            scene black
            with Fade(1.5,0.0,1.5)
    $ renpy.fix_rollback()
    scene zhaoheshideng
    with irisin
    play music "Tr07LOOP_WingsofEternity.wav"
    show ryukaa at center
    with dissolve
    ryuka "早。"
    hisaki "早。"
    ryuka "今天干什么？"
    hisaki "今天先了解一下桐市先生的妻子，这是一个非常重要的突破口。"
    ryuka "那左桃呢？"
    hisaki "我一会打电话问问她。"
    ryuka "别一会了，就现在吧，我也好奇。"
    hisaki "好吧。"
    "我拨通了左桃的电话。"
    $ _dismiss_pause = False
    hide ryukaa with fade
    stop music
    scene black with dissolve
    play music "kk_scene19_loop.ogg"
    show text "{color=#ff0000}你好！我是左桃。{/color}"
    with Fade(1,0.0,1)
    with Pause(2)
    show text "{color=#000dff}我是鸠山寿希。{/color}"
    with Fade(1,0.0,1)
    with Pause(2)
    show text "{color=#ff0000}你打电话过来是有什么事吗？{/color}"
    with Fade(1,0.0,1)
    with Pause(2)
    show text "{color=#000dff}之前这家是不是有派人过来？{/color}"
    with Fade(1,0.0,1)
    with Pause(2)
    show text "{color=#ff0000}确实有，但是他们已经辞职了。{/color}"
    with Fade(1,0.0,1)
    with Pause(2)
    show text "{color=#000dff}辞职？为什么？{/color}"
    with Fade(1,0.0,1)
    with Pause(2)
    show text "{color=#ff0000}他们没说原因，只是简单的想辞职。{/color}"
    with Fade(1,0.0,1)
    with Pause(2)
    show text "{color=#000dff}那他们有关于这家的其他信息吗？{/color}"
    with Fade(1,0.0,1)
    with Pause(2)
    show text "{color=#ff0000}他们没说，如果你有需要，我一会给你发他们的联系方式，你自己去问。{/color}"
    with Fade(1,0.0,1)
    with Pause(2)
    $ _dismiss_pause = False
    stop music
    scene zhaoheshideng
    with irisin
    play music "Tr04LOOP_RabbitRhythm.wav"
    show ryukaa at center
    with dissolve
    "通话结束了，一会儿我就收到了左桃发来的短信。"
    ryuka "左桃怎么说的？"
    hisaki "她说，那几个人辞职了，不干了。"
    hide ryukaa
    show ryukag
    ryuka "唉。。。。。？"
    ryuka "我们不会就是他们的接班人吧？"
    hisaki "极有可能！"
    ryuka "那他们为什么不干了？"
    hisaki "原因不详。"
    hide ryukag
    show ryukab
    ryuka "那这背后肯定有极大的故事！"
    "她好像又开始莫名兴奋起来了。"
    hisaki "一会再联系他们吧。"
    hisaki "我们去问问素山小姐。"
    hide ryukab
    with dissolve
    stop music
    scene menkouri
    play music "kk_scene32_loop.ogg"
    show mina2:
        xcenter 0.5
        yalign 1.5
    with dissolve
    "素山小姐正在工作。"
    show ryukah at left
    with moveinleft 
    ryuka "打扰了，我们想问您一些东西。"
    mina "我知道你们是想问有关若夜母亲的事吧。"
    hisaki "是的是的。"
    mina "若夜母亲名字叫凯瑟琳，是个外国人，若夜的白色头发就是随她母亲。"
    $ xiansuo_4 = 1
    mina "只可惜她死的早，"
    mina "不然若夜也不会这样了。"
    hisaki "外国人？"
    hide ryukah
    show ryukaa at left
    ryuka "还有关于她的信息了吗？"
    mina "没了，不过我倒是知道几个若夜的同学。"
    mina "就是若夜好久没去过学校了，我也不清楚还能不联系上。"
    ryuka "她之前在哪个学校？"
    mina "东市学院，C-1班级。"
    hisaki "够了，谢谢。"
    mina "嗯，希望对你们有帮助。"
    hide mina2 with moveoutright
    ryuka "所以我们是要去东市学院吗？"
    hisaki "嗯，就在下午吧，我们去问问情况。"
    hide ryukaa with dissolve
    stop music
    jump chapters_4