from save_json import writeAJson
from database import Database

from ProductAnalyzer import *

db = Database(database="Mercado", collection="mercado")
db.resetDatabase()
mercado = db.collection.find()

result = TotalB()
writeAJson(result, "Total_gasto_do_cliente_B")

result1 = ProdutoMenosVendido()
writeAJson(result1, "Produto_menos_vendido")

result2 = ClienteQueMenosGastou()
writeAJson(result2, "Cliente_que_menos_gastou_em_uma_unica_compra")

result3 = ListaDosProdutos()
writeAJson(result3, "Produtos_que_tiveram_uma_quantidade_vendida_acima_de_2_unidades")

