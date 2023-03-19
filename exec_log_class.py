'''
    exec_log_class.py
    
'''

# #############################################
# License: GNU GENERAL PUBLIC LICENSE GPL-3.0 #
# Copyright: R.J. Nap - AutoExec.nl           #
# Thank you for using Exec_log                #
# If possible, please support me at:          #
# BTC: 3PBtoTbpfB7rv6qx8Mg2vFr92Qvc3UjSSD     #
# #############################################


class exec_logging():

    def __init__(self):
        pass

    def exec_log(self, message="Log call.", level="debug",  developer=False):
        
        self.message = message
        self.level = level
        self.developer = developer
        
        ''' 
            # Enhance your Python logging with colors
            
            Hi, I am exec_log 0.1 Class function , and I add color to your linux logging requests. You can use strings or int for your logging level and log to console or cvs

            All default logging is done on level [DEBUG] unless specified: debug/info/warning/error/critical.

            All default logging is done on level [1] unless specified: 1/2/3/4/5.

            If developer mode is True, console logging is active instead of file logging.

            ## Usage

            from exec_log_class import exec_logging as exec_log
            exec_log("test my log")

            Example 1: exec_log("foo") returns debug log message 'foo'

            Example 2: exec_log("foo", 1) returns debug log message 'foo'

            Example 3: exec_log("foo", "debug") returns debug log message 'foo'

            Example 4: exec_log(str(foo), level="warning")

            Example 5: exec_log("foo" + "bar" + str(i), level="Warning", developer=False)

            ## Wrong usage

            Example 6: exec_log("foo", "doom") returns level error

            Example 7: exec_log("foo", 9) returns level error

            ### Have a nice day logging!
    
        '''
        
        import logging
    
        # Function variables are defined based on Developer Mode True or False
        
        if self.developer == True:
            
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

            # Debug output to log file as cvs
            
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

        if self.developer == True:
            
            # logging output to console

            logging.basicConfig(format=settings_log["format"], level=settings_log["level"])

        else:
            
            import os
    
            # if the log file is new, we start by adding a header
            
            if os.path.exists(settings_log["log_file"]) == False:
                print("create logfile")
                log_csv = open(file=settings_log["log_file"], mode="x",encoding="utf-8")
                log_csv.write(settings_log["header"])
                log_csv.close
                
            # logging output to file
            
            logging.basicConfig(format=settings_log["format"], filename=settings_log["log_file"], level=settings_log["level"], filemode="a", encoding="utf-8")
            
    
        # Handle log request 

        if str(self.level) == "debug" or str(self.level)      == "1":
            message = settings_log["color_debug"] + self.message + settings_log["color_reset"]
            return logging.debug(message)
        
        elif str(self.level) == "info" or str(self.level)     == "2":
            message = settings_log["color_info"] + self.message + settings_log["color_reset"] 
            return logging.info(message)
        
        elif str(self.level) == "warning" or str(self.level)  == "3":
            message = settings_log["color_warning"] + self.message + settings_log["color_reset"] 
            return logging.warning(message)
        
        elif str(self.level) == "error" or str(self.level)    == "4":
            message = settings_log["color_error"] + self.message + settings_log["color_reset"] 
            return logging.error(message)    
                
        elif str(self.level) == "critical" or str(self.level) == "5":
            message = settings_log["color_critical"] + self.message + settings_log["color_reset"] 
            return logging.critical(message)
        
        else:
            return logging.error("invalid log level: " + str(self.level))     

# NFO Console colour output
#
# https://docs.python.org/3/library/logging.html

# https://docs.python.org/3/library/logging.html#logrecord-attributes
# 
# NFO Format LogRecord attributes

'''

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
