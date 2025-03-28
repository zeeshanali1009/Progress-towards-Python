# --Modules and pips 
# ---Modules are the external functionalities or a set of functionalities
# which we bring into the ide and then use it further
# ---Pip is basically a command which we use to install the module in the terminal
# REPL(Read Print Evaluate Loop)  this is the functionalit of the windows terminal to start th python 
# programming involving all these steps

import pyjokes

joke = pyjokes.get_joke()
print(joke)