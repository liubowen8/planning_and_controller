"""
Polygon 是一个对计算iou非常有用的class，可以完成多边形和多边形重叠面积的计算
"""
from shapely.geometry import Polygon

juxinga= [[0,0],[0,2],[2,2],[2,0],[0,0]]
A=Polygon(juxinga)
print(A.area)

juxingb= [[1,1],[1,3],[3,3],[3,1]]
B=Polygon(juxingb)
print(B.area)

print(A.intersection(B)) 
# POLYGON ((1 2, 2 2, 2 1, 1 1, 1 2))  A.intersection(B) 还是一个Polygon对象
# 2d IOU 的计算：
inter = A.intersection(B).area
unionx= A.area + B.area - inter
iou = inter / unionx
print(iou)
"""
3D IOU的计算，3D IOU 按道理来说 bounding box可能不是水平的
如果不是水平的不好计算，所以这里相当于是简单化处理了，
现在我们有八角的3d坐标，上面的四个角，可以通过计算均值，得到一个高度，
下面的四个角，同样可以通过计算均值，得到一个高度，
而上面 和 下面的矩形，直接使用x，z的坐标  → 这相当于完成了一个投影操作，最后处理的bounding box都是水平的
"""
# 计算得到高度的overlap， 
heightoverlap= .0 # 计算得到高度上的overlap
Aheight=.0  
Bheight=.0
inter = A.intersection(B).area # A ，B分别是2个 3d bounding box的上面的矩形，这样就得到了一个相交的Polygon
inter_tiji = inter * heightoverlap
union_tiji = A.area * Aheight + B.area*Bheight - inter_tiji
IOU3d = inter_tiji / union_tiji