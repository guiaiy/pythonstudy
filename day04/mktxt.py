import os

def get_fname():
    fname=input('please input a file name: ')
    while os.path.exists('/tmp/'+fname):
        print('file existed,put input again')
        fname=input()
    return fname

def get_content():
    content=[]
    print('plesase input content,print "end" to exit')
    while True:
        line=input('> ')
        if line=='end':
            break
        content.append(line)
    return content

def wfile(fname,content):
    with open('/tmp/'+fname,'w') as f1:
        for line in content:
            f1.write(line+'\n')



if __name__ == '__main__':
    fname=get_fname()
    content=get_content()
    wfile(fname,content)