from datetime import date
from . import db


def get_post_list():  # generator
    """Yeild a list of posts

    :returns: array[post()]
    """
    size = len(db)
    if size == 0:
        return
    for n in range(max(size - 10, 1), size + 1):  # whoo one-based indexing
        yield db.get(eid=n)


def get_post(eid):
    return db.get(eid=eid)


def add_post(request):
    """Add a post to posts TinyDB

    :returns: '', 204 (No Content)
    """
    post = request.get_json()
    today = date.today()
    post_template = {key: post[key] for key in ('post', 'title')}  # proxy dict
    post_template.update(year=today.year, month=today.month)
    return db.insert(post_template)


def update_post(eid, request):
    post = request.get_json()
    return db.update(lambda entry: entry.update(post), eids=(eid,))[0]


def delete_post(eid):
    pass  # ::TODO:: find a way to sort out dead posts
