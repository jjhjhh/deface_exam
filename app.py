#!/usr/bin/env python3
import subprocess

from flask import Flask, request, render_template, redirect

APP = Flask(__name__)


@APP.route('/')
def index():
    return render_template('index.html')


@APP.route('/ping', methods=['GET', 'POST'])
def ping():
    print('1')
    if request.method == 'POST':
        host = request.form.get('command','')
        cmd = f'"{host}"'
        try:
            print('2')
            output = subprocess.check_output(['/bin/sh', '-c', cmd], timeout=5)
            return render_template('flag.html', data=output.decode('utf-8'))
        except subprocess.TimeoutExpired:
            return render_template('index.html', data=f'Timeout!')
        except subprocess.CalledProcessError:
            return render_template('index.html', data="Error!")

    return render_template('index.html')


if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=5002)
