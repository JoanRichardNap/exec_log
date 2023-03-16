# exec_log

## Enhance your Python logging with colors

Hi, I am exec_log 0.1 , and I add color to your linux logging requests. You can use strings or int for your logging level and log to console or cvs

All default logging is done on level [DEBUG] unless specified: debug/info/warning/error/critical.

All default logging is done on level [1] unless specified: 1/2/3/4/5.

If developer mode is True, console logging is active instead of file logging.

## Usage

from exec_log import exec_log
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

---

#### License: GNU GENERAL PUBLIC LICENSE       #
#### Copyright: R.J. Nap - AutoExec            #
#### Thank you for using Exec_log              #
#### If possible, please support me at:        #
#### BTC: 3PBtoTbpfB7rv6qx8Mg2vFr92Qvc3UjSSD   #