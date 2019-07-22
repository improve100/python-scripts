#!/usr/bin/env python

import sys, os

oldstr = "robot_localization"
newstr = "msf_localization"
Oldstr = "RobotLocalization"
Newstr = "MSFLocalization"
OLDSTR = "ROBOT_LOCALIZATION"
NEWSTR = "MSF_LOCALIZATION" 

replace_dir_count = 0

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
	    replace_dir_count = replace_dir_count + 1
        #else:
	#    replace_dir_count = False
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
		    if t.find("#include") != -1:
			if t.find("#ifndef") != -1:
			    if t.find("#include") > t.find("#ifndef"):
				t = t[t.find("#ifndef"):]
			    else:
				t = t[t.find("#include"):]
			else:
			    t = t[t.find("#include"):]
		    elif t.find("#ifndef") != -1:
			t = t[t.find("#ifndef"):]
                    f.seek(0, 0)    
                    f.truncate()
                    f.write(t)

if __name__ == '__main__':
    lister(sys.argv[1])  
    while replace_dir_count:
	lister(newroot)  
	replace_dir_count = replace_dir_count - 1
    print("complete done,have fun")                                                      
