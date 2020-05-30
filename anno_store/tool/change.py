import os
class wider_change():
    def __init__(self,path,out_path):
        self.path=path
        self.opath=out_path
    def create_ann(self):
        with open(self.path,'r') as f:
            linelist = f.readlines()

        out_f = open(self.opath,'w')
        ind=0
        Nlines=len(linelist)
        while ind<Nlines:
            if linelist[ind][2]=='-':
                buf=linelist[ind][:-1]
                ind+=1
                N = int(linelist[ind])
                ind+=1
                for _ in range(N):
                    bbox = list(map(int,linelist[ind].split()[:4]))
                    bbox = [bbox[0],bbox[1],bbox[0]+bbox[2],bbox[1]+bbox[3]]
                    bbox = list(map(str,bbox))
                    buf+=(' '+' '.join(bbox))
                    ind+=1
                out_f.write(buf+'\n')
            else:
                ind+=1
        out_f.close()
                

path = 'wider_face_train_bbx_gt.txt'
out_path = 'anno_train.txt'
widerc=wider_change(path,out_path)
widerc.create_ann()