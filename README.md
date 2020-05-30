# Instructions
MTCNN is a face detection model

The Chinese introduction can be found [here](https://blog.csdn.net/qq_32478489/article/details/106193921)

[paper](https://kpzhang93.github.io/MTCNN_face_detection_alignment/paper/spl.pdf)

Referring to [kuaikuaikim/DFace](https://github.com/kuaikuaikim/DFace) and [Sierkinhane/mtcnn-pytorch](https://github.com/Sierkinhane/mtcnn-pytorch), I fixed some bugs that would appear in the training, added the table of learning rate, and optimized the training parameters.Testing on the WiderFace validation set, I found it performance better than the model weight they had originally provided.
#### Test image
![测试图](https://img-blog.csdnimg.cn/20200518164255263.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMyNDc4NDg5,size_16,color_FFFFFF,t_70#pic_center)
# WiderFace Val Performance in MTCNN
MTCNN-original is the test result of the original weight parameter
MTCNN-trained is the test result of my training

| Style | easy | medium | hard |
|:-|:-:|:-:|:-:|
| MTCNN-original | 65.3% | 65.1% | 40.3% |
| MTCNN-trained | **71.4%** | **70.4%** | **43.2%** |

![Easy](https://img-blog.csdnimg.cn/20200518154123825.JPG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMyNDc4NDg5,size_16,color_FFFFFF,t_70)

![medium](https://img-blog.csdnimg.cn/20200518154123819.JPG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMyNDc4NDg5,size_16,color_FFFFFF,t_70)

![hard](https://img-blog.csdnimg.cn/20200518154123812.JPG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzMyNDc4NDg5,size_16,color_FFFFFF,t_70)


# Installation
1.pytorch 
2.opencv 
# test
### a single picture
Modify the image path in the program

```Shell
python detect.py
```
# Train the model
download [widerface](http://shuoyang1213.me/WIDERFACE/)
Organise the dataset directory as follows:
```Shell
  ./data_set/face_detection/
    WIDER_train/
      images/
    WIDER_val/
      images/
```
I have made the label file
```Shell
./anno_store/anno_train.txt
```
If you want to make your own labels
The reference program
./anno_store/tool/change.py

### train pnet
**prepare pnet data**
```Shell
python mtcnn/data_preprocessing/gen_Pnet_train_data.py
python mtcnn/data_preprocessing/assemble_pnet_imglist.py
```
**train pnet**
```Shell
python mtcnn/train_net/train_p_net.py
```
**prepare rnet data**
```Shell
python mtcnn/data_preprocessing/gen_Rnet_train_data.py
python mtcnn/data_preprocessing/assemble_rnet_imglist.py
```
**train rnet**
```Shell
python mtcnn/train_net/train_r_net.py
```
**prepare onet data**
```Shell
python mtcnn/data_preprocessing/gen_Onet_train_data.py
python mtcnn/data_preprocessing/assemble_onet_imglist.py
```
**prepare onet**
```Shell
python mtcnn/train_net/train_o_net.py
```
# Evaluation widerface val
```Shell
python wildface_test.py
```
# References

[kuaikuaikim/DFace](https://github.com/kuaikuaikim/DFace)

[Sierkinhane/mtcnn-pytorch](https://github.com/Sierkinhane/mtcnn-pytorch)
