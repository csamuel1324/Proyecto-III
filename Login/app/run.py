from app import app_web

app = app_web()

if __name__ == "__main__":
    app.run(debug=True,port=2000)