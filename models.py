from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Categoria(db.Model):
    __tablename__ = 'categorias'
    id_categoria = db.Column(db.Integer, primary_key=True)
    nombre_categoria = db.Column(db.String(255), nullable=False)
    descripcion_categoria = db.Column(db.String(255), nullable=False)

    articulos = db.relationship('Articulo', back_populates='categoria')

class Ubicacion(db.Model):
    __tablename__ = 'ubicacion'
    id_ubicacion = db.Column(db.Integer, primary_key=True)
    nombre_ubicacion = db.Column(db.String(255), nullable=False)
    descripcion_ubicacion = db.Column(db.String(255))

    articulos = db.relationship('Articulo', back_populates='ubicacion')

class Articulo(db.Model):
    __tablename__ = 'articulos'
    id_articulo = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.String(255), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)
    usuario_adicion = db.Column(db.String(255), nullable=False)
    id_ubicacion = db.Column(db.Integer, db.ForeignKey('ubicacion.id_ubicacion'), nullable=False)
    id_categoria = db.Column(db.Integer, db.ForeignKey('categorias.id_categoria'), nullable=False)

    categoria = db.relationship('Categoria', back_populates='articulos')
    ubicacion = db.relationship('Ubicacion', back_populates='articulos')
    movimientos = db.relationship('HistorialMovimiento', back_populates='articulo')

class HistorialMovimiento(db.Model):
    __tablename__ = 'historial_movimientos'
    id_movimiento = db.Column(db.Integer, primary_key=True)
    tipo_movimiento = db.Column(db.String(255), nullable=False)
    cantidad_modificada = db.Column(db.Integer, nullable=False)
    fecha_movimiento = db.Column(db.DateTime, nullable=False)
    usuario_responsable = db.Column(db.String(255), nullable=False)
    descripcion_movimiento = db.Column(db.String(255))
    id_articulo = db.Column(db.Integer, db.ForeignKey('articulos.id_articulo'), nullable=False)

    articulo = db.relationship('Articulo', back_populates='movimientos')

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre_usuario = db.Column(db.String(255), nullable=False)
    roles = db.Column(db.String(255), nullable=False)
    contraseña = db.Column(db.String(255), nullable=False)
    cedula = db.Column(db.Integer, nullable=False)
    correo_electronico = db.Column(db.String(255))
