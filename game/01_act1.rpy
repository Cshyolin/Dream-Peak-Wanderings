label act1:

    # 第一幕：独家新闻的价码


    scene bg mountain_road_night with dissolve

    play music "wind_goddess.ogg" volume 0.1

    # UI: 屏幕四周带有绿色的相机对焦框与焦距参数。

    show aya interested_with_wing at left_image with moveinleft

    aya "哎呀呀，这可真是个不得了的夜晚。"
    aya "虽然嘴上总说着天狗的职责就是追求真相。"
    aya "但实际上，我只是更喜欢看到平静的水面被砸进大石头那一瞬间的浪花罢了。"

    show aya interested_with_wing at left_image:
        shake
    
    aya "今晚的云台山安静得有些反常，连平日里最聒噪的毛玉和无名小妖都不见了踪影。"

    show aya serious:
        linear 0.3 xpos 0.85
    aya "空气里黏糊糊的，总觉得有什么大事要发生。"

    show aya serious at right_image:
        shake

    aya "红魔馆的那位家里蹲魔法使，平时不是在地下室看书就是在喝茶。"
    show aya excited
    aya "现在竟然露出了这种因惊讶而略显失态的表情。"

    show aya sly_smile at right_image
    aya "看吧，我的新闻直觉从不骗我……这不就是送上门来的头版头条吗？"

    hide aya with moveoutleft

    show knowledge surpriesd at right_image with moveinright

    play sound "camera_shutter.ogg"

    show pure_white with Dissolve(0.05)
    hide pure_white with Dissolve(0.15)

    show aya interested_with_wing at left_image with moveinleft

    aya "哎呀呀呀呀，这次可是又有了一个抗衡博丽大结界的东西哦……"

    show aya proud_with_closed_eyes at left_image
    """对付这些自诩优雅、看不起外界或者天狗的家伙,"""
    """你越是用这种无所谓的态度去戳她们的痛处,"""
    """她们就越容易暴露出破绽。"""

    show knowledge troubled

    show aya proud at left_image
    """瞧，帕秋莉的眼神变了。"""
    """原本应该充斥着魔力流动的空气,"""
    """现在简直就像是冻结成了一整块实心的冰。"""

    show aya excited at left_image
    """这沉重得让人喘不过气来的氛围，真是太棒了！"""
    """这才是大新闻该有的开场！"""

    show knowledge dislike at right_image
    knowledge "我买了。"

    queue sound "heavy_whoosh.ogg"
    queue sound "coin_clink.ogg" volume 1.5

    show knowledge sigh at right_image
    show aya suprised at left_image
    aya "哟，不愧是红魔馆的移动图书馆，一出手就是这么多钱，连半分犹豫都没有。"

    show aya sigh at left_image
    aya "既然买卖成了，我也得拿出点真家伙来。"
    """不然这位大人怕是要用火魔法把我身上的羽毛全都烤焦。"""

    show aya sigh at left_image:
        shake

    play sound "newspaper_flip.ogg"

    aya "这可是独家。云台山并不是在长树，而是这整座山，正在变成一棵“树”。"

    show knowledge serious at right_image
    show aya helpless_smile at left_image
    show knowledge cold at right_image
    knowledge "照片。"

    show aya smile at left_image
    aya "什么照片？"

    show knowledge coldsmile at right_image
    knowledge "你偷拍的那张。"
    aya "怎么能叫偷拍呢……"

    show knowledge battle at right_image
    pause 0.5

    show aya terrified at left_image
    aya "……欸别扔符卡！我给你就是！"

    show knowledge alert at right_image
    show aya helpless_smile at left_image
    """真是个开不起玩笑的女人。"""

    show aya serious at left_image
    show knowledge serious at right_image

    play sound "newspaper_flip.ogg"

    aya "不过，那幅地脉图根本不是什么山川走势。"
    aya "简直就像是一个正在疯狂生长的神经系统。"
    aya "这玩意儿散发出来的味道，绝对不是幻想乡。"
    aya "至少不是博丽大结界内现存的任何一种结界。"

    show knowledge thinking at right_image
    knowledge "这不是魔法，也不是道术。这是“观测者的干涉”。"
    knowledge "文文，那个孙美天到底在做什么？"
    aya "我不知道，从现在的状况来看，她想毁掉整个幻想乡。"
    aya "没有人能够保证在另一个幻想结界出现时幻想乡不会出什么问题。"

    show knowledge serious at right_image
    aya "顺带一提，灵梦小姐已经进到“树冠层”了。"
    aya "那里的风景……啧啧，相当具有冲击力。"

    show aya smile_with_wings at left_image

    hide aya with moveouttop

    aya "那么，文文新闻，先行一步！"

    return