import telegram
from buttons import main_buttons, oil_buttons, wash_buttons, air_buttons
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, chat
from telegram.ext import (
    CallbackContext,
    Updater,
    PicklePersistence,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler
)


def main_menu_keyboard():#меню кнопки

    keyboard = ([
        [telegram.KeyboardButton(main_buttons[0]),],
        [
            telegram.KeyboardButton(main_buttons[1]),
            telegram.KeyboardButton(main_buttons[2]),
        ]
    ])
    return telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=False
    )

def resieve_oil():#BENZIN_BUTTONS
    keyboard = ([
    [telegram.KeyboardButton(oil_buttons[0]),
    telegram.KeyboardButton(oil_buttons[1]),
    ],
    [
        
        telegram.KeyboardButton(oil_buttons[2]),
        telegram.KeyboardButton(oil_buttons[3]),
        
    ],
    [telegram.KeyboardButton(oil_buttons[4])]
    
])
    return telegram.ReplyKeyboardMarkup(
    keyboard, resize_keyboard=True, one_time_keyboard=False
)
def resieve_wash():#WASH_BUTTONS
    keyboard = ([
    [telegram.KeyboardButton(wash_buttons[0]),
    telegram.KeyboardButton(wash_buttons[1]),
    ],
    [
        
        telegram.KeyboardButton(wash_buttons[2]),
        telegram.KeyboardButton(wash_buttons[3]),
        
    ],
    [telegram.KeyboardButton(wash_buttons[4])]
    
])
    return telegram.ReplyKeyboardMarkup(
    keyboard, resize_keyboard=True, one_time_keyboard=False
)
def resieve_air():#AIR_BUTTONS
    keyboard = ([
    [telegram.KeyboardButton(air_buttons[0]),
    telegram.KeyboardButton(air_buttons[1]),
    ],
    [
        
        telegram.KeyboardButton(air_buttons[2]),
        telegram.KeyboardButton(air_buttons[3]),
        
    ],
    [telegram.KeyboardButton(air_buttons[5])],
    [telegram.KeyboardButton(air_buttons[4])]
    
])
    return telegram.ReplyKeyboardMarkup(
    keyboard, resize_keyboard=True, one_time_keyboard=False
)
# OIL PRICE
def ii_inline_menu(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton('Газпром Нефть', callback_data='ii_gasprom'),
            InlineKeyboardButton('Bishkek Petroleum', callback_data='ii_bpetroleum'),
        ],
        [
            InlineKeyboardButton('Роснефть', callback_data='ii_rusneft'),
            InlineKeyboardButton('Партнер Нефть', callback_data='ii_partnerneft'),

            
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "Выберите АЗС",
        reply_markup=reply_markup
    )
def v_inline_menu(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton('Газпром Нефть', callback_data='v_gasprom'),
            InlineKeyboardButton('Bishkek Petroleum', callback_data='v_bpetroleum'),
        ],
        [
            InlineKeyboardButton('Роснефть', callback_data='v_rusneft'),
            InlineKeyboardButton('Партнер Нефть', callback_data='v_partnerneft'),

            
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "Выберите АЗС",
        reply_markup=reply_markup
    )
def o_inline_menu(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton('Газпром Нефть', callback_data='o_gasprom'),
            InlineKeyboardButton('Bishkek Petroleum', callback_data='o_bpetroleum'),
        ],
        [
            InlineKeyboardButton('Роснефть', callback_data='o_rusneft'),
            InlineKeyboardButton('Партнер Нефть', callback_data='o_partnerneft'),

            
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "Выберите АЗС",
        reply_markup=reply_markup
    )
def dt_inline_menu(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton('Газпром Нефть', callback_data='dt_gasprom'),
            InlineKeyboardButton('Bishkek Petroleum', callback_data='dt_bpetroleum'),
        ],
        [
            InlineKeyboardButton('Роснефть', callback_data='dt_rusneft'),
            InlineKeyboardButton('Партнер Нефть', callback_data='dt_partnerneft'),

            
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "Выберите АЗС",
        reply_markup=reply_markup
    )
