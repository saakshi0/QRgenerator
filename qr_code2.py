import qrcode
#Customized QR code generation
from PIL import Image

qrc=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10, border=10)

qrc.add_data("https://www.udemy.com/course/the-complete-python-course/learn/quiz/5673298#questions")

qrc.make(fit=True)
img=qrc.make_image(fill_color='red',back_color='white')
img.save('udemy_py.png')