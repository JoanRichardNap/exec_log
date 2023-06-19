'''
    exec_log.py
    
'''

# #############################################
# License: GNU GENERAL PUBLIC LICENSE GPL-3.0 #
# Copyright: R.J. Nap - AutoExec.nl           #
# Thank you for using Exec_log                #
# If possible, please support me at:          #
# BTC: 3PBtoTbpfB7rv6qx8Mg2vFr92Qvc3UjSSD     #
# #############################################

import logging

def exec_log(message="Log call.", level="debug", developer=False):
    
        ''' 
            Enhance your Python logging with colors
            
            Hi, I am exec_log 0.1 function, and I add color to your linux logging requests. You can use strings or int for your logging level and log to console or cvs

            All default logging is done on level [DEBUG] unless specified: debug/info/warning/error/critical.

            All default logging is done on level [1] unless specified: 1/2/3/4/5.

            If developer mode is True, console logging is active instead of file logging.

            Usage

            from exec_log import exec_log
            exec_log("test my log")

            Example 1: exec_log("foo") returns debug log message 'foo'

            Example 2: exec_log("foo", 1) returns debug log message 'foo'

            Example 3: exec_log("foo", "debug") returns debug log message 'foo'

            Example 4: exec_log(str(foo), level="warning")

            Example 5: exec_log("foo" + "bar" + str(i), level="Warning", developer=False)

            Wrong usage

            Example 6: exec_log("foo", "doom") returns level error

            Example 7: exec_log("foo", 9) returns level error

            Have a nice day logging!
     
        '''
    
        # Function variables are defined based on Developer Mode True or False
        
        if developer == True:
            
            # Debug output to console in style for developer
            
            settings_log = {
                            "color_debug"           : "\x1b[37;44m\n", 
                            "color_info"            : "\x1b[37;42m\n",
                            "color_warning"         : "\x1b[30;43m\n",
                            "color_error"           : "\x1b[34;45m\n",
                            "color_critical"        : "\x1b[37;41m\n",
                            "color_reset"           : "\x1b[0m",
                            "format"                : "%(message)s %(asctime)s %(created)f %(filename)s %(funcName)s %(levelname)s %(levelno)s %(lineno)d %(module)s %(msecs)d %(name)s %(pathname)s %(process)d %(processName)s %(relativeCreated)d %(thread)d %(threadName)s",
                            "level"                 : logging.DEBUG,
                            "log_file"              : ""                      
                            }
        else:

            # settings for output to log file as cvs
            
            settings_log = {
                            "color_debug"           : "", 
                            "color_info"            : "",
                            "color_warning"         : "",
                            "color_error"           : "",
                            "color_critical"        : "",
                            "color_reset"           : "",
                            "header"                : "levelname     , levelno     , message     , funcName     , lineno     , module     , name     , pathname     , process     , processName     , relativeCreated     , thread     , threadName    ,  created     , asctime     ,   msecs     ",
                            "format"                : "%(levelname)s , %(levelno)s , %(message)s , %(funcName)s , %(lineno)d , %(module)s , %(name)s , %(pathname)s , %(process)d , %(processName)s , %(relativeCreated)d , %(thread)d , %(threadName)s,  %(created)f , %(asctime)s ,   %(msecs)d ",
                            "level"                 : logging.INFO,
                            "log_file"              : 'log/log.csv'
                            }     
        
        # Set basicConfig for development or application logging

        if developer == True:
            
            # logging output to console

            logging.basicConfig(format=settings_log["format"], level=settings_log["level"])

        else:
            
            import os
      
            # if the log file is new, we start by adding a header
            
            if os.path.exists(settings_log["log_file"]) == False:
                log_csv = open(settings_log["log_file"], "x")
                log_csv.write(settings_log["header"])
                
                log_csv.close
                
            # logging output to file
            
            logging.basicConfig(format=settings_log["format"], filename=settings_log["log_file"], level=settings_log["level"], filemode="a", encoding="utf-8")
              
        # Handle log request 

        if str(level) == "debug" or str(level)      == "1":
            message = settings_log["color_debug"] + message + settings_log["color_reset"]
            return logging.debug(message)
        
        elif str(level) == "info" or str(level)     == "2":
            message = settings_log["color_info"] + message + settings_log["color_reset"] 
            return logging.info(message)
        
        elif str(level) == "warning" or str(level)  == "3":
            message = settings_log["color_warning"] + message + settings_log["color_reset"] 
            return logging.warning(message)
        
        elif str(level) == "error" or str(level)    == "4":
            message = settings_log["color_error"] + message + settings_log["color_reset"] 
            return logging.error(message)    
                
        elif str(level) == "critical" or str(level) == "5":
            message = settings_log["color_critical"] + message + settings_log["color_reset"] 
            return logging.critical(message)
        
        else:
            return logging.error("invalid log level: " + str(level))     
        
# Stand-alone Function Testing

if __name__ ==  '__main__':
    
    messages = (
                ("Testing loglevel 5: critical", 5),
                ("Testing loglevel 4: error",    4),
                ("Testing loglevel 3: warning",  3),
                ("Testing loglevel 2: info",     2), 
                ("Testing loglevel 1: debug",    1)
               )

    for i in messages:
        
            exec_log(i[0], i[1], True)

# NFO Console colour output
#
# https://docs.python.org/3/library/logging.html
#
# https://docs.python.org/3/library/logging.html#logrecord-attributes



'''

    NFO Format LogRecord attributes:
    
    Attribute name      Format                  Description
    ==================  ======================  ===========
    asctime             %(asctime)s             Human-readable time when the LogRecord was created. By default this is of the form ‘2003-07-08 16:49:45,896’ (the numbers after the comma are millisecond portion of the time).
    created             %(created)f             Time when the LogRecord was created (as returned by time.time()).
    filename            %(filename)s            Filename portion of pathname.
    funcName            %(funcName)s            Name of function containing the logging call.
    levelname           %(levelname)s           Text logging level for the message ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL').
    levelno             %(levelno)s             Numeric logging level for the message (DEBUG, INFO, WARNING, ERROR, CRITICAL).
    lineno              %(lineno)d              Source line number where the logging call was issued (if available).
    message             %(message)s             The logged message, computed as msg percent args. This is set when Formatter.format() is invoked.
    module              %(module)s              Module (name portion of filename).
    msecs               %(msecs)d               Millisecond portion of the time when the LogRecord was created.
    name                %(name)s                Name of the logger used to log the call.
    pathname            %(pathname)s            Full pathname of the source file where the logging call was issued (if available).
    process             %(process)d             Process ID (if available).
    processName         %(processName)s         Process name (if available).
    relativeCreated     %(relativeCreated)d     Time in milliseconds when the LogRecord was created, relative to the time the logging module was loaded.
    thread              %(thread)d              Thread ID (if available).
    threadName          %(threadName)s          Thread name (if available).

'''

# EOF
