from flask import Flask

app = Flask(__name__)

def about():
    return "이것은 about 페이지입니다."

app.add_url_rule("/about", "about", about)

if __name__ == "__main__":
    app.run(debug=True)
