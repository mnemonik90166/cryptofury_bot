import curl
import sys

from selenium import webdriver
from datetime import datetime
from selenium.webdriver.chrome.options import Options
import telegram_send
import time
import urllib3
import requests
#browser exposes an executable file
#Through Selenium test we will invoke the executable file which will then #invoke actual browser

# chrome_options = Options()
# chrome_options.add_argument("--headless")
# driver = webdriver.Chrome(executable_path="C:\\Users\\wingate\\Desktop\\scripting_addons_blender\\addon\\addon\\chromedriver.exe", options = chrome_options)
while '1' == '1':
    driver = webdriver.Chrome(
        executable_path="D:\\NFT\\chromedriver_win32\\chromedriver.exe")
    # # to maximize the browser window
    driver.minimize_window()

    # #get method to launch the URL
    url1 = "https://www.tradingview.com/chart/?symbol=BINANCE%3AETCUSDT"
    driver.get("https://www.tradingview.com/chart/?symbol=BINANCE%3AETCUSDT")
    # to refresh the browser
    html = driver.page_source
    # https://www.binance.com/ru/trade/ARPA_USDT?layout=pro
    # time.sleep(2)
    # body > div.js-rootresizer__contents > div.layout__area--center > div.chart-container.single-visible.active > div.chart-container-border > div > table > tr:nth-child(1) > td.chart-markup-table.pane.pane--cursor-pointer > div > div.noWrap-1WIwNaDF.legend-1WIwNaDF.newCollapser-1WIwNaDF > div.legendMainSourceWrapper-1WIwNaDF > div.wrapper-3X2QgaDd.notAvailableOnMobile-3X2QgaDd.withoutBg-3X2QgaDd > div.apply-common-tooltip.button-3X2QgaDd.buyButton-3X2QgaDd > span.buttonText-3X2QgaDd

    # header = requests.get(str(url1))
    #
    # bigstring = header.text
    x = html.find('spreadQtyWrapper')
    # y = bigstring.find('paneControls')
    # vkladka = bigstring[x:y]
    y = html.find('buttonText')

    price = html[y:x]
    #print(price)
    atmprice = price[21:26]
    #print(atmprice)
    coin = url1[-18:]
    koin = 1 # how much coins i have
    buyprice = 55.04 # market price i buy coins, USDT
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    # print("date and time =", dt_string)

    # print('     ')
    # print(coin + ' ' + 'Price$: ' + atmprice + ' ' + '$' + '   ' + '-->' + ' ' + 'date: ' + dt_string + ' ' + 'ETC')
    # print('     ')

    atmprice_float = float(atmprice)
    #print(atmprice_float)
    # print(atmprice_float)
    z = koin * atmprice_float # in $ how much i have
    z_dot = str(koin * atmprice_float) # in $ how much i have
    # print(price)
    inv = koin * buyprice # in $ how much i spent to buy
    invest = str(koin * buyprice) # in $ how much i spent to buy
    invest_rub = str(koin * buyprice * 70) # in RUB how much i spent to buy
    delta = z - inv # MAIN VARIABLE - HOW MUCH I LOST IN $$$$$
    #print(z, z_dot, inv, invest, invest_rub, delta)

    # print('BUY PRICE: ' + str(buyprice) + '  ' + '$')
    # # print("coin + ' ' + 'Price$: ' + atmprice + ' ' + '$' + '   ' + '-->' + ' ' + 'date: ' + dt_string + 'ETC\n' ' \n' 'BUY PRICE: ' + str(buyprice) + '  '+ '$\n' 'YOU HOLD: ' + str(koin) + '  ' + coin[-9:] + ' ' + 'coins\n' 'YOUR INVESTMENTS\TOTAL: ' + invest[:-7] + ' ' + '$' + ' ' + '//' + ' ' + invest_rub[:-7] + ' ' + 'RUB\n' '\n' 'TOTAL VALUE IN $ RIGHT NOW: ' + z_dot[:-7] + ' ' + '$' + ' ' + '//' + ' ' + str(z*70)[:-7] + ' ' + 'RUB\n' '\n' 'YOU EARN/LOSE: ' + str(delta)[:-13] + ' ' + '$' + ' ' + '//' + ' ' + str(delta*70)[:-11] + ' ' + 'RUB'")
    # print('YOU HOLD: ' + str(koin) + '  ' + coin[-9:] + ' ' + 'coins')
    #
    # print('YOUR INVESTMENTS\TOTAL: ' + invest[:-7] + ' ' + '$' + ' ' + '//' + ' ' + invest_rub[:-7] + ' ' + 'RUB')
    # print('  ')
    # print('TOTAL VALUE IN $ RIGHT NOW: ' + z_dot[:-7] + ' ' + '$' + ' ' + '//' + ' ' + str(z * 70)[:-7] + ' ' + 'RUB')
    # print('  ')
    #
    # print('YOU EARNED: ' + str(delta)[:-13] + ' ' + '$' + ' ' + '//' + ' ' + str(delta * 70)[:-11] + ' ' + 'RUB')

    telegram_send.send(messages=[
        coin[-7:-4] + ' ' + 'Etherium Classic: ' + 'Price$: ' + atmprice + ' ' + '$' + '   ' + '-->' + ' ' + 'date: ' + dt_string + 'ETC\n' ' \n' 'BUY PRICE: ' + str(
            buyprice) + '  ' + '$\n' 'YOU HOLD: ' + str(koin) + '  ' + coin[
                                                                       -9:] + ' ' + 'coins\n' 'YOUR INVESTMENTS\TOTAL: ' + invest + ' ' + '$ ' + ' ' + '//' + ' ' + invest_rub[
                                                                                                                                                                  :6] + ' ' + 'RUB\n' '\n' 'TOTAL VALUE IN $ RIGHT NOW: ' + z_dot[:6] + ' ' + '$ ' + ' ' + '//' + ' ' + str(
            z * 70)[:6] + ' ' + 'RUB\n' 'YOU EARN / LOSE: ' + ' ' + str(delta)[:6] + ' ' + '$ ' + ' ' + '//' + ' ' + str(
            delta * 70)[:6] + ' ' + 'RUB'])

    driver.close()
    time.sleep(1)
