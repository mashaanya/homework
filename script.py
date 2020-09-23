# homework
import argparse
import os
st = os.getcwd()
stinfo=os.stat('/Users/admin/PycharmProjects/pythonProject/hf.py')
parser=argparse.ArgumentParser()
'''
in command line you should require only '-i (something)' and you will get everything that you want
or you can input 'python name of the directory' enter
sorry, i don't understand how to get name of the file i think my code is wrong but it works somehow)) and i don't grasp how to remane, because of don't know the name of the file and i have problems with arguments in command line 
'''
parser.add_argument("-i","--information",help='information you want to get')
parser.add_argument("-f","--filename",default=os.path,nargs=1,help="file name")
parser.add_argument('-m','--mtime',default=os.path.getmtime(st),nargs=1,help="This is modification time")
parser.add_argument('-s','--size',default=stinfo.st_size,nargs=1,help='This is the size of the file')
#parser.add_argument('-r','--rename',default=os.renames(st,input()),help='this rename your file')
args=parser.parse_args()
filename=args.filename
mtime=args.mtime
size=args.size
#rename=args.rename
print(filename)
print(mtime)
print(size)
#print(rename)
