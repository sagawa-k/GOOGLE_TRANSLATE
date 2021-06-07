import eel
import desktop
import translate

ITEM_MASTER_CSV_PATH="./item_master.csv"

app_name="html"
end_point="index.html"
size=(700,600)

@ eel.expose
def text_translate(base_text, base_country, result_country):
    translate.text_translate(base_text, base_country, result_country)

desktop.start(app_name, end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)