import os
import fnmatch
import traceback
import sys

def GuessDirSeparator(strpath):
    """return a directory separator likely used in strpath, return os.sep if no separator seems to be used"""
    import os
    osep = os.sep
    if(strpath.find(osep)>=0):
        return osep
    if(strpath.find("/")>=0):
        return "/"
    if(strpath.find("\\")):
        return "\\"
    return osep

def AddStringsToFileName(filepath=r"path\to\a\file.ext", addbefore="", addafter=""):
    """Return filepath so that r"path\to\a\file.ext" is returned as r"path\to\a\"+addbefore+"file"+addafter+"ext"""
    import os
    separator = GuessDirSeparator(filepath)
    base = os.path.basename(filepath)
    dname = os.path.dirname(filepath)
    basesplit = base.split(".")
    filename = basesplit[0]
    extension = ""
    if(len(basesplit)>0):
        extension = "." + ".".join(basesplit[1:])
    filename = addbefore + filename + addafter + extension
    return os.path.join(dname, filename)

def locate(pattern, topdir):
    import fnmatch
    for path, dirs, files in os.walk(os.path.abspath(topdir)):
        for filename in fnmatch.filter(files, pattern):
            yield os.path.join(path, filename)

try:
    #
    # USER INPUT
    top = r"C:\path\to\toppath" # root folder to start in
    pattern = "*" # only files like this
    pre = "before_" # to append before file name
    post = "_after" # to append before file name
    logpath = r"C:\temp\logme.txt" # path to a logfile
    # USER INPUT END
    #
    logsep = "\t"
    errorfreerun = True
    logfile = open(logpath, "w")
    #
    ff = locate(pattern, top)
    for f in ff:
        #print "renaming: " + str(f)
        try:
            newname = AddStringsToFileName(f, pre, post)
            logfile.write(f + logsep)
            os.rename(f, newname) # rename it
            logfile.write(newname)
        except Exception, e:
            logfille.write("Error: " + str(e))
            errorfreerun = False
        finally:
            logfile.write("\n")
    #
    if not errorfreerun:
        gp.addwarning("There were some errors! See "+ logpath + " for details!")
    #
except:
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    pymsg = tbinfo + "\n" + str(sys.exc_type)+ ": " + str(sys.exc_value)
    print pymsg
finally:
    if "logfile" in dir():
        logfile.close()
