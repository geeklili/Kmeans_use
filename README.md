# Kmeans_use
一个kmeans使用的小例子

### sklearn k-means聚类实用封装库

用法：
* 传入的参数均为list类型，x1为x坐标，x2为y坐标，
* types_num为聚类数，
* types为各类的名称,
* colors为各类点的颜色，
* shapes为各类点的形状
* 返回一个kmeans_model对象，其labels_属性记录着聚类的标签（如0，1，2等），
* cluster_centers_属性记录着聚类的中心
* 另外也返回聚类后的x1_result和x2_result对象，
* x1_result记录着原x1列表的聚类结果，

* 即x1_result列表中有n个元素（n为聚类数），其中每个元素都是一个列表（原x1列表中属于该类的所有元素组成的列表）

* x2_result同上
