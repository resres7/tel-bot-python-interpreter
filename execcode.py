import sys
from Naked.toolshed.shell import execute_js, run_js

class Execcode:
    """Execut python code with LS 'skulpt-kw.js' lib 
    input:
        code: sorce python code str()
        pathsrc: path to LS lib str() 
    use Execcode.execjs() to get 'res: ' + result str()
    """
    def __init__(self, code, pathsrc="interpreterjs/main.js"): #skulpt-kw
        self.code = "'" + code + "'" 
        #print("in Execcode --> scr" + self.code)
        #print("-"*40)
        self.pathsrc = pathsrc

    def execjs(self):
        result = run_js(self.pathsrc, arguments=self.code, suppress_stdout=True)
        #result.
        print(result)
        print("in Execcode.execjs() --> result" + result.decode("utf-8"))
        print("-"*40)
        return result.decode("utf-8")


if __name__ == "__main__":
    execcode = Execcode("print(111+222)")
    #print(execcode.src)
    print(execcode.execjs())