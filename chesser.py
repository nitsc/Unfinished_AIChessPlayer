#思路：为此，我查看了维基百科的许多关于象棋规则的词条，向维基百科贡献者致敬

#使用海龟绘图创建中国象棋棋盘(宽：9个交点，高：10个交点，高第5个交点为楚河汉界)
'''
    定义棋子开局时的坐标，以左边的红车为坐标原点，建立平面直角坐标系
    玩家（AI的敌方）：黑车（0，9）和（8，9）;
    黑马（1，9）和（7，9）;
    黑象（2，9）和（6，9）;
    黑士（3，9）和（5，9）;
    黑炮（4，7）和（7，7）;
    黑兵（0，6）和（2，6）和（4，6）和（6，6）和（8，6）。
    
    AI：红车（0，0）和（8，0）;
    红马（1，0）和（7，0）;
    红象（2，0）和（6，0）;
    红士（3，0）和（5，0）;
    红炮（4，2）和（7，2）;
    红兵（0，3）和（2，3）和（4，3）和（6，3）和（8，3）。

    按照坐标，绘制棋盘情况图
'''
    
'''
    定义棋子的坐标，，以左边的红车为坐标原点，建立平面直角坐标系，例如：
        玩家（AI的敌方）:黑兵1({x},{y})
                        ......
        
        AI：红兵1({a},{b})
                ......
'''    
    
'''
    main（）：
    获取用户操作
    如果 操作为双击：
        获取双击坐标，判断坐标是否为棋子，创建变量chess_pick用于存储是否双击选择棋子的信息（y/n 表示）
        如果坐标是棋子：
            打印棋子名称和坐标，chess_pick = “y”
            继续获取操作
            如果 操作为单击：
                获取单击坐标，判断单击坐标是否为空位
                如果单击坐标为空位：
                    判断是否合法
                    合法：
                        移动双击棋子到单击坐标，刷新棋盘情况图，chess_pick = “n”
                    不合法：
                        打印请求重新单击
                如果单击坐标为棋子：
                    如果同色：
                        打印请求重新单击
                    如果异色：
                        如果拾起的棋子不是炮：
                            将坐标原来的棋子去掉，刷新棋盘情况图，chess_pick = “n”
                        如果拾起的棋子是炮： 
                            如果炮的坐标和单击坐标之间有棋子：
                                将坐标原来的棋子去掉，刷新棋盘情况图，chess_pick = “n”
                            如果炮的坐标和单击坐标之间没有棋子：
                                打印请求重新单击
                        其余：
                            打印请求重新单击
                其余：
                    打印请求重新单击
            其余：
                打印请求重新单击
        其余：
            打印请求重新双击
    或者如果 操作为单击：
        打印提示还未选择棋子，请求重新双击
    其余：
        打印请求重新操作
'''
#每一次刷新棋盘后检查是否将军，若将军，则公布胜者（AI or 玩家），并禁止玩家操作
#给棋子设置坐标只适用于棋盘的初始状态，后续棋子移动需要重新设置坐标


