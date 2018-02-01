#!/usr/bin/env python

import sys, os

oldstr = "yujin"
newstr = "vking"
Oldstr = "Yujin"
Newstr = "Vking"
OLDSTR = "YUJIN"
NEWSTR = "VKING" 

def lister(root):                                           # for a root dir
    if not os.path.isdir(root):
        print(root,"is not directory!")
        sys.exit(-1)
#    print("test")
#    sys.exit(0)
    if oldstr in root:
        newroot = root.replace(oldstr,newstr)
        os.rename(root,newroot) 
    else:
        newroot = root
    for (thisdir, subshere, fileshere) in os.walk(newroot):    
        if "/." in thisdir:
            continue
        print('[' + thisdir + ']')
        if oldstr in thisdir:
            newthisdir = thisdir.replace(oldstr,newstr)
            os.rename(thisdir,newthisdir) 
            print('[new' + newthisdir + ']')
            thisdir = newthisdir    #have a bug: if rename the directory,os.walk cann't execute full,must run more times
            #lister(thisdir)
        for fname in fileshere:                             
            if fname.startswith('.'):
                continue
            path = os.path.join(thisdir, fname)                                  
            print('****'+path)
            if oldstr in fname:
                newpath = path.replace(oldstr,newstr)
                os.rename(path,newpath)
                print('&&&&'+newpath)
                path = newpath
            if os.path.exists(path):
                with open(path,'r+') as f:
                    t = f.read()
                    t = t.replace(oldstr,newstr)
                    t = t.replace(Oldstr,Newstr)
                    t = t.replace(OLDSTR,NEWSTR)
                    f.seek(0, 0)    
                    f.truncate()
                    f.write(t)

if __name__ == '__main__':
    lister(sys.argv[1])                                                          
