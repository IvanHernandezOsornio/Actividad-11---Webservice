CREATE DATABASE l3xfh7abxcftmrsc;

USE l3xfh7abxcftmrsc;

DROP TABLE IF EXISTS clientes;

CREATE TABLE IF NOT EXISTS clientes(
id_cliente INT(1) AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(50) NOT NULL COMMENT 'NOMBRE DEL CLIENTE',
apellido_paterno VARCHAR(50) NOT NULL COMMENT 'APELLIDO PATERNO DEL CLIENTE',
apellido_materno VARCHAR(50) NOT NULL COMMENT 'APELLIDO MATERNO DEL CLIENTE',
telefono VARCHAR(50) NULL COMMENT 'TELEFONO DEL CLIENTE',
email VARCHAR(50) NOT NULL COMMENT 'EMAIL DEL CLIENTE')
ENGINE = MYISAM CHARSET = LATIN1 COMMENT 'CLIENTES DE LA FERRETERIA';


INSERT INTO clientes VALUES 
(1,'Luis Angel','Hernandez','Osornio','7751234567','luis@hotmail.com'),
(2,'Nancy','Hernandez','Osornio','7759876532','nancy@hotmail.com'),
(3,'Anel','Hernández','Osornio','7751472536','anel@hotmail.com');

SELECT * FROM clientes;