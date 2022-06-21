from pymongo import MongoClient

conn = MongoClient('localhost', 27017) #cria conexao com o DB

bdExistentes = conn.list_database_names() #retorna os bd existentes
db = conn.cadastrodb #cria/define o banco de dados 'cadastrodb'
bdName = db.posts.name #retorna o nome do bd

'''db.create_collection("mycollection")''' #cria uma collection
colecoesExistente = db.list_collection_names() #retorna as collection existentes naquele bd
qtdColecao = db.mycollection.estimated_document_count() #conta a qtd de documentos na collection 'mycollection'
col = db["mycollection"] #cria uma conexao (assim n precissa escreve 'db.collectionName' td hr, apenas 'col')

post1 = {"codigo": "ID-9987725","prod_name": "Geladeira","marcas": ["brastemp", "consul", "elecrolux"],
        "data_cadastro": '20/02/2019'} #dados q serao inseridos
post2 = {"codigo": "ID-2209876","prod_name": "Televisor","marcas": ["samsung", "panasonic", "lg"],
        "data_cadastro": '18/02/2019'} #dados q serao inseridos

'''post_id = collection.insert_one(post1).inserted_id''' #insere os dados e o _id e retorna o id
'''post_id = collection.insert_one(post2).inserted_id''' #insere os dados e o _id e retorna o id

find = col.find_one({"prod_name": "Televisor"}) #procura por certos dados no banco e retorna-os

for posts1 in db.collection.find(): #retorna os documentos da collection 'posts'
    print()
    #print(posts1)