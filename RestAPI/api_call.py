import requests

def add_book(title, author, first_sentence, published):
    data = {"title": title, "author": author, "first_sentence": first_sentence, "published": published}
    r = requests.post('http://localhost:5000/api/books', json=data)
    return r.json()

def update_book(id, title, author, first_sentence, published):
    data = {"id": id, "title": title, "author": author, "first_sentence": first_sentence, "published": published}
    r =requests.put('http://localhost:5000/api/books/{}'.format(id), json=data)
    return r.json()

def get_book(id):
    r = requests.get('http://localhost:5000/api/books/{}'.format(id))
    return r.json()

def get_books():
    r = requests.get('http://localhost:5000/api/books')
    return r.json()
