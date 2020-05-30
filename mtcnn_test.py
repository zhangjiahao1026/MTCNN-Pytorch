import cv2
from mtcnn.core.detect import create_mtcnn_net, MtcnnDetector
from mtcnn.core.vision import vis_face




if __name__ == '__main__':
    #original model
    """ p_model_path = "./original_model/pnet_epoch.pt"
    r_model_path = "./original_model/rnet_epoch.pt"
    o_model_path = "./original_model/onet_epoch.pt" """
    #trained model
    p_model_path = "./original_model/pnet_epoch_train.pt"
    r_model_path = "./original_model/rnet_epoch_train.pt"
    o_model_path = "./original_model/onet_epoch_train.pt"
    pnet, rnet, onet = create_mtcnn_net(p_model_path=p_model_path, r_model_path=r_model_path, o_model_path=o_model_path, use_cuda=False)
    mtcnn_detector = MtcnnDetector(pnet=pnet, rnet=rnet, onet=onet, min_face_size=24,threshold=[0.6, 0.7, 0.7])

    img = cv2.imread("1.jpg")
    img_bg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    bboxs, landmarks = mtcnn_detector.detect_face(img)
    # print box_align
    save_name = 'r_1.jpg'
    vis_face(img_bg,bboxs,landmarks, save_name)
