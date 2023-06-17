from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'London, UK',
    'salary': 'GBP £55.000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'London, UK',
    'salary': 'GBP £65.000'
  },
  {
    'id': 3,
    'title': 'Web Developer',
    'location': 'Remote',
    'salary': 'GBP £60.000'
  },
  {
    'id': 4,
    'title': 'UI Designer',
    'location': 'USA',
    'salary': 'USD $45.000'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