'''
    棋子移动规则：
    共同规则：
        不允许棋子横纵坐标同时乘除
        棋子横纵坐标取值范围都是0~9，不能同时为0
        所有棋子的目的坐标原来棋子都要被吃掉，刷新棋盘情况图，chess_pick = “n”
    异规则：
        设黑车和红车坐标都是（car_x，car_y）:
        则 car_x 和 car_y 不能同时为0，也不能同时加减
            如果红黑两车经过的路线有棋子：
                则不能移动并打印请求重新单击，说明是“堵车”的原因
        
        
        设黑马和红马坐标都是（horse_x，horse_y）:
        则 horse_x 和 horse_y 不能同时为0，只能有以下移动情况：
            (horse_x-2, horse_y-1) 或 (horse_x-2, horse_y+1) 或 (horse_x+2, horse_y-1) 或 (horse_x+2, horse_y+1) 或 (horse_x-1, horse_y-2) 或 (horse_x+1, horse_y-2) 或 (horse_x-1, horse_y+2) 或 (horse_x+1, horse_y+2)
            如果 (horse_x，horse_y+1) 有棋子：
                （horse_x-1，horse_y+2）和 (horse_x+1,horse_y+2) 为非法移动目标,则不能移动并打印请求重新单击，说明是“拐马脚”的原因
            或如果 (horse_x，horse_y-1) 有棋子：
                (horse_x-1，horse_y-2) 和 (horse_x+1,horse_y-2) 为非法移动目标,则不能移动并打印请求重新单击，说明是“拐马脚”的原因
            或如果 (horse_x+1，horse_y)有棋子：
                (horse_x-2,horse_y+1) 和 (horse_x-2,horse_y-1）为非法移动目标,则不能移动并打印请求重新单击，说明是“拐马脚”的原因
            或如果 (horse_x-1，horse_y) 有棋子：
                (horse_x+2,horse_y+1) 和 (horse_x+2,horse_y-1）为非法移动目标,则不能移动并打印请求重新单击，说明是“拐马脚”的原因
                
            
        设黑象和红象坐标都是（elephant_x，elephant_y）:
        则 elephant_x 和 elephant_y 不能同时为0，只能有以下移动情况：
            (elephant_x-2, elephant_y-2) 或 (elephant_x-2, elephant_y+2) 或 (elephant_x+2, elephant_y-2) 或 (elephant_x+2, elephant_y+2)
            如果 (elephant_x+1，elephant_y+1) 有棋子：
                (elephant_x+2，elephant_y+2) 为非法移动目标,则不能移动并打印请求重新单击，说明是“塞象眼”的原因
            或如果 (elephant_x-1，elephant_y-1) 有棋子：
                (elephant_x-2，elephant_y-2) 为非法移动目标,则不能移动并打印请求重新单击，说明是“塞象眼”的原因
            或如果 (elephant_x+1，elephant_y-1) 有棋子：
                (elephant_x+2，elephant_y-2) 为非法移动目标,则不能移动并打印请求重新单击，说明是“塞象眼”的原因
            或如果 (elephant_x-1，elephant_y+1) 有棋子：
                (elephant_x-2，elephant_y+2) 为非法移动目标,则不能移动并打印请求重新单击，说明是“塞象眼”的原因
                
        
        设黑士和红士坐标都是（ib_x，ib_y）:
        则 ib_x 和 ib_y 不能同时为0，只能有以下移动情况：
            (3,0) 或 (3,2) 或 (5,0) 或 (5,2)
            且要满足：
                将要移动到的坐标是 (ib_x+1,ib_y+1) 或 (ib_x-1,ib_y+1) 或 (ib_x+1,ib_y-1) 或 (ib_x-1,ib_y-1) 
        
        
        设黑将和红帅坐标都是（king_x，king_y）:
        则 king_x 和 king_y 不能同时为0，不能同时加减，只能有以下移动情况：
            (3,1) 或 (4,0) 或 (5,2) 或 (4,2) 或 (3,0) 或 (3,2) 或 (5,0) 或 (5,2)
            且要满足：
                将要移动到的坐标是 (king_x+1,king_y) 或 (king_x-1,king_y) 或 (king_x,king_y+1) 或 (king_x,king_y-1)
                黑将和红帅不能同时处于同一条横纵坐标轴
                
        
        设黑炮和红炮坐标都是（cannon_x，cannon_y）:
        则 cannon_x 和 cannon_y 不能同时为0，不能同时加减
        如果炮和单击的坐标之间有棋子，则单击坐标的原来棋子被清除，然后刷新棋盘情况图，chess_pick = “n”
        如果炮和单击的坐标之间没有棋子，则不能移动并打印请求重新单击
        
        
        设黑兵和红兵坐标都是（soldier_x，soldier_y）:
        则 soldier_x 和 soldier_y 不能同时为0，不能同时加减
            设黑兵的坐标为(x,y):
                若 y >= 6:
                    x不变，y只能 -1
                若 y < 6:
                    x只能-1或+1，y只能 -1
                若 y == 0 ：
                    x只能 +1或-1，y不变
            设红兵的坐标为(a,b):
                若 b <= 3:
                    x 不变，y只能+1
                若 9 > b > 3:
                    x只能-1或+1，y只能+1
                若 b == 9:
                    x只能 +1或-1，y不变        
'''
#给棋子设置表达式坐标只是用来制定规则，棋子移动时，棋子坐标会根据规则变化，而移动规律坐标不变


