import cv2
from mtcnn.core.detect import create_mtcnn_net, MtcnnDetector
from mtcnn.core.vision import vis_face
import os
import numpy as np
class wildtest():
    def __init__(self,image_dir,result_dir,p_net_m,r_net_m,o_net_m):
        self.image_dir=image_dir
        self.result_dir=result_dir
        self.p_net_m = p_net_m
        self.r_net_m = r_net_m
        self.o_net_m = o_net_m
    def detect(self):
        pnet, rnet, onet = create_mtcnn_net(p_model_path=self.p_net_m, r_model_path=self.r_net_m, o_model_path=self.o_net_m, use_cuda=True)
        mtcnn_detector = MtcnnDetector(pnet=pnet, rnet=rnet, onet=onet, min_face_size=24,threshold=[0.1,0.1,0.1])

        event_list = os.listdir(self.image_dir)
        for event in event_list:
            print(event)
            event_dir = os.path.join(self.image_dir,event)
            res_dir = os.path.join(self.result_dir,event)
            if not os.path.exists(res_dir):
                os.makedirs(res_dir)
            images_list = os.listdir(event_dir)
            for images in images_list:
                images_path = os.path.join(event_dir,images)
                img = cv2.imread(images_path)
                bboxs,landmarks = mtcnn_detector.detect_face(img)
                if bboxs.shape[0]!=0:
                    bboxs[:,2]=bboxs[:,2]-bboxs[:,0]
                    bboxs[:,3]=bboxs[:,3]-bboxs[:,1]
                    bboxs[:,:4] = np.round(bboxs[:,:4])
                """ print(bboxs)
                save_name = 'r_304.jpg'
                vis_face(img,bboxs,landmarks, save_name) """
                fpath = os.path.join(res_dir,images[:-4]+'.txt')
                f = open(fpath,'w')
                f.write(images[:-4]+'\n')
                f.write(str(bboxs.shape[0])+'\n')
                for i in range(bboxs.shape[0]):
                    f.write('{:.0f} {:.0f} {:.0f} {:.0f} {:.3f}\n'.format(bboxs[i,0],bboxs[i,1],bboxs[i,2],bboxs[i,3],bboxs[i,4]))
                f.close()
                
image_dir = './data_set/face_detection/WIDER_train/images/'
result_dir = './anno_store/wider_val/'
p_net_m = './original_model/pnet_epoch_train.pt'
r_net_m = './original_model/rnet_epoch_train.pt'
o_net_m = './original_model/onet_epoch_train.pt'
wildtest = wildtest(image_dir,result_dir,p_net_m,r_net_m,o_net_m)
wildtest.detect()