#! /usr/bin/python

"""Quick backups made easy.
   You can configure this script (lines 19, 22) to backup files so that a copy of the file with date and time as yyyymmddHHMM is appended to the file name.
   The script uses Tkinter to build a user interface. When you execute this script, you can select files you want to backup from a list box.
"""

import time
import shutil
import string
from Tkinter import *
import tkMessageBox

######################################################
####### do not change anything above this line #######
####### everything you need to change in the following two statements ######

# list of full paths to the files you want to backup (e.g.: ['C:/myfolder/myfile.xls', 'C:/myfolder2/mydocument.doc'] )
files = ['E:/00_thesis/docu.doc', 'E:/00_thesis/data/mydata.csv']

# full path to the folder you want to copy to (e.g.: 'D:/backup/')
outpath = 'G:/backup/thesis/'

####### do not change anything below this line #######
#######################################################

def Backup_sel():
    sel = []
    for i in lst.curselection():
        sel.append(lst.get(i))
    t = time.strftime('%x')[:-2] + time.strftime('%X')
    t = t.replace('/','')
    t = t.replace(':','')
    t = t[:-2]
    p = []
    for i in sel:
        p.append(data[1][data[0].index(i)])
    for i in range(len(sel)):
        f = sel[i]
        lblStatus['text'] = f
        inx = string.find(f, '.')
        bckup_name = f[:inx] + '_' + t + f[inx:]
        shutil.copy(p[i], outpath + bckup_name) 
        #tkMessageBox.showinfo("Backup", "backup of: " + p[i] + " as: " + outpath + bckup_name)
    lblStatus['text'] = "Done."

def Backup_all():
    t = time.strftime('%x')[:-2] + time.strftime('%X')
    t = t.replace('/','')
    t = t.replace(':','')
    t = t[:-2]
    for i in files:
        f = i.split("/")[-1]
        inx = string.find(f, '.')
        bckup_name = f[:inx] + '_' + t + f[inx:]
        shutil.copy2(i, outpath + bckup_name)
        #tkMessageBox.showinfo("Backup", "backup of: " + i + " as: " + outpath + bckup_name)

root = Tk()

lbl = Label(root, text="Choose file(s) to backup:")
lst = Listbox(root, width=30, selectmode='multiple')
btnBck = Button(root, text="Backup Selected", command=Backup_sel)
btnBckAll = Button(root, text="Backup All", command=Backup_all)
lblStatus = Label(root, text="", fg='blue')

lbl.grid(row=0, column=0, columnspan=2)
lst.grid(row=1, column=0, columnspan=2)
btnBck.grid(row=2, column=0, pady=5, padx=5, sticky=W)
btnBckAll.grid(row=2, column=1, pady=5, padx=5, sticky=E)
lblStatus.grid(row=3, column=0, columnspan=2)

names = []
for i in files:
    name = i.split("/")[-1]
    names.append(name)
    lst.insert(END, name)

data = [names, files]

root.mainloop()