'''
    请求API
    获取所有棋子坐标
    prompt = f“你是一名红方中国象棋棋手，以下是棋盘情况（以左边的红车为坐标原点，建立平面直角坐标系）：敌方（黑方）棋子情况：黑兵1({x},{y})......。我方（红方）：红兵1({a},{b})......。请你使用“<要移动的棋子原坐标>,<要移动的棋子要移动到的坐标>”的句式回答下一步红棋的走法，不要害怕，你认为怎么走就怎么走，不需要任何解释”
    打印API回复，分析回复，提取出要移动的棋子原坐标和要移动的棋子要移动到的坐标，然后根据提取出的坐标，移动棋子，并刷新棋盘情况图
'''


import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
import os
import time

'''
global c_x1, c_y1,c_x2,c_y2,c_x3,c_y3,c_x4, c_y4,h_x1,h_y1,h_x2,h_y2,h_x3,h_y3,h_x4,h_y4, e_x1,e_y1,e_x2,e_y2,e_x3,e_y3,e_x4,e_y4,b_x1,b_y1,b_x2,b_y2,b_x3,b_y3,b_x4,b_y4,s_x1,s_y1,s_x2,s_y2,s_x3,s_y3,s_x4,s_y4,s_x5,s_y5,s_x6,s_y6,s_x7,s_y7,s_x8,s_y8,s_x9,s_y9,s_x10,s_y10,a_x1,a_y1,a_x2,a_y2,cn_x1,cn_y1,cn_x2,cn_y2,cn_x3,cn_y3,cn_x4,cn_y4,nx,ny
c_x1, c_y1,c_x2,c_y2,c_x3,c_y3,c_x4, c_y4,h_x1,h_y1,h_x2,h_y2,h_x3,h_y3,h_x4,h_y4, e_x1,e_y1,e_x2,e_y2,e_x3,e_y3,e_x4,e_y4,b_x1,b_y1,b_x2,b_y2,b_x3,b_y3,b_x4,b_y4,s_x1,s_y1,s_x2,s_y2,s_x3,s_y3,s_x4,s_y4,s_x5,s_y5,s_x6,s_y6,s_x7,s_y7,s_x8,s_y8,s_x9,s_y9,s_x10,s_y10,a_x1,a_y1,a_x2,a_y2,cn_x1,cn_y1,cn_x2,cn_y2,cn_x3,cn_y3,cn_x4,cn_y4,nx,ny = float()


list = [(c_x1, c_y1),(c_x2,c_y2),(c_x3,c_y3),(c_x4, c_y4),(h_x1,h_y1),(h_x2,h_y2),(h_x3,h_y3),(h_x4,h_y4), (e_x1,e_y1),(e_x2,e_y2),(e_x3,e_y3),(e_x4,e_y4),(b_x1,b_y1),(b_x2,b_y2),(b_x3,b_y3),(b_x4,b_y4),(s_x1,s_y1),(s_x2,s_y2),(s_x3,s_y3),(s_x4,s_y4),(s_x5,s_y5),(s_x6,s_y6),(s_x7,s_y7),(s_x8,s_y8),(s_x9,s_y9),(s_x10,s_y10),(a_x1,a_y1),(a_x2,a_y2),(cn_x1,cn_y1),(cn_x2,cn_y2),(cn_x3,cn_y3),(cn_x4,cn_y4),(nx,ny)
]
'''

