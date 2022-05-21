from app import app

@app.route('/')
def index():
    return 'Welcome To TKU Recommendation System API'

if __name__ == '__main__':
    app.run(debug = True)