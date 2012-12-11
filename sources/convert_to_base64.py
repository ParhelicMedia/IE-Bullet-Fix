import glob
import base64

file = open("./iebulletfix.css.template", "r")
template = file.read()
file.close()

b64str = base64.b64encode(open("./bullet_disc.png", "rb").read())
template = template.replace("!!DISC!!", b64str.decode("UTF-8"))

b64str = base64.b64encode(open("./bullet_circle.png", "rb").read())
template = template.replace("!!CIRCLE!!", b64str.decode("UTF-8"))

b64str = base64.b64encode(open("./bullet_square.png", "rb").read())
template = template.replace("!!SQUARE!!", b64str.decode("UTF-8"))

file = open("./iebulletfix.css", "w")
file.write(template)
file.close()
