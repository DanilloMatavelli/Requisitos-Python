from data.conexao import Conexao
import datetime

class Descricao:
    def cadastrardescricao(descricao, nivel, valor):
        # CADASTRANDO AS INFORMAÇÕES NO BANCO DE DADOS
        # Criando a coneção 

        conexao = Conexao.criar_conexao()

        # O cursor será responsavel por manipular o banco de dados 
        cursor = conexao.cursor()

        # Criando o SQL que será executado 
        sql = """INSERT INTO  tb_requisitos
                    (descricao, nivel, valor)
                VALUES
                    (%s, %s, %s)"""
        
        valores = (descricao, nivel , valor)

        # Executando o comando SQL
        cursor.execute(sql,valores)

        # Confirmo a alteração
        conexao.commit()

        # Fecho a conexão com o Banco
        cursor.close()
        conexao.close()

        
        # Pegar as mensagens e fazer aparecer no HTML
        
    def recuperar_mensagens():
            
            # Criar conexão
            conexao = Conexao.criar_conexao()
            
            # O cursor será responsavel por manipular o banco de dados 
            cursor = conexao.cursor(dictionary = True)
            
            # Define a consulta SQL
            sql = """SELECT cod_requisito,
                            descricao as descricao, 
                            nivel,
                            valor,
                            situacao
                    FROM tb_requisitos"""
                    
            # Executando o comando SQL
            cursor.execute(sql)
            
            # Pegas os resultados do usuario e aparecer no HTML
            # Recuperando os dados e guardando em uma variavel
            resultado = cursor.fetchall()
            
            # Fecha a conexão com o banco
            cursor.close()
            conexao.close()
            
            return resultado
    
    # Pegar as descrições e excluir do HTML
    def deletar_descricao(codigo):
        # DELETANDO AS INFORMAÇÕES NO BANCO DE DADOS
        # Criando a coneção 

        conexao = Conexao.criar_conexao()

        # O cursor será responsavel por manipular o banco de dados 
        cursor = conexao.cursor()

        # Criando o SQL que será executado para deletar o comentário
        sql = """DELETE FROM tb_requisitos
                 WHERE cod_requisito = %s"""
        
        # O valor do cod_comentario a ser deletado
        valores = (codigo,)

        # Executando o comando SQL
        cursor.execute(sql,valores)

        # Confirmo a alteração
        conexao.commit()

        # Fecho a conexão com o Banco
        cursor.close()
        conexao.close()
    
    # Pegar para trocar a situação para resolvida no HTML
    def resolver_descricao(codigo):
        # DELETANDO AS INFORMAÇÕES NO BANCO DE DADOS
        # Criando a coneção 

        conexao = Conexao.criar_conexao()

        # O cursor será responsavel por manipular o banco de dados 
        cursor = conexao.cursor()

        # Criando o SQL que será executado para deletar o comentário
        sql = """UPDATE tb_requisitos
                 SET situacao = 'Resolvida'
                 WHERE cod_requisito = %s"""
        
        # O valor do cod_comentario a ser deletado
        valores = (codigo,)

        # Executando o comando SQL
        cursor.execute(sql,valores)

        # Confirmo a alteração
        conexao.commit()

        # Fecho a conexão com o Banco
        cursor.close()
        conexao.close()

    # Pegar para trocar a situação para pendente no HTML
    def pendente_descricao(codigo):
        # DELETANDO AS INFORMAÇÕES NO BANCO DE DADOS
        # Criando a coneção 

        conexao = Conexao.criar_conexao()

        # O cursor será responsavel por manipular o banco de dados 
        cursor = conexao.cursor()

        # Criando o SQL que será executado para deletar o comentário
        sql = """UPDATE tb_requisitos
                 SET situacao = 'Pendente'
                 WHERE cod_requisito = %s"""
        
        # O valor do cod_comentario a ser deletado
        valores = (codigo,)

        # Executando o comando SQL
        cursor.execute(sql,valores)

        # Confirmo a alteração
        conexao.commit()

        # Fecho a conexão com o Banco
        cursor.close()
        conexao.close()