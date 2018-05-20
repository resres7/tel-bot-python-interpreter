import os, sys, time, threading
from multiprocessing import Process
import telebot
from execcode import Execcode

CONFIG = {}
with open("config.txt") as file:
    for line in file:
        name, value = line.split("==")
        CONFIG[name] = value.rstrip()
ADMINS = CONFIG.get("ADMINS")
bot = telebot.TeleBot(CONFIG.get("TOKEN"))

class Telbotinterp:
    def __init__(self, admins=ADMINS, bot=bot, test=False):
        self.admins = admins
        self.bot = bot
        self.procs = {}
        if not test:
            self.threadchecker = threading.Thread(target=self.checkprocs)

        @bot.message_handler(content_types=["text"])
        def dopython(msg):
            """Do then was typed 'code:\n' 
            execution code with build-in function 'eval()'
            collect result with redirect sys.stdout
            """
            if msg.text.startswith("code:\n"):
                if self.sequrity(msg.text): bot.reply_to(msg, "You cant use danger modules")
                else: self.runprocess(msg.text[5:], msg)
            else: bot.reply_to(msg, msg.text.upper()) # until testing
        
    def executionpythonjs(self, code, msg):
        """Execution code with JS lib 'skulpt-kw.js' and collect result 
            input: 
                code: str() type
                msg: telebot.TeleBot object
            output:
                result/error: str() type
        """
        reply = Execcode(code).execjs()
        bot.reply_to(msg, "result: " + reply) 

    def sequrity(self, code):
        """Check if user import sys
        """
        bad_words = ['os', 'open', 'import', '__import__',
                    '__builtins__','__class__','__subclasses__']
        for exc in bad_words:
            if code.find(exc) != -1:
                return True

    def runprocess(self, code, msg):
        proc = Process(target=self.executionpythonjs, args=(code, msg))
        proc.start()
        self.procs[proc.pid] = time.time()
        print("{}{}",self.threadchecker.is_alive(),"{}{}")
        if not self.threadchecker.is_alive():
            self.threadchecker = threading.Thread(target=self.checkprocs)
            self.threadchecker.start()

    def checkprocs(self, delay=0.5):
        while True:
            print("checkprocs".center(30, "~")  + "\n" + str(self.procs))
            time.sleep(delay)
            chkdict = []
            for proc, starttime in self.procs.items():
                if time.time() - starttime >= 1:
                    print(f"{proc} added to del list, time was expired== {time.time() - starttime}")
                    chkdict.append(proc)
            for proc in chkdict:
                try:
                    os.kill(proc, 0)
                except Exception as e:
                    print(e)
                del self.procs[proc]

    def start(self):
        self.bot.polling(none_stop=True)
        

if __name__ == "__main__":
    tbi = Telbotinterp(admins=ADMINS, bot=bot)
    tbi.start()


