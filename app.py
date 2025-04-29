#!/usr/bin/env python3
import subprocess

from flask import Flask, request, render_template, redirect, jsonify

APP = Flask(__name__)

PRICES = {
    "써티즈 배지": 500,
    "써티즈 티셔츠": 17000,
    "아이스 아메리카노": 1500,
    "맥북": 5500000
}

@APP.route('/')
def index():
    return render_template('index.html')


@APP.route('/testing')
def testing():
    return render_template('testing.html')


@APP.route('/store')
def store():
    return render_template('store.html')


@APP.route('/api/click', methods=['POST'])
def click():
    data = request.get_json()
    balance = int(data.get('balance'))
    product = data.get('product')
    
    if (product not in PRICES.keys()):
        return jsonify({"earned": "없는 상품입니다."})
    

    print(balance, product)


    if (balance > PRICES[product] ):
        if(product=="맥북"):
            return jsonify({"earned": product+" 이(가) 구매되었습니다!🎉 Flag{WEB_HACKING_BASIC}"})
        else:
            return jsonify({"earned": product+" 이(가) 구매되었습니다!🎉"})
    else:
        return jsonify({"earned": "코인이 부족합니다."})

@APP.route('/ping', methods=['GET', 'POST'])
def ping():
    print('1')
    if request.method == 'POST':
        host = request.form.get('command','')
        cmd = f'"{host}"'
        try:
            print('2')
            output = subprocess.check_output(['/bin/sh', '-c', cmd], timeout=5)
            return render_template('testing.html', data=output.decode('utf-8'))
        except subprocess.TimeoutExpired:
            return render_template('testing.html', data=f'Timeout!')
        except subprocess.CalledProcessError:
            return render_template('testing.html', data="Error!")

    return render_template('testing.html')


if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=5000,debug=True)
