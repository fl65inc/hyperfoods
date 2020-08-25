# -*- coding: utf-8 -*-
"""
DRUGS Project module: printlog.py

PrintLog module - print statements and log them if log file started.


--------------------------------------------------------------------------

Lead Developer: Dr. Ivan Laponogov (mailto:i.laponogov@imperial.ac.uk) 

Chief project investigator: Dr. Kirill Veselkov (mailto:kirill.veselkov04@imperial.ac.uk)

License: 

The MIT License (MIT)

Copyright 2019 Imperial College London

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

"""

#===========================Import section=================================

#Importing standard and external modules

import os;

#==========================================================================
#From here the main code starts
class LoggingException(Exception):

    def __init__(self, value):
        self.parameter = value
        printlog(value, print_enabled = False);
        
    def __str__(self):
        return repr(self.parameter)



__logging = False;
__logclosed = True;
__logfilename = '';
__log_autoclose = True;
__logfile = None;
__verbosity_level = 0;

def start_log(fname, autoclose = True, overwrite_existing = True, verbosity_level = 0):
    """
    Begin logging of the printed strings. 
    
    Args:
        fname - name of the log file (str). If no path is supplied as part of 
                the file name - current working directory is used instead.
                
        autoclose - defines if file is kept closed between log events. Assures
                    that whatever is written to the file is there and not lost
                    in the buffer in case the program crashes. Also helps to be
                    able to see the log in Windows as it is written. May add 
                    some overhead though if logging is used extensively.
                    Default value - True
    
        overwrite_existing - If True the existing log file will be 
                             overwritten. Otherwise it will be continued.
                             Default value - True
    
    Returns:
        None
    
    """
    global __logging;
    global __logfilename;
    global __log_autoclose;
    global __logfile;
    global __logclosed;
    global __verbosity_level;
    
    __verbosity_level = int(verbosity_level);
    
    fname = os.path.abspath(fname);

    __log_autoclose = autoclose;
    __logging = True;
    __logfilename = os.path.abspath(fname);
    
    if os.path.isfile(__logfilename):
        if overwrite_existing:
            os.remove(__logfilename);
    
    path, name = os.path.split(fname);
    if not os.path.exists(path):
        os.makedirs(path);
            
    if not autoclose:
        if os.path.isfile(__logfilename):
            __logfile = open(__logfilename, 'a');
        else:
            __logfile = open(__logfilename, 'w');
        __logclosed = False;
        

def stop_log():
    """
    Stops logging.
    
    Args:
        None
        
    Returns:
        None
    
    """
    global __logfile;
    global __logclosed;
    global __logging;
    
    __logging = False;
    
    if not __logclosed:
        __logfile.close();
        __logclosed = True;
        
        
def printlog(logstring = '', print_enabled = True, log_enabled = True, verbosity_level = 0):
    """
    Print logstring and write it to the log file.
    
    Args:
        logstring - string to be printed and/or logged. Default = ''
        
        print_enabled - print the logstring if True. Default = True. Does not 
                        depend on whether the log is started or not.
        log_enabled - write logstring to logfile if True and logging is started with
                      start_log(log_filename). Default True.
    
    Returns:
        None
    
    """
    global __verbosity_level;

    if verbosity_level > __verbosity_level:
        return
    
    global __logging;
    global __logfilename;
    global __log_autoclose;
    global __logfile;
    global __logclosed;
    
    
    if print_enabled:
        print(logstring);
    
    if log_enabled:
        if __logging:
            if __log_autoclose:
                if os.path.isfile(__logfilename):
                    with open(__logfilename, 'a') as fout:
                        fout.write('%s\n'%logstring);
                else:
                    with open(__logfilename, 'w') as fout:
                        fout.write('%s\n'%logstring);
            else:
                __logfile.write('%s\n'%logstring);
        
    
        
        
        