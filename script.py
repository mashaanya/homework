# homework
import argparse
import os,time
st = os.getcwd()
stinfo = os.stat('/Users/admin/PycharmProjects/pythonProject/hf.py')
parser=argparse.ArgumentParser()
#parser.add_argument("-i","--information",action='store_true',help='information you want to get')
parser.add_argument("-f","--filename",action='store_true',help="file name")
parser.add_argument('-m','--mtime',action='store_true',help="This is modification time")
parser.add_argument('-s','--size',action='store_true',help='This is the size of the file')
parser.add_argument('-r','--rename',action='store_true',help='this rename your file')
args=parser.parse_args()
filename=args.filename
mtime=args.mtime
size=args.size
rename=args.rename
if mtime:

    ti=time.ctime(stinfo.st_mtime)
    print('The last modofication time is ', ti)
if size:
    s=os.path.getsize('/Users/admin/PycharmProjects/pythonProject/hf.py')
    print('The size of the file is', s/(2**10))
if filename:
    print('The file is','/Users/admin/PycharmProjects/pythonProject/hf.py')
if rename:
    os.rename('/Users/admin/PycharmProjects/pythonProject/hf.py', '/Users/admin/PycharmProjects/pythonProject/new_name.py ')
    print('Your filename has changed ')
'''
upper code renames your file into new_name.
If you want to rename it into what you input after -r in command line you can check the following code, which is the same in other parts:

import argparse
import os,time
st = os.getcwd()
stinfo = os.stat('/Users/admin/PycharmProjects/pythonProject/hf.py')
parser=argparse.ArgumentParser()
#parser.add_argument("-i","--information",action='store_true',help='information you want to get')
parser.add_argument("-f","--filename",action='store_true',help="file name")
parser.add_argument('-m','--mtime',action='store_true',help="This is modification time")
parser.add_argument('-s','--size',action='store_true',help='This is the size of the file')
parser.add_argument('-r','--rename',default='B',help='this rename your file')
args=parser.parse_args()
filename=args.filename
mtime=args.mtime
size=args.size
rename=args.rename
if mtime:

    ti=time.ctime(stinfo.st_mtime)
    print('The last modofication time is ', ti)
if size:
    s=os.path.getsize('/Users/admin/PycharmProjects/pythonProject/hf.py')
    print('The size of the file is', s/(2**10))
if filename:
    print('The file is','/Users/admin/PycharmProjects/pythonProject/hf.py')
if rename:
    os.rename('/Users/admin/PycharmProjects/pythonProject/hf.py', rename)
    print('Your filename has changed ')
'''



