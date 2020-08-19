# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    app.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: HoangPham <HoangPham@student.42.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/08/19 10:33:04 by HoangPham         #+#    #+#              #
#    Updated: 2020/08/19 21:19:25 by HoangPham        ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from flask import Flask, jsonify, request
import json
import re
import collections

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

def setInitialValues(textLength, response, string):
    textLength['withSpaces'] = len(string)
    textLength['withoutSpaces'] = len(string) - string.count(' ')
    response["textLength"] = textLength
    response['wordCount'] = len(string.split())
    response["characterCount"] = []

def getStrAlphaAndSort(string):
    strAlpha = "".join(re.findall("[a-zA-Z]+", string))
    strAlpha = strAlpha.lower()
    strAlpha = "".join(sorted(strAlpha))

    return strAlpha

def setResponseCharacterCount(response, strAlpha):
    arr = []
    for c in strAlpha:
        if c not in arr:
            arr.append(c)
            characterCount = strAlpha.count(c)
            character = { c:characterCount }
            response["characterCount"].append(character)


@app.route("/analyze", methods=['GET', 'POST'])

def analyze():
    textLength = {}
    response = collections.OrderedDict()

    if request.method == 'POST':

        # Get data from POST request body
        data = request.get_json()

        if 'text' in data:
            string = data['text']
            if type(string) is not str:
                return jsonify(message="Wrong Data Type, expected string"), 404
 
            # Set dictionary's initial key and values
            setInitialValues(textLength, response, string)

            # Get all English alphabet character from string and sort them
            strAlpha = getStrAlphaAndSort(string)

            # Get string's characters and number of occurences of each character, set them to response['characterCount']
            setResponseCharacterCount(response, strAlpha)

            return jsonify(response)
        else:
            return jsonify(message="Unsupported data's key"), 404
    else:
        return jsonify(message="this API only support POST request :("), 404

if __name__ == '__main__':
    app.run(debug=True)
