from cProfile import label
import numpy as np
import matplotlib.pyplot as plt

def PR(y_test, pred_y): # pred
    # pred_y 为softmax
    # 转为标签
    preds_t = np.array(pred_y).argmax(axis=1)  # 得到预测的结果
   
    a = np.array(pred_y)
    a = np.around(a, 3)
    thresholds = set(a.reshape(-1))  # 这里是得到所有的得到，reshape(-1)的意思就是将矩阵拉平为 一维向量，set去重
    thresholds = sorted(thresholds)  # 记录所有得分情况，并去重从小到大排序，寻找各个阈值点

    macro_precis = []
    macro_recall = []
    for threshold in thresholds:
        cls_n = pred_y[0].shape[0]
        true_p = [0 for _ in range(cls_n)]
        true_n = [0 for _ in range(cls_n)]
        false_p = [0 for _ in range(cls_n)]
        false_n = [0 for _ in range(cls_n)]

        for j in range(y_test.shape[0]):
            # cls, pd, [n0, n1, n2] = file.strip().split(" ")       # 分别计算比较各个类别的得分，分开计算，各自为二分类，
            # 最后求平均，得出宏pr

            cls, pd = y_test[j], preds_t[j]  # 最后求平均，得出宏pr
            n = pred_y[j]
            print(n)
            print(j)

            for c in range(len(n)):  ## 循环类别
                # 遍历所有样本，第0类为正样本,，其他类为负样本,
                if float(n[c]) >= float(threshold) and int(cls) == c: # 大于等于阈值，并且真实为正样本，即为真阳，
                    true_p[c] += 1
                elif float(n[c]) >= float(threshold) and int(cls) != c:  # 大于等于阈值，真实为负样本，即为假阳；
                    false_p[c] += 1
                elif float(n[c]) < float(threshold) and int(cls) == c:# 小于阈值，真实为正样本，即为假阴
                    false_n[c] += 1

        precsions = []
        # 计算各类别的精确率，小数防止分母为0
        for k in range(cls_n):
            precsion = (true_p[k] + 0.00000000001) / (true_p[k] + false_p[k] + 0.00000000001)
            precsions.append(precsion)

        # 计算各类别的召回率，小数防止分母为0
        recalls = []
        for k in range(cls_n):
            recall = (true_p[k] + 0.00000000001) / (true_p[k] + false_n[k] + 0.00000000001)
            recalls.append(recall)

        precision1 = sum(precsions) / cls_n
        recall = sum(recalls) / cls_n  # 多分类求得平均精确度和平均召回率，即宏macro_pr
        macro_precis.append(precision1)
        macro_recall.append(recall)

    macro_precis.append(1)
    macro_recall.append(0)
    print(macro_precis)
    print(macro_recall)

    x = np.array(macro_recall)
    y = np.array(macro_precis)
    plt.figure()
    plt.xlim([-0.01, 1.01])
    plt.ylim([-0.01, 1.01])
    plt.xlabel('recall')
    plt.ylabel('precision')
    plt.title('PR curve')
    plt.plot(x, y)
    # plt.show()


predict = [[0.2, 0.3, 0.5], [0.1, 0.8, 0.1], [0.25, 0.5, 0.25],[0.9,0.05,0.05]]
predict = np.array(predict)
label = [1,1,0]
label = np.array(label)

PR(label, predict)