CREATE DATABASE IF NOT EXISTS loja_moveis;

USE loja_moveis;

CREATE TABLE IF NOT EXISTS cliente(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS venda(
	id INT PRIMARY KEY AUTO_INCREMENT,
	id_cliente INT NOT NULL,
	id_funcionario INT NOT NULL,
	data DATE,
    CONSTRAINT id_cliente FOREIGN KEY (id_cliente) REFERENCES cliente(id),
    CONSTRAINT id_funcionario FOREIGN KEY (id_funcionario) REFERENCES funcionario(id)
);

CREATE TABLE IF NOT EXISTS funcionario(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(100) NOT NULL,
    id_cargo INT NOT NULL,
    CONSTRAINT id_cargo FOREIGN KEY (id_cargo) REFERENCES cargo(id)
);

CREATE TABLE IF NOT EXISTS cargo(
		id INT PRIMARY KEY AUTO_INCREMENT,
		cargo VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS item_venda(
	id INT PRIMARY KEY AUTO_INCREMENT,
	id_venda INT NOT NULL,
	id_produto INT NOT NULL,
    quantidade INT NOT NULL,
    preco_unitario FLOAT NOT NULL,
	preco_pago FLOAT NOT NULL,
	desconto FLOAT NOT NULL,
    CONSTRAINT id_venda FOREIGN KEY(id_venda) REFERENCES venda(id),
    CONSTRAINT id_produto FOREIGN KEY(id_produto) REFERENCES produto(id)
);

CREATE TABLE IF NOT EXISTS produto(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(50) NOT NULL,
    valor FLOAT NOT NULL
);