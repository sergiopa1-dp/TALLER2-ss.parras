from flask import Flask, render_template, jsonify
from Ant.perro import Perro
from Ant.gato import Gato
from Ant.Huron import Huron
from Ant.Boa import Boa_Constrictor

def create_app():
    app = Flask(__name__, template_folder='views')

    # crear instacias d elos animales
    perro = Perro("Zeus", "Rottweiler", 3, 45.8)
    gato = Gato("Destructor de Mundos", "Naranja", 5, 4)
    huron = Huron("Huroncito", 10.0, 2, "España", 500.0)
    boa = Boa_Constrictor("Boa", 25.0, 10, "Brasil", 400.00)

    @app.route('/')
    def index():
        return render_template('animal_sounds.html')

    @app.route('/api/animal/sound/<animal_type>', methods=['GET'])
    def get_animal_sound(animal_type):
        animals = {
            'perro': perro,
            'gato': gato,
            'huron': huron,
            'boa': boa
        }
        
        if animal_type.lower() in animals:
            sound = animals[animal_type.lower()].emitir_sonido()
            return jsonify({
                'animal': animal_type,
                'sound': sound,
                'success': True
            })
        else:
            return jsonify({'error': 'Animal not found', 'success': False}), 404

    @app.route('/api/animals/sounds', methods=['GET'])
    def get_all_sounds():
        return jsonify({
            'perro': perro.emitir_sonido(),
            'gato': gato.emitir_sonido(),
            'huron': huron.emitir_sonido(),
            'boa': boa.emitir_sonido()
        })

    return app