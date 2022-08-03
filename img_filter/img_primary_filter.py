import re   # 正则表达式处理的python库
import os
import cv2
import shutil
import numpy as np
import matplotlib.pyplot as plt



# 检测输入图像是否需要
def check_img(img_path):
    img = cv2.imread(img_path, flags=cv2.IMREAD_COLOR)

    # file info
    file_size = os.path.getsize(img_path)   # 文件大小
    img_height, img_width = img.shape[:2]
    if file_size < 10 * 1024 or img_width < 256 or img_height < 256:
        return False

    # image basic feature
    img_dy = img[:img_height-1] - img[1:]
    img_dx = img[:, :img_width-1] - img[:, 1:]
    img_gradient = np.mean(np.abs(img_dx)) + np.mean(np.abs(img_dy))
    print(img_path, "img_gradient =", img_gradient)
    if img_gradient < 50:
        return False

    return True


if __name__ == '__main__':
    root_dir = "../Image-Downloader-master/download_images/cat"
    file_suffix = "jpeg|jpg|png"    # 正则表达式 或
    remove_dir = root_dir + "/remove"   # 需要删掉的数据放到/remove
    if not os.path.exists(remove_dir):
        os.makedirs(remove_dir)
    for img_name in os.listdir(root_dir):
        # 对处理文件的类型进行过滤
        if re.search(file_suffix, img_name) is None:    # 是否需要的文件类型 .后缀名
            continue
        img_path = root_dir + "/" + img_name    # 完整路径
        if not check_img(img_path):
            output_path = remove_dir + "/" + img_name
            # shutil.move(img_path, output_path)
