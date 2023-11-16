import logging
from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN
from buttons import *
from lavash import *

bot =Bot(token=API_TOKEN)
dp=Dispatcher(bot)


logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Tilni tanlang", reply_markup=lang)


@dp.message_handler(text = "🇺🇿O'zbekcha")
async def exo(message: types.Message):
    await message.answer('Asosiy menu', reply_markup=info_uz)

@dp.message_handler(text = "🇷🇺Руский")
async def exo(message: types.Message):
    await message.answer('Asosiy menu', reply_markup=info_ru)

@dp.message_handler(text = "🇺🇸English")
async def exo(message: types.Message):
    await message.answer('Asosiy menu', reply_markup=info_en)    

@dp.message_handler(text = "Tilni o'zgartirish")
async def exo(message: types.Message):
    await message.answer('Asosiy menu', reply_markup=info_ru)

@dp.message_handler(text = "Изменить язык")
async def exo(message: types.Message):
    await message.answer('Asosiy menu', reply_markup=info_en)

@dp.message_handler(text = "Change language")
async def exo(message: types.Message):
    await message.answer('Asosiy menu', reply_markup=info_uz)

@dp.message_handler(text = "Change language")
async def exo(message: types.Message):
    await message.answer('Asosiy menu', reply_markup=info_uz)

@dp.message_handler(text = "Biz bilan aloqa☎️")
async def exo(message: types.Message):
    await message.answer('+998-90-941-04-19')

@dp.message_handler(text = "Sozlamalar⚙️")
async def exo(message: types.Message):
    await message.answer('Sozlanmoqda!!!')    

@dp.message_handler(text = "Buyurtma berish🧑‍💻")
async def exo(message: types.Message):
    await message.answer('Asosiy menu', reply_markup=menu_asosiy)

@dp.callback_query_handler(text = "back")
async def exo(call: types.CallbackQuery):
    await call.message.answer('Asosiy menu',reply_markup=menu_asosiy)    

@dp.callback_query_handler(text = "lavash")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat lavashlar menusi!!!", reply_markup=lavash_menu)

@dp.callback_query_handler(text = "mol_go'sht")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!!", reply_markup=lavash_mol_goshtli)


@dp.callback_query_handler(text = "orqa")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat lavashlar menusi!!!", reply_markup=lavash_menu) 

@dp.callback_query_handler(text = "mini_mol")
async def exo(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('lavash/lavash_gosht.jpg','rb'),
        caption='''✅Narxi: 18 000 ming so'm 
Tarkibi:Xamir, go'sht, chips, pomidor, bodring, sous, moyonez
Miqdorini tanlang...''', reply_markup=miqdor
    ) 

@dp.callback_query_handler(text = "back_mini")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!!", reply_markup=lavash_mol_goshtli)

@dp.callback_query_handler(text = "classik_mol")
async def exo(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("lavash/lavash_gosht.jpg",'rb'),
        caption='''✅Narxi: 20 000 ming so'm 
Tarkibi:Xamir, go'sht, chips, pomidor, bodring, sous, moyonez
Miqdorini tanlang...''', reply_markup=miqdor1)

@dp.callback_query_handler(text = "back_classik")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!!", reply_markup=lavash_mol_goshtli)

@dp.callback_query_handler(text = "tovuq_go'shtlik")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!!", reply_markup=lavash_tovuq_goshtlik)

@dp.callback_query_handler(text = "mini_tovuq")
async def exo(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("lavash/lavash_tovuq.jpg",'rb'),
        caption='''✅Narxi: 19 000 ming so'm 
Tarkibi: Xamir,tovuq go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang...''',reply_markup=miqdor_mini)

@dp.callback_query_handler(text = "back_tovuq")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!!", reply_markup=lavash_tovuq_goshtlik)

@dp.callback_query_handler(text = "classik_tovuq")
async def exo(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('lavash/lavash_tovuq.jpg','rb'),
        caption='''✅Narxi: 22 000 ming so'm 
Tarkibi: Xamir,tovuq go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang...''',reply_markup=miqdor_classik_chicken
    ) 

@dp.callback_query_handler(text = "back_chick")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!!", reply_markup=lavash_tovuq_goshtlik)

@dp.callback_query_handler(text = "back_chicken")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat lavashlar menusi!!!", reply_markup=lavash_menu)


@dp.callback_query_handler(text = "pishloqli_mol_go'shtlik")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!!", reply_markup=lavash_pishloqli)

@dp.callback_query_handler(text = "mini_pishloq")
async def exo(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('lavash/lavash_sir.jpg','rb'),
        caption = '''✅Narxi: 18 000 ming so'm 
Tarkibi: Pishloq, xamir,mol go'sht,pishloq,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang...''', reply_markup=lavash_pishloqli)

@dp.callback_query_handler(text = "back_mini_sir")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!!", reply_markup=lavash_pishloqli)

