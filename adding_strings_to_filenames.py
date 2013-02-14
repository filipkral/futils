import os
import fnmatch
import traceback
import sys

def GuessDirSeparator(strpath):
    """return a directory separator likely used in strpath, return os.sep if no separator seems to be used"""
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

def ListFiles(pattern, topdir):
    import fnmatch
    for path, dirs, files in os.walk(os.path.abspath(topdir)):
        for filename in fnmatch.filter(files, pattern):
            yield os.path.join(path, filename)

def main(top = r"C:\path\to\toppath", pattern = "*", pre = "before_",  post = "_after", logpath = r"C:\temp\logme.txt"):
    """
    Rename all files under *top* folder (recursively) that match *pattern* so that the new file name si *pre*+originalfilename+*post*+.ext.
    top: root folder to start in
    pattern: rename only files that match this pattern, use e.g. *.jpg to deal with jpg files only, use * to include all files
    pre: string to append at the beginning of a file name
    post: string to append at the end of a file name
    logpath: path to a logfile
    """

    try:
        logsep = "\t"
        errorfreerun = True
        logfile = open(logpath, "w")
        #
        ff = ListFiles(pattern, top)
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
            print "There were some errors! See "+ logpath + " for details!"
        #
    except:
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        pymsg = tbinfo + "\n" + str(sys.exc_type)+ ": " + str(sys.exc_value)
        print pymsg
    finally:
        if "logfile" in dir():
            logfile.close()

if __name__ == '__main__':
    pass
    #example use:
    #main(top = r"C:\path\to\top\dir", pattern = "*", pre = "before_",  post = "_after", logpath = r"C:\temp\logme.txt")
