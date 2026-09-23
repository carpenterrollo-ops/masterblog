"""Flask web application for managing blog posts with full CRUD functionality."""
"""Warning: By startup a predefined setup for blog post are created."""
"""Deactivate this behaviour by removing our comment out datahandler.generate_data_mock()."""
from flask import Flask, render_template, request, redirect, url_for
import datahandler

app = Flask(__name__)


@app.route('/')
def hello_world():
    """Redirect to index page."""
    return redirect(url_for('index'))


def convert_to_blogpost(form):
    """Extract and structure blog post data from the submitted form."""
    # expect 'author', 'title', 'content'
    author = form.get('author')
    title = form.get('title')
    content = form.get('content')
    return {"author": author, "title": title, "content": content}


@app.route('/index')
def index():
    """Fetch all blog posts and render the main index page."""
    # add code here to fetch the job posts from a file
    blog_posts = datahandler.get_all_blogposts()
    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    """Handle creation of a new blog post via GET (form) and POST (submission)."""
    # adds new entry to blogentries
    if request.method == 'POST':
        new_entry = convert_to_blogpost(request.form)
        datahandler.add_or_update_entry(new_entry)
        return redirect(url_for('index'))
    return render_template('add.html')


@app.route("/delete/<int:post_id>", methods=["DELETE", "POST"])
def delete(post_id):
    """Delete blog post for given id. Available with post for browser compatibility"""
    datahandler.delete_entry(post_id)
    return redirect(url_for('index'))


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    """Redirect to update page or replace blogpost with updated version"""
    # Fetch the blog posts from the JSON file
    post = datahandler.fetch_post_by_id(post_id)
    print(f"found by id: {post}")
    if post is None:
        # Post not found
        return "Post not found", 404

    if request.method == 'POST':
        # Update the post in the JSON file
        new_entry = convert_to_blogpost(request.form)
        new_entry["id"] = post_id
        print(f"update entry with id: {new_entry}")
        datahandler.add_or_update_entry(new_entry)
        # Redirect back to index
        return redirect(url_for('index'))

    # Else, it's a GET request
    # So display the update.html page
    return render_template('update.html', post=post)


if __name__ == '__main__':
    datahandler.generate_data_mock()
    app.run(host="0.0.0.0", port=5000, debug=True)
