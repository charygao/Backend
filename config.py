# 常量定义
# DOC_DIM = (16, 12)
DOC_DIM = (14, 14)
BOARDER_SIZE = 2
MARGIN_SIZE = 4

BLANK_SIZE = (560, 60)
# BLANK_SIZE = (0, 0)
FONT_SIZE = 50
FOREGROUND_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)
FONT_NAME_Fangzheng = "FangZhengKaiTi"
FONT_NAME_Sun = "SimSun"
FONT_NAME_HuaWen = "HuaWenSun"
FONT_NAME_Micro = "MicroSun"
# TODO diff from IMAGE_SIZE
# DOC_IMAGE_SIZE = ((FONT_SIZE+2*MARGIN_SIZE) * DOC_DIM[0] + 2*BOARDER_SIZE + 2*BLANK_SIZE[0],
#                   (FONT_SIZE+2*MARGIN_SIZE)*DOC_DIM[1] + 2*BOARDER_SIZE + 2*BLANK_SIZE[1])

IMAGE_SIZE = ((FONT_SIZE+2*MARGIN_SIZE) * DOC_DIM[0] + 2*BOARDER_SIZE,
              (FONT_SIZE+2*MARGIN_SIZE)*DOC_DIM[1] + 2*BOARDER_SIZE)

# print(IMAGE_SIZE)

