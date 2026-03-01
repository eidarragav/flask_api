from flask import jsonify, request, current_app
from models import User, Post, Book, db

def register_routes(app):
    @app.route('/api/users', methods = ['GET'])
    def get_users():
        users = User.query.all()
        return jsonify([{'id': u.id, 'name' : u.name, 'email' : u.email} for u in users])

    @app.route('/api/users', methods = ['POST'])
    def post_users():
        data = request.get_json()
        new_user = User(
            name = data["name"],
            email = data["email"]
        )

        db.session.add(new_user)
        db.session.commit()

        return jsonify({'id': new_user.id, 'name': new_user.name, 'emai': new_user.email})
    
    @app.route('/api/users/<int:id>', methods = ['PUT'])
    def update_users(id):
        data = request.get_json()

        user_modify = User.query.get_or_404(id)
        user_modify.name = data["name"]
        user_modify.email = data["email"]

        db.session.commit()

        return jsonify({'id': user_modify.id, 'name' : user_modify.name, 'email' : user_modify.name})
    

    @app.route('/api/users/<int:id>', methods = ['DELETE'])
    def delete_users(id):
        data = request.get_json()
        user = User.query.get_or_404(id)

        db.session.delete(user)
        db.session.commit()

        return jsonify({'STATUS' : 200})
    
    @app.route("/api/books", methods = ['GET'])
    def get_books():
        books = Book.query.all()
        return jsonify([{'id': b.id, 'title': b.title, 'isbn' : b.isbn, 
                         'price' : b.isbn, 'author_id' : b.author_id} for b in books])

    @app.route("/api/books", methods = ['POST'])
    def post_books():
        
        user_id = request.headers.get("X-User-Id")
        data = request.get_json()
        
        book = Book(
            title = data["title"],
            isbn = data["isbn"],
            price = data["price"],
            author_id = user_id
        )

        db.session.add(book)
        db.session.commit()

        return jsonify({"message" : "Libro creado"} )
    
    @app.route("/api/me/books", methods =['GET'])
    def me_books():
        xauthor_id = int(request.headers.get('X-User-Id'))
        books = Book.query.filter_by(author_id = xauthor_id).all()
        
        return jsonify([{'id' : b.id, 'title' : b.title, 
                         'isbn' : b.isbn, 'price' : b.price} for b in books])

    
    