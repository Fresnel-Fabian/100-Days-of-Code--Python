from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import choice
'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        # Method 1
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            #Create a new dictionary entry:
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary
        # Method 2 : Alternatively use Dictionary Comprehension to do the same thing
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random", methods=["GET"])
def random():
    result = db.session.execute(db.select(Cafe)).scalars().all()
    random_cafe = choice(result)
    return jsonify(cafe=random_cafe.to_dict())
    # return jsonify(cafe={
    #     "id": random_cafe.id,
    #     "name": random_cafe.name,
    #     "map_url": random_cafe.map_url,
    #     "img_url": random_cafe.img_url,
    #     "location": random_cafe.location,
    #     "seats": random_cafe.seats,
    #     "has_toilet": random_cafe.has_toilet,
    #     "has_wifi": random_cafe.has_wifi,
    #     "has_sockets": random_cafe.has_sockets,
    #     "can_take_calls": random_cafe.can_take_calls,
    #     "coffee_price": random_cafe.coffee_price,
    # })
    


    

## HTTP GET - Read Record
@app.route("/all", methods=["GET"])
def get_all():
    result = db.session.execute(db.select(Cafe).order_by(Cafe.id)).scalars().all()
    return jsonify(cafes = [cafe.to_dict() for cafe in result])

@app.route("/search", methods=["GET"])
def search():
    loc = request.args.get("loc")
    result = db.session.execute(db.select(Cafe).where(Cafe.location == loc))
    all_cafes = result.scalars().all()
    if all_cafes:
        return jsonify(cafes = [cafe.to_dict() for cafe in all_cafes])
    return jsonify(error={"Not found": "Sorry, we don't have a cafe at that location."}), 404
## HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add():
    data = request.form
    new_entry = Cafe(
        name = data.get("name"),
        map_url = data["map_url"],
        img_url = data["img_url"],
        location = data["location"],
        seats = data["seats"],
        has_toilet = bool(data["has_toilet"]),
        has_wifi = bool(data["has_wifi"]),
        has_sockets = bool(data["has_sockets"]),
        can_take_calls = bool(data["can_take_calls"]),
        coffee_price = data["coffee_price"],
    )
    
    db.session.add(new_entry)
    db.session.commit()
    return jsonify(response= {
        "success": "Successfully added the new cafe."
    })

## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    coffee_price = request.args.get("coffee_price")
    cafe = db.session.get(Cafe, cafe_id)
    if cafe:
        cafe.coffee_price = coffee_price
        db.session.commit()
        return jsonify(response= {
            "success": "Successfully updated the price."
        })
    else:
        return jsonify(error={"Not found": "Sorry a cafe with that id was not found in the database"}), 404

## HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api_key")
    if api_key == "TopSecretAPIKey":
        cafe = db.session.get(Cafe, cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={
                "success": "Successfullly deleted the cafe."
            })
        return jsonify(error={
            "Not Found": "Sorry a cafe with that id was not found in the database."
        }), 404
    return jsonify(error={
        "Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."
        }), 403


if __name__ == '__main__':
    app.run(debug=True)
