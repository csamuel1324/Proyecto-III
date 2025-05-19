from flask import Flask, render_template
from models import db

app = Flask(__name__)

# Configuración de conexión a MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/bd-inventario'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar SQLAlchemy
db.init_app(app)

@app.route('/')
def index():
    # Ahora carga el archivo index.html en templates/
    return render_template('index.html')

@app.route('/usuario')
def usuario():
    return render_template('usuario.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crea las tablas si no existen
    app.run(debug=True)
