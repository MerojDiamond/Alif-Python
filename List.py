class List:
    content={}
    file=""
    sum=0
    def __init__(self,file):
        self.file=file
        content=open("list.txt").readlines()
        for v in content:
            if not v:
                continue
            line=v.split('-')
            self.content[line[0].strip()]=int(line[1].strip())
    def add_update(self):
        content = open(self.file).readlines()
        for v in content:
            if not v:
                continue
            line = v.split('-')
            self.content[line[0].strip()] = int(line[1].strip())
        self.file_update()
    def delete(self):
        content = open(self.file).readlines()
        for v in content:
            if not v:
                continue
            line=v
            try:
                line=v.split('-')[0]
            except:
                pass
            self.content.pop(line)
        self.file_update()
    def summ(self):
        content = open("list.txt").readlines()
        for v in content:
            if not v:
                continue
            line = v.split('-')
            self.sum += int(line[1].strip())
    def get_list(self):
        return self.content
    def get_summ(self):
        return self.sum
    def file_update(self):
        content=""
        keys=list(self.content)
        for i in range(len(keys)):
            content+=str(keys[i])+'-'+str(self.content[keys[i]])+'\n'
        open("list.txt","w").write(content)