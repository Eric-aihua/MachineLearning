# encoding:utf-8
import os
import numpy as np
import PIL.Image as Image
import matplotlib.pyplot as plt
"""模拟一个完整的人脸识别系统"""
test_face_dir='/home/eric/sourcecode/MachineLearning/PythonDataAnylize/testdata/face_detection/att_faces'
test_face_paths=['%s/s10/7.pgm'%(test_face_dir),'%s/s10/6.pgm'%(test_face_dir),'%s/s22/1.pgm'%(test_face_dir),'%s/s18/5.pgm'%(test_face_dir),'%s/s16/3.pgm'%(test_face_dir),'%s/s12/1.pgm'%(test_face_dir)]
face_datasource_path=test_face_dir

# 定义脸部识别功能类
class FaceDetection(object):
    
    def __init__(self,train_path):
        self.eps=1.0e-16
        #特征值
        self.eig_v=0
        #特征向量
        self.eig_vect=0
        self.mu=0
        self.projections=[]
        self.dist_metrics=0
        self.path=train_path
        self.Mat=[]
        self.X=[]
        self.Y=[]
        
    
    #加载测试图片，将图片数据放到self.X中，将标签数据放到self.Y中
    def load_images(self):
        print 'start to loading face database images'
        classlabel=0
        for dirname,dirnames,filenames in os.walk(self.path):
            for subdir in dirnames:
                subdir_path=os.path.join(dirname,subdir)
                for subdir_file in os.listdir(subdir_path):
                    subdir_file_path=os.path.join(subdir_path,subdir_file)
                    img=Image.open(subdir_file_path)
                    long_img=img.convert('L')
                    self.X.append(np.asarray(long_img,dtype=np.float64))
                    self.Y.append(subdir)
                classlabel+=1
        print self.Y
    
    #将图片的数据放入到一个由行向量构成的集成
    def gen_row_matrix(self):
        print 'start converting images to matrix'
        self.Mat=np.empty((0,self.X[0].size),dtype=self.X[0].dtype)
        for row in self.X:
            self.Mat=np.vstack((self.Mat,np.asarray(row).reshape(1,-1)))
    
    #图片库数据的PCA转换，并计算出特征向量和均值
    def pca(self,k=3):
        [n,d]=np.shape(self.Mat)
        if k>n:k=n
        self.mu=self.Mat.mean(axis=0)
        # 进行零均值话，减去平均值
        self.Mat-=self.mu
        # 计算协方差矩阵,以及算出特征值与特征向量
        if n>d:
            XTX=np.dot(self.Mat.T,self.Mat)
            [self.eig_v,self.eig_vect]=np.linglg.eig(XTX)
        else:
            XTX=np.dot(self.Mat,self.Mat.T)
            [self.eig_v,self.eig_vect]=np.linalg.eig(XTX)
        self.eig_vect=np.dot(self.Mat.T,self.eig_vect)
        for i in range(n):
            self.eig_vect[:,i]=self.eig_vect[:,i]/np.linalg.norm(self.eig_vect[:,i])
        # 将特征向量按照特征值大小进行从上倒下排列，取前K个
        idx=np.argsort(-self.eig_v)
        self.eig_v=self.eig_v[idx]
        self.eig_vect=self.eig_vect[:,idx]
        self.eig_v=self.eig_v[0:k].copy()
        self.eig_vect=self.eig_vect[:,0:k].copy()

        
    #对所有的图片进行投影操作
    def compute(self):
        print 'start executing pca compute'
        for xi in self.X:
            self.projections.append(self.project(xi.reshape(1,-1)))
        
    
    #投影
    def project(self,xi):
        if self.mu is None:return np.dot(xi,self.eig_vect)
        return np.dot(xi-self.mu,self.eig_vect)
    
    #欧式距离
    def distEclud(self,vecA,vecB):
        return np.linalg.norm(vecA-vecB)+self.eps
    #余旋距离
    def comSim(self,vecA,vecB):
        return (np.dot(vecA,vecB.T)/((np.linalg.norm(vecA)*np.linalg.norm(vecB))+self.eps))[0,0]
    
    
    
    def train(self):
        print 'start to trainging face database'
        self.load_images()
        self.gen_row_matrix()
        self.pca()
        self.compute()
        
    # 列出每个分类的平均脸
    def subplot(self,title,images):
        fig=plt.figure()
        fig.text(.5,.95,title,horizontalalignment='center')
        for i in xrange(len(images)):
            ax0=fig.add_subplot(4,4,(i+1))
            plt.imshow(np.asarray(images[i]),cmap='gray')
            #隐藏坐标
            plt.xticks([]),plt.yticks([])
        plt.show()       
        
    # 根据路径生成矩阵对象
    def generate_matrix_obj_by_path(self,test_img_path):
        img=Image.open(test_img_path)
        long_img=img.convert('L')
        return np.asarray(long_img,dtype=np.float64)
                    
            
    #对目标图片进行预测
    def predict(self,test_img_path):
                
        img=self.generate_matrix_obj_by_path(test_img_path)
        
        print 'start predicting......'
        min_dist=np.finfo('float').max
        min_class=-1
        #计算预测图片的投影
        Q=self.project(img.reshape(1,-1))
        for i in xrange(len(self.projections)):
            dist=self.dist_metric(self.projections[i],Q)
            if dist<min_dist:
                min_dist=dist
                min_class=self.Y[i]
        print 'actualy image is:%s predict result is:%s' %(test_img_path,min_class)
        
       

def face_detection():
    fd=FaceDetection(face_datasource_path)
    # 指定相似性比较算法
    fd.dist_metric=fd.distEclud
    fd.train()
    E=[]
    X=np.mat(np.zeros((10,10304)))
    #预览16个人脸库的数据
    for i in xrange(16):
        # 每种脸包含10张图片
        X=fd.Mat[i*10:(i+1)*10,:].copy()
        #生成平均脸
        X=X.mean(axis=0)
        imgs=X.reshape(112,92)
        E.append(imgs)    
    #fd.subplot('AT$T Face Database!',images=E)
    for test_face_path in test_face_paths:
        fd.predict(test_face_path)
    


if __name__ =='__main__':
    face_detection()

