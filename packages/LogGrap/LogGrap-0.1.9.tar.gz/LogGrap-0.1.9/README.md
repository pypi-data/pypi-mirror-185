# PyLogs
### A logging package for your python project
***

## Description
PyLogs allow you to add a logger to your python project. This logger can send the logs directly to the terminal and/or save them in an external file. Several options are available, such as :
- format
- type
- more in coming...

If you need help, go on my [GitHub](https://github.com/SsomGrap/PyLogs)

Work on python 3. For Windows, macOS and Linux.
***

## Installation
You just need to run this command in your **terminal** :

Windows 
```
py -m pip install --upgrade LogGrap
```

Linux
```
python3 -m pip install --upgrade LogGrap
```
***

## Functions and Constant
A list of all functions and constant in this package.
```
pylogs.TYPE_NEUTRAL
pylogs.TYPE_INFO
pylogs.TYPE_WARN
pylogs.TYPE_ERROR
pylogs.TYPE_CRITICAL
```
```
pylogs.Logger(String : name, String : directory)

pylogs.Logger.getFormat(String (opt): type)
pylogs.Logger.setFormat(String : format, String (opt): type)

pylogs.Logger.setTerminalOutput(Boolean : terminalOutPut, String (opt): type)
pylogs.Logger.setFileOutput(Boolean : fileOutPut, String (opt): type)

pylogs.Logger.neutral(String : text)

pylogs.Logger.loggerPrint(String : type, String : text)

pylogs.Logger.info(String : text)
pylogs.Logger.warn(String : text)
pylogs.Logger.error(String : text)
pylogs.Logger.critical(String : text)
```
***

## Exemple
An example of how to implement PyLogs to your projects
```
>>> import pylogs
>>> MyLogger = pylogs.Logger(name="MyLogger", directory="./logs")
>>> MyLogger.setFormat(pylogs.TYPE_INFO, " - [%hour] [%name] "
>>> MyLogger.info("Connected")

# Create a log file named with the date of your computer
# It contain the output
 - [11:08:50] [MyLogger] Connected

>>> MyLogger.fileOutput(False) # Turn off the file ouput for all logs
>>> MyLogger.neutral("A random message")
A random message

>>> MyLogger.fileOutput(TYPE_CRITICAL, True) # Turn on the file output for the critical messages
>>> MyLogger.terminalOutput(TYPE_CRITICAL, False)
>>> MyLogger.critical("critical error")

# The output will be in the logs file but not in the terminal (Only for the critical messages)
```
***

## Credits
developed by *ssomgrap*