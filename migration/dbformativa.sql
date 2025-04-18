CREATE DATABASE db_formativa;
use db_formativa;

CREATE TABLE tb_requisitos (
	cod_requisito INT AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(200),
    nivel VARCHAR(20),
    valor FLOAT,
    situacao VARCHAR(20) DEFAULT 'pendente'
    );