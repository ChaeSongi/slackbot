from rtmbot import RtmBot
from rtmbot.core import Plugin
import random
import secret


class HelloPlugin(Plugin):
    def process_message(self, data):
        reply =['네 송이님','왜요?','🐕🐕🐕']
        if "송이" in data["text"]:
            num = random.randrange(0,2)
            self.outputs.append([data["channel"], reply[num]])
        elif "주사위" == data["text"]:
            die = str(random.randint(1, 6))
            self.outputs.append([data["channel"], die])
        else:
            pass


config = {
    "SLACK_TOKEN": secret.SLACK_TOKEN,
    "ACTIVE_PLUGINS": ["main.HelloPlugin"]
}
bot = RtmBot(config)
bot.start()
