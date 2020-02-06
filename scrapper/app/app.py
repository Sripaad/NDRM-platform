import scrap
import pushData
import requests
import sys
from flask import Flask, request, render_template

app = Flask(__name__)
hitCount = 0

@app.route('/', methods=['GET', 'POST'])
def Index():
    errors = []
    results = {}
    if hitCount == 0:
        pd = pushData.Server()
        pd.awsConfigure()
        hitCount+=1
    if request.method == "POST":
        # get keyword that the user has entered
        try:
            keyWord = request.form['key-box']
            print(keyWord)
            scrap.Scrapp(keyWord)
        except:
            errors.append(
                "Unable to get Keyword. Please make sure it's valid and try again."
            )
    return render_template('admin.html', errors=errors, results=results)

if __name__ == '__main__':
    app.run(debug=True,port=5000, host='0.0.0.0')