import qrcode as qr
#direct qrcode generation-default QR
img=qr.make("https://www.udemy.com/course/the-complete-python-course/learn/quiz/5673298#questions")
img.save("udemy_python.png")