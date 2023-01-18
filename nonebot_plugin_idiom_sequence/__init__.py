#import pandas as pd
#import numpy as np
import os, json, random
from pathlib import Path
from nonebot import on_command, on_fullmatch
from nonebot.adapters.onebot.v11 import Message, MessageEvent
from nonebot.params import CommandArg
from nonebot.plugin import PluginMetadata
from nonebot.typing import T_State

global status # 0 为不开始, 1 为刚开始, 2 为开始, 不一定要用2
global prev # 上一个
global prev_abbreviation
global prev_end

status = False
prev = ''
prev_abbreviation = ''

files = Path() / os.path.dirname(__file__) / "idiom.json"
idioms = json.loads(files.read_text(encoding='utf-8'))

def test(word):
    global status
    global prev
    global prev_abbreviation
    global prev_end
    for d in idioms:
        if word in d['word']:
            comp = d['pinyin'].split(' ')
            if comp[0] == prev_end:
                return {'status': True, 'word': d['word'], 'abbreviation': d['abbreviation'], 'derivation': d['derivation'], 'explanation': d['explanation'], 'pinyin': d['pinyin'], 'example': d['example'], 'end': comp[len(comp) - 1]}
    else:
        return {'status': False}

def info(word):
    for d in idioms:
        if word == d['word']:
            return d
    else:
        return 0

'''
__plugin_meta__ = PluginMetadata(
    name="成语接龙",
    description="来和机器人玩成语接龙吧！！！",
    usage=(
        "来机器人玩成语接龙吧！指令： < 成语接龙 | 成语接龙 + 一个成语 >"
    )
)

files = Path() / os.path.dirname(__file__) / "idiom.json"

idiom = pd.read_json(files)
t = idiom.pinyin.str.split()
idiom["firstChar"] = t.str[0]
idiom["lastChar"] = t.str[-1]
idiom = idiom.set_index("word")[["firstChar", "lastChar"]]
word2 = ""
lastChar = ""

resp_sentence = ["太厉害了",
                 "竟然被你答上来了",
                 "你简直是个文学家",
                 "你很棒哦",
                 "开始佩服你了呢"]
'''
start = on_fullmatch('成语接龙', priority=12, block=True)
@start.handle()
async def start_handle(event: MessageEvent, state: T_State):
    global status
    global prev
    global prev_abbreviation
    global prev_end
    if status == False:
        status = True
        idx = random.randint(0, len(idioms) - 1)
        init_word = idioms[idx]['word']
        init_abbreviation = idioms[idx]['abbreviation']
        init_pinyin = idioms[idx]['pinyin'].split(' ')
        init_end = init_pinyin[len(init_pinyin) - 1]
        await start.send('成语接龙开始⚖️我先说: ' + init_word + '\n解释: ' + idioms[idx]['explanation'] + '\n出自: ' + idioms[idx]['derivation'] + '\n例子: ' + idioms[idx]['example'])
        prev = init_word
        prev_abbreviation = init_abbreviation
        prev_end = init_end
        await start.send('''1.成语接龙只可以接成语(系统会检测，如不是成语会提醒)🔮\n2.本次的接龙可以使用同音字🛡️\n3.接龙有/无时间限制⚔️\n4.确认玩家及其先后顺序🐺''')
    elif status:
        await start.send('成语接龙已经开始了哦')

end = on_command('结束接龙', aliases = {'结束成语接龙'}, priority=12, block=True)
@end.handle()
async def end_handle(event: MessageEvent, state: T_State):
    global status
    global prev
    global prev_abbreviation
    if status == False:
        await start.send('还没开始怎么结束')
    else:
        await start.send('已经结束成语接龙')
        status = False



main = on_command('我接', aliases={'接龙', '接', 'j'}, priority=12, block=True)
# chen_yu_help = on_command('成语接龙帮助', aliases={'接龙帮助'}, priority=12, block=True)

'''
@chen_yu_help.handle()
async def chen_yu_help_():
    await chen_yu_help.finish(__plugin_meta__.usage)
'''

@main.handle()
async def main_handle(event: MessageEvent, state: T_State, msg: Message = CommandArg()):
    global status
    global prev
    global prev_abbreviation
    global prev_end
    # global idiom
    # global word2
    # global lastChar
    msg = msg.extract_plain_text().strip()
    if msg and status:
        res = test(msg)
        if (res['status']):
            prev = msg
            prev_abbreviation = res['abbreviation']
            prev_end = res['end']
            await main.send('🎉' + str(res['word']) + '🎉 ' + str(res['pinyin']) + '\n解释: ' + str(res['explanation']) + '\n出自: ' + str(res['derivation']) + '\n例子: ' + str(res['example']))
        else:
            await main.send('这个词好像不是成语或者它接不上啊, 上一个成语是: ' + prev + ' 音节: '+ prev_end)

            '''
            hint = np.random.choice(idiom[idiom.firstChar == msg[-1]].index)
            await main.send("厉害啦!")
            '''

        '''
            word2 = np.random.choice(idiom.index)
            await main.send("你输入的不是一个成语，那我就先开始啦，接招：【" + word2 + "】，认输或者不想玩了记得告诉我:< 不玩了|取消 >哦！！")
        else:
            words = idiom.index[idiom.firstChar == idiom.loc[msg, "lastChar"]]
            word2 = np.random.choice(words)
            if msg[-1] != word2[0]:
                words = idiom.index[idiom.firstChar == idiom.loc[msg, "lastChar"]]
                word2 = np.random.choice(words)
                if msg[-1] != word2[0]:
                    await chen_yu.finish("恭喜你赢了！你太厉害了，开局我就被你打败了，好不甘心！！！")
            lastChar = idiom.loc[word2, "lastChar"]
            await chen_yu.send("接招!我的答案是【" + word2 + "】，认输或者不想玩了记得告诉我:< 不玩了|取消 >哦！")
        '''
    '''
    else:
        word2 = np.random.choice(idiom.index)
        lastChar = idiom.loc[word2, "lastChar"]
        await chen_yu.send('那我就先开始啦，接招：【' + word2 + '】，认输或者不想玩了记得告诉我:< 不玩了|取消 >哦！')
    '''

'''
@chen_yu.got('text', prompt='')
async def chen_yu_got_(event: MessageEvent, state: T_State):
    global idiom
    global word2
    global lastChar
    tp = state["text"].extract_plain_text().strip()
    if tp == "不玩了" or tp == "取消":
        await chen_yu.finish("好的，游戏结束啦，欢迎下次来玩哦~！")
    else:
        if tp not in idiom.index:
            await chen_yu.reject("你输入的不是一个成语，请重新输入！")
        elif lastChar and idiom.loc[tp, 'firstChar'] != lastChar:
            await chen_yu.finish("哈哈，你的答案错了，我赢啦，游戏结束！！！")
        elif idiom.index[idiom.firstChar == idiom.loc[tp, "lastChar"]].shape[0] == 0:
            await chen_yu.finish("恭喜你赢了！你太厉害了，我被你打败！！！")
        else:
            words = idiom.index[idiom.firstChar == idiom.loc[tp, "lastChar"]]
            word2 = np.random.choice(words)
            if tp[-1] != word2[0]:
                words = idiom.index[idiom.firstChar == idiom.loc[tp, "lastChar"]]
                word2 = np.random.choice(words)
                if tp[-1] != word2[0]:
                    await chen_yu.finish("恭喜你赢了！你太厉害了，我被你打败！！！")
            lastChar = idiom.loc[word2, "lastChar"]
            await chen_yu.reject(np.random.choice(resp_sentence) + "，我的答案是【" + word2 + "】")
'''