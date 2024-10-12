label chapters_4:
    scene xiaoluri
    with dissolve
    play music "Tr07LOOP_WingsofEternity.wav"
    "我们又来到这条路。"
    mosheng "两位请等一下。"
    show kazumi2
    with dissolve
    "出现在我们眼前的是一位陌生的少女。"
    kazumi "我叫九楽佳澄，叫我佳澄就好，也是若夜的朋友。"
    show ryukab at left
    with moveinleft
    ryuka "你好。"
    hisaki "你好。"
    kazumi "你们是在打听若夜的消息？"
    hide ryukab
    show ryukag at left
    ryuka "是，不对，你是怎么知道的？"
    kazumi "昨天晚上她跟我发信息了"
    if xiansuo_3 == 1:
        kazumi "她昨天晚上又找我发泄情绪。"
        kazumi "不过跟以往比起来稳定不少。"
        kazumi "感觉看开了好多，也不知道算不算好事。"
    else:
        kazumi "她昨天晚上又找我发泄情绪。"
        kazumi "还是一如既往的难哄。"
        kazumi "开导了快一个小时，她才肯睡觉。"
    kazumi "不知道你们到底起没起用处。"
    "说的挺欠揍，但是合理，他们到底有没有用？现在还是未知数。"
    "又或者，真的没有一点用。"
    "所谓的病情好转，都是演戏罢了。"
    "想到这里，冷汗直冒。"
    "他有预感，这件事会极其复杂。"
    kazumi "不好意思，跑题了。"
    hide kazumi2
    show kazumi3
    kazumi "我知道你们在打听她的信息，我也会帮忙。只不过别把我供出来就行。"
    hisaki "供出来？为什么？"
    show angry11
    kazumi "啊呀，你问的太多了。"
    "我识趣的闭上嘴。"
    "她没说，但是好像又什么都说了。"
    hide kazumi3
    show kazumi6
    hide angry11
    stop music
    play music "Tr1_Find Out (Music Box Ver.).wav"
    kazumi "该说正事了。"
    kazumi "我应该从哪讲起呢......"
    kazumi "我想着从她性格刚开始变化的时候开始。"
    hide ryukag
    hide kazumi6
    scene black
    with dissolve
    kazumi "应该是一年多之前。"
    kazumi "淳谷若夜第一次来到这个城市。"
    kazumi "那时候的她一切正常。"
    stop music
    play music "Tr04LOOP_RabbitRhythm.wav"
    hisaki "可以说重点吗？"
    kazumi "哎呀，别打岔。"
    hisaki "我的意思是，你可以正常点。你这样会让我觉得你是在讲故事。"
    kazumi "哦，你在质疑我？"
    scene xiaoluri
    with dissolve
    show kazumi2 with dissolve
    kazumi "真实性我可以保证。"
    kazumi "你也没有别的好方法了吧？"
    "她说的没错。"
    "我不能放弃任何一个线索。"
    hisaki "好吧，你说。"
    kazumi "重点是，一切的改变都从若夜的妈妈离世开始。"
    hisaki "这我也知道。"
    kazumi "你怎么什么都知道？那我还说什么？"
    hisaki "说重点。"
    kazumi "重点我已经说过了，再说就不合适了。"
    ryuka "就要不合适的。"
    hisaki "有多不合适？"
    hide kazumi2
    show kazumi4
    kazumi "被若夜知道会被她捅死的......"
    hisaki "没事，我们也不会说出去的。"
    ryuka "嗯嗯。"
    kazumi "真的？"
    hisaki "真的。"
    kazumi "那我就说了。"
    hide kazumi4
    show kazumi1
    hisaki "说吧。"
    "总觉得是攻守之势异也。"
    kazumi "若夜有一个随身携带的笔记本。" #or 密码本？
    kazumi "我认识她的时候，她就已经会把自己的心事写在那个笔记本上。"
    ryuka "你看过？"
    kazumi "当然！我和她的关系很好，之前还在那个本子上一起画过涂鸦。"
    kazumi "不过也是从那时候开始，她就把本子的密码换了，也从来没给别人看过。"
    hisaki "为什么要上锁？"
    kazumi "秘密。"
    $ xiansuo_5 = 1
    """
    她没打算说，我也没打算问。

    至于密码，那也没必要问了。

    反正问了也是白问。
    """
    kazumi "对了，你们的生日是什么时候？"
    hisaki "为什么要问这个？"
    kazumi "我之前给若夜准备了生日礼物，但是吧，她不喜欢，又不能浪费，只好给你们当生日礼物了。"
    ryuka "我的生日还要好久。"
    hisaki "我的生日......"
    python:
        month_num = 0
        day_num = 0
        month_input = renpy.input("请输入你的生日月份，如一月，则输入1，以此类推。", length=2)
        month_input = month_input.strip()
        day_input = renpy.input("请输入你的生日当月日期，如一号，则输入1，以此类推。", length=2)
        day_input = day_input.strip()
        now_month = get_month()
        now_day = get_day()
        month_input_num = int(month_input)
        day_input_num = int(day_input)
        months_num = (12 - now_month + month_input_num) % 12
        if month_input_num == now_month and day_input_num == now_day:
            month_num += 1
            day_num += 1
        if day_input_num == now_day and month_input_num != now_month:
            day_num += 3
        if day_input_num != now_day and month_input_num == now_month:
            month_num += 4

    if month_num + day_num == 2:
        kazumi "就在这天啊。"
    if month_num == 4:
        kazumi "就在这个月啊。"
    if day_num == 3:
        kazumi "那还有[months_num]个月到你的生日了。"
    else:
        kazumi "那还早。"
    kazumi "总之我先记下了。"
    kazumi "至于礼物，生不生日的无所谓了。"
    kazumi "我只想着快点送走。"
    show ryukaa at left
    with moveinleft
    ryuka "呃，为什么？"
    kazumi "瘆人啊，你们知道那是什么吗？"
    kazumi "是仿真娃娃。"
    kazumi "大半夜真的会吓死人的。"
    hisaki "我大概懂了。"
    "这么着急，估计被吓得不轻"
    kazumi "你们能理解那种，大半夜有一双发光的大眼睛盯着你的感觉吗？"
    kazumi "还是红光......"