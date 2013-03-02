#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        harvest_browsemes
# Purpose:     Search for specified files (called BROWSEME.html by default) in a directory tree and retrieve content of html tag specified id (id="browseme" by default) into a specified output text file.
#
# Author:      filipkral
#
# Created:     27/02/2013
# Copyright:   no copyright, but I'd be glad if you mention that you used code written by Filip Kral (www.filipkral.com)
# Licence:     Public Domain. The author is not responsible and cannot be held resposnible for any demage caused by using this code.
#-------------------------------------------------------------------------------

import os, sys
from HTMLParser import HTMLParser

class LocalHTMLParser(HTMLParser):
    """Purpose built HTMLParser designed to find content of a tags with id equal to strings in keyidtags list (browsme and browsemetoo by default). When the html feed contains more than one tag with the same id, only the content of the last one will be retrieved!
    Instantiate object of this class, call the .feed method and then call .getdata to retrieve what the parser encountered.
    Case is ignored when searching for is that match keyidtags.
    Currently, if the tag you want to retrieve content for contains inner tags, only the part before the first inner tag will be retrieved.
    The get data method returns content of tags sorted according to the order of names in keyidtags
    """

    def __init__(self, keyidtags=['browseme', 'browsemetoo']):
        HTMLParser.__init__(self)
        self.keyidtags = map(str.lower, map(str, keyidtags))
        self.keyidtagfound = False
        self.datafound = {}

    def handle_starttag(self, tag, attrs):
        if self.keyidtagfound == False:
            if attrs != []:
                for key, value in attrs:
                    if str(key).lower() == 'id' and str(value).lower() in self.keyidtags:
                        self.keyidtagfound = str(value).lower()
                        break
        return

    def handle_endtag(self, tag):
        if self.keyidtagfound != False:
            self.keyidtagfound = False
        return

    def handle_data(self, data):
        if self.keyidtagfound != False:
            self.datafound.update({str(self.keyidtagfound):str(data)})
            self.keyidtagfound = False

    def getdata(self, separator='\t'):
        giveout = []
        for k in self.keyidtags:
            if k in self.datafound.keys():
                giveout.append(self.datafound[k])
            else:
                giveout.append('')
        return str(separator).join(giveout)


def main(top, outputfilepath, readmefilename='BROWSEME.html', keytagids=['browseme', 'browsemetoo'], outputsep='\t', ignore_case=True):
    """Walk through a folder structure under folder top and retrieve content of files called readmename into a text file outputfilepath
    top: root folder to start listing files in
    outputfilepath: path to the text file to store outputs in, will be open in 'w' mode(!)
    readmefilename: name of the files to look for
    keytagsids: list of names of id tags to look for
    outputsep: separator to be used in the output file
    ignore_case: if True, case will be ignored when looking for files called as readmefilename
    """
    try:
        parser = LocalHTMLParser(keyidtags=keytagids)

        ofile = open(outputfilepath, 'w')
        content = ''

        # walk through folders
        for (adirpath, dirnames, filenames) in os.walk(top=top):
            for fname in filenames:

                # check if the file is the kind of file that should be handled
                pickit = False
                if ignore_case:
                    pickit = (fname).lower() == str(readmefilename).lower()
                else:
                    pickit = str(fname) == str(readmefilename)

                # deal with the file
                if pickit:
                    try:
                        fpath = os.path.join(str(adirpath), str(fname))
                        rf = open(fpath, 'r')
                        content = rf.read()
                        parser.feed(content)
                        content = parser.getdata()
                        ofile.write(os.path.realpath(fpath) + outputsep + str(content).replace('\n', '').replace('\r', '') + '\n')
                    except Exception, ex:
                        ofile.write(fpath + outputsep + str(ex))
                    finally:
                        if 'rf' in dir():
                            if not rf.closed:
                                rf.close()
    except Exception, e:
        print e
    finally:
        if 'ofile' in dir():
            ofile.close()

if __name__ == '__main__':

    ### example use: ###
    #
    # call with minimal parameters
    #main(top=r'D:\programming', outputfilepath=r'D:\programming\readsum.txt')
    # call with full parameters
    #main(top=r'D:\programming', outputfilepath=r'D:\programming\readsum.txt', readmefilename='BROWSEME.html', outputsep='\t', keytagids=['browseme', 'browsemetoo'], ignore_case=True)
    pass
