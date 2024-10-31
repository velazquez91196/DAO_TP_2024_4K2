from baseDeDatos import BaseDeDatos

def crearTablas():
    db = BaseDeDatos().connect('tablas.db')
    cursor = db.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Autos (
        vin TEXT PRIMARY KEY,
        marca TEXT,
        modelo TEXT,
        año INTEGER,
        precio REAL,
        estado TEXT,
        cliente_id INTEGER,
        FOREIGN KEY(cliente_id) REFERENCES Cliente(id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        apellido TEXT,
        direccion TEXT,
        telefono TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Ventas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        auto_vin TEXT,
        cliente_id INTEGER,
        fecha_venta TEXT,
        vendedor_id INTEGER,
        FOREIGN KEY(auto_vin) REFERENCES Auto(vin),
        FOREIGN KEY(cliente_id) REFERENCES Cliente(id),
        FOREIGN KEY(vendedor_id) REFERENCES Vendedor(id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Servicios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        auto_vin TEXT,
        tipo_servicio TEXT,
        fecha TEXT,
        costo REAL,
        FOREIGN KEY(auto_vin) REFERENCES Auto(vin)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Vendedores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        apellido TEXT,
        comisiones REAL
    )
    ''')

    db.commit()
    db.close()

if __name__ == '__main__':
    crearTablas()
