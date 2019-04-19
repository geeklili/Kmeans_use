# -*- coding: utf-8 -*-
import json
from collections import defaultdict
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans


def km():
    """文件为一个大的字典类型，字典的key是实体，值是其向量"""
    # with open('./data/pca_vector_dict.txt', encoding='utf-8') as f:
    with open('./data/entity_vec.json', encoding='utf-8') as f:
        content_di = json.loads(f.read())
        # print(content_di)
        li_key = list()
        li_vec = list()

        for a, b in content_di.items():
            li_key.append(a)
            li_vec.append(b)
        li_key = np.array(li_key)
        li_vec = np.array(li_vec)
        kmeans_model = KMeans(n_clusters=100, max_iter=300000).fit(li_vec)
        ret = dict(zip(li_key, kmeans_model.predict(li_vec)))

        new_di = defaultdict(list)
        for c, d in ret.items():
            new_di[d].append(c)

        li = list()
        for e, g in new_di.items():
            print(e)
            print(g)
            li.append(g)
        data = pd.DataFrame(li)
        print(data)
        data.to_excel('./data/entity_cluster_100.xlsx')


if __name__ == '__main__':
    km()
