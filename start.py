import sys
from io import StringIO
import telebot

ADMINS = [398614726]
bot = telebot.TeleBot("423768346:AAGzF8dyVMle1oBqxbhPN_BHa3xnHFH90go")

@bot.message_handler(content_types=["text"])
def dopython(msg):
    """Do then was typed 'code:\n' 
    execution code with build-in function 'eval()'
    collect result with redirect sys.stdout
    """
    if msg.text.startswith("code:\n"): 
        bot.reply_to(msg, "result: " + executionpython(msg.text[5:]))
    else: bot.reply_to(msg, msg.text.upper())
    
def executionpython(code):
    """Execution code eval() and collect result 
        input: 
            code: str() type
        output:
            result/error: str() type
    """
    tmp = sys.stdout
    redirectedout = sys.stdout = StringIO()
    try:
        print(eval(code))
    except Exception as e:
        print(f"in your vode was error:\n{e}") 
    sys.stdout = tmp
    return redirectedout.getvalue()

if __name__ == "__main__":
    bot.polling(none_stop=True)
    #print(executionpython("print('s')"))


