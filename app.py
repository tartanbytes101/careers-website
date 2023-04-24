from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Glasgow',
  'salary': '£54,000'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Edinburgh',
  'salary': '£60,000'
}, {
  'id': 3,
  'title': 'Frontend Developer',
  'location': 'Ayr',
  'salary': '£44,000'
}, {
  'id': 4,
  'title': 'Games Developer',
  'location': 'Dundee',
  'salary': '£70,000'
}, {
  'id': 5,
  'title': 'Backend Engineer',
  'location': 'London'
}]


@app.route("/")
def hello_world():
  return render_template("homeB.html", jobs=JOBS, company_name="cacaBoom")


#__json endpoint for API (Application Programming Interface)
#__ more info go to: https://www.w3schools.com/js/js_api_intro.asp
#__ adding /api/jobs to url in browser address bar will display jason file of jobs data
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


#__start the app
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