@dp.callback_query_handler(text = "classik_pishloq")
async def exo(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('lavash/lavash_sir.jpg','rb'),
        caption='''✅Narxi:20 000 ming so'm 
Tarkibi: Pishloq,xamir,mol go'sht,pishloq,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang''',reply_markup=lavash_pishloqli)

@dp.callback_query_handler(text = "back_classic_sir")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!!", reply_markup=lavash_pishloqli)

@dp.callback_query_handler(text = "back_sir")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat lavashlar menusi!!!", reply_markup=lavash_menu)    
        
@dp.callback_query_handler(text = "qalampirli_mol_go'shtli")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!!", reply_markup=lavash_qalampirli) 

@dp.callback_query_handler(text = "back_qalampir")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat lavashlar menusi!!!", reply_markup=lavash_menu) 

@dp.callback_query_handler(text = "mini_qalampir")
async def exo(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("lavash/qalampir.jpg", 'rb'),
        caption='''✅Narxi: 19 000 ming so'm 
Tarkibi: Xamir, garimdori go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang...''', reply_markup=miqdor_mini_qalampir
    )                   

@dp.callback_query_handler(text = "back_mini_qalampir")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!!",reply_markup=lavash_qalampirli)                   

@dp.callback_query_handler(text = "classik_qalampir")
async def exo(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('lavash/qalampir.jpg', 'rb'),
        caption='''✅Narxi: 20 000 ming so'm 
Tarkibi: Xamir,garimdori go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang...''',reply_markup=miqdor_classik_qalampir

    )                   

@dp.callback_query_handler(text = "back_classik_qalampir")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!!",reply_markup=lavash_qalampirli)                   

@dp.callback_query_handler(text = "qalampirli_tovuq_go'shtlik")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!!",reply_markup=lavash_qalampir_tovuq)                   

@dp.callback_query_handler(text = "back_qalampir_tovuq")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat lavashlar menusi!!!",reply_markup=lavash_menu)                   

@dp.callback_query_handler(text = "mini_qalampir_tovuq")
async def exo(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open('lavash/qalampir_tovuq.jpg','rb'),
        caption = '''✅Narxi: 17 000 ming so'm 
Tarkibi: Xamir,garimdori,tovuq go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang...''',reply_markup=miqdor_mini_tovuq)

@dp.callback_query_handler(text = "back_mini_qalampir_tovuq")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!!",reply_markup=lavash_qalampir_tovuq)                   

@dp.callback_query_handler(text = "classik_qalampir_tovuq")
async def exo(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open('lavash/qalampir_tovuq.jpg','rb'),
        caption = '''✅Narxi: 20 000 ming so'm 
Tarkibi:Xamir,garimdori tovuq go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang...''',reply_markup=miqdor_classik_tovuq_qalampir)

@dp.callback_query_handler(text = "back_classik_qalampir_tovuq")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!!",reply_markup=lavash_qalampir_tovuq)

@dp.callback_query_handler(text = "pishloqli_tovuq_go'shtlik")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!!",reply_markup=lavash_pishloqli_tovuq)

@dp.callback_query_handler(text = "back_pishloq_tovuq")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat lavashlar menusi!!!",reply_markup=lavash_menu)

@dp.callback_query_handler(text = "mini_pishloq_tovuq")
async def exo(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open('lavash/mini_sirli.jpg','rb'),
        caption = '''✅Narxi: 18 000 ming so'm 
Tarkibi:Xamir,tovuq go'sht,pishloq,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang...''', reply_markup=miqdor_mini_tovuq_pishloq)

@dp.callback_query_handler(text = "back_classik_qalampir_pishloq")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!!",reply_markup=lavash_pishloqli_tovuq)

@dp.callback_query_handler(text = "classik_pishloq_tovuq")
async def exo(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open('lavash/mini_sirli.jpg','rb'),
        caption='''✅Narxi: 20 000 ming so'm 
Tarkibi:Xamir,tovuq go'sht,pishloq,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang...''',reply_markup=miqdor_classic_tovuq_pishloq)
    
@dp.callback_query_handler(text = "back_classik_classic_pishloq")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!!",reply_markup=lavash_pishloqli_tovuq)

@dp.callback_query_handler(text = "flitter")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!!",reply_markup=lavash_flitter)
    
@dp.callback_query_handler(text = "back_flitter")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat lavashlar menusi!!!", reply_markup=lavash_menu)

@dp.callback_query_handler(text = "mini_flitter")
async def exo(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("lavash/mini_sirli.jpg", 'rb'),
        caption='''✅Narxi: 19 000 ming so'm 
Tarkibi: Xamir, qarsildoq muztogʼ salati,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang...''', reply_markup=mini_flitter)    

@dp.callback_query_handler(text = "back_mini_flitter")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!!", reply_markup=lavash_flitter)

@dp.callback_query_handler(text = "classik_flitter")
async def exo(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open('lavash/mini_sirli.jpg','rb'),
        caption='''✅Narxi: 21 000 ming so'm 
Tarkibi: Xamir, qarsildoq muztogʼ salati,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang...''', reply_markup=classic_flitter)

