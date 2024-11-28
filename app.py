from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from dotenv import load_load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aquarium.db'
db = SQLAlchemy(app)

# Database Models
class Fish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    species = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer, default=0)
    health = db.Column(db.Integer, default=100)
    last_fed = db.Column(db.DateTime, default=datetime.utcnow)
    tank_id = db.Column(db.Integer, db.ForeignKey('tank.id'))

class Tank(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    temperature = db.Column(db.Float, default=25.0)
    ph_level = db.Column(db.Float, default=7.0)
    oxygen_level = db.Column(db.Float, default=8.0)
    fishes = db.relationship('Fish', backref='tank', lazy=True)

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/tanks')
def get_tanks():
    tanks = Tank.query.all()
    return jsonify([{
        'id': tank.id,
        'name': tank.name,
        'temperature': tank.temperature,
        'ph_level': tank.ph_level,
        'oxygen_level': tank.oxygen_level,
        'fish_count': len(tank.fishes)
    } for tank in tanks])

@app.route('/api/fish')
def get_fish():
    tank_id = request.args.get('tank_id', type=int)
    if tank_id:
        fishes = Fish.query.filter_by(tank_id=tank_id).all()
    else:
        fishes = Fish.query.all()
    return jsonify([{
        'id': fish.id,
        'species': fish.species,
        'name': fish.name,
        'age': fish.age,
        'health': fish.health,
        'last_fed': fish.last_fed.isoformat()
    } for fish in fishes])

@app.route('/api/add_fish', methods=['POST'])
def add_fish():
    data = request.json
    new_fish = Fish(
        species=data['species'],
        name=data['name'],
        tank_id=data['tank_id']
    )
    db.session.add(new_fish)
    db.session.commit()
    return jsonify({'message': 'Fish added successfully', 'id': new_fish.id})

@app.route('/api/feed_fish/<int:fish_id>', methods=['POST'])
def feed_fish(fish_id):
    fish = Fish.query.get_or_404(fish_id)
    fish.last_fed = datetime.utcnow()
    fish.health = min(100, fish.health + 10)
    db.session.commit()
    return jsonify({'message': 'Fish fed successfully'})

@app.route('/api/update_tank/<int:tank_id>', methods=['POST'])
def update_tank(tank_id):
    tank = Tank.query.get_or_404(tank_id)
    data = request.json
    if 'temperature' in data:
        tank.temperature = data['temperature']
    if 'ph_level' in data:
        tank.ph_level = data['ph_level']
    if 'oxygen_level' in data:
        tank.oxygen_level = data['oxygen_level']
    db.session.commit()
    return jsonify({'message': 'Tank updated successfully'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
