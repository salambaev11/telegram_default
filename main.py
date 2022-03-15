import telegram
from telegram import Update, chat
from telegram.callbackquery import CallbackQuery
from telegram.ext import (
    CallbackContext,
    Updater,
    PicklePersistence,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler
)
from telegram.files.document import Document
from idauto import TOKEN
from menu import main_menu_keyboard, resieve_air, resieve_oil, resieve_wash, ii_inline_menu , v_inline_menu, dt_inline_menu, o_inline_menu, wlenin_inline_menu, wsverdl_inline_menu,wperv_inline_menu,wokt_inline_menu,alen_inline_menu,aperv_inline_menu,asver_inline_menu,aokt_inline_menu
from buttons import main_buttons, oil_buttons, wash_buttons,air_buttons
import os

PORT = int(os.environ.get('PORT',5000))


OIL_REGEX = r"(?=("+(main_buttons[0])+r"))"# REGEX OF OIL
WASH_REGEX = r"(?=("+(main_buttons[1])+r"))"# REGEX OF WASH
AIR_REGEX = r"(?=("+(main_buttons[2])+r"))"# REGEX OF AIR
II_REGEX = r"(?=("+(oil_buttons[1])+r"))"# 92  BENZA
V_REGEX = r"(?=("+(oil_buttons[0])+r"))"# 95  BENZA
O_REGEX = r"(?=("+(oil_buttons[2])+r"))"# 80  BENZA
DT_REGEX = r"(?=("+(oil_buttons[3])+r"))"# dt BENZA
OILMENU_REGEX = r"(?=("+(oil_buttons[4])+r"))" # back menu oil
WASHMENU_REGEX = r"(?=("+(wash_buttons[4])+r"))" # back menu oil
AIRMENU_REGEX = r"(?=("+(air_buttons[4])+r"))" # back menu oil
WASHLEN_REGEX = r"(?=("+(wash_buttons[1])+r"))"# ленин мойка
WASHSVE_REGEX = r"(?=("+(wash_buttons[0])+r"))"# свер мойка
WASHPER_REGEX = r"(?=("+(wash_buttons[2])+r"))"# перв мойка
WASHOKT_REGEX = r"(?=("+(wash_buttons[3])+r"))"# окт мойка
CTOLEN_REGEX = r"(?=("+(air_buttons[1])+r"))"
CTOSVE_REGEX = r"(?=("+(air_buttons[0])+r"))"
CTOPER_REGEX = r"(?=("+(air_buttons[2])+r"))"
CTOOKT_REGEX = r"(?=("+(air_buttons[3])+r"))"
CTOZAP_REGEX = r"(?=("+(air_buttons[5])+r"))"









def start(update: Update, context: CallbackContext):#start

    context.bot.send_sticker(
        chat_id =update.effective_chat.id,
        sticker ='CAACAgIAAxkBAAEDym5h-o917NcYu85qQjIUgDNdS1SpKQAC7A0AAmOLRgyOU1GQ_5KePCME'
    )
    update.message.reply_text(
        "Добро пожаловать, {username} ".format(
            username=update.effective_user.first_name \
                if update.effective_user.first_name is not None \
                else update.effective_user.username
        ),
        reply_markup=main_menu_keyboard()
    )
def resive_oil_menu(update: Update, context: CallbackContext):#OIL BUTTONS 95
    update.message.reply_text(
        "Выбери какой бензин",
        reply_markup=resieve_oil()
    )
def resive_wash_menu(update: Update, context: CallbackContext):#WASH BUTTONS MOYKA
    update.message.reply_text(
        "Выбери нужный район",
        reply_markup=resieve_wash()
    )
def resive_air_menu(update: Update, context: CallbackContext):#AIR BUTTONS VULKAN
    update.message.reply_text(
        "Выбери нужный район",
        reply_markup=resieve_air()
    )
def resive_zapis_menu(update: Update, context: CallbackContext):#AIR BUTTONS VULKAN
    update.message.reply_text(
        """
Инструкция для записи:
Запись. ФИО Название автосервиса Номер телефона
Пример записи:
Запись. Адам Адамов Лукоил 0701234567 
(слово "Запись" обязательно!)       
""",
        reply_markup=resieve_air()
    )
def zapis(update: Update, context: CallbackContext):
    msg = update.message.text
    msg = msg.lower()
    username =(update.effective_user.name if update.effective_user.name is not None \
                else update.effective_user.username
                    )
    if msg[:6] == 'запись':
        context.bot.send_message(
            chat_id='@adm_guideauto',
            text=msg+'\nusername: '+username
        )
