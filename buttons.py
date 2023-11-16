from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

lang = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("🇷🇺Руский"),
            KeyboardButton("🇺🇿O'zbekcha"),
            KeyboardButton("🇺🇸English")
        ]
    ],
    resize_keyboard=True
)

info_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Buyurtma berish🧑‍💻")
        ],

        [ 
            KeyboardButton("Biz bilan aloqa☎️"),
            KeyboardButton("Sozlamalar⚙️")
        ],      
        [
            KeyboardButton("Tilni o'zgartirish")    
        ]
    ],
    resize_keyboard=True
)

info_ru = ReplyKeyboardMarkup(

    keyboard=[
        [
            KeyboardButton("Заказ🧑‍💻")
        ],    
        [ 
            KeyboardButton("Свяжитесь с нами☎️"),
            KeyboardButton("Настройки⚙️")
        ],
        [    
            KeyboardButton("Изменить язык")
        ],    

        ],
    
    resize_keyboard=True
)

info_en = ReplyKeyboardMarkup(

    keyboard=[
        [
            KeyboardButton("Order🧑‍💻")
        ],    
        [ 
            KeyboardButton("Contact us☎️"),
            KeyboardButton("Settings⚙️")
        ],
        [    
            KeyboardButton("Change language")
        ],    

        ],
    
    resize_keyboard=True
)

menu_asosiy = InlineKeyboardMarkup(
    inline_keyboard=[
     [
        InlineKeyboardButton(text="Lavash🌯", callback_data="lavash"),
        InlineKeyboardButton(text="Hot-dog🌭", callback_data="hot-dog")
     ],
     [
        InlineKeyboardButton(text="Clab Sendvich🥪", callback_data="clab"),
        InlineKeyboardButton(text="Shourma🌮", callback_data="shourma")

     ],
     [
        InlineKeyboardButton(text="Burger🍔", callback_data="burger"),
        InlineKeyboardButton(text="Donar🍱", callback_data="donar")

     ],
     [
         InlineKeyboardButton(text = "Gazaklar🍟", callback_data="gazaklar"),
         InlineKeyboardButton(text= "Ichimliklar🍹", callback_data="ichimliklarr")
     ],
     [
         InlineKeyboardButton(text="Desertlar🍰", callback_data="desertlar"),
         InlineKeyboardButton(text="Pizza🍕", callback_data="pizza")
     ],

     
    
    ]
    
 )

lavash_menu = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="Mol go'shtlik🥩", callback_data="mol_go'sht"),
        InlineKeyboardButton(text="Qalampirli mol go'shtlik", callback_data="qalampirli_mol_go'shtli")
    ],
    [
        InlineKeyboardButton(text="Tovuq go'shtlik🍗", callback_data="tovuq_go'shtlik"),
        InlineKeyboardButton(text="Qalampirlik tovuq go'shtilik", callback_data="qalampirli_tovuq_go'shtlik")
    ],
    [
        InlineKeyboardButton(text="Pishloqli mol go'shtlik", callback_data="pishloqli_mol_go'shtlik"),
        InlineKeyboardButton(text="Pishloqli tovuq go'shtlik", callback_data="pishloqli_tovuq_go'shtlik")
    ],
    [
        InlineKeyboardButton(text="Flitter🥬", callback_data="flitter")
    ],    
    [
        InlineKeyboardButton(text="◀️Ortga", callback_data="back")
    ]
    ]
)

clab_sendvich = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Classic Clab sendvich👍", callback_data="clab_sendvich"),
            InlineKeyboardButton("Tovuqli Sandvich👍👍", callback_data="tovuq_sand")
        ],
        [
            InlineKeyboardButton("◀️Ortga", callback_data="back_sand")
        ]
    ]
)

Burgerss = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Gamburger👍", callback_data="gamburger"),
            InlineKeyboardButton("Chizburger👍👍", callback_data="chizburger")
        ],
        [
            InlineKeyboardButton("◀️Ortga", callback_data="back_burg")
        ]
    ]
)

Gazaklarr = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Fries 15g👍👍", callback_data="free"),
            InlineKeyboardButton("Kartoshka Derevyanski👍👍", callback_data="derevyan")
        ],
        [
            InlineKeyboardButton(text="Gurunch katta👍👍", callback_data="guruch_katta"),
            InlineKeyboardButton(text="Gurunch kichik👍👍", callback_data="guruch_kichik")
        ],
        [
            InlineKeyboardButton("◀️Ortga", callback_data="back_gazak")
        ]
    ]
)

Desertlarr = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Assalim👍👍", callback_data="asalim"),
            InlineKeyboardButton("Qulupnay👍👍", callback_data="qulupnay")
        ],
        [
            InlineKeyboardButton(text="Choko👍👍", callback_data="choko"),
        ],
        [
            InlineKeyboardButton("◀️Ortga", callback_data="back_desert")
        ]
    ]
)

Hot_dogs = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Hot Dog Baget dabl👍👍", callback_data="baget"),
            InlineKeyboardButton("Classik👍👍", callback_data="classik_hot")
        ],
        [
            InlineKeyboardButton(text="Korolevskiy👍👍", callback_data="korolev"),
            InlineKeyboardButton(text="Tovuqli👍👍", callback_data="Tovuq_hot"),
        ],
        [
            InlineKeyboardButton("◀️Ortga", callback_data="back_hotdog")
        ]
    ]
)

Shourmaa = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Mol go'shtli shourma👍👍", callback_data="shourma_mol"),
            InlineKeyboardButton("Tovuq go'shtli shourma👍👍", callback_data="shourma_tovuq")
        ],
        [
            InlineKeyboardButton(text="Mol go'shtli (qalampir) shourma👍👍", callback_data="shourma_qalampir_mol"),
            InlineKeyboardButton(text="Tovuq go'shtli (qalampir) shourma👍👍", callback_data="shourma_qalampir_tovuq"),
        ],
        [
            InlineKeyboardButton("◀️Ortga", callback_data="back_shourma")
        ]
    ]
)

Donarr = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Go'shtli donar👍👍", callback_data="go'shtli_donar"),
            InlineKeyboardButton(text="Tovuq go'shtli👍👍", callback_data="tovuqli_donar")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_donar")
        ]
    ]
)     

ichimliklar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Choy va kofe👍👍", callback_data="choylar_cofee"),
            InlineKeyboardButton(text="Yaxna ichimliklar👍👍", callback_data="yaxna_ichimliklar")
        ],
        [
            InlineKeyboardButton(text="Fresh va tabiiy soklar👍👍", callback_data="freesh")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_ichimliklar")
        ]
    ]
)     
pizzalar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ananaslik🍍🍕", callback_data="ananaslik"),
            InlineKeyboardButton(text="Peperoni🍕", callback_data="peperoni")
        ],
        [
            InlineKeyboardButton(text="Margarita🍕", callback_data="margarita")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_pizza")
        ]
    ]
)     

lavash_mol_goshtli = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Mini👍", callback_data="mini_mol"),
            InlineKeyboardButton(text="Classik👍👍", callback_data="classik_mol")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="orqa")
        ]
    ]
)

miqdor = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_mini")
        ]   
    ]


)

miqdor1 = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_classik")
        ]   
    ]


)

lavash_tovuq_goshtlik = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Mini👍", callback_data="mini_tovuq"),
            InlineKeyboardButton(text="Classik👍👍", callback_data="classik_tovuq")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data='back_chicken')
        ]
    ]
)

miqdor_mini = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_tovuq")
        ]   
    ]


)
 
miqdor_classik_chicken = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_chick")
        ]   
    ]


)

lavash_pishloqli = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Mini👍", callback_data="mini_pishloq"),
            InlineKeyboardButton(text="Classik👍👍", callback_data="classik_pishloq")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_sir")
        ]
    ]
)

miqdor_mini_sir = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_mini_sir")
        ]   
    ]


)

miqdor_classik_sir = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_classic_sir")
        ]   
    ]


)

lavash_qalampirli = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Mini👍", callback_data="mini_qalampir"),
            InlineKeyboardButton(text="Classik👍👍", callback_data="classik_qalampir")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_qalampir")
        ]
    ]
)

miqdor_mini_qalampir = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_mini_qalampir")
        ]   
    ]
)
  
miqdor_classik_qalampir = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_classik_qalampir")
        ]   
    ]


)

lavash_qalampir_tovuq = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Mini👍", callback_data="mini_qalampir_tovuq"),
            InlineKeyboardButton(text="Classik👍👍", callback_data="classik_qalampir_tovuq")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_qalampir_tovuq")
        ]
    ]
)

miqdor_mini_tovuq = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_mini_qalampir_tovuq")
        ]   
    ]


)
miqdor_classik_tovuq_qalampir = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_classik_qalampir_tovuq")
        ]   
    ]


)

lavash_pishloqli_tovuq = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Mini👍", callback_data="mini_pishloq_tovuq"),
            InlineKeyboardButton(text="Classik👍👍", callback_data="classik_pishloq_tovuq")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_pishloq_tovuq")
        ]
    ]
)

miqdor_mini_tovuq_pishloq = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_classik_qalampir_pishloq")
        ]   
    ]
)
miqdor_classic_tovuq_pishloq = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_classik_classic_pishloq")
        ]   
    ]

)

lavash_flitter = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Mini👍", callback_data="mini_flitter"),
            InlineKeyboardButton(text="Classik👍👍", callback_data="classik_flitter")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_flitter")
        ]
    ]
)

mini_flitter = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_mini_flitter")
        ]   
    ]

)
classic_flitter = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_classik_flitter")
        ]   
    ]

)

miqdor_clab_classik = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_clabb")
        ]   
    ]


)

miqdor_clab_tovuqli = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_clabb_tovuq")
        ]   
    ]


)

miqdor_gamburger = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_gamb")
        ]   
    ]


)

miqdor_chizburger = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_chiz")
        ]   
    ]
)

miqdor_frie = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_frie")
        ]   
    ]
)

miqdor_dera = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_dera")
        ]   
    ]
)

miqdor_katta_gurunch = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_katta_grunch")
        ]   
    ]
)

miqdor_kichik_gurunch = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_kichik_grunch")
        ]   
    ]
)
miqdor_assalim = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_assalim_desert")
        ]   
    ]
)

miqdor_qulupnay = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_qulupnay_desert")
        ]   

    ]
)

miqdor_choco = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_choco_desert")
        ]   
        
    ]
)

miqdor_baget = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_hot_baget")
        ]   
        
    ]
)

miqdor_classik_hot = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_hot_classik")
        ]   
        
    ]
)

miqdor_korolev_hot = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_korolev_classik")
        ]   
        
    ]
)

miqdor_tovuq_hot = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_tovuq_classik")
        ]   
        
    ]
)



miqdor_mol_gosh_shourma = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Mini👍", callback_data="mini_mol_go'shtli"),
            InlineKeyboardButton(text="Classik👍👍", callback_data="classik_mol_go'shtlik")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_mol_go'shtlik")
        ]
    ]
)

miqdor_shourma_mini_gosht = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_mini_gosht_shourma")
        ]   
        
    ]
)

miqdor_shourma_classik_gosht = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_classik_gosht_shourma")
        ]   
        
    ]
)

miqdor_tovuq_gosh_shourma = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Mini👍", callback_data="mini_tovuq_go'shtli"),
            InlineKeyboardButton(text="Classik👍👍", callback_data="classik_tovuq_go'shtlik")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_tovuq_go'shtlik")
        ]
    ]
)

miqdor_shourma_mini_tovuq = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_mini_tovuq_shourma")
        ]   
        
    ]
)

miqdor_shourma_classik_tovuq = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_classik_tovuq_shourma")
        ]   
        
    ]
)

miqdor_mol_qalampir_shourma = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Mini👍", callback_data="mini_mol_qalampir_go'shtli"),
            InlineKeyboardButton(text="Classik👍👍", callback_data="classik_mol_qalampir_go'shtlik")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_tovuq_go'shtlik")
        ]
    ]
)

miqdor_shourma_mini_mol_goshtlar_qalampir = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_mini_mol_qalampir_shourma")
        ]   
        
    ]
)

miqdor_shourma_classik_mol_goshtlar_qalampir = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_classik_mol_qalampir_shourma")
        ]   
        
    ]
)

miqdor_tovuq_qalampir_shourma = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Mini👍", callback_data="mini_tovuq_qalampir_go'shtli"),
            InlineKeyboardButton(text="Classik👍👍", callback_data="classik_tovuq_qalampir_go'shtlik")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_tovuq_qalampir_shourmaa")
        ]
    ]
)

miqdor_shourma_mini_tovuq_qalampir = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_mini_tovuq_qalampir_shourma")
        ]   
        
    ]
)

miqdor_shourma_classik_tovuq_qalampir = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back__tovuq_qalampir_shourma")
        ]   
        
    ]
)

goshli_donarr = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_gosht_donar")
        ]   
        
    ]
)

tovuqli_donarr = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_tovuq_donar")
        ]   
        
    ]
)

choy_cofeee = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Choylar👍", callback_data="choyylar"),
            InlineKeyboardButton(text="Kofelar👍👍", callback_data="Cofees")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="orqaga_choy_cofee")
        ]
    ]
)

choy_only = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ko'k choy👍", callback_data="kok_choy"),
            InlineKeyboardButton(text="Qora choy👍👍", callback_data="qora_choy")
        ],
        [
            InlineKeyboardButton(text="Limon choy👍👍", callback_data="limon_choyy")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="orqaga_choy_only")
        ]
    ]
)

choy_kok = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_choy_kuk")
        ]   
        
    ]
)

black_kok = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_choy_black")
        ]   
        
    ]
)

limon_choyy = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_choy_limon")
        ]   
        
    ]
)

cofee_only = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Americano👍👍", callback_data="amerikano"),
            InlineKeyboardButton(text="Cappucino👍👍", callback_data="capuccino")
        ],
        [
            InlineKeyboardButton(text="Cofe 3vs1👍👍", callback_data="cofe3v1"),
            InlineKeyboardButton(text="Latte👍👍", callback_data="cofe_latte")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="orqaga_cofee_only")
        ]
    ]
)

americano_cofee = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_amiricano")
        ]   
        
    ]
)

latte_kofeee = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_lattee")
        ]   
        
    ]
)

capu_cofee = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_capu")
        ]   
        
    ]
)

vs3_cofee = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_3vs")
        ]   
        
    ]
)

yaxna_only = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Fanta🍹", callback_data="fantaa"),
            InlineKeyboardButton(text="Sprite🥤", callback_data="sprite")
        ],
        [
            InlineKeyboardButton(text="Coca-cola🍷", callback_data="cola"),
            InlineKeyboardButton(text="Nestle🍹", callback_data="nestle")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="orqaga_yaxna_only")
        ]
    ]
)

fanta_cha = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_fantacha")
        ]   
        
    ]
)

spritecha= InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_sprite")
        ]   
        
    ]
)

colachala= InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_coca")
        ]   
        
    ]
)

nestle_water= InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_water")
        ]   
        
    ]
)

freesh_only = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Bliss🧃🧃", callback_data="blisss"),
            InlineKeyboardButton(text="Olma va sabzi🥂", callback_data="olma_sabzi")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="orqaga_fresh_only")
        ]
    ]
)

fresh_blis= InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_blis")
        ]   
        
    ]
)

fresh_olma_sabzi = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_apple_carrot")
        ]   
        
    ]
)

pizza_ananass = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_ananas_pizza")
        ]   
        
    ]
)

pizza_peperoni = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_peperoni_pizza")
        ]   
        
    ]
)

pizza_margarita = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="◀️Ortga", callback_data="back_margarita_pizza")
        ]   
        
    ]
)