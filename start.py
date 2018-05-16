import sys, time
from multiprocessing import Process
import telebot
from execcode import Execcode

ADMINS = [398614726]
bot = telebot.TeleBot("423768346:AAGzF8dyVMle1oBqxbhPN_BHa3xnHFH90go")

class telbotinterp:
    def __init__(self, admins=ADMINS, bot=bot):
        self.admins = admins
        self.bot = bot
        self.procs = {}

        @bot.message_handler(content_types=["text"])
        def dopython(msg):
            """Do then was typed 'code:\n' 
            execution code with build-in function 'eval()'
            collect result with redirect sys.stdout
            """
            if msg.text.startswith("code:\n"):
                if self.sequrity(msg.text): bot.reply_to(msg, "You cant use sys module")
                else: self.executionpythonjs(msg.text[5:], msg)
            else: bot.reply_to(msg, msg.text.upper()) # until testing
        
    def executionpython(self, code, msg):
        """Execution code eval() and collect result 
            input: 
                code: str() type
                msg: telebot.TeleBot object
            output:
                result/error: str() type
        """
        try:
            reply = str(eval(compile(code, '<string>', 'eval')))
        except Exception as e:
            print(f"in your vode was error:\n{e}") 
        bot.reply_to(msg, "result: " + reply)

    def executionpythonjs(self, code, msg):
        """Execution code with JS lib 'skulpt-kw.js' and collect result 
            input: 
                code: str() type
                msg: telebot.TeleBot object
            output:
                result/error: str() type
        """
        reply = Execcode(code).execjs()
        #print("in start.executionpythonjs() --> reply" + reply)
        #print("-"*40)
        bot.reply_to(msg, "result: " + reply) 

    def sequrity(self, code):
        """Check if user import sys
        """
        def security_exp(msg):
            bad_words = ('os', 'open', 'import', '__import__',
                        '__builtins__','__class__','__subclasses__')
            for exc in bad_words:
                if msg.find(exc) != -1:
                    return False


    def runprocess(self, code, msg):
        proc = Process(target=self.executionpython, args=(code, msg))
        self.procs[proc.name] = [proc, time.time()]
        proc.start()

    def start(self):
        self.bot.polling(none_stop=True)

    def checkprocs(self):
        while 1:
            time.sleep(0.1)
            for proc, val in self.procs.items():
                if time.time() - val[1] >= 60:
                    pass#kill proc
        


if __name__ == "__main__":
    #st = str(exec("1+2"))
    #print(st, "<---")
    tbi = telbotinterp(admins=ADMINS, bot=bot)
    tbi.start()
    #print(executionpython("print('s')"))


