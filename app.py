import os
from flask import Flask
from flask import render_template
app =  Flask(__name__)
bg_color=os.environ.get('BG_COLOR','green')

@app.route("/")
def main():
	print(bg_color)
	return render_template('change-bg.html',bgColor=bg_color)

if __name__ == "__main__":
	app.run(host="0.0.0.0",port="80")
