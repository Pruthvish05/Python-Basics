import qrcode
d = "hi there"
img = qrcode.make(d)
img.save(r"C:/Users/Pruthvish/OneDrive/qrcode.png")