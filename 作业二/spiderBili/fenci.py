import jieba

import jieba
test_sentence1 = '他在上海外国语大学打开了LOL'
test_sentence2 = '老番茄打败了纳什男爵并制作了B站视频，获得了首页通知书'
test_sentence3 = '住口！大胆妖僧，我一看就知道你不是人，看我让你原形毕露，大威天龙！世尊地藏！大罗法咒！般若诸佛！般若巴麻哄！飞龙在天！去！'
test_sentence4 = '希望看到简介的人能在弹幕打个看简介，蟹蟹！'
t1 = '|'.join(jieba.cut(test_sentence1))
t2 = '|'.join(jieba.cut(test_sentence2))
t3 = '|'.join(jieba.cut(test_sentence3))
t4 = '|'.join(jieba.cut(test_sentence4))

jieba.load_userdict('bilibili.txt')
print(t1)
print('|'.join(jieba.cut(test_sentence1)))

print(t2)
print('|'.join(jieba.cut(test_sentence2)))

print(t3)
print('|'.join(jieba.cut(test_sentence3)))

print(t4)
print('|'.join(jieba.cut(test_sentence4)))