# ETH CLASSIC BLOCK ENDS #
    driver = webdriver.Chrome(
        executable_path="D:\\NFT\\chromedriver_win32\\chromedriver.exe")
    # # to maximize the browser window
    driver.minimize_window()

    # #get method to launch the URL
    url1 = "https://www.tradingview.com/chart/?symbol=BINANCE%3AATOMUSDT"
    driver.get("https://www.tradingview.com/chart/?symbol=BINANCE%3AATOMUSDT")
    # to refresh the browser
    html = driver.page_source
    # https://www.binance.com/ru/trade/ARPA_USDT?layout=pro
    # time.sleep(2)
    # body > div.js-rootresizer__contents > div.layout__area--center > div.chart-container.single-visible.active > div.chart-container-border > div > table > tr:nth-child(1) > td.chart-markup-table.pane.pane--cursor-pointer > div > div.noWrap-1WIwNaDF.legend-1WIwNaDF.newCollapser-1WIwNaDF > div.legendMainSourceWrapper-1WIwNaDF > div.wrapper-3X2QgaDd.notAvailableOnMobile-3X2QgaDd.withoutBg-3X2QgaDd > div.apply-common-tooltip.button-3X2QgaDd.buyButton-3X2QgaDd > span.buttonText-3X2QgaDd

    # header = requests.get(str(url1))
    #
    # bigstring = header.text
    x = html.find('spreadQtyWrapper')
    # y = bigstring.find('paneControls')
    # vkladka = bigstring[x:y]
    y = html.find('buttonText')

    price = html[y:x]
    # print(price)
    atmprice = price[21:26]
    # print(atmprice)
    coin = url1[-18:]
    koin = 0.45  # how much coins i have
    buyprice = 39.49  # market price i buy coins, USDT
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    # print("date and time =", dt_string)

    # print('     ')
    # print(coin + ' ' + 'Price$: ' + atmprice + ' ' + '$' + '   ' + '-->' + ' ' + 'date: ' + dt_string + ' ' + 'ETC')
    # print('     ')

    atmprice_float = float(atmprice)
    # print(atmprice_float)
    # print(atmprice_float)
    z = koin * atmprice_float  # in $ how much i have
    z_dot = str(koin * atmprice_float)  # in $ how much i have
    # print(price)
    inv = koin * buyprice  # in $ how much i spent to buy
    invest = str(koin * buyprice)  # in $ how much i spent to buy
    invest_rub = str(koin * buyprice * 70)  # in RUB how much i spent to buy
    delta0 = z - inv  # MAIN VARIABLE - HOW MUCH I LOST IN $$$$$
    # print(z, z_dot, inv, invest, invest_rub, delta)

    # print('BUY PRICE: ' + str(buyprice) + '  ' + '$')
    # # print("coin + ' ' + 'Price$: ' + atmprice + ' ' + '$' + '   ' + '-->' + ' ' + 'date: ' + dt_string + 'ETC\n' ' \n' 'BUY PRICE: ' + str(buyprice) + '  '+ '$\n' 'YOU HOLD: ' + str(koin) + '  ' + coin[-9:] + ' ' + 'coins\n' 'YOUR INVESTMENTS\TOTAL: ' + invest[:-7] + ' ' + '$' + ' ' + '//' + ' ' + invest_rub[:-7] + ' ' + 'RUB\n' '\n' 'TOTAL VALUE IN $ RIGHT NOW: ' + z_dot[:-7] + ' ' + '$' + ' ' + '//' + ' ' + str(z*70)[:-7] + ' ' + 'RUB\n' '\n' 'YOU EARN/LOSE: ' + str(delta)[:-13] + ' ' + '$' + ' ' + '//' + ' ' + str(delta*70)[:-11] + ' ' + 'RUB'")
    # print('YOU HOLD: ' + str(koin) + '  ' + coin[-9:] + ' ' + 'coins')
    #
    # print('YOUR INVESTMENTS\TOTAL: ' + invest[:-7] + ' ' + '$' + ' ' + '//' + ' ' + invest_rub[:-7] + ' ' + 'RUB')
    # print('  ')
    # print('TOTAL VALUE IN $ RIGHT NOW: ' + z_dot[:-7] + ' ' + '$' + ' ' + '//' + ' ' + str(z * 70)[:-7] + ' ' + 'RUB')
    # print('  ')
    #
    # print('YOU EARNED: ' + str(delta)[:-13] + ' ' + '$' + ' ' + '//' + ' ' + str(delta * 70)[:-11] + ' ' + 'RUB')
    delta_sum = delta+delta0
    delta_sum_rub = delta_sum * 70

    telegram_send.send(messages=[
        coin[
        -7:-4] + ' ' + 'ATOM: ' + 'Price$: ' + atmprice + ' ' + '$' + '   ' + '-->' + ' ' + 'date: ' + dt_string + 'ETC\n' ' \n' 'BUY PRICE: ' + str(
            buyprice) + '  ' + '$\n' 'YOU HOLD: ' + str(koin) + '  ' + coin[
                                                                       -9:] + ' ' + 'coins\n' 'YOUR INVESTMENTS\TOTAL: ' + invest[
                                                                                                                           :6] + ' ' + '$ ' + ' ' + '//' + ' ' + invest_rub[
                                                                                                                                                                  :6] + ' ' + 'RUB\n' '\n' 'TOTAL VALUE IN $ RIGHT NOW: ' + z_dot[:6] + ' ' + '$ ' + ' ' + '//' + ' ' + str(
            z * 70) + ' ' + 'RUB\n' 'YOU EARN / LOSE: ' + ' ' + str(delta0)[:-13] + ' ' + '$ ' + ' ' + '//' + ' ' + str(
            delta0 * 70)[:6] + ' ' + 'RUB'])
    telegram_send.send(messages=['TOTAL CREDIT: ' + str(delta_sum)[:6] + ' $ ' + '//// ' + str(delta_sum_rub)[:6] + ' RUB']) # to do total money

    driver.close()
    time.sleep(600) # MODIFY AMOUNT IN SECONDS HOW OFTEN YOU WANNA TG BOT MESSAGES