def menu(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Главное меню",
        reply_markup=main_menu_keyboard()
    )

def button(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == 'ii_gasprom':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
🛢️Газпром Нефть
💵Ценa: 59.90 сом
📍Адреса: https://clck.ru/arxDA            
            """
        )
    if query.data == 'ii_bpetroleum':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
🛢️ Bishkek Petroleum
💵Ценa: 58.90 сом
📍Адреса: https://clck.ru/aryBA            
            """
        )
    if query.data == 'ii_rusneft':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
🛢️РосНефть
💵Ценa: 59.90 сом
📍Адреса: https://clck.ru/aryBd            
            """
        )
    if query.data == 'ii_partnerneft':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
🛢️Партнёр Нефть
💵Ценa: 55.90 сом
📍Адреса: https://clck.ru/aryC3           
            """
        )



    if query.data == 'v_gasprom':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
🛢️Газпром Нефть
💵Ценa: 64.70 сом
📍Адреса: https://clck.ru/arxDA            
            """
        )
    if query.data == 'v_bpetroleum':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
🛢️ Bishkek Petroleum
💵Ценa: 64.50 сом
📍Адреса: https://clck.ru/aryBA            
            """
        )
    if query.data == 'v_rusneft':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
🛢️РосНефть
💵Ценa: 64.90 сом
📍Адреса: https://clck.ru/aryBd            
            """
        )
    if query.data == 'v_partnerneft':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
🛢️Партнёр Нефть
💵Ценa: 60.90 сом
📍Адреса: https://clck.ru/aryC3           
            """
        )


    if query.data == 'o_gasprom':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
🛢️Газпром Нефть
💵Ценa: 35.50 сом
📍Адреса: https://clck.ru/arxDA            
            """
        )
    if query.data == 'o_bpetroleum':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
🛢️ Bishkek Petroleum
💵Ценa: 34.90
📍Адреса: https://clck.ru/aryBA            
            """
        )
    if query.data == 'o_rusneft':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
🛢️РосНефть
💵Ценa: нет в продаже
📍Адреса: https://clck.ru/aryBd            
            """
        )
    if query.data == 'o_partnerneft':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
🛢️Партнёр Нефть
💵Ценa: 36.90 сом
📍Адреса: https://clck.ru/aryC3           
            """
        )


    if query.data == 'dt_gasprom':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
🛢️Газпром Нефть
💵Ценa: 52.50 сом
📍Адреса: https://clck.ru/arxDA            
            """
        )
    if query.data == 'dt_bpetroleum':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
🛢️ Bishkek Petroleum
💵Ценa: 59.50 сом
📍Адреса: https://clck.ru/aryBA            
            """
        )
    if query.data == 'dt_rusneft':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
🛢️РосНефть
💵Ценa: 60.00 сом
📍Адреса: https://clck.ru/aryBd            
            """
        )
    if query.data == 'dt_partnerneft':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
🛢️Партнёр Нефть
💵Ценa: 52.50 сом
📍Адреса: https://clck.ru/aryC3           
            """
        )

# LENIN Wash
    if query.data == 'w_atrium':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
💦Автомойка "Атриум"
📍​Адрес: https://go.2gis.com/lav5y 
⏰Режим работы: Ежедневно с 09:00 до 22:00
📞Номер: +996500040604 
💸Цена: ​Комплексная мойка от 300 сом
🗣Отзыв:⭐️⭐️⭐️⭐️
            """
        )
    if query.data == 'w_grand':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
💦Автомойка "Grand"
📍​Адрес: https://go.2gis.com/jjp0i
⏰Режим работы: Ежедневно с 08:00 до 23:00
📞Номер: +996505055725
💸Цена: ​Комплексная мойка от 200 сом
🗣Отзыв:⭐️⭐️⭐️⭐️


            """
        )
    if query.data == 'w_moby':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
💦Автомойка "Moby"
📍​Адрес: https://go.2gis.com/ogdhr
⏰Режим работы: Ежедневно с 08:00 до 21:00
📞Номер: +996558399161
💸Цена: ​Комплексная мойка от 250 сом
🗣Отзыв:⭐️⭐️⭐️⭐️

            """
        )
    if query.data == 'w_level':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
💦Автомойка "Level"
📍​Адрес: https://go.2gis.com/g4ni5s
⏰Режим работы: Круглосуточно
💸Цена: ​Комплексная мойка от 250 сом
🗣Отзыв:⭐️⭐️⭐️⭐️⭐️
            """
        )



