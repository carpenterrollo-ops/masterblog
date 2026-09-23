"""Datahandler module for managing persistent storage of blog posts in JSON format."""

import os
import json

_FILE_DIRECTORY = "src/"
_FILE_NAME = "blogposts.json"
_FILE_PATH = _FILE_DIRECTORY + _FILE_NAME
data_mock = [
    {"id": 1, "author": "John Doe", "title": "First Post", "content": "This is my first post."},
    {"id": 2, "author": "Jane Doe", "title": "Second Post", "content": "This is another post."}
]


def delete_file(file_path: str):
    """Delete the specified file if it exists."""
    if os.path.exists(file_path):
        os.remove(file_path)


def generate_data_mock():
    """Generate the initial mock JSON data file with default blog posts."""
    with open(_FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(data_mock, f, indent=4)


def add_or_update_entry(data: dict):
    """Add a new blog post or update an existing post based on its ID."""
    if data is None:
        return
    all_blog_posts = get_all_blogposts()
    post_id = data.get("id")
    if not post_id:
        max_id = max((post["id"] for post in all_blog_posts), default=0)
        data["id"] = max_id + 1
        all_blog_posts.append(data)
    else:
        found = False
        for index, post in enumerate(all_blog_posts):
            if post["id"] == post_id:
                all_blog_posts[index] = data
                found = True
                break
        if not found:
            raise ValueError(f"Blog post with id {post_id} does not exist")
    save_all_blogposts(all_blog_posts)


def delete_entry(index_for_deletion: int):
    """Delete a blog post from the JSON storage by its unique post ID."""
    all_blog_posts = get_all_blogposts()
    list_index_to_delete = None
    for index, post in enumerate(all_blog_posts):
        if post["id"] == index_for_deletion:
            list_index_to_delete = index
            break
    if list_index_to_delete is None:
        raise ValueError(f"Blog post with id {index_for_deletion} does not exist")

    del all_blog_posts[list_index_to_delete]
    save_all_blogposts(all_blog_posts)


def get_all_blogposts() -> list:
    """Retrieve and return all blog posts stored in the JSON file."""
    if os.path.exists(_FILE_PATH):
        with open(_FILE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        raise FileNotFoundError(f'File not found: {_FILE_PATH}')


def save_all_blogposts(posts: list):
    """Overwrite the JSON file content with the updated list of blog posts."""
    with open(_FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(posts, f, indent=4)


def fetch_post_by_id(post_id: int):
    """Fetch and return a single post dictionary by its unique post ID."""
    for post in get_all_blogposts():
        if post["id"] == post_id:
            return post
    return None


if __name__ == '__main__':
    generate_data_mock()
