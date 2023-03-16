
# test

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

# EOF