@dp.callback_query_handler(text = "back_classik_flitter")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!!", reply_markup=lavash_flitter)

@dp.callback_query_handler(text = "clab")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Marhamat Clab sendvichlar menusi!!!", reply_markup=clab_sendvich)

@dp.callback_query_handler(text = "back_sand")
async def exo(call: types.CallbackQuery):
    await call.message.answer("Asosiy menu", reply_markup=menu_asosiy)

@dp.callback_query_handler(text = "clab_sendvich")
async def exo(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("lavash/clab_class.jpg", 'rb'),
        caption='''✅Narxi: 22 000 ming so'm 
Tarkibi: Kulcha, tovuq go'shti, pomidor, sous,  piyoz.
Miqdorini tanlang...''', reply_markup=miqdor_clab_classik)

@dp.callback_query_handler(text = "back_clabb")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Marhamat Clab sendvichlar menusi!!!", reply_markup=clab_sendvich)
    
@dp.callback_query_handler(text = "tovuq_sand")
async def exo(call: types.CallbackQuery):
    text = '''✅Narxi: 24 000 ming so'm 
Tarkibi: Kulcha, tovuq go'shti, pomidor, sous,  piyoz.
Miqdorini tanlang...'''
    await call.message.answer_photo(
        photo = open("lavash/clab_class.jpg",'rb'),
        caption = text, reply_markup=miqdor_clab_tovuqli)

@dp.callback_query_handler(text = "back_clabb_tovuq")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Marhamat Clab sendvichlar menusi!!!", reply_markup=clab_sendvich)
        

@dp.callback_query_handler(text = "burger")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Marhamat Burgerlar menusi!!!", reply_markup=Burgerss)

@dp.callback_query_handler(text = "back_burg")
async def exo(call: types.CallbackQuery):
    await call.message.answer("Asosiy menu", reply_markup=menu_asosiy)   

@dp.callback_query_handler(text = "gamburger")
async def exo(call: types.CallbackQuery):
    text = '''✅Narxi: 22 000 ming so'm 
Miqdorini tanlang...'''
    await call.message.answer_photo(
        photo = open('lavash/gamburger.jpg','rb'),
        caption=text, reply_markup=miqdor_gamburger) 

@dp.callback_query_handler(text = "back_gamb")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Marhamat Burgerlar menusi!!!", reply_markup=Burgerss)      

@dp.callback_query_handler(text = "chizburger")
async def exo(call: types.CallbackQuery):
    text = '''✅Narxi: 20 000 ming so'm 
Miqdorini tanlang...'''
    await call.message.answer_photo(
        photo = open("lavash/chizburger.jpg",'rb'),
        caption=text, reply_markup=miqdor_chizburger) 

@dp.callback_query_handler(text = "back_chiz")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Marhamat Burgerlar menusi!!!", reply_markup=Burgerss)         

@dp.callback_query_handler(text = "gazaklar")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Marhamat Fries menusi!!!", reply_markup=Gazaklarr)         

@dp.callback_query_handler(text = "back_gazak")
async def exo(call: types.CallbackQuery):
    await call.message.answer("Asosiy menu", reply_markup=menu_asosiy)         

@dp.callback_query_handler(text = "free")
async def exo(call: types.CallbackQuery):
    text = '''✅Narxi: 6 000 ming so'm 
Tarkib: kartoshka, sous....   
Miqdorini tanlang...'''
    await call.message.answer_photo(
        photo = open('lavash/frie.jpg','rb'),
        caption=text, reply_markup=miqdor_frie) 

@dp.callback_query_handler(text = "back_frie")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Marhamat Fries menusi!!!", reply_markup=Gazaklarr)         

@dp.callback_query_handler(text = "derevyan")
async def exo(call: types.CallbackQuery):
    text = '''✅Narxi: 10 000 ming so'm
Tarkib: kartoshka, sous...      
Miqdorini tanlang...'''
    await call.message.answer_photo(
        photo = open('lavash/derev.jpg', 'rb'),
        caption=text, reply_markup=miqdor_dera)    

@dp.callback_query_handler(text = "back_dera")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Marhamat Fries menusi!!!", reply_markup=Gazaklarr)         

@dp.callback_query_handler(text = "guruch_katta")
async def exo(call: types.CallbackQuery):
    text = '''✅Narxi: 8 000 ming so'm
Tarkib: gurunch, salat bargi, sous...     
Miqdorini tanlang...'''
    await call.message.answer_photo(
        photo=open('lavash/gurunch.jpg','rb'),
        caption=text, reply_markup=miqdor_katta_gurunch)

@dp.callback_query_handler(text = "back_katta_grunch")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Marhamat Fries menusi!!!", reply_markup=Gazaklarr)         

@dp.callback_query_handler(text = "guruch_kichik")
async def exo(call: types.CallbackQuery):
    text = '''✅Narxi: 10 000 ming so'm
Tarkib: gurunch, salat bargi, sous...     
Miqdorini tanlang...'''
    await call.message.answer_photo(
        photo=open("lavash/gurunch.jpg",'rb'),
        caption=text, reply_markup=miqdor_kichik_gurunch)   

