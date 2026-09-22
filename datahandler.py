import os
import json

_file_directory = "src/"
_file_name = "blogposts.json"
_file_path = _file_directory + _file_name
data_mock = [
    {"id": 1, "author": "John Doe", "title": "First Post", "content": "This is my first post."},
    {"id": 2, "author": "Jane Doe", "title": "Second Post", "content": "This is another post."}
    # More blog posts can go here...
]

def delete_file(file_path):
    #delete file
    if os.path.exists(file_path):
        os.remove(file_path)

def generate_data_mock():
    #Generate json datasource with starting datas
    with open(_file_path, "w") as f:
        json.dump(data_mock, f, indent=4)

def add_or_change_entry(data:dict):
    # if no id set, new entry will be added
    # existing id signals entry change. if index does not exist, error is raised
    if data is None:
        return
    all_blog_posts = get_all_blogposts()
    post_id = data.get("id")
    if not post_id:
        max_id = max(( post["id"] for post in all_blog_posts ), default=0)
        data["id"]= max_id + 1
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

def delete_entry(index_for_deletion:int):
    #delete an entry
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


def get_all_blogposts():
    # returns all entries from datasource
    if os.path.exists(_file_path):
        with open(_file_path) as f:
            return json.load(f)
    else:
        raise FileNotFoundError(f'File not found: {_file_path}')

def save_all_blogposts(posts: list):
    #overwrite file content of datasource with new entries
    with open(_file_path, "w") as f:
        json.dump(posts, f, indent=4)

if __name__ == '__main__':
    generate_data_mock()