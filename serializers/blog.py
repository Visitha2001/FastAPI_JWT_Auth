# one doc
def DecodeBlog(doc) -> dict:
    return {
        '_id': str(doc['_id']),
        'title': doc['title'],
        'subtitle': doc['subtitle'],
        'content': doc['content'],
        'author': doc['author'],
        'date': doc['date'],
        "tags": doc.get("tags", [])
    }

# all blogs
def DecodeBlogs(docs) -> list:
    return [DecodeBlog(doc) for doc in docs]