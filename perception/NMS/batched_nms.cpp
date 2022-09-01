// 这个是针对多类别的nms
// 相比于 单类别的nms ， 这个多了一个信息，就是预测的类别 predict_class
// 四个信息：
// boxs 二维数组 n*4  这里的4表示的是左上角坐标和右下角坐标
// scores 一维数组 n， 和boxes是对应的，表示这个box对应的检测score
// 预测的类别 信息 predict_classes 一维数组 n， 和boxes是对应的，表示这个box对应的检测类别 是一个 0到 n-1的一个int类型整数
// 一个变量 表示 阈值
#include<bits/stdc++.h>
using namespace std;

// 第一步 找到 最大的 尺度   →  用于 offset
float find_max_x_or_y(vector<vector<float> > boxes){
    float max_x_or_y=-1;
    for(int i=0; boxes.size(); i++){
        for(int j=0; j<boxes[0].size(); j++){
            if(boxes[i][j]> max_x_or_y) max_x_or_y=boxes[i][j];
        }
    }
    return max_x_or_y;
}


// 第二步 使用 最大的尺度进行 偏移， 把那些不同类别的，相距比较近的框 偏移开
// 通过offset操作，现在的boxes就可以直接使用了，就可以直接调用 NMS.cpp 文件进行计算了
void offset_operator(vector<vector<float> > &boxes, vector<int> predict_classes, float max_x_or_y_){
    for(int i=0; i<boxes.size(); i++){
        int class_of_this_box = predict_classes[i];
        for(int j=0; j<boxes[0].size(); j++){
            boxes[i][j]= boxes[i][j]+ class_of_this_box* max_x_or_y_;
            // 这里的 max_x_or_y 是使用 原来的， 没有offset的时候的boxes列表计算得到的
        }
    }
}