# SimpleChat
ローカルネットワークで利用できるシンプルなチャット  
(Vue.js,Flask,Mongo DBの練習で制作)  

## Image 
<img width="300" alt="screenshot" src="https://user-images.githubusercontent.com/56730772/72658208-0d399300-39f1-11ea-8089-db9bbdc78ecf.png">


## Requirements
* python 3.7.3

## Install
コマンドラインで以下を実行
$ python -m venv simplechat  
$ ./simplechat/Scripts/activate  
$ pip -r requirements.txt  

## Start
1. 自分のIPアドレスをsimplechat.jsのAPIURLに書き込む -> var APIURL = http://123.45.67.890:8000  
2. SimpleChat/にてコマンドラインで以下を実行  
$ ./simplechat/Scripts/activate  
$ python server.py  
$ python -m http.server 8080
3. http://123.45.67.890:8080/simplechat.htmlにアクセス  

## End
* server.pyを終了する
* python http.serverを終了する
* コマンドラインで$./simplechat/Scripts/deactivate を実行する
