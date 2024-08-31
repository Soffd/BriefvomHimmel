label chapters_3:
    $ _dismiss_pause = True
    $ quick_menu = True
    scene hefengjiamendeng
    with moveintop
    play music "Tr4_PORTMERIA_LOOP.wav"
    show ryukab at center
    with dissolve
    ryuka "{b}想不到素山小姐的手艺可真是不错。{/b}"
    ryuka "{b}都有点吃撑了。{/b}"
    ryuka "{b}住在这里会不会胖十斤啊？{/b}"
    hisaki "{b}你倒是注意一点啊。{/b}"
    hisaki "{b}我们是客人，注意一下礼节问题。{/b}"
    ryuka "{b}但是真的好吃啊。{/b}"
    ryuka "{b}素山小姐的番茄料理是我的神！{/b}"
    ryuka "{b}下次一定要向她拜师学艺。{/b}"
    hisaki "{b}唉，你真是......{/b}"
    ryuka "{b}怎么了，这有什么问题吗？{/b}"
    hisaki "{b}没问题，非常合理。{/b}"
    ryuka "{b}那不就好了。{/b}"
    hide ryukab
    show ryukaa at center
    ryuka "{b}话说，若夜那孩子没来吃饭呢。{/b}"
    hisaki "{b}应该是看到我们也在，没来吧。{/b}"
    hisaki "{b}那孩子还是有点怕生的。{/b}"
    ryuka "{b}也对哦。{/b}"
    hisaki "{b}天色不早了，去睡觉吧。{/b}"
    ryuka "{b}这个点吗？有点早吧。{/b}"
    hisaki "{b}不早了，是该睡了。{/b}"
    ryuka "{b}好吧。{/b}"
    hide ryukaa
    with dissolve
    stop music
    scene hefenglangdeng
    with dissolve
    play music "ouxi_out.mp3"
    "{b}柳香的房间与我的房间在不同的地方。{/b}"
    "{b}我去我的房间需要路过这里。{/b}"
    wakayo "{b}可恶啊！{/b}"
    "{b}这个声音……{/b}"
    "{b}我循着声音轻声走过去。{/b}"
    "{b}这是若夜的房间吧。{/b}"
    menu:
        "默默在门口偷听":
            "{b}我静静地听着房里的动静。{/b}"
            "{b}随后我听到了“咣当”的一声，好像是有什么坚硬的东西掉在了地板上。{/b}"
            "{b}紧接着我听到一阵脚步声。{/b}"
            "{b}她要开门了，还是快点离开吧。{/b}"
        "当做没听到，回自己房间":
            "{b}这孩子在发脾气吗？{/b}"
            "{b}也许晚上没吃饭也是因为这个原因。{/b}"
            "{b}又或者是自己的到来惹到她了。{/b}"
            "{b}这些都要查啊。{/b}"
        "敲门，询问情况":
            "{b}咯咯。{/b}"
            "{b}我敲了敲门。{/b}"
            wakayo "{b}谁啊？{/b}"
            hisaki "{b}是我。你没事吧。{/b}"
            show wakayo1 at center
            with dissolve
            wakayo "{b}没事。{/b}"
            hisaki "{b}你这明显不是没事的样子。{/b}"
            wakayo "{b}这……{/b}"
            wakayo "{b}唉……{/b}"
            hide wakayo1
            show wakayo6 at center
            wakayo "{b}其实也没什么。{/b}"
            wakayo "{b}只是晚饭有番茄罢了。{/b}"
            hisaki "{b}就因为这个？{/b}"
            wakayo "{b}这可是非常重要的。{/b}"
            wakayo "{b}我讨厌番茄。{/b}"
            $ xiansuo_3 = 1
            hisaki "{b}哦，我懂。{/b}"
            hisaki "{b}挑食是吧。{/b}"
            wakayo "{b}这可不是挑食。{/b}"
            hisaki "{b}行行行，你说的都对。{/b}"
            hide wakayo6
            show wakayo1 at center
            stop music
            play music "tenshinoyume.mp3"
            wakayo "{b}我有一件事想问问你。{/b}"
            hisaki "{b}什么事？{/b}"
            wakayo "{b}人死之后，真的就不会有消息了吗？{/b}"
            hisaki "{b}你为什么突然这么问？{/b}"
            "{b}这孩子果然还是没有走出来吗？{/b}"
            hide wakayo1
            show wakayo2 at center
            wakayo "{b}我想妈妈了。{/b}"
            hisaki "{b}听我说。{/b}"
            hisaki "{b}人类活在这个世界上是必然要死的，区别就是早与晚。{/b}"
            hisaki "{b}但是呢，他们也在这个世界上留下了许多美好的事。{/b}"
            wakayo "{b}妈妈也是吗？{/b}"
            hisaki "{b}当然。{/b}"
            hisaki "{b}总有一天，你会找到的。{/b}"
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
    ryuka "{b}早。{/b}"
    hisaki "{b}早。{/b}"
    ryuka "{b}今天干什么？{/b}"
    hisaki "{b}今天先了解一下桐市先生的妻子，这是一个非常重要的突破口。{/b}"
    ryuka "{b}那左桃呢？{/b}"
    hisaki "{b}我一会打电话问问她。{/b}"
    ryuka "{b}别一会了，就现在吧，我也好奇。{/b}"
    hisaki "{b}好吧。{/b}"
    "{b}我拨通了左桃的电话。{/b}"
    $ _dismiss_pause = False
    hide ryukaa with fade
    stop music
    scene black with dissolve
    play music "kk_scene19_loop.ogg"
    show text "{b}{color=#ff0000}你好！我是左桃。{/b}{/color}"
    with Fade(1,0.0,1)
    with Pause(2)
    show text "{b}{color=#000dff}我是鸠山寿希。{/b}{/color}"
    with Fade(1,0.0,1)
    with Pause(2)
    show text "{b}{color=#ff0000}你打电话过来是有什么事吗？{/b}{/color}"
    with Fade(1,0.0,1)
    with Pause(2)
    show text "{b}{color=#000dff}之前这家是不是有派人过来？{/b}{/color}"
    with Fade(1,0.0,1)
    with Pause(2)
    show text "{b}{color=#ff0000}确实有，但是他们已经辞职了。{/b}{/color}"
    with Fade(1,0.0,1)
    with Pause(2)
    show text "{b}{color=#000dff}辞职？为什么？{/b}{/color}"
    with Fade(1,0.0,1)
    with Pause(2)
    show text "{b}{color=#ff0000}他们没说原因，只是简单的想辞职。{/b}{/color}"
    with Fade(1,0.0,1)
    with Pause(2)
    show text "{b}{color=#000dff}那他们有关于这家的其他信息吗？{/b}{/color}"
    with Fade(1,0.0,1)
    with Pause(2)
    show text "{b}{color=#ff0000}他们没说，如果你有需要，我一会给你发他们的联系方式，你自己去问。{/b}{/color}"
    with Fade(1,0.0,1)
    with Pause(2)
    $ _dismiss_pause = False
    stop music
    scene zhaoheshideng
    with irisin
    play music "Tr04LOOP_RabbitRhythm.wav"
    show ryukaa at center
    with dissolve
    "{b}通话结束了，一会儿我就收到了左桃发来的短信。{/b}"
    ryuka "{b}左桃怎么说的？{/b}"
    hisaki "{b}她说，那几个人辞职了，不干了。{/b}"
    hide ryukaa
    show ryukag
    ryuka "{b}唉。。。。。？{/b}"
    ryuka "{b}我们不会就是他们的接班人吧？{/b}"
    hisaki "{b}极有可能！{/b}"
    ryuka "{b}那他们为什么不干了？{/b}"
    hisaki "{b}原因不详。{/b}"
    hide ryukag
    show ryukab
    ryuka "{b}那这背后肯定有极大的故事！{/b}"
    "{b}她好像又开始莫名兴奋起来了。{/b}"
    hisaki "{b}一会再联系他们吧。{/b}"
    hisaki "{b}我们去问问素山小姐。{/b}"
    hide ryukab
    with dissolve
    stop music
    scene menkouri
    play music "kk_scene32_loop.ogg"
    show mina2:
        xcenter 0.5
        yalign 1.5
    with dissolve
    "{b}素山小姐正在工作。{/b}"
    show ryukah at left
    with moveinleft 
    ryuka "{b}打扰了，我们想问您一些东西。{/b}"
    mina "{b}我知道你们是想问有关若夜母亲的事吧。"
    hisaki "{b}是的是的。"
    mina "{b}若夜母亲名字叫凯瑟琳，是个外国人，若夜的白色头发就是随她母亲。"
    $ xiansuo_4 = 1
    mina "{b}只可惜她死的早，"
    mina "{b}不然若夜也不会这样了。"
    hisaki "{b}外国人？"
    hide ryukah
    show ryukaa at left
    ryuka "{b}还有关于她的信息了吗？"
    mina "{b}没了，不过我倒是知道几个若夜的同学。"
    mina "{b}就是若夜好久没去过学校了，我也不清楚还能不联系上。"
    ryuka "{b}她之前在哪个学校？"
    mina "{b}东市学院，C-1班级。"
    hisaki "{b}够了，谢谢。"
    mina "{b}嗯，希望对你们有帮助。"
    hide mina2 with moveoutright
    ryuka "{b}所以我们是要去东市学院吗？"
    hisaki "{b}嗯，就在下午吧，我们去问问情况。"
    hide ryukaa with dissolve
    stop music
    jump chapters_4