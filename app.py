from flask import Flask, render_template, request, redirect, url_for
import datahandler

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/index')
def index():
    # add code here to fetch the job posts from a file
    blog_posts = datahandler.get_all_blogposts()
    return render_template('index.html', posts=blog_posts)

@app.route('/add', methods=['GET', 'POST'])
def add():
    #adds new entry to blogentries
    if request.method == 'POST':
        author = request.form.get('author')
        title = request.form.get('title')
        content = request.form.get('content')
        new_entry = {"author": author, "title": title, "content": content}
        datahandler.add_or_change_entry(new_entry)
        return redirect(url_for('index'))
    return render_template('add.html')


if __name__ == '__main__':
    app.run(debug=True)
    datahandler.generate_data_mock()
    app.run(host="0.0.0.0", port=5000, debug=True)