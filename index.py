import scrapping as scrapping
import database as database
import kakaotalk as kkot
import corona19 as corona19
import weather as weather
# url, select 등은 dictionary로 정리하기

# scp_result = scrapping.scrapping()

# db_result = database.db_insert(scp_result)

# db_result = database.db_select()

# kkot.kakaotalk(db_result['title'].to_json())

corona19 = corona19.corona19()
print(corona19)

database.insert('corona19',corona19)

# weather = weather.weather()