def graphics():
    # 获取脚本文件的当前路径
    current_path = os.path.dirname(os.path.abspath(__file__))

    # 创建一个平面直角坐标系
    plt.figure(figsize=(10, 9))

    # 设置坐标轴范围
    plt.xlim(0, 10)
    plt.ylim(0, 9)

    # 设置坐标轴比例
    plt.xticks(range(11))
    plt.yticks(range(10, -1, -1))

    # 添加坐标轴标签
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')

    # 加载图片
    path = os.path.join(current_path, "Xiangqi_board.svg.png" ) # 使用上传的图片路径
    image = plt.imread(path)

    # 显示图片，确保图片在坐标轴上铺满整个第一象限
    plt.imshow(image, extent=[0, 8, 0, 9], origin='lower')

    # 设置坐标轴比例为1，以保持图片的纵横比
    plt.gca().set_aspect('auto')

                
                                
    # 加载“红车1”图片
    c_path1 = os.path.join(current_path, "Xiangqi_rl1.svg.png") 
    c_image1 = mpimg.imread(c_path1)
    rotated_image1c = np.rot90(c_image1, 2)
    flipped_image1c = np.fliplr(rotated_image1c)

    # 初始位置
    c_x1, c_y1 = -0.5, -0.5
    
    global c_img
    # 显示“红车1”字图片
    c_img = plt.imshow(flipped_image1c, extent=[c_x1, c_x1 + 1, c_y1, c_y1 + 1], origin='lower' )

    # 初始位置
    c_x2, c_y2 = 7.5, -0.5

    # 显示“红车2”字图片
    c_img = plt.imshow(flipped_image1c, extent=[c_x2, c_x2 + 1, c_y2, c_y2 + 1], origin='lower' )
        
        
        
    # 加载“红马1”字图片
    h_path1 = os.path.join(current_path, "Xiangqi_hl1.svg.png")
    h_image1 = mpimg.imread(h_path1)
    rotated_image1h = np.rot90(h_image1, 2)
    flipped_image1h = np.fliplr(rotated_image1h)

    # 初始位置
    h_x1, h_y1 = 0.5, -0.5

    # 显示“红马1”字图片
    h_img = plt.imshow(flipped_image1h, extent=[h_x1, h_x1 + 1, h_y1, h_y1 + 1], origin='lower' )

    # 初始位置
    h_x2, h_y2 = 6.5, -0.5

    # 显示“红马2”字图片
    h_img = plt.imshow(flipped_image1h, extent=[h_x2, h_x2 + 1, h_y2, h_y2 + 1], origin='lower' )



    # 加载“红象1”字图片
    e_path1 = os.path.join(current_path, "Xiangqi_el1.svg.png") 
    e_image1 = mpimg.imread(e_path1)
    rotated_image1e = np.rot90(e_image1, 2)
    flipped_image1e = np.fliplr(rotated_image1e)

    # 初始位置
    e_x1, e_y1 = 1.5, -0.5

    # 显示“红象1”字图片
    e_img = plt.imshow(flipped_image1e, extent=[e_x1, e_x1 + 1, e_y1, e_y1 + 1], origin='lower' )

    # 初始位置
    e_x2, e_y2 = 5.5, -0.5

    # 显示“红象2”字图片
    e_img = plt.imshow(flipped_image1e, extent=[e_x2, e_x2 + 1, e_y2, e_y2 + 1], origin='lower' )



    # 加载“红士1”字图片
    b_path1 = os.path.join(current_path, "Xiangqi_al1.svg.png") 
    b_image1 = mpimg.imread(b_path1)
    rotated_image1b = np.rot90(b_image1, 2)
    flipped_image1b = np.fliplr(rotated_image1b)

    # 初始位置
    b_x1, b_y1 = 2.5, -0.5

    # 显示“红士1”字图片
    b_img = plt.imshow(flipped_image1b, extent=[b_x1,b_x1 + 1, b_y1, b_y1 + 1], origin='lower' )

    # 初始位置
    b_x2, b_y2 = 4.5, -0.5

    # 显示“红士2”字图片
    b_img = plt.imshow(flipped_image1b, extent=[b_x2, b_x2 + 1, b_y2, b_y2 + 1], origin='lower' )



    # 加载“红帅1”字图片
    a_path1 = os.path.join(current_path, "Xiangqi_gl1.svg.png") 
    a_image1 = mpimg.imread(a_path1)
    rotated_image1a = np.rot90(a_image1, 2)
    flipped_image1a = np.fliplr(rotated_image1a)

    # 初始位置
    a_x1, a_y1 = 3.5, -0.5

    # 显示“红帅1”字图片
    a_img = plt.imshow(flipped_image1a, extent=[a_x1,a_x1 + 1, a_y1, a_y1 + 1], origin='lower' )



    # 加载“红炮1”字图片
    cn_path1 = os.path.join(current_path, "Xiangqi_cl1.svg.png") 
    cn_image1 = mpimg.imread(cn_path1)
    rotated_image1cn = np.rot90(cn_image1, 2)
    flipped_image1cn = np.fliplr(rotated_image1cn)

    # 初始位置
    cn_x1, cn_y1 = 0.5, 1.5

    # 显示“红炮1”字图片
    cn_img = plt.imshow(flipped_image1cn, extent=[cn_x1,cn_x1 + 1, cn_y1, cn_y1 + 1], origin='lower' )

    # 初始位置
    cn_x2, cn_y2 = 6.5, 1.5

    # 显示“红炮2”字图片
    cn_img = plt.imshow(flipped_image1cn, extent=[cn_x2, cn_x2 + 1, cn_y2, cn_y2 + 1], origin='lower' )



    # 加载“红兵1”字图片
    s_path1 = os.path.join(current_path, "Xiangqi_sl1.svg.png") 
    s_image1 = mpimg.imread(s_path1)
    rotated_image1s = np.rot90(s_image1, 2)
    flipped_image1s = np.fliplr(rotated_image1s)

    # 初始位置
    s_x1, s_y1 = -0.5, 2.5

    # 显示“红兵1”字图片
    s_img = plt.imshow(flipped_image1s, extent=[s_x1,s_x1 + 1, s_y1, s_y1 + 1], origin='lower' )

    # 初始位置
    s_x2, s_y2 = 1.5, 2.5

    # 显示“红兵2”字图片
    s_img = plt.imshow(flipped_image1s, extent=[s_x2, s_x2 + 1, s_y2, s_y2 + 1], origin='lower' )

    # 初始位置
    s_x3, s_y3 = 3.5, 2.5

    # 显示“红兵3”字图片
    s_img = plt.imshow(flipped_image1s, extent=[s_x3, s_x3 + 1, s_y3, s_y3 + 1], origin='lower' )

    # 初始位置
    s_x4, s_y4 = 5.5, 2.5

    # 显示“红兵4”字图片
    s_img = plt.imshow(flipped_image1s, extent=[s_x4, s_x4 + 1, s_y4, s_y4 + 1], origin='lower' )

    # 初始位置
    s_x5, s_y5 = 7.5, 2.5

    # 显示“红兵5”字图片
    s_img = plt.imshow(flipped_image1s, extent=[s_x5, s_x5 + 1, s_y5, s_y5 + 1], origin='lower' )



    # 加载“黑车1”图片
    c_path2 = os.path.join(current_path, "Xiangqi_rd1.svg.png") 
    c_image2 = mpimg.imread(c_path2)
    rotated_image2c = np.rot90(c_image2, 2)
    flipped_image2c = np.fliplr(rotated_image2c)

    # 初始位置
    c_x3, c_y3 = -0.5, 8.5

    # 显示“黑车1”字图片
    c_img = plt.imshow(flipped_image2c, extent=[c_x3, c_x3 + 1, c_y3, c_y3 + 1], origin='lower' )

    # 初始位置
    c_x4, c_y4 = 7.5, 8.5

    # 显示“黑车2”字图片
    c_img = plt.imshow(flipped_image2c, extent=[c_x4, c_x4 + 1, c_y4, c_y4 + 1], origin='lower' )



    # 加载“黑马1”字图片
    h_path2 = os.path.join(current_path, "Xiangqi_hd1.svg.png") 
    h_image2 = mpimg.imread(h_path2)
    rotated_image2h = np.rot90(h_image2, 2)
    flipped_image2h = np.fliplr(rotated_image2h)

    # 初始位置
    h_x3, h_y3 = 0.5, 8.5

    # 显示“黑马1”字图片
    h_img = plt.imshow(flipped_image2h, extent=[h_x3, h_x3 + 1, h_y3, h_y3 + 1], origin='lower' )

    # 初始位置
    h_x4, h_y4 = 6.5, 8.5

    # 显示“黑马2”字图片
    h_img = plt.imshow(flipped_image2h, extent=[h_x4, h_x4 + 1, h_y4, h_y4 + 1], origin='lower' )



    # 加载“黑象1”字图片
    e_path2 = os.path.join(current_path, "Xiangqi_ed1.svg.png") 
    e_image2 = mpimg.imread(e_path2)
    rotated_image2e = np.rot90(e_image2, 2)
    flipped_image2e = np.fliplr(rotated_image2e)

    # 初始位置
    e_x3, e_y3 = 1.5, 8.5

    # 显示“黑象1”字图片
    e_img = plt.imshow(flipped_image2e, extent=[e_x3, e_x3 + 1, e_y3, e_y3 + 1], origin='lower' )

    # 初始位置
    e_x4, e_y4 = 5.5, 8.5

    # 显示“黑象2”字图片
    e_img = plt.imshow(flipped_image2e, extent=[e_x4, e_x4 + 1, e_y4, e_y4 + 1], origin='lower' )



    # 加载“黑士1”字图片
    b_path2 = os.path.join(current_path, "Xiangqi_ad1.svg.png") 
    b_image2 = mpimg.imread(b_path2)
    rotated_image2b = np.rot90(b_image2, 2)
    flipped_image2b = np.fliplr(rotated_image2b)

    # 初始位置
    b_x3, b_y3 = 2.5, 8.5

    # 显示“红士1”字图片
    b_img = plt.imshow(flipped_image2b, extent=[b_x3,b_x3 + 1, b_y3, b_y3 + 1], origin='lower' )

    # 初始位置
    b_x4, b_y4 = 4.5, 8.5

    # 显示“红士2”字图片
    b_img = plt.imshow(flipped_image2b, extent=[b_x4, b_x4 + 1, b_y4, b_y4 + 1], origin='lower' )



    # 加载“黑帅1”字图片
    a_path2 = os.path.join(current_path, "Xiangqi_gd1.svg.png") 
    a_image2 = mpimg.imread(a_path2)
    rotated_image2a = np.rot90(a_image2, 2)
    flipped_image2a = np.fliplr(rotated_image2a)

    # 初始位置
    a_x2, a_y2 = 3.5, 8.5

    # 显示“红帅1”字图片
    a_img = plt.imshow(flipped_image2a, extent=[a_x2,a_x2 + 1, a_y2, a_y2 + 1], origin='lower' )



    # 加载“黑炮1”字图片
    cn_path2 = os.path.join(current_path, "Xiangqi_cd1.svg.png") 
    cn_image2 = mpimg.imread(cn_path2)
    rotated_image2cn = np.rot90(cn_image2, 2)
    flipped_image2cn = np.fliplr(rotated_image2cn)

    # 初始位置
    cn_x3, cn_y3 = 0.5, 6.5

    # 显示“黑炮1”字图片
    cn_img = plt.imshow(flipped_image2cn, extent=[cn_x3,cn_x3 + 1, cn_y3, cn_y3 + 1], origin='lower' )

    # 初始位置
    cn_x4, cn_y4 = 6.5, 6.5

    # 显示“黑炮2”字图片
    cn_img = plt.imshow(flipped_image2cn, extent=[cn_x4, cn_x4 + 1, cn_y4, cn_y4 + 1], origin='lower' )



    # 加载“黑兵1”字图片
    s_path2 = os.path.join(current_path, "Xiangqi_sd1.svg.png") 
    s_image2 = mpimg.imread(s_path2)
    rotated_image2s = np.rot90(s_image2, 2)
    flipped_image2s = np.fliplr(rotated_image2s)

    # 初始位置
    s_x6, s_y6 = -0.5, 5.5

    # 显示“黑兵1”字图片
    s_img = plt.imshow(flipped_image2s, extent=[s_x6,s_x6 + 1, s_y6, s_y6 + 1], origin='lower' )

    # 初始位置
    s_x7, s_y7 = 1.5, 5.5

    # 显示“黑兵2”字图片
    s_img = plt.imshow(flipped_image2s, extent=[s_x7, s_x7 + 1, s_y7, s_y7 + 1], origin='lower' )

    # 初始位置
    s_x8, s_y8 = 3.5, 5.5

    # 显示“黑兵3”字图片
    s_img = plt.imshow(flipped_image2s, extent=[s_x8, s_x8 + 1, s_y8, s_y8 + 1], origin='lower' )

    # 初始位置
    s_x9, s_y9 = 5.5, 5.5

    # 显示“黑兵4”字图片
    s_img = plt.imshow(flipped_image2s, extent=[s_x9, s_x9 + 1, s_y9, s_y9 + 1], origin='lower' )

    # 初始位置
    s_x10, s_y10 = 7.5, 5.5

    # 显示“黑兵5”字图片
    s_img = plt.imshow(flipped_image2s, extent=[s_x10, s_x10 + 1, s_y10, s_y10 + 1], origin='lower' )


    plt.show()


def main():
    graphics()
    cmd = str(input("合法句式：<棋子原来的坐标> <要移动到的坐标>"))
    cmd_parts = cmd.split()
    oldxy = cmd_parts[0]
    newxy = cmd_parts[1]
    oldxy_parts = oldxy.split(',')
    oldx = oldxy_parts[0]
    oldy = oldxy_parts[1]
    newxy_parts = newxy.split(',')
    newx = newxy_parts[0]
    newy = newxy_parts[1]
    c_img.set_extent([newx, newx + 1, newy, newy + 1])

    
if "1" == "1":
    main()