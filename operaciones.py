# operations.py
from persistencia.baseDeDatos import BaseDeDatos
from dominio.auto import Auto
from dominio.cliente import Cliente
from dominio.venta import Venta
from dominio.servicio import Servicio
from dominio.vendedor import Vendedor # No lo piden en la consigna pero van a haber que agregar un par de vendedores


def registrar_auto(auto: Auto):
    db = BaseDeDatos().connect('concesionaria.db')
    cursor = db.cursor()
    cursor.execute('''
    INSERT INTO Auto (vin, marca, modelo, año, precio, estado, cliente_id)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (auto.vin, auto.marca, auto.modelo, auto.año, auto.precio, auto.estado, auto.cliente))
    db.commit()
    db.close()


def registrar_cliente(cliente: Cliente):
    db = BaseDeDatos().connect('concesionaria.db')
    cursor = db.cursor()
    cursor.execute('''
    INSERT INTO Cliente (nombre, apellido, direccion, telefono)
    VALUES (?, ?, ?, ?)
    ''', (cliente.nombre, cliente.apellido, cliente.direccion, cliente.telefono))
    db.commit()
    db.close()


def registrar_venta(venta: Venta):
    db = BaseDeDatos().connect('concesionaria.db')
    cursor = db.cursor()
    cursor.execute('''
    SELECT estado FROM Auto WHERE vin = ?
    ''', (venta.auto,))
    auto = cursor.fetchone()
    if auto and auto[0] == 'vendido':
        raise ValueError("El auto ya ha sido vendido.")

    cursor.execute('''
    INSERT INTO Venta (auto_vin, cliente_id, fecha_venta, vendedor_id)
    VALUES (?, ?, ?, ?)
    ''', (venta.auto, venta.cliente, venta.fecha_venta, venta.vendedor))

    cursor.execute('''
    UPDATE Auto SET estado = 'vendido' WHERE vin = ?
    ''', (venta.auto,))

    db.commit()
    db.close()


def registrar_servicio(servicio: Servicio):
    db = BaseDeDatos().connect('concesionaria.db')
    cursor = db.cursor()
    cursor.execute('''
    SELECT estado FROM Auto WHERE vin = ?
    ''', (servicio.auto,))
    auto = cursor.fetchone()
    if not auto or auto[0] != 'vendido':
        raise ValueError("El servicio debe estar asociado a un auto vendido.")

    cursor.execute('''
    INSERT INTO Servicio (auto_vin, tipo_servicio, fecha, costo)
    VALUES (?, ?, ?, ?)
    ''', (servicio.auto, servicio.tipo_servicio, servicio.fecha, servicio.costo))
    db.commit()
    db.close()