@dp.callback_query_handler(text = "back_kichik_grunch")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Marhamat Fries menusi!!!", reply_markup=Gazaklarr)         

@dp.callback_query_handler(text = "desertlar")
async def exo(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open('lavash/deserts.jpg', 'rb'),
        caption="✅Marhamat desertlar menusi!!!", reply_markup=Desertlarr)  

@dp.callback_query_handler(text = "back_desert")
async def exo(call: types.CallbackQuery):
    await call.message.answer("Asosiy menu", reply_markup=menu_asosiy) 

@dp.callback_query_handler(text = "asalim")
async def exo(call: types.CallbackQuery):
    text = """✅Narxi: 14 000 so'm 
Аnʼnaviy taʼm - asal asosidagi biskvit va krem
Miqdorini tanlang"""
    await call.message.answer_photo(
        photo = open('lavash/asalim.jpg','rb'),
        caption=text, reply_markup=miqdor_assalim)         

@dp.callback_query_handler(text = "back_assalim_desert")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Marhamat desertlar menusi!!!", reply_markup=Desertlarr) 

@dp.callback_query_handler(text = "qulupnay")
async def exo(call: types.CallbackQuery):
    text = '''✅Narxi: 15 000 so'm 
Qulupnayli Muss.
Miqdorini tanlang'''
    await call.message.answer_photo(
        photo=open('lavash/qulupnay.jpg','rb'),
        caption=text, reply_markup=miqdor_qulupnay) 

@dp.callback_query_handler(text = "back_qulupnay_desert")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Marhamat desertlar menusi!!!", reply_markup=Desertlarr) 

@dp.callback_query_handler(text = "choko")
async def exo(call: types.CallbackQuery):
    text = '''✅Narxi: 17 000 ming so'm 
Аnʼnaviy taʼm - shokolat asosidagi biskvit va krem.
Miqdorini tanlangg'''
    await call.message.answer_photo(
        photo=open('lavash/choko.jpg','rb'),
        caption=text, reply_markup=miqdor_choco) 

@dp.callback_query_handler(text = "back_choco_desert")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Marhamat desertlar menusi!!!", reply_markup=Desertlarr)   

@dp.callback_query_handler(text = "hot-dog")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Marhamat hot-doglar menusi!!!", reply_markup=Hot_dogs)  

@dp.callback_query_handler(text = "back_hotdog")
async def exo(call: types.CallbackQuery):
    await call.message.answer("Asosiy menu", reply_markup=menu_asosiy)  

@dp.callback_query_handler(text = "baget")
async def exo(call: types.CallbackQuery):
    text = '''✅Narxi: 18 000 ming so'm 
Tarkibi: Kulcha,sosiska 2x,ketchup va xantal,qovurilgan piyoz.
Miqdorini tanlang...'''
    await call.message.answer_photo(
        photo = open('lavash/baget_dabl.jpg','rb'),
        caption=text, reply_markup=miqdor_baget) 

@dp.callback_query_handler(text = "back_hot_baget")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Marhamat hot-doglar menusi!!!", reply_markup=Hot_dogs)  

@dp.callback_query_handler(text = "classik_hot")
async def exo(call: types.CallbackQuery):
    text = '''✅Narxi: 8 000 ming so'm 
Tarkibi: Kulcha,sosiska,ketchup va xantal,qovurilgan piyoz.
Miqdorini tanlang...'''
    await call.message.answer_photo(
        photo = open('lavash/classik_hot.jpg', 'rb'),
        caption=text, reply_markup=miqdor_classik_hot) 

@dp.callback_query_handler(text = "back_hot_classik")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Marhamat hot-doglar menusi!!!", reply_markup=Hot_dogs)  

@dp.callback_query_handler(text = "korolev")
async def exo(call: types.CallbackQuery):
    text = '''✅Narxi: 8 000 ming so'm 
Tarkibi: Kulcha,sosiska,ketchup va xantal,qovurilgan piyoz.
Miqdorini tanlang...'''
    await call.message.answer_photo(
        photo = open('lavash/korolevske.jpg', 'rb'),
        caption=text, reply_markup=miqdor_korolev_hot)  

@dp.callback_query_handler(text = "back_korolev_classik")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Marhamat hot-doglar menusi!!!", reply_markup=Hot_dogs)  

@dp.callback_query_handler(text = "Tovuq_hot")
async def exo(call: types.CallbackQuery):
    text = '''✅Narxi: 17 000 ming so'm 
Tarkibi: Kulcha,sosiska,ketchup va xantal,qovurilgan piyoz.
Miqdorini tanlang...'''
    await call.message.answer_photo(
        photo = open('lavash/tovuqli_hot.jpg', 'rb'),
        caption=text, reply_markup=miqdor_tovuq_hot)  

