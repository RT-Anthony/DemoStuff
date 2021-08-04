import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def do_a_thing():
    pass

def do_async_thing():
    pass

def get_list_of_things():
    pass

def get_list_of_async_things():
    pass

books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

@app.route('/', methods=['GET'])
def home():
    return "Hello"

@app.route('/process', methods=['GET', 'PUT'])
def run_process():
    if request.method == 'PUT':
        status = do_a_thing()
        return jsonify(status)
    return jsonify(get_list_of_things())



@app.route('/async_process', methods=['GET', 'PUT'])
def run_async():
    if request.method == 'PUT':
        status = do_async_thing()
        return jsonify(status)
    return jsonify(get_list_of_async_things())

@app.route('/api/books', methods=['GET', 'POST'])
def add_book():
    if request.method == 'GET':
        return jsonify(books)
    id = len(books)
    req = request.get_json()
    data = {"id": id,
            "title": req["title"],
            "author": req["author"],
            "first_sentence": req["first_sentence"],
            "published": req["published"]}
    books.append(data)
    return jsonify(books[id])

@app.route('/api/books/<int:id>', methods=['GET', 'PUT'])
def get_book(id):
    if request.method == 'PUT':
        if len(books) <= id:
            return "Record not found", 400
        req = request.get_json()
        data = {"id": id,
                "title": req["title"],
                "author": req["author"],
                "first_sentence": req["first_sentence"],
                "published": req["published"]}
        books[id] = data
    return jsonify(books[id])

@app.route("/api/shots", methods=["GET", "POST"]])
def get_shots():
    pass
    

if __name__ == '__main__':
    app.run()