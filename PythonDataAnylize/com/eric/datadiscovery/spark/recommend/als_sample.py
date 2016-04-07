# -*- coding:utf-8 -**

'''主要使用ALS方法来演示如何实现电影推荐系统'''
from pyspark import SparkContext
from pyspark.mllib.recommendation import ALS, MatrixFactorizationModel, Rating

__author__ = 'dell'


data_file = "/opt/talas/ml-100k/u.data"  # Should be some file on your system
sc = SparkContext("local", "RecommanderSystem")
row_data_rdd=sc.textFile(data_file)

def load_rating_data():
    rating_data=row_data_rdd.map(lambda x:x.split("\t")).\
        map(lambda raw_rating_data:Rating(raw_rating_data[0],raw_rating_data[1],raw_rating_data[2]))
    return rating_data


#对指定的用户进行电影推荐
def recommand_movies(user_id):
    rating_data=load_rating_data()
    #rating_model=ALS.train(rating_data,50,10,0.1)
    rating_model=ALS.train(rating_data,100,10,0.1)
    #预测特定用户对特定电影的评分
    moveid=123
    predict_result=rating_model.predict(user_id,moveid)
    print "预测用户：%s 对电影: %s  的评测分数是：%s" %(user_id,moveid,predict_result)
    #为789用户推荐10个商品
    recommand_result=rating_model.recommendProducts(user_id,10)
    return recommand_result


def compare_recommand_result_bymanual(recommand_result,user_id):
    rating_data=load_rating_data()
    #按照用户进行分组，并返回指定用户的Rating对象列表
    user_ralated_movies=rating_data.keyBy(lambda x:x[0]).lookup(str(user_id))
    #对结果按照movie进行排序
    user_ralated_movies.sort(key=lambda rat:rat[2],reverse=True)
    index=1
    for recommand_info,actual_info in zip(recommand_result,user_ralated_movies[0:10]):
        print "%d  推荐电影ID:%s  预计评分：%s   实际电影ID:%s  实际评分：%s" %(index,recommand_info[1],recommand_info[2],actual_info[1],actual_info[2])
        index+=1

if __name__ == '__main__':
    user_id=789
    #获取指定用户的推荐电影
    recommand_result=recommand_movies(user_id)

    #人工比较推荐的结果
    compare_recommand_result_bymanual(recommand_result,user_id);