# WASHING AUTO
def wlenin_inline_menu(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton('Атриум', callback_data='w_atrium'),
            InlineKeyboardButton('Grand', callback_data='w_grand'),
        ],
        [
            InlineKeyboardButton('Moby', callback_data='w_moby'),
            InlineKeyboardButton('Level', callback_data='w_level'),

            
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "Выберите автомойку",
        reply_markup=reply_markup
    )
def wsverdl_inline_menu(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton('Wash & car', callback_data='w_washncar'),
            InlineKeyboardButton('Мустанг', callback_data='w_mustang'),
        ],
        [
            InlineKeyboardButton('Parliament', callback_data='w_parlament'),
            InlineKeyboardButton('Hi way', callback_data='w_hiway'),

            
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "Выберите автомойку",
        reply_markup=reply_markup
    )
def wperv_inline_menu(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton('Маяк', callback_data='w_mayak'),
            InlineKeyboardButton('DS-21', callback_data='w_ds21'),
        ],
        [
            InlineKeyboardButton('Auto Plus', callback_data='w_autoplus'),
            InlineKeyboardButton('Рестарт', callback_data='w_restart'),

            
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "Выберите автомойку",
        reply_markup=reply_markup
    )
def wokt_inline_menu(update: Update, context: CallbackContext):


    keyboard = [
        [
            InlineKeyboardButton('X-biker brothers', callback_data='w_xbiker'),
            InlineKeyboardButton('Лейка', callback_data='w_leyka'),
        ],
        [
            InlineKeyboardButton('Мойдодыр', callback_data='w_moydodyr'),
            InlineKeyboardButton('CAR CITY', callback_data='w_carcity'),

            
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "Выберите автомойку",
        reply_markup=reply_markup
    )


def alen_inline_menu(update: Update, context: CallbackContext):


    keyboard = [
        [
            InlineKeyboardButton('Hybrid Plus', callback_data='a_hybrid'),
            InlineKeyboardButton('GDI', callback_data='a_gdi'),
        ],
        [
            InlineKeyboardButton('Геркулес', callback_data='a_herkules'),
            InlineKeyboardButton('Vale Motors', callback_data='a_valemotors'),

            
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "Выберите автосервис",
        reply_markup=reply_markup
    )
def asver_inline_menu(update: Update, context: CallbackContext):


    keyboard = [
        [
            InlineKeyboardButton('Total Quartz', callback_data='a_quartz'),
            InlineKeyboardButton('AutoHouse', callback_data='a_autohouse'),
        ],
        [
            InlineKeyboardButton('Honda Service', callback_data='a_honda'),
            InlineKeyboardButton('Autolive', callback_data='a_autolive'),

            
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "Выберите автосервис",
        reply_markup=reply_markup
    )
def aperv_inline_menu(update: Update, context: CallbackContext):


    keyboard = [
        [
            InlineKeyboardButton('Ордо Моторс', callback_data='a_ordo'),
            InlineKeyboardButton('InjectPlus', callback_data='a_injectplus'),
        ],
        [
            InlineKeyboardButton('Лукойл', callback_data='a_lukoil'),
            InlineKeyboardButton('Anyway', callback_data='a_anyway'),

            
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "Выберите автосервис",
        reply_markup=reply_markup
    )
def aokt_inline_menu(update: Update, context: CallbackContext):


    keyboard = [
        [
            InlineKeyboardButton('Hype Auto service', callback_data='a_hype'),
            InlineKeyboardButton('Дилижанс', callback_data='a_dilijans'),
        ],
        [
            InlineKeyboardButton('Мотор', callback_data='a_motor'),
            InlineKeyboardButton('JAVA', callback_data='a_java'),

            
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "Выберите автосервис",
        reply_markup=reply_markup
    )