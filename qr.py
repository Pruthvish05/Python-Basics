import qrcode
d = "hey there"
img = qrcode.make(d)
img.save(r"C:\Users\Pruthvish\Desktop\qrcode.png")