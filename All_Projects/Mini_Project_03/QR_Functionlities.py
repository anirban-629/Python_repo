import qrcode as q
from PIL import Image
qr=q.QRCode(
    version=1,
    error_correction=q.constants.ERROR_CORRECT_H,
    box_size=10,
    border=5
)
qr.add_data("labigialsdbflasdnflaknscliabgdsiLGBfwnepfnqcnar oqpvwehqwofeqpeflaskj wqoefjoma 124 ")
qr.make(fit=True)
img=qr.make_image(fill_color='Green',back_color="white")
img.save("HackerRank_QR.png")