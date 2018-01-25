
import sys, os

oldstr = "kobuki"
newstr = "vking"


def lister(root):                                           # for a root dir
    for (thisdir, subshere, fileshere) in os.walk(root):    # generate dirs in tree
        if "/." in thisdir:
            continue
        print('[' + thisdir + ']')
        if 'kobuki' in thisdir:
            newthisdir = thisdir.replace('kobuki','vking')
            os.rename(thisdir,newthisdir) 
            print('[new' + newthisdir + ']')
            thisdir = newthisdir
        for fname in fileshere:                             # print files in this dir
            if fname.startswith('.'):
                continue
            path = os.path.join(thisdir, fname)             # add dir name prefix
            print('****'+path)
            if "kobuki" in fname:
                newpath = path.replace('kobuki','vking')
                os.rename(path,newpath)
                print('&&&&'+newpath)
                path = newpath
            if os.path.exists(path):
                with open(path,'r+') as f:
                    t = f.read()
                    t = t.replace('kobuki', 'vking')
                    t = t.replace('Kobuki', 'Vking')
                    t = t.replace('KOBUKI', 'VKING')
                    f.seek(0, 0)    
                    f.write(t)

if __name__ == '__main__':
    lister(sys.argv[1])                                     # dir name in cmdline
