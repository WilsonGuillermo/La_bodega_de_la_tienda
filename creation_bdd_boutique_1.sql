-- Wilson Memo Mosquera
-- Version 2
-- Ajout de contraintes

-- Crear la base de datos 
DROP DATABASE boutique;
CREATE DATABASE IF NOT EXISTS boutique;

-- Usar la base de datos
USE boutique;

-- tablas de referencia
-- Crear tabla de roles
CREATE TABLE IF NOT EXISTS roles (
	id_roles INT AUTO_INCREMENT PRIMARY KEY,
	nombre_del_role VARCHAR(255) NOT NULL,
	derechos VARCHAR(255) NOT NULL,
    CONSTRAINT UC_roles UNIQUE(id_roles,nombre_del_role)
) ENGINE = InnoDB
COMMENT = 'tabla de roles';

INSERT into roles (nombre_del_role, derechos)
VALUES ('Admin', 'cocina, sala, bar, mantenimiento, stockage_alimentacion, caja'),
       ('Responsable', 'stockage_alimentacion, sala, bar, mantenimiento, caja'),
       ('Cocinero', 'cocina, bar, mantenimiento, stockage_alimentacion'),
       ('Mesero', 'sala, bar, mantenimiento, caja'),
       ('Aseador', 'cocina, sala, bar, mantenimiento');

commit;

-- Crear la tabla de usuarios
-- verifier: CONSTRAINT fk_usuarios_rol FOREIGN KEY (rol) REFERENCES roles(nombre_del_role),
CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre_usuario VARCHAR(255) NOT NULL,
    contrasena VARCHAR(255) NOT NULL,
    rol VARCHAR(255) NOT NULL,
    CONSTRAINT UC_nombre_usuario UNIQUE(nombre_usuario),
    INDEX(nombre_usuario)
)ENGINE = InnoDB
COMMENT = 'tabla de los utilisadores';


-- Crear tabla mesa
CREATE TABLE IF NOT EXISTS referencial_mesas (
    id_mesa INT AUTO_INCREMENT PRIMARY KEY,
    numero_cubiertos_tabla INT,
    CONSTRAINT UC_referencial_mesas UNIQUE(id_mesa)
)ENGINE = InnoDB
COMMENT = 'tabla de las mesas';

INSERT into referencial_mesas (numero_cubiertos_tabla)
VALUES (6), (4), (8), (2);

commit;

-- Crear tabla de tipos de productos
CREATE TABLE IF NOT EXISTS referencia_tipos_ingredientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    categoria VARCHAR(255) NOT NULL,
    unidad VARCHAR(255) NOT NULL,
    perecedero BIT,
    CONSTRAINT unica_categoria_referencia_typos_ingredientes UNIQUE(categoria)
)ENGINE = InnoDB
COMMENT = 'tabla de los tipos de productos';

INSERT into referencia_tipos_ingredientes (categoria, unidad, perecedero)
VALUES ( 'carnes', 'gramos', 1 );
INSERT into referencia_tipos_ingredientes (categoria, unidad, perecedero)
VALUES ( 'pescados', 'gramos', 1 );
INSERT into referencia_tipos_ingredientes (categoria, unidad, perecedero)
VALUES ( 'lacteos', 'centilitros', 1 );
INSERT into referencia_tipos_ingredientes (categoria, unidad, perecedero)
VALUES ( 'granos', 'gramos', 0);
INSERT into referencia_tipos_ingredientes (categoria, unidad, perecedero)
VALUES ( 'enlatados', 'gramos', 0);
INSERT into referencia_tipos_ingredientes (categoria, unidad, perecedero)
VALUES ( 'abarrotes', 'gramos', 0 );

commit;

-- Crear tabla de productos utilisados
CREATE TABLE IF NOT EXISTS referencia_ingredientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    categoria VARCHAR(255) NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    CONSTRAINT fk_categoria_referencia_ingredientes FOREIGN KEY (categoria) REFERENCES referencia_tipos_ingredientes(categoria),
    CONSTRAINT unica_nombre_referencia_ingredientes UNIQUE(nombre)
)ENGINE = InnoDB
COMMENT = 'tabla de productos utilisados';

