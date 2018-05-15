var Sk = require("./skulpt-kw") 


function runit(code){
    var prog = code;
    var output = "";
    Sk.configure({output:outf});
    try {
        Sk.importMainWithBody("<stdin>", false, prog);
    } catch (e) {
        alert(e);
    }
}

runit("1+2");