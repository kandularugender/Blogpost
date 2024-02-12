from flask import Flask 
app = Flask(__name__)

@app.route('/jhg')
def home():
    return 'Rugender'

if __name__ == '__main__':
    app.run(debug=True)    
    






