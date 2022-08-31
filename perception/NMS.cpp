#include<bits/stdc++.h>
using namespace std;
// 首先要搞清楚nms输入的东西是什么
// nms有三个输入 ，nms只需要三个输入
// boxs 二维数组 n*4  这里的4表示的是左上角坐标和右下角坐标
// scores 一维数组 n， 和boxes是对于的，表示这个box对于的检测score
// 一个变量 表示 阈值

// 返回值是一个 数组，里面是要选择的那些框的下标。

struct boxes_score_index
{
    /* data */
    vector<float> box;
    float score;
    int index;
};// 这里构造一个结构体，用于后面的排序，可以将box 还有index信息一起跟着 score进行排序

static bool cmp(boxes_score_index x, boxes_score_index y){
    return x.score> y.score;
} // 根据score的值进行排序

float iou(vector<float> box_x, vector<float> box_y){
    // x1,y1,x2,y2  
    float left_x_max=max(box_x[0], box_y[0]);
    float right_x_min=min(box_x[2], box_y[2]);

    float top_y_max=max(box_x[1], box_y[1]);
    float bottom_y_min=min(box_x[3], box_y[3]);

    float inter;
    if( right_x_min - left_x_max >0 && bottom_y_min- top_y_max >0){
        inter = (right_x_min- left_x_max)*(bottom_y_min- top_y_max);
    }else{
        inter = 0.0;
    }

    return inter/((box_x[2]-box_x[0])*(box_x[3]- box_x[1])+(box_y[2]- box_y[0])*(box_y[3]- box_y[1]));

} // 计算两个 box之间的iou

vector<int> nms(vector<vector<float> > boxes, vector<float> scores, float threshold){
    vector<int> res;
    vector<boxes_score_index> boxes_score_index_s;
    for(int i=0; i< boxes.size(); i++){
        boxes_score_index bsi;
        bsi.box= boxes[i];
        bsi.score=scores[i];
        bsi.index=i;
        boxes_score_index_s.push_back(bsi);
    }
    // 使用vector 构建一个 我们定义的结构体的数组
    sort(boxes_score_index_s.begin(), boxes_score_index_s.end());
    // 对数组进行排序
    while(!boxes_score_index_s.empty()){
        boxes_score_index first_one;
        first_one= boxes_score_index_s[0];
        res.push_back(first_one.index);  
        // 拿到第一个，因为第一个是score最大的，并把 数组的第一个 box的index 导入数组中。
        for(int i=1; i< boxes_score_index_s.size(); i++){
            boxes_score_index compared_one= boxes_score_index_s[i];
            float iou_value= iou(first_one.box, compared_one.box);
            if(iou_value> threshold){
                boxes_score_index_s.erase(boxes_score_index_s.begin()+i);
                i--;  // 这里的i-- 是为了在vector删除一个元素之后，回到上次的位置，不然就会跳过一些元素，导致nms出错。
            }
        }
        // for循环，遍历之后的每一个box，如果iou大于阈值就把它删除掉
    }
    return res;
}