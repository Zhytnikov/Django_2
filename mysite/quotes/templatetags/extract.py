from ..utils import get_mongodb
from django import template
from bson import ObjectId

register = template.Library()

def get_author(_id):

    db = get_mongodb()
    author = db.authors.find_one({"_id": ObjectId(_id)})

    return author['fullname']


register.filter('author', get_author)
