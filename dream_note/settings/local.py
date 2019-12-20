from dream_note.settings.base import *
from dream_note.settings.template_settings.simple_ui import *
# 数据库配置
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': "dream_note",
        "HOST": "127.0.0.1"
    }
}