INSERT into referencia_ingredientes (categoria, nombre)
VALUES ( 'carnes', 'entrecote' ),
       ( 'pescados', 'dorada' ),
       ( 'lacteos', 'leche' ),
       ( 'granos', 'arroz' ),
       ( 'enlatados', 'sardinas' ),
       ( 'abarrotes', 'panelas'),
       ( 'carnes', 'fauxfilet' ),
       ( 'pescados', 'bocachico' ),
       ( 'lacteos', 'queso' ),
       ( 'granos', 'lentejas' ),
       ( 'enlatados', 'atun' ),
       ( 'abarrotes', 'azucar'),
       ( 'carnes', 'steak' ),
       ( 'pescados', 'bare' ),
       ( 'lacteos', 'yogurt' ),
       ( 'granos', 'frijoles' ),
       ( 'enlatados', 'cangrejos' ),
       ( 'abarrotes', 'sal');

commit;

-- Crear la tabla de ingredientes
CREATE TABLE IF NOT EXISTS ingredientes (
    id_ingrediente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    cantidad INT NOT NULL,
    fecha_vencimiento DATE NOT NULL,
	tipo VARCHAR(255) NOT NULL,
    CONSTRAINT fk_nombre_ingredientes FOREIGN KEY (nombre) REFERENCES referencia_ingredientes(nombre),
    CONSTRAINT fk_tipo_ingredientes FOREIGN KEY (tipo) REFERENCES referencia_tipos_ingredientes(categoria),
    CONSTRAINT UC_ingredientes UNIQUE(id_ingrediente, nombre),
    INDEX(nombre, tipo, cantidad)
)ENGINE = InnoDB
COMMENT = 'tabla de productos';

-- Crear la tabla de menús
CREATE TABLE IF NOT EXISTS menus (
    id_menu INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10, 2) NOT NULL,
	ingredientes_principales TEXT,
    fecha_creacion DATETIME NOT NULL
)ENGINE = InnoDB
COMMENT = 'tabla de los menus';

-- Crear la tabla de platos a la carta
CREATE TABLE IF NOT EXISTS platos_carta (
    id_platos INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10, 2) NOT NULL,
	ingredientes_principales TEXT,
    fecha_creacion DATETIME NOT NULL
)ENGINE = InnoDB
COMMENT = 'tabla de los platos a la carta';

-- Crear la tabla de pedidos
CREATE TABLE IF NOT EXISTS pedidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_menu INT,
    id_plato_carta INT,
    cantidad INT NOT NULL,
    fecha_pedido DATETIME NOT NULL,
    FOREIGN KEY (id_menu) REFERENCES menus(id_menu),
    FOREIGN KEY (id_plato_carta) REFERENCES platos_carta(id_platos)
)ENGINE = InnoDB
COMMENT = 'tabla de los pedidos';

-- Crear la carta
CREATE TABLE IF NOT EXISTS carta(
    id_carta INT AUTO_INCREMENT PRIMARY KEY,
    lista_de_menus VARCHAR(255) NOT NULL,
    lista_de_platos VARCHAR(255) NOT NULL,
    lista_de_bebidas VARCHAR(255) NOT NULL,
    lista_de_postres VARCHAR(255) NOT NULL
)ENGINE = InnoDB
COMMENT = 'tabla de la carta';

-- Crear la carta
CREATE TABLE IF NOT EXISTS informal(
    id_informal INT AUTO_INCREMENT PRIMARY KEY,
    lista_de_sandwiches VARCHAR(255) NOT NULL,
    lista_de_bebidas VARCHAR(255) NOT NULL,
    lista_de_postres VARCHAR(255) NOT NULL
)ENGINE = InnoDB
COMMENT = 'tabla de productos informales';
