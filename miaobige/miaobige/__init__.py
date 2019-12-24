import os
import sys

import django

DJANGO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(os.path.join(__file__, os.pardir))))

sys.path.append('')  # 将项目路径添加到系统搜寻路径当中
os.environ['DJANGO_SETTINGS_MODULE'] = 'dream_note.settings.local'  # 设置项目的配置文件

django.setup()  # 加载项目配置
