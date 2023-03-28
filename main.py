from save_json import writeAJson
from database import Database

from ProductAnalyzer import *

db = Database(database="Mercado", collection="mercado")
db.resetDatabase()
mercado = db.collection.find()

#Escrevendo os Arquivos JSON

#Arquivo do Total gasto do Cliente B
writeAJson(TotalB(), "Total_gasto_do_cliente_B")

#Arquivo do produto menos vendido
writeAJson(ProdutoMenosVendido(), "Produto_menos_vendido")

#Arquivo do cliente que menos gastou realizando uma unica compra
writeAJson(ClienteQueMenosGastou(), "Cliente_que_menos_gastou_em_uma_unica_compra")

#Arquivo dos produtos vendidos mais de uma vez
writeAJson(ListaDosProdutos(), "Produtos_que_tiveram_uma_quantidade_vendida_acima_de_2_unidades")