# Sverdl Wash
    if query.data == 'w_washncar':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
💦Автомойка "Wash & car"
📍​Адрес:https://go.2gis.com/bwk8m
⏰Режим работы: Круглосуточно
📞Номер: +996777557778 
💸Цена: ​Комплексная мойка от 200 сом
🗣Отзыв:⭐️
            """
        )
    if query.data == 'w_mustang':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
💦Автомойка "Мустанг"
📍​Адрес: https://go.2gis.com/bg0x35
⏰Режим работы: Ежедневно с 09:00 до 22:00
📞Номер: +996706592020
💸Цена: ​Комплексная мойка от 450 сом
🗣Отзыв:⭐️⭐️⭐️

            """
        )
    if query.data == 'w_parlament':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
💦Автомойка "Parliament"
📍​Адрес: https://go.2gis.com/jtjzu
⏰Режим работы: Круглосуточно
📞Номер: +996999200005
💸Цена: ​Комплексная мойка от 200 сом
🗣Отзыв:⭐️⭐️⭐️⭐️⭐️
            """
        )
    if query.data == 'w_hiway':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
💦Автомойка "Hi way"
📍​Адрес: https://go.2gis.com/zsc9eu
⏰Режим работы: Ежедневно с 07:00 до 24:00
📞Номер: +996777987337
💸Цена: ​Комплексная мойка от 250 сом
🗣Отзыв:⭐️⭐️⭐️
            """
        )



# Pervomaiskiy Wash
    if query.data == 'w_mayak':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
💦Автомойка "Маяк"
📍​Адрес: https://go.2gis.com/0ap5pa
⏰Режим работы: Ежедневно с 08:00 до 24:00
📞Номер: +996 700224433 
💸Цена: ​Комплексная мойка от 200 сом
🗣Отзыв:⭐️⭐️⭐️⭐️⭐️
            """
        )
    if query.data == 'w_ds21':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
💦Автомойка "DS-21"
📍​Адрес: https://go.2gis.com/cfnte5
⏰Режим работы: Круглосуточно
📞Номер: +996703050707
💸Цена: ​Комплексная мойка от 200 сом
🗣Отзыв:⭐️⭐️

            """
        )
    if query.data == 'w_autoplus':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
💦Автомойка "Auto Plus"
📍​Адрес: https://go.2gis.com/0ua4fn
⏰Режим работы: Ежедневно с 08:00 до 24:00
📞Номер: +996709999099
💸Цена: ​Комплексная мойка от 250 сом
🗣Отзыв:⭐️⭐️⭐️⭐️⭐️
            """
        )
    if query.data == 'w_restart':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
💦Автомойка "Рестарт"
📍​Адрес: https://go.2gis.com/qwpj4x
⏰Режим работы: Ежедневно с 08:00 до 20:00
📞Номер: +996703000918
💸Цена: ​Комплексная мойка от 200 сом
🗣Отзыв:⭐️⭐️⭐️⭐️
            """
        )


#Oktyabrskiy Wash
    if query.data == 'w_xbiker':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
💦Автомойка "X-biker brothers"
📍​Адрес: https://go.2gis.com/k4vjx
⏰Режим работы: Круглосуточно
📞Номер: +996700000984
💸Цена: ​Комплексная мойка от 250 сом
🗣Отзыв:⭐️⭐️⭐️
            """
        )
    if query.data == 'w_leyka':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
💦Автомойка "Лейка"
📍​Адрес: https://go.2gis.com/oo55i
⏰Режим работы:Круглосуточно
📞Номер: +996222003002 
💸Цена: ​Комплексная мойка от 200 сом
🗣Отзыв:⭐️⭐️
            """
        )
    if query.data == 'w_moydodyr':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
💦Автомойка "Мойдодыр"
📍​Адрес: https://go.2gis.com/xddcr9
⏰Режим работы: Ежедневно с 09:00 до 23:00
📞Номер: +996550674965
💸Цена: ​Комплексная мойка от 250 сом
🗣Отзыв:⭐️⭐️⭐️
            """
        )
    if query.data == 'w_carcity':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
💦Автомойка "CAR CITY"
📍​Адрес: https://go.2gis.com/gq82sw
⏰Режим работы: Пн-Сб c 09:00 до 18:00
📞Номер: +996312427280
💸Цена: ​Комплексная мойка от 300 сом
🗣Отзыв:⭐️⭐️⭐️⭐️⭐️
            """
        )


