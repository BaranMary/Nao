import sqlite3 as sql
import numpy as np
conn = sql.connect('./userinfo.db')

c = conn.cursor()

# c.execute("""CREATE TABLE userinfo(

#     username text,
#     feature_array text,
#     summary text,
#     question text

# )""")

# c.execute("insert into userinfo values (?,?,?)",('apple','[0.12,0.2,0.3,0.4,0.21421,0.214,0.44]','NULL'))
# c.execute("insert into userinfo values (?,?,?)",('banan','[0.22,0.2,0.3,0.4,0.21421,0.214,0.44]','NULL'))
# c.execute("insert into userinfo values (?,?,?)",('car','[0.32,0.2,0.3,0.4,0.21421,0.214,0.44]','NULL'))

# c.execute("insert into userinfo values (?,?,?)",('dog','[0.42,0.2,0.3,0.4,0.21421,0.214,0.44]','NULL'))

# print(c.execute("select * from userinfo").fetchall())

# conn.commit()

# known_user_name=c.execute("select username from userinfo").fetchall()
# known_user_features=c.execute("select feature_array from userinfo").fetchall()
# print(np.array(known_user_name).flatten()[1])
# known_user_name=np.array(c.execute("select username from userinfo").fetchall()).flatten()
# temp_feature=np.array(c.execute("select feature_array from userinfo").fetchall()).flatten()
# print(known_user_name,temp_feature)


# print(c.execute("select * from userinfo where username=*").fetchall())

#--------- delete --------------
# c.execute("delete from userinfo")



print(c.execute("select * from userinfo ").fetchall())








# print(c.execute("select * from userinfo").fetchall())
conn.commit()
conn.close()
          


