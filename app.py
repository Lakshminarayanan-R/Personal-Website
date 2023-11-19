from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/projects')
def projects():
  return render_template('projects_page.html')

@app.route('/blogs')
def blogs():
  return render_template('blogs.html')

@app.route('/book_review')
def book_review():
  return render_template('bookreview.html')

if __name__ == "__main__":
  app.run(host = '0.0.0.0',debug=True)