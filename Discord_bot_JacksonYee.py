#!/user/bin/env python
# -*- coding: utf-8 -*-

import logging
import discord
import json
import re
from datetime import datetime
from pprint import pprint
from datetime import datetime # datetime.now().year
import random # 用於隨機選歌

from JacksonYee import runLoki

logging.basicConfig(level=logging.DEBUG)

ans_dict = {"birthday":["我在2000年11月28日出生", "我在2000年出生", "我11月出生", "我的生日是11月28日", f"{datetime.now().year - 2000}歲"], 
            "talent":["我表演過Beatbox、爵士鼓、吉他、貝斯、鋼琴、嗩吶、葫蘆絲、手風琴、中國鼓、快板、笛子", "我是個演員，也是個歌手，也是個舞者，我也會寫書法、變臉、變魔術、繪畫、滑雪", "我會跳舞，5歲就開始學舞了！我會跳街舞、拉丁舞、民族舞、機械舞、中國舞、爵士舞...，我也會編舞^^", "我是易烊千璽"], 
            "debut":["我和王俊凱、王源在2013年8月6日已TFBOYS組合成員身份出道。", "我的應援色是紅色", "我喜歡我的粉絲們，我都叫他們千紙鶴、鳥姐、鶴"],
            "family":["我是中華人民國湖南人", "我姓「易」，不姓「易烊」。「烊」在我老家是歡迎的意思，意思是歡迎千禧年的到來", "我有個弟弟，他的名字也是四個字。他叫做易烊昱華，小名楠楠", "我的英文名字是Jackson Yee，拼音是 Yi Yang Qian Xi"],
            "university":["我畢業於中央戲劇學院"],
            "songs":["我最新的三首歌是白日貓、等她在午夜前和同乘，一個多月前發行於劉艷芬", "我的音樂類型屬於華語流行音樂、cpop", "你想聽哪首歌？"],
            "album":["我目前出過四張專輯，我樂意沉默釋放內心焰火、溫差感、後座劇場、劉艷芬，最新的專輯（劉艷芬）有出實體專輯，你想了解哪張專輯？", "我樂意沉默釋放內心焰火發行於2018年11月28日，有Don't Tie Me Down、親愛的，這裏沒有一個人、災、恆溫動物、舒適圈、Nothing To Lose (unplugged)，共六首歌", "溫差感發行於2019年12月20日，有入夢（Intro）、末日長河、犧牲的一半、再一，再二，再三、兩個傍晚的月亮、Gone、酣然（Interlude）、冷靜和熱情之間、Fall、I Adore You、陷落美好、念想（鋼琴版）、初醒（Outro），共十三首歌", '後座劇場發行於2020年11月27日，有39km、野花、38.7km、愛情鳥、35km、親密愛人、4km、孤獨的人是可恥的、0.5km、愛的箴言、0.01km、送別，共十二首歌', '劉艷芬發行於2023年4月25日，有20:55、九里莊人才中心、21:00、你好，我是        、冷屁股、霓裳、22:12、五光十色、22:28、彳亍、22:33、白日貓、等她在午夜前、23:00、同乘，共十五首歌'],
            "links":['https://www.youtube.com/watch?v=WdKH-DI4rqI&pp=ygUW57KJ6Zyn5rW3IOaYk-eDiuWNg-eSvQ%3D%3D', 'https://www.youtube.com/watch?v=L3ScfN_87jE&pp=ygUf5piT54OK5Y2D55K9IGRvbid0IHRpZSBtZSBkb3duIA%3D%3D', 'https://www.youtube.com/watch?v=Et1UqcyPw1k&pp=ygUu5piT54OK5Y2D55K9IOimquaEm-eahO-8jOmAmeijj-aykuacieS4gOWAi-S6ug%3D%3D', 'https://www.youtube.com/watch?v=IEcb-FB1iLQ&pp=ygUQ5piT54OK5Y2D55K9IOeBvQ%3D%3D', 'https://www.youtube.com/watch?v=LOlhh9NaZI8&pp=ygUZ5piT54OK5Y2D55K9IOaBhua6q-WLleeJqQ%3D%3D', 'https://www.youtube.com/watch?v=rhA2BwdKiBI&pp=ygUW5piT54OK5Y2D55K9IOiIkumBqeWciA%3D%3D', 'https://www.youtube.com/watch?v=quVlyW3cZqU&pp=ygUo5piT54OK5Y2D55K9IE5vdGhpbmcgVG8gTG9zZSAodW5wbHVnZ2VkKQ%3D%3D', 'https://www.youtube.com/watch?v=AeyXZmTcxYA&pp=ygUe5piT54OK5Y2D55K9IOWFpeWkou-8iEludHJv77yJ', 'https://www.youtube.com/watch?v=ZKsFTltej4c&pp=ygUZ5piT54OK5Y2D55K9IOacq-aXpemVt-aysw%3D%3D', 'https://www.youtube.com/watch?v=UTAyNEpKICg&pp=ygUc5piT54OK5Y2D55K9IOeKp-eJsueahOS4gOWNig%3D%3D', 'https://www.youtube.com/watch?v=srdP-TVf220&pp=ygUl5piT54OK5Y2D55K9IOWGjeS4gO-8jOWGjeS6jO-8jOWGjeS4iQ%3D%3D', 'https://www.youtube.com/watch?v=Y2B7wcOzkB0&pp=ygUi5piT54OK5Y2D55K9IOWFqeWAi-WCjeaZmueahOaciOS6rg%3D%3D', 'https://www.youtube.com/watch?v=PuKCZNM2AI0&pp=ygUR5piT54OK5Y2D55K9IGdvbmU%3D', 'https://www.youtube.com/watch?v=ZihSNeiT9xw&pp=ygUi5piT54OK5Y2D55K9IOmFo-eEtu-8iEludGVybHVkZe-8iQ%3D%3D', 'https://www.youtube.com/watch?v=pTPtSOlVIxo&pp=ygUi5piT54OK5Y2D55K9IOWGt-mdnOWSjOeGseaDheS5i-mWkw%3D%3D', 'https://www.youtube.com/watch?v=p-JZ2647Eso&pp=ygUR5piT54OK5Y2D55K9IEZhbGw%3D', "不好意思，尚未儲存此歌曲連結"],
            "films":["少年的你、送你一朵小紅花、中國醫生、長津湖、奇蹟·笨小孩、長津湖之水門橋、世間有她、滿江紅，共八部電影", "滿江紅是我最新的電影，我飾演孫均", "我在世間有她中飾演李昭華", "我在長津湖之水門橋中飾演伍萬里", "我在奇蹟·笨小孩中飾演景浩", "我在長津湖中飾演伍萬里", "我在中國醫生中飾演楊小洋", "我在送你一朵小紅花中飾演韋一航", "我在少年的你中飾演劉北山"]
            }


punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")
def getLokiResult(inputSTR):
    punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")
    inputLIST = punctuationPat.sub("\n", inputSTR).split("\n")
    filterLIST = []
    resultDICT = runLoki(inputLIST, filterLIST)
    logging.debug("Loki Result => {}".format(resultDICT))
    return resultDICT

class BotClient(discord.Client):

    def resetMSCwith(self, messageAuthorID):
        '''
        清空與 messageAuthorID 之間的對話記錄
        '''
        templateDICT = self.templateDICT
        templateDICT["updatetime"] = datetime.now()
        return templateDICT

    async def on_ready(self):
        # ################### Multi-Session Conversation :設定多輪對話資訊 ###################
        self.templateDICT = {"updatetime" : None,
                             "latestQuest": ""
        }
        self.mscDICT = { #userid:templateDICT
        }
        # ####################################################################################
        print('Logged on as {} with id {}'.format(self.user, self.user.id))

    async def on_message(self, message):
        # Don't respond to bot itself. Or it would create a non-stop loop.
        # 如果訊息來自 bot 自己，就不要處理，直接回覆 None。不然會 Bot 會自問自答個不停。
        if message.author == self.user:
            return None

        logging.debug("收到來自 {} 的訊息".format(message.author))
        logging.debug("訊息內容是 {}。".format(message.content))
        if self.user.mentioned_in(message):
            replySTR = "我是預設的回應字串…你會看到我這串字，肯定是出了什麼錯！"
            logging.debug("本 bot 被叫到了！")
            msgSTR = message.content.replace("<@{}> ".format(self.user.id), "").strip()
            logging.debug("人類說：{}".format(msgSTR))
            if msgSTR == "ping":
                replySTR = "pong"
            elif msgSTR == "ping ping":
                replySTR = "pong pong"

