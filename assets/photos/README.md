# 网站照片

当前照片路径与成员对应关系见根目录 website-content.json 的 faculty / people / group_photos。

将新照片放到本目录，运行 python tools/check_images.py 压缩超尺寸图片并归档原图，再运行 python tools/sync_content.py 更新网页和缓存版本。小图保持原样；缺失照片使用姓氏占位。
