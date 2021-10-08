# Module
# Iseng Sloerrrrrrrrrrrrr
# Made By X - MrG3P5
import requests
from os import system as SYSS
from sys import exit as EXT

API = 'https://bins-su-api.now.sh/api/'
brblue = '\x1b[94m'
white = '\x1b[37m'

class main(object):

    @classmethod
    def check(cls, bins):
        if bins == '':
            EXT('[!] Bin Not Found!')
        else:
            cls.main(bins)
    @classmethod
    def main(cls, x):
        BINS = x
        x = {
            'author': 'X-MrG3P5',
            'url': 'https://bins-su-api.now.sh/api/'+x,
            'version': '0.1.1'
        }
        req = requests.get(x['url'])
        requests_json = req.json()
        if requests_json['result'] == 'false':
            EXT('[!] Bins Error!')
        else:
            r = requests_json['data']
            cls.main_check(r)
    @classmethod
    def main_check(cls, r):
        full_data = r
        data = {
            'Bin': full_data['bin'],
            'Vendor': full_data['vendor'],
            'Type': full_data['type'],
            'Level': full_data['level'],
            'Bank': full_data['bank'],
            'Country': full_data['country'],
        }
        print("""
{}[{}+{}] Bin     : {}{}
{}[{}+{}] Vendor  : {}{}
{}[{}+{}] Type    : {}{}
{}[{}+{}] Level   : {}{}
{}[{}+{}] Bank    : {}{}
{}[{}+{}] Country : {}{}{}""".format(brblue, white, brblue, white, data['Bin'], brblue, white, brblue, white, data['Vendor'], brblue, white, brblue, white, data['Type'], brblue, white, brblue, white, data['Level'], brblue, white, brblue, white, data['Bank'], brblue, white, brblue, white, data['Country'], brblue))

def banner():
    my_banner = """
 {}____  _              ____ _               _    
| __ )(_)_ __        / ___| |__   ___  ___| | __
|  _ \| | '_ \ _____| |   | '_ \ / _ \/ __| |/ /
| |_) | | | | |_____| |___| | | |  __/ (__|   < -> {}Made By
{}|____/|_|_| |_|      \____|_| |_|\___|\___|_|\_\-> {}X - MrG3P5{}""".format(brblue, white, brblue, white, brblue)
    print(my_banner)

if __name__=='__main__':
    banner()
    while True:
        try:
            BINS = input('\n[{}?{}] Bins : {}'.format(white, brblue, white))
            main.check(BINS)
        except KeyboardInterrupt:
            EXT('\nOke Byeeeeeee')