# Lenin avtoservis
    if query.data == 'a_hybrid':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
🛠Автосервис "Hybrid Plus"
📍​Адрес: https://go.2gis.com/vdsw5
⏰Режим работы: Пн-Пт c 09:00 до 18:00
📞Номер: +996772070125
🗣Отзыв:⭐️⭐️⭐️⭐️⭐️
            """
        )
    if query.data == 'a_gdi':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
🛠Автосервис "GDI"
📍​Адрес: https://go.2gis.com/wsz51n
⏰Режим работы: Пн-Пт c 10:00 до 18:00
📞Номер: +996555790037
🗣Отзыв:⭐️⭐️⭐️⭐️⭐️
            """
        )
    if query.data == 'a_herkules':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
🛠Автосервис "Геркулес"
📍​Адрес: https://go.2gis.com/cptlt
⏰Режим работы: Ежедневно c 09:00 до 19:00
📞Номер: +996702900190
🗣Отзыв:⭐️⭐️⭐️⭐️
            """
        )
    if query.data == 'a_valemotors':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
🛠Автосервис "Vale Motors"
📍​Адрес: https://go.2gis.com/befxsa
⏰Режим работы: Пн-Пт c 09:00 до 20:00
📞Номер: +996700490090
🗣Отзыв:⭐️⭐️⭐️⭐️⭐️
            """
        )

    if query.data == 'a_quartz':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
🛠Автосервис "Total Quartz"
📍​Адрес: https://go.2gis.com/ukvc3
⏰Режим работы: Ежедневно с 09:00 до 20:00
📞Номер: +996555466371
🗣Отзыв:⭐️⭐️⭐️⭐️⭐️
            """
        )
    if query.data == 'a_autohouse':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
🛠Автосервис "AutoHouse"
📍​Адрес: https://go.2gis.com/qcvmf
⏰Режим работы: Пн-Cб c 09:30 до 20:00
📞Номер: +996 550779777
🗣Отзыв:⭐️⭐️⭐️⭐️⭐️
            """
        )
    if query.data == 'a_honda':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
🛠Автосервис "Honda Service"
📍​Адрес: https://go.2gis.com/d38f71
⏰Режим работы: Пн-Сб c 09:00 до 19:00
📞Номер: +996700123070
🗣Отзыв:⭐️⭐️⭐️⭐️⭐️
            """
        )
    if query.data == 'a_autolive':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
🛠Автосервис "Autolive"
📍​Адрес: https://go.2gis.com/v3rrv
⏰Режим работы: Пн-Сб c 09:00 до 18:00
📞Номер: +996770008934
🗣Отзыв:⭐️⭐️⭐️⭐️⭐️
            """
        )

    if query.data == 'a_ordo':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
🛠Автосервис "Ордо моторс"
📍​Адрес: https://go.2gis.com/uyr7a
⏰Режим работы: Пн-Сб c 09:00 до 20:00
📞Номер: +996700433883
🗣Отзыв:⭐️⭐️⭐️
            """
        )
    if query.data == 'a_injectplus':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
🛠Автосервис "InjectPlus"
📍​Адрес: https://go.2gis.com/aiepi
⏰Режим работы: Пн-Сб c 09:00 до 19:00
📞Номер: +996704808785
🗣Отзыв:⭐️⭐️⭐️⭐️⭐️
            """
        )
    if query.data == 'a_lukoil':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
🛠Автосервис "Лукойл"
📍​Адрес: https://go.2gis.com/xky33
⏰Режим работы: Пн-Сб c 09:00 до 19:00
📞Номер: +996555939517
🗣Отзыв:⭐️⭐️⭐️
            """
        )
    if query.data == 'a_anyway':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
🛠Автосервис "Anyway"
📍​Адрес: https://go.2gis.com/0e233
⏰Режим работы: Ежедневно 09:00 до 20:00
📞Номер: +996555152283
🗣Отзыв:⭐️⭐️⭐️⭐️
            """
        )

    if query.data == 'a_hype':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
