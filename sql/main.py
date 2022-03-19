#%%
from sqlalchemy import create_engine
import pandas as pd
# %%
# criando a conexão com o banco de dados
engine = create_engine(
    'postgresql+psycopg2://root:root@localhost/test_db')
# %%
# criando a query
sql = '''
select * from clientes;
'''

# %%
# criando um dataframe
df_clientes =  pd.read_sql_query(sql,engine)
df_artist =  pd.read_sql_query(sql,engine)
df_song = pd.read_sql_query('select * from vw_song;',engine)

# inserindo dados 
sql = '''
insert into tb_artist (
SELECT t1."date"
	,t1."rank"
	,t1.artist
	,t1.song 
FROM PUBLIC."Billboard" AS t1 
where t1.artist like 'Nirvana'
order by t1.artist, t1.song , t1."date" 
);

'''
engine.execute(sql)