from flask import Flask, render_template
import random

app = Flask(__name__)

# list of images with hundegger machines
images = [
    "https://www.hundegger.de/fileadmin/_processed_/9/4/csm_TURBO-Drive_Kopf_575c4b392d.jpg",
	"https://www.hundegger.de/fileadmin/_processed_/9/a/csm_ROBOT-Drive_980_9c64e4142a.jpg",
	"https://www.hundegger.de/fileadmin/_processed_/e/4/csm_K2i_mit_Robot_links_09_2011_360_113c7df256.jpg",
	"https://www.hundegger.de/fileadmin/_processed_/7/2/csm_PBA_980_4123788029.jpg",
	"https://www.hundegger.de/fileadmin/_processed_/7/2/csm_PBA_980_4123788029.jpg"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