🛠Автосервис "Hype Auto service"
📍​Адрес: https://go.2gis.com/s6w60
⏰Режим работы: Ежедневно 09:30 до 20:00
📞Номер: +996772555148
🗣Отзыв:⭐️⭐️⭐️⭐️
            """
        )
    if query.data == 'a_dilijans':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
🛠Автосервис "Дилижанс"
📍​Адрес: https://go.2gis.com/dmvui
⏰Режим работы: Пн-Сб 09:00 до 18:00
📞Номер: +996556908222
🗣Отзыв:⭐️⭐️⭐️⭐️
            """
        )
    if query.data == 'a_motor':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
🛠Автосервис "Мотор"
📍​Адрес: https://go.2gis.com/kz7qx
⏰Режим работы: Пн-Сб 09:00 до 18:00
📞Номер: +996703322430
🗣Отзыв:⭐️⭐️⭐️⭐️⭐️
            """
        )
    if query.data == 'a_java':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
🛠Автосервис "JAVA"
📍​Адрес: https://go.2gis.com/7kupkt
⏰Режим работы: Пн-Сб 09:00 до 20:00
📞Номер: +996556442804
🗣Отзыв:⭐️⭐️⭐️⭐️
            """
        )





updater = Updater(TOKEN, persistence=PicklePersistence(filename='bot_data'))
updater.dispatcher.add_handler(CommandHandler('start',start))#start

updater.dispatcher.add_handler(MessageHandler(# BENZIN
    Filters.regex(OIL_REGEX),
    resive_oil_menu
))
updater.dispatcher.add_handler(MessageHandler(# мойка
    Filters.regex(WASH_REGEX),
    resive_wash_menu
))
updater.dispatcher.add_handler(MessageHandler(# вулканизация
    Filters.regex(AIR_REGEX),
    resive_air_menu
))

updater.dispatcher.add_handler(MessageHandler(#92 benza
    Filters.regex(II_REGEX),
    ii_inline_menu
))
updater.dispatcher.add_handler(MessageHandler(# 95 benza
    Filters.regex(V_REGEX),
    v_inline_menu
))
updater.dispatcher.add_handler(MessageHandler(#gas 
    Filters.regex(O_REGEX),
    o_inline_menu
))
updater.dispatcher.add_handler(MessageHandler(#diesel
    Filters.regex(DT_REGEX),
    dt_inline_menu
))

updater.dispatcher.add_handler(MessageHandler(#diesel
    Filters.regex(WASHLEN_REGEX),
    wlenin_inline_menu
))
updater.dispatcher.add_handler(MessageHandler(#diesel
    Filters.regex(WASHSVE_REGEX),
    wsverdl_inline_menu
))
updater.dispatcher.add_handler(MessageHandler(#diesel
    Filters.regex(WASHPER_REGEX),
    wperv_inline_menu
))
updater.dispatcher.add_handler(MessageHandler(#diesel
    Filters.regex(WASHOKT_REGEX),
    wokt_inline_menu
))


updater.dispatcher.add_handler(MessageHandler(#diesel
    Filters.regex(CTOLEN_REGEX),
    alen_inline_menu
))
updater.dispatcher.add_handler(MessageHandler(#diesel
    Filters.regex(CTOSVE_REGEX),
    asver_inline_menu
))
updater.dispatcher.add_handler(MessageHandler(#diesel
    Filters.regex(CTOPER_REGEX),
    aperv_inline_menu
))
updater.dispatcher.add_handler(MessageHandler(#diesel
    Filters.regex(CTOOKT_REGEX),
    aokt_inline_menu
))



updater.dispatcher.add_handler(MessageHandler(#benzaMENU
    Filters.regex(OILMENU_REGEX),
    menu
))
updater.dispatcher.add_handler(MessageHandler(#MOYKAmenu
    Filters.regex(WASHMENU_REGEX),
    menu
))
updater.dispatcher.add_handler(MessageHandler(#VULKANmenu
    Filters.regex(AIRMENU_REGEX),
    menu
))
updater.dispatcher.add_handler(MessageHandler(#diesel
    Filters.regex(CTOZAP_REGEX),
    resive_zapis_menu
))
updater.dispatcher.add_handler(MessageHandler(#diesel
    Filters.regex,
    zapis
))


















updater.dispatcher.add_handler(CallbackQueryHandler(button))

updater.start_webhook(listen="0.0.0.0",
                        port=int(PORT),
                        url_path=TOKEN)
updater.bot.setWebhook(' https://botanos.herokuapp.com/' + '5110815131:AAHRfHqxUH7mkT1X4QASY1oWcgm6Cl8ROyI')
updater.idle()