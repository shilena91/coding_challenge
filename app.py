# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    application.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: HoangPham <pham.hoang1591@gmail.com>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/08/19 10:33:04 by HoangPham         #+#    #+#              #
#    Updated: 2020/08/19 10:33:04 by HoangPham        ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from flask import Flask, jsonify, request
import json
import re
import collections


app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

@app.route("/analyze", methods=['GET', 'POST'])

def analyze():
    textLength = {}
    response = collections.OrderedDict()


    data = request.get_json()
    analyzeData = data['text']
    textLength['withSpaces'] = len(analyzeData)
    textLength['withoutSpaces'] = len(analyzeData) - analyzeData.count(' ')
    strAlpha = "".join(re.findall("[a-zA-Z]+", analyzeData))
    strAlpha = strAlpha.lower()
    strAlpha = "".join(sorted(strAlpha))
    response["textLength"] = textLength
    response['wordCount'] = len(analyzeData.split())
    response["characterCount"] = []
    arr = []
    for c in strAlpha:
        if c not in arr:
            arr.append(c)
            characterCount = strAlpha.count(c)
            character = { c:characterCount }
            response["characterCount"].append(character)
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True) 
