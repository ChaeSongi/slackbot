from rtmbot import RtmBot
from rtmbot.core import Plugin
import random
import secret


def answer(text):
    if "송이" in text:
        reply = "네^ㅇ^!!??"
    elif "주사위" == text:
        reply = str(random.randint(1, 6))
    else:
        reply = None
    return reply

class HelloPlugin(Plugin):
    def process_message(self, data):
        reply = answer(data["text"])
        if reply is not None:
            self.outputs.append([data["channel"],reply])
            
class Hello(Plugin):
    def process_message(self, data):
        results =['할수있댕!!왈왈','간식주세요','으으으으으르르르렁','같이해요']
        if "댕댕" in data["text"]:
            num = random.randrange(0,3)
            self.outputs.append([data["channel"], results[num]])



config = {
    "SLACK_TOKEN": secret.SLACK_TOKEN,
    "ACTIVE_PLUGINS": ["main.HelloPlugin"]
}
bot = RtmBot(config)
bot.start()
