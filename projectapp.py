from flask import Flask,render_template,request
import foodscrapper
app=Flask("comparator")

@app.route('/index')
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/scrapper', methods=['GET', 'POST'])
def scrapper():
  items = []
  if request.method == "POST":
    query = request.form["query"]
    items = foodscrapper.scrapinfo(query)
  return render_template('scrapper.html', items = items)


if __name__ == '__main__':
    app.run(port = 8029, debug = True)
    #app.run(host='0.0.0.0')