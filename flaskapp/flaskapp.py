from flask import Flask
from flask import render_template

from collections import Counter

app = Flask(__name__)

@app.route("/")
def root():
  return "Spiro is a getting fat!"

@app.route("/songs", methods=['GET', 'POST'])
def songs():
  return "What's up"

@app.route("/upload", methods=['GET', 'POST'])
def upload():
  return "time to upload!"

@app.route("/complete", methods=['GET', 'POST'])
def upload_complete():
  return "COMPLETE"

@app.route("/countme/<input_str>")
def count_me(input_str):
  input_counter = Counter(input_str)
  response = []
  for letter, count in input_counter.most_common():
    response.append('"{}": {}'.format(letter, count))
  return '<br>'.join(response)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
  app.run()