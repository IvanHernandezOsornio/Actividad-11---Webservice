CREATE DATABASE l3xfh7abxcftmrsc;

USE l3xfh7abxcftmrsc;

DROP TABLE IF EXISTS clientes;

CREATE TABLE IF NOT EXISTS clientes(
id_cliente INT(1) AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(50) NOT NULL,
apellido_paterno VARCHAR(50) NOT NULL,
apellido_materno VARCHAR(50) NOT NULL,
telefono VARCHAR(50) NULL,
email VARCHAR(50) NOT NULL')
ENGINE = MYISAM CHARSET = LATIN1;


INSERT INTO clientes VALUES 
(1,'Luis Angel','Hernandez','Osornio','7751234567','luis@hotmail.com'),
(2,'Nancy','Hernandez','Osornio','7759876532','nancy@hotmail.com'),
(3,'Anel','Hernández','Osornio','7751472536','anel@hotmail.com');

SELECT * FROM clientes;
