'''
    test.py
'''

# #############################################
# License: GNU GENERAL PUBLIC LICENSE GPL-3.0 #
# Copyright: R.J. Nap - AutoExec.nl           #
# Thank you for using Exec_log                #
# If possible, please support me at:          #
# BTC: 3PBtoTbpfB7rv6qx8Mg2vFr92Qvc3UjSSD     #
# #############################################


output = input("enter [d] for developer console output and [l] for log file output: ")

if output == "d":
    
    developer = True
    print("developer: " + str(developer))
    
else:
    
    developer = False
    print("developer: " + str(developer))

question = input("enter [f] for function test or enter [c] for class test: ")

if question == "f":
    print("log file " + "function call")
    from exec_log import exec_log
    exec_log("testing log level 1", "debug",    developer)
    exec_log("testing log level 2", "info",     developer)
    exec_log("testing log level 3", "warning",  developer)
    exec_log("testing log level 4", "error",    developer)
    exec_log("testing log level 5", "critical", developer)

else:
    print("Class call")
    from exec_log_class import exec_logging as exec_log
    exec_log().exec_log(message="testing log level 1", level="debug",    developer=developer)
    exec_log().exec_log(message="testing log level 2", level="info",     developer=developer)
    exec_log().exec_log(message="testing log level 3", level="warning",  developer=developer)
    exec_log().exec_log(message="testing log level 4", level="error",    developer=developer)
    exec_log().exec_log(message="testing log level 5", level="critical", developer=developer)

i = 0

style_end = "\x1b[0m"

while i < 9:
    print("\x1b[3" + str(i) + ";40m\n" + "Color test font-color: 3" + str(i) + " background-color: 40" + style_end)
    print("\x1b[3" + str(i) + ";41m\n" + "Color test font-color: 3" + str(i) + " background-color: 41" + style_end)
    print("\x1b[3" + str(i) + ";42m\n" + "Color test font-color: 3" + str(i) + " background-color: 42" + style_end)
    print("\x1b[3" + str(i) + ";43m\n" + "Color test font-color: 3" + str(i) + " background-color: 43" + style_end)
    print("\x1b[3" + str(i) + ";44m\n" + "Color test font-color: 3" + str(i) + " background-color: 44" + style_end)
    print("\x1b[3" + str(i) + ";45m\n" + "Color test font-color: 3" + str(i) + " background-color: 45" + style_end)
    print("\x1b[3" + str(i) + ";46m\n" + "Color test font-color: 3" + str(i) + " background-color: 46" + style_end)
    print("\x1b[3" + str(i) + ";47m\n" + "Color test font-color: 3" + str(i) + " background-color: 47" + style_end)
    print("\x1b[3" + str(i) + ";48m\n" + "Color test font-color: 3" + str(i) + " background-color: 48" + style_end)
    i = i +1

# EOF