# ##########初次對話：這裡是 keyword trigger 的。
            elif msgSTR.lower() in ["哈囉","嗨","你好","您好","hi","hello", "hihi", "hi hi", "hello hello", "在嗎？", "在嗎", "易烊千璽", "易烊千玺"]:
                #有講過話(判斷對話時間差)
                if message.author.id in self.mscDICT.keys():
                    timeDIFF = datetime.now() - self.mscDICT[message.author.id]["updatetime"]
                    #有講過話，但與上次差超過 5 分鐘(視為沒有講過話，刷新template)
                    if timeDIFF.total_seconds() >= 300:
                        self.mscDICT[message.author.id] = self.resetMSCwith(message.author.id)
                        replySTR = "嗨嗨，我們好像見過面，但卓騰的隱私政策不允許我記得你的資料，抱歉！"
                    #有講過話，而且還沒超過5分鐘就又跟我 hello (就繼續上次的對話)
                    else:
                        replySTR = self.mscDICT[message.author.id]["latestQuest"]
                #沒有講過話(給他一個新的template)
                else:
                    self.mscDICT[message.author.id] = self.resetMSCwith(message.author.id)
                    replySTR = msgSTR.title()

# ##########非初次對話：這裡用 Loki 計算語意
            else: #開始處理正式對話
                #從這裡開始接上 NLU 模型
                resultDICT = getLokiResult(msgSTR)
                logging.debug("######\nLoki 處理結果如下：")
                logging.debug(resultDICT)

                if 'birthday' in resultDICT:
                    if resultDICT['birthday'] == '出生日': 
                        replySTR = ans_dict['birthday'][0]
                    elif resultDICT['birthday'] == '出生年':
                        replySTR = ans_dict['birthday'][1]
                    elif resultDICT['birthday'] == '出生月':
                        replySTR = ans_dict['birthday'][2]
                    elif resultDICT['birthday'] == '生日':
                        replySTR = ans_dict['birthday'][3]
                    elif resultDICT['birthday'] == '年齡':
                        replySTR = ans_dict['birthday'][4]
                elif 'talent' in resultDICT:
                    if resultDICT['talent'] == '樂器': 
                        replySTR = ans_dict['talent'][0]
                    elif resultDICT['talent'] == '才藝': 
                        replySTR = ans_dict['talent'][1]
                    elif resultDICT['talent'] == '跳舞': 
                        replySTR = ans_dict['talent'][2]
                    elif resultDICT['talent'] == '易烊千璽': 
                        replySTR = ans_dict['talent'][3]
                elif 'debut' in resultDICT:
                    if resultDICT['debut'] == '團體出道': 
                        replySTR = ans_dict['debut'][0]
                    elif resultDICT['debut'] == '應援色': 
                        replySTR = ans_dict['debut'][1]
                    elif resultDICT['debut'] == '粉絲': 
                        replySTR = ans_dict['debut'][2]
                elif 'family' in resultDICT:
                    if resultDICT['family'] == '湖南': 
                        replySTR = ans_dict['family'][0]
                    elif resultDICT['family'] == '姓氏': 
                        replySTR = ans_dict['family'][1]
                    elif resultDICT['family'] == '弟弟': 
                        replySTR = ans_dict['family'][2]
                    elif resultDICT['family'] == '英文名': 
                        replySTR = ans_dict['family'][3]
                elif 'university' in resultDICT:
                    if resultDICT['university'] == '大學': 
                        replySTR = ans_dict['university'][0]
                elif 'songs' in resultDICT:
                    if resultDICT['songs'] == '新歌': 
                        replySTR = ans_dict['songs'][0]
                    elif resultDICT['songs'] == '風格': 
                        replySTR = ans_dict['songs'][1]
                    elif resultDICT['songs'] == '聽歌': 
                        replySTR = ans_dict['songs'][2]
                elif 'album' in resultDICT:
                    if resultDICT['album'] == '專輯': 
                        replySTR = ans_dict['album'][0]
                    elif resultDICT['album'] == '我樂意沉默釋放內心焰火': 
                        replySTR = ans_dict['album'][1]
                    elif resultDICT['album'] == '溫差感': 
                        replySTR = ans_dict['album'][2]
                    elif resultDICT['album'] == '後座劇場': 
                        replySTR = ans_dict['album'][3]
                    elif resultDICT['album'] == '劉艷芬': 
                        replySTR = ans_dict['album'][4]            
                elif 'links' in resultDICT:
                    if resultDICT['links'] == '都好' or resultDICT['links'] == '都可以' or resultDICT['links'] == '隨便': 
                        replySTR = random.choice(ans_dict['links'])
                    elif resultDICT['links'] == '粉霧海': 
                        replySTR = ans_dict['links'][0]
                    elif resultDICT['links'] == "Don't Tie Me Down": 
                        replySTR = ans_dict['links'][1]
                    elif resultDICT['links'] == '親愛的，這裏沒有一個人': 
                        replySTR = ans_dict['links'][2]
                    elif resultDICT['links'] == '災': 
                        replySTR = ans_dict['links'][3]
                    elif resultDICT['links'] == '恆溫動物': 
                        replySTR = ans_dict['links'][4]
                    elif resultDICT['links'] == '舒適圈': 
                        replySTR = ans_dict['links'][5]
                    elif resultDICT['links'] == 'Nothing To Lose' or resultDICT['links'] ==  'Nothing To Lose (unplugged)': 
                        replySTR = ans_dict['links'][6]
                    elif resultDICT['links'] == '入夢（Intro）' or resultDICT['links'] == '入夢': 
                        replySTR = ans_dict['links'][7]
                    elif resultDICT['links'] == '末日長河': 
                        replySTR = ans_dict['links'][8]
                    elif resultDICT['links'] == '犧牲的一半': 
                        replySTR = ans_dict['links'][9]
                    elif resultDICT['links'] == '再一，再二，再三': 
                        replySTR = ans_dict['links'][10]
                    elif resultDICT['links'] == '兩個傍晚的月亮': 
                        replySTR = ans_dict['links'][11]
                    elif resultDICT['links'] == 'Gone': 
                        replySTR = ans_dict['links'][12]
                    elif resultDICT['links'] == '酣然（Interlude）' or resultDICT['links'] == '酣然': 
                        replySTR = ans_dict['links'][13]
                    elif resultDICT['links'] == '冷靜和熱情之間': 
                        replySTR = ans_dict['links'][14]
                    elif resultDICT['links'] == 'Fall': 
                        replySTR = ans_dict['links'][15]
                    else:
                        replySTR = ans_dict['links'][16]

                elif 'films' in resultDICT:
                    if resultDICT['films'] == '電影': 
                        replySTR = ans_dict['films'][0]
                    elif resultDICT['films'] == '滿江紅': 
                        replySTR = ans_dict['films'][1]
                    elif resultDICT['films'] == '世間有她': 
                        replySTR = ans_dict['films'][2]
                    elif resultDICT['films'] == '長津湖之水門橋': 
                        replySTR = ans_dict['films'][3]
                    elif resultDICT['films'] == '奇蹟·笨小孩': 
                        replySTR = ans_dict['films'][4] 
                    elif resultDICT['films'] == '長津湖': 
                        replySTR = ans_dict['films'][5] 
                    elif resultDICT['films'] == '中國醫生': 
                        replySTR = ans_dict['films'][6] 
                    elif resultDICT['films'] == '送你一朵小紅花': 
                        replySTR = ans_dict['films'][7] 
                    elif resultDICT['films'] == '少年的你': 
                        replySTR = ans_dict['films'][8] 

                else:
                    replySTR = "不好意思，檔案還在建立中，或許你可以先詢問其他問題 > <"


            await message.reply(replySTR)


if __name__ == "__main__":
    # with open("account.info", encoding="utf-8") as f: #讀取account.info
    #     accountDICT = json.loads(f.read())
    client = BotClient(intents=discord.Intents.default())
    client.run("discord_token")  # accountDICT["discord_token"]改成機器人的token string