@dp.callback_query_handler(text = "back_tovuq_classik")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Marhamat hot-doglar menusi!!!", reply_markup=Hot_dogs)  

@dp.callback_query_handler(text = "shourma")
async def exo(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('lavash/shourmalar.jpg','rb'),
        caption="✅Marhamat shourmalar menusi!!!", reply_markup=Shourmaa)  

@dp.callback_query_handler(text = "back_shourma")
async def exo(call: types.CallbackQuery):
    await call.message.answer("Asosiy menu", reply_markup=menu_asosiy)  

@dp.callback_query_handler(text = "shourma_mol")
async def exo(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('lavash/mol_gosh_shourma.jpg','rb'),
        caption="✅Kategoriyalardan birini tanlang", reply_markup=miqdor_mol_gosh_shourma)

@dp.callback_query_handler(text = "back_mol_go'shtlik")
async def exo(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('lavash/shourmalar.jpg','rb'),
        caption="✅Marhamat shourmalar menusi!!!", reply_markup=Shourmaa)  



@dp.callback_query_handler(text = "mini_mol_go'shtli")
async def exo(call: types.CallbackQuery):
    text = '''✅Narxi: 18 000 ming so'm
Kulcha, mol go'sht, pomidor, sous,  piyoz. 
Miqdorini tanlang...'''
    await call.message.answer_photo(
        photo=open('lavash/mol_gosh_shourma.jpg','rb'),
        caption=text, reply_markup=miqdor_shourma_mini_gosht)

@dp.callback_query_handler(text = "back_mini_gosht_shourma")
async def exo(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('lavash/mol_gosh_shourma.jpg','rb'),
        caption="✅Kategoriyalardan birini tanlang", reply_markup=miqdor_mol_gosh_shourma)

    
@dp.callback_query_handler(text = "classik_mol_go'shtlik")
async def exo(call: types.CallbackQuery):
    text ='''✅Narxi: 22 000 ming so'm
Kulcha, mol go'sht, pomidor, sous,  piyoz. 
Miqdorini tanlang...'''
    await call.message.answer_photo(
        photo = open('lavash/mol_gosh_shourma.jpg','rb'),
        caption=text, reply_markup=miqdor_shourma_classik_gosht)

@dp.callback_query_handler(text = "back_classik_gosht_shourma")
async def exo(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('lavash/mol_gosh_shourma.jpg','rb'),
        caption="✅Kategoriyalardan birini tanlang", reply_markup=miqdor_mol_gosh_shourma)

    
@dp.callback_query_handler(text = "shourma_tovuq")
async def exo(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('lavash/tovuq_gosh_shourma.jpg','rb'),
        caption="✅Kategoriyalardan birini tanlang", reply_markup=miqdor_tovuq_gosh_shourma)
    
@dp.callback_query_handler(text = "back_tovuq_go'shtlik")
async def exo(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('lavash/shourmalar.jpg','rb'),
        caption="✅Marhamat shourmalar menusi!!!", reply_markup=Shourmaa)  
  

@dp.callback_query_handler(text = "mini_tovuq_go'shtli")
async def exo(call: types.CallbackQuery):
    text = '''✅Narxi: 17 000 ming so'm
Kulcha, tovuq go'sht, pomidor, sous,  piyoz. 
Miqdorini tanlang...'''
    await call.message.answer_photo(
        photo=open('lavash/tovuq_gosh_shourma.jpg','rb'),
        caption=text, reply_markup =miqdor_shourma_mini_tovuq)

@dp.callback_query_handler(text = "back_mini_tovuq_shourma")
async def exo(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('lavash/tovuq_gosh_shourma.jpg','rb'),
        caption="✅Kategoriyalardan birini tanlang", reply_markup=miqdor_tovuq_gosh_shourma)

@dp.callback_query_handler(text = "classik_tovuq_go'shtlik")
async def exo(call: types.CallbackQuery):
    text = '''✅Narxi: 20 000 ming so'm
Kulcha, tovuq go'sht, pomidor, sous,  piyoz. 
Miqdorini tanlang...'''
    await call.message.answer_photo(
        photo = open('lavash/tovuq_gosh_shourma.jpg','rb'),
        caption=text, reply_markup=miqdor_shourma_classik_tovuq)  
    
@dp.callback_query_handler(text = "back_classik_tovuq_shourma")
async def exo(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('lavash/tovuq_gosh_shourma.jpg','rb'),
        caption="✅Kategoriyalardan birini tanlang", reply_markup=miqdor_tovuq_gosh_shourma)

@dp.callback_query_handler(text = "shourma_qalampir_mol")
async def exo(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('lavash/mol_gosh_qalampir.jpg','rb'),
        caption="✅Kategoriyalardan birini tanlang", reply_markup=miqdor_mol_qalampir_shourma)  


@dp.callback_query_handler(text = "back_shourma")
async def exo(call: types.CallbackQuery):
    await call.message.answer("Asosiy menu", reply_markup=menu_asosiy) 

@dp.callback_query_handler(text = "mini_mol_qalampir_go'shtli")
async def exo(call: types.CallbackQuery):
    text = '''✅Narxi: 23 000 ming so'm
Kulcha, mol go'sht, pomidor, sous,  piyoz. 
Miqdorini tanlang..'''
    await call.message.answer_photo(
        photo=open('lavash/mol_gosh_qalampir.jpg','rb'),
        caption=text, reply_markup=miqdor_shourma_mini_mol_goshtlar_qalampir) 

@dp.callback_query_handler(text = "back_mini_mol_qalampir_shourma")
async def exo(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('lavash/mol_gosh_qalampir.jpg','rb'),
        caption="✅Kategoriyalardan birini tanlang", reply_markup=miqdor_mol_qalampir_shourma) 
    
@dp.callback_query_handler(text = "classik_mol_qalampir_go'shtlik")
async def exo(call: types.CallbackQuery):
    text = '''✅Narxi: 25 000 ming so'm
Kulcha, mol go'sht, pomidor, sous,  piyoz. 
Miqdorini tanlang...'''
    await call.message.answer_photo(
        photo=open('lavash/mol_gosh_qalampir.jpg','rb'),
        caption=text, reply_markup=miqdor_shourma_classik_mol_goshtlar_qalampir) 
                
@dp.callback_query_handler(text = "back_classik_mol_qalampir_shourma")
async def exo(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('lavash/mol_gosh_qalampir.jpg','rb'),
        caption="✅Kategoriyalardan birini tanlang", reply_markup=miqdor_mol_qalampir_shourma) 
    
@dp.callback_query_handler(text = "shourma_qalampir_tovuq")
async def exo(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('lavash/tovuq_gosh_qalampir_shourma.jpg','rb'),
        caption="✅Kategoriyalardan birini tanlang", reply_markup=miqdor_tovuq_qalampir_shourma) 

@dp.callback_query_handler(text = "back_tovuq_qalampir_shourmaa")
async def exo(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('lavash/shourmalar.jpg','rb'),
        caption="✅Marhamat shourmalar menusi!!!", reply_markup=Shourmaa)  


@dp.callback_query_handler(text = "mini_tovuq_qalampir_go'shtli")
async def exo(call: types.CallbackQuery):
    text = '''✅Narxi: 20 000 ming so'm
Kulcha, tovuq go'sht, garimdori, pomidor, sous,  piyoz. 
Miqdorini tanlang..'''
    await call.message.answer_photo(
        photo=open("lavash/tovuq_gosh_qalampir_shourma.jpg",'rb'),
        caption=text, reply_markup=miqdor_shourma_mini_tovuq_qalampir) 

@dp.callback_query_handler(text = "back_mini_tovuq_qalampir_shourma")
async def exo(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('lavash/tovuq_gosh_qalampir_shourma.jpg','rb'),
        caption="✅Kategoriyalardan birini tanlang", reply_markup=miqdor_tovuq_qalampir_shourma) 

@dp.callback_query_handler(text = "classik_tovuq_qalampir_go'shtlik")
async def exo(call: types.CallbackQuery):
    text = '''✅Narxi: 24 000 ming so'm
Kulcha, tovuq go'sht,garimdori, pomidor, sous,  piyoz. 
Miqdorini tanlang...'''
    await call.message.answer_photo(
        photo=open('lavash/tovuq_gosh_qalampir_shourma.jpg','rb'),
        caption=text, reply_markup=miqdor_shourma_classik_tovuq_qalampir) 

@dp.callback_query_handler(text = "back__tovuq_qalampir_shourma")
async def exo(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('lavash/tovuq_gosh_qalampir_shourma.jpg','rb'),
        caption="✅Kategoriyalardan birini tanlang", reply_markup=miqdor_tovuq_qalampir_shourma) 

@dp.callback_query_handler(text = "donar")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Marhamat donarlar menusi!!!", reply_markup=Donarr) 

@dp.callback_query_handler(text = "back_donar")
async def exo(call: types.CallbackQuery):
    await call.message.answer("Asosiy menu", reply_markup=menu_asosiy) 

@dp.callback_query_handler(text = "go'shtli_donar")
async def exo(call: types.CallbackQuery):
    text = '''✅Narxi: 23 000 ming so'm 
Tarkib: Kulcha, mol go'sht, pomidor, sous,  piyoz.    
Miqdorini tanlang...'''
    await call.message.answer_photo(
        photo=open("lavash/donar_goshli.jpg",'rb'),
        caption=text, reply_markup=goshli_donarr) 

@dp.callback_query_handler(text = "back_gosht_donar")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Marhamat donarlar menusi!!!", reply_markup=Donarr) 

@dp.callback_query_handler(text = "tovuqli_donar")
async def exo(call: types.CallbackQuery):
    text = '''✅Narxi: 23 000 ming so'm 
Tarkib: Kulcha, tovuq go'sht, pomidor, sous, piyoz.     
Miqdorini tanlang...'''
    await call.message.answer_photo(
        photo=open('lavash/donar_tovuqli.jpg','rb'),
        caption=text, reply_markup=tovuqli_donarr) 

@dp.callback_query_handler(text = "back_tovuq_donar")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Marhamat donarlar menusi!!!", reply_markup=Donarr)     

@dp.callback_query_handler(text = "ichimliklarr")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Marhamat ichimliklar menusi!!!", reply_markup=ichimliklar)

@dp.callback_query_handler(text = "back_ichimliklar")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Marhamat ichimliklar menusi!!!", reply_markup=menu_asosiy)
            
@dp.callback_query_handler(text = "choylar_cofee")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!!", reply_markup=choy_cofeee)

@dp.callback_query_handler(text = "orqaga_choy_cofee")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Marhamat ichimliklardan birini tanlang!!!", reply_markup=ichimliklar)
                        
@dp.callback_query_handler(text = "choyylar")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Marhamat choylar menusi!!!", reply_markup=choy_only)

@dp.callback_query_handler(text = "orqaga_choy_only")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!!", reply_markup=choy_cofeee)

@dp.callback_query_handler(text = "kok_choy")
async def exo(call: types.CallbackQuery):
    text = '''✅Ko'k choy 
Narxi: 3 000 so'm!'''
    await call.message.answer_photo(
        photo = open('lavash/kok_choy.jpg','rb'),
        caption=text, reply_markup=choy_kok)
    
@dp.callback_query_handler(text = "back_choy_kuk")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Marhamat choylar menusi!!!", reply_markup=choy_only)
                        
@dp.callback_query_handler(text = "qora_choy")
async def exo(call: types.CallbackQuery):
    text = '''✅Qora choy 
Narxi: 3 000 so'm!'''
    await call.message.answer_photo(
        photo=open('lavash/kok_choy.jpg','rb'),
        caption=text, reply_markup=black_kok)
                        
@dp.callback_query_handler(text = "back_choy_black")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Marhamat choylar menusi!!!", reply_markup=choy_only)
                        
@dp.callback_query_handler(text = "limon_choyy")
async def exo(call: types.CallbackQuery):
    text = '''✅Limon choy 
Narxi: 5 000 so'm!'''
    await call.message.answer_photo(
        photo=open('lavash/limon_choy.jpg','rb'),
        caption=text, reply_markup=limon_choyy)

@dp.callback_query_handler(text = "back_choy_limon")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!!", reply_markup=choy_only)
                        
@dp.callback_query_handler(text = "Cofees")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Marhamat kofelar menusi!!!", reply_markup=cofee_only)

@dp.callback_query_handler(text = "orqaga_cofee_only")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!!", reply_markup=choy_cofeee)

@dp.callback_query_handler(text = "amerikano")
async def exo(call: types.CallbackQuery):
    text = '''✅Americano 
Narxi: 12 000 so'm!'''
    await call.message.answer_photo(
        photo=open("lavash/americano.jpg",'rb'),
        caption=text, reply_markup=americano_cofee)

@dp.callback_query_handler(text = "back_amiricano")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Marhamat kofelar menusi!!!", reply_markup=cofee_only)

@dp.callback_query_handler(text = "capuccino")
async def exo(call: types.CallbackQuery):
    text = '''✅Cappuccino 
Narxi: 18 000 so'm!'''
    await call.message.answer_photo(
        photo=open('lavash/cappucino.jpg','rb'),
        caption=text, reply_markup=capu_cofee)
                
@dp.callback_query_handler(text = "back_capu")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Marhamat kofelar menusi!!!", reply_markup=cofee_only)
                                                    
@dp.callback_query_handler(text = "cofe3v1")
async def exo(call: types.CallbackQuery):
    text = '''✅Cofe 3v1 
Narxi: 3 000 so'm!'''
    await call.message.answer_photo(
        photo=open('lavash/cofee_3vs1.jpg','rb'),
        caption=text, reply_markup=vs3_cofee)
                                       
@dp.callback_query_handler(text = "back_3vs")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Marhamat kofelar menusi!!!", reply_markup=cofee_only)
                                                    
@dp.callback_query_handler(text = "cofe_latte")
async def exo(call: types.CallbackQuery):
    text = '''✅Latte big 120g☕️
Narxi: 15 000 so'm!'''
    await call.message.answer_photo(
        photo=open('lavash/latte.jpg','rb'),
        caption=text, reply_markup=latte_kofeee)

@dp.callback_query_handler(text = "back_lattee")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Marhamat kofelar menusi!!!", reply_markup=cofee_only)
                                                
@dp.callback_query_handler(text = "yaxna_ichimliklar")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!!", reply_markup=yaxna_only)
                                        
@dp.callback_query_handler(text = "orqaga_yaxna_only")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Marhamat ichimliklardan birini tanlang!!!", reply_markup=ichimliklar)

@dp.callback_query_handler(text = "fantaa")
async def exo(call: types.CallbackQuery):
    text = '''✅Fanta
Narxi: 11 000 so'm!'''
    await call.message.answer_photo(
        photo=open("lavash/fanta.jpg",'rb'),
        caption=text, reply_markup=fanta_cha)

@dp.callback_query_handler(text = "back_fantacha")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!!", reply_markup=yaxna_only)

@dp.callback_query_handler(text = "sprite")
async def exo(call: types.CallbackQuery):
    text = '''✅Sprite
Narxi: 13 000 so'm!'''
    await call.message.answer_photo(
        photo=open("lavash/sprite.jpg",'rb'),
        caption=text, reply_markup=spritecha)

@dp.callback_query_handler(text = "back_sprite")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!!", reply_markup=yaxna_only)

@dp.callback_query_handler(text = "cola")
async def exo(call: types.CallbackQuery):
    text = '''✅Coca Cola
Narxi: 12 000 so'm!'''
    await call.message.answer_photo(
        photo=open("lavash/cola.jpg",'rb'),
        caption=text, reply_markup=colachala)

@dp.callback_query_handler(text = "back_coca")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!!", reply_markup=yaxna_only)

@dp.callback_query_handler(text = "nestle")
async def exo(call: types.CallbackQuery):
    text = '''✅Nestle
Narxi: 4 000 so'm!'''
    await call.message.answer_photo(
        photo=open('lavash/nestle.jpg','rb'),
        caption=text, reply_markup=nestle_water)

@dp.callback_query_handler(text = "back_water")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!!", reply_markup=yaxna_only)

@dp.callback_query_handler(text = "freesh")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Marhamat fresh sharbatlar menusi!!!", reply_markup=freesh_only)

@dp.callback_query_handler(text = "orqaga_fresh_only")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Marhamat ichimliklar menusi!!!", reply_markup=ichimliklar)

@dp.callback_query_handler(text = "blisss")
async def exo(call: types.CallbackQuery):
    text = '''✅Sok Bliss
Narxi: 10 000 so'm!'''
    await call.message.answer_photo(
        photo=open('lavash/bliss.jpg','rb'),
        caption=text, reply_markup=fresh_blis)

@dp.callback_query_handler(text = "back_blis")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Marhamat fresh sharbatlar menusi!!!", reply_markup=freesh_only)

@dp.callback_query_handler(text = "olma_sabzi")
async def exo(call: types.CallbackQuery):
    text = '''✅Fresh sabzi + olma
Narxi: 13 000 so'm!'''
    await call.message.answer_photo(
        photo=open('lavash/olma.jpg','rb'),
        caption=text, reply_markup=fresh_olma_sabzi)

@dp.callback_query_handler(text = "back_apple_carrot")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Marhamat fresh sharbatlar menusi!!!", reply_markup=freesh_only)

@dp.callback_query_handler(text = "pizza")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Marhamat pizzalar menusi!!!", reply_markup=pizzalar)

@dp.callback_query_handler(text = "back_pizza")
async def exo(call: types.CallbackQuery):
    await call.message.answer("Asosiy menu", reply_markup=menu_asosiy)

@dp.callback_query_handler(text = "ananaslik")
async def exo(call: types.CallbackQuery):
    text = '''✅Narxi: 65 000 so'm 
Пицца с Ананасом.
Пицца с Колбасой     33см.
Соус Томатный Для Пиццы
3 вида колбас 130гр.
Тонкое тесто
Кукуруза
Сыр 100гр.
ГрибыMiqdorini tanlang...'''
    await call.message.answer_photo(
        photo=open('lavash/ananaslik.jpg','rb'),
        caption=text, reply_markup=pizza_ananass)

@dp.callback_query_handler(text = "back_ananas_pizza")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Marhamat pizzalar menusi!!!", reply_markup=pizzalar)

@dp.callback_query_handler(text = "peperoni")
async def exo(call: types.CallbackQuery):
    text = '''✅Narxi: 75 000 ming so'm 
Пицца Пепперони
Пицца Пепперони     33см.
Соус Томатный Для Пиццы
Тонкое тесто.
Сыр 110 гр.
Miqdorini tanlang...'''
    await call.message.answer_photo(
        photo=open('lavash/peperoni.jpg','rb'),
        caption=text, reply_markup=pizza_peperoni)

@dp.callback_query_handler(text = "back_peperoni_pizza")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Marhamat pizzalar menusi!!!", reply_markup=pizzalar)

@dp.callback_query_handler(text = "margarita")
async def exo(call: types.CallbackQuery):
    text = '''✅Narxi: 60 000 ming so'm 
Пицца Маргарита
Пицца Маргарита  33см.
Соус Томатный Для Пиццы 
Тонкое тесто 
Сыр 100гр.
Помидоры
Miqdorini tanlang...'''
    await call.message.answer_photo(
        photo = open("lavash/margarita.jpg",'rb'),
        caption=text, reply_markup=pizza_margarita)

@dp.callback_query_handler(text = "back_margarita_pizza")
async def exo(call: types.CallbackQuery):
    await call.message.answer("✅Marhamat pizzalar menusi!!!", reply_markup=pizzalar)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)