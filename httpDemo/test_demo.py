#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/21 20:39
# @Author  : Yuki
import json

import requests
from jsonpath import jsonpath
from hamcrest import *
from jsonschema import validate


class TestDemo:
    def test_get(self):
        r = requests.get('https://httpbin.testing-studio.com/get')
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200

    def test_query(self):
        payload = {
            "level": 1,
            "name": "Yuki"
        }
        r = requests.get("https://httpbin.testing-studio.com/get", params=payload)
        print(r.text)
        assert r.status_code == 200

    def test_post_form(self):
        payload = {
            "level": 1,
            "name": "Yuki"
        }
        r = requests.post("https://httpbin.testing-studio.com/post", data=payload)
        print(r.text)
        assert r.status_code == 200

    def test_headers(self):
        r = requests.get('https://httpbin.testing-studio.com/get', headers={"name": "Yuki"})
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200
        assert r.json()["headers"]["Name"] == "Yuki"

    # json断言
    def test_post_json(self):
        payload = {
            "level": 1,
            "name": "Yuki"
        }
        r = requests.post("https://httpbin.testing-studio.com/post", json=payload)
        print(r.text)
        assert r.status_code == 200
        assert r.json()["json"]["level"] == 1

    # jsonpath 断言
    def test_hogwarts_json(self):
        r = requests.post("https://home.testing-studio.com/categories.json")
        print(r.text)
        assert r.status_code == 200
        assert r.json()["category_list"]["categories"][0]["name"] == "社区治理"
        print(jsonpath(r.json(), "$..name"))
        assert jsonpath(r.json(), "$..name")[0] == "社区治理"

    # hamcrest 断言
    def test_hamcrest(self):
        r = requests.post("https://home.testing-studio.com/categories.json")
        print(r.text)
        assert r.status_code == 200
        assert_that(r.json()["category_list"]["categories"][0]["name"], equal_to("社区治理"))

    # schema 断言
    def test_jsonschema(self):
        r = requests.post("https://home.testing-studio.com/categories.json")
        data = r.json()
        with open("./demo_schema.json", encoding="utf-8") as f:
            schema = json.load(f)
            print(schema)
            validate(data, schema=schema)

    def test_headers_cookies(self):
        url = "http://httpbin.testing-studio.com/cookies"
        headers = {
            'User-Agent': 'Yuki'
        }
        cookie_data = {
            "Yuki": "girl",
            "Momo": "babe"
        }
        r = requests.get(url=url, headers=headers, cookies=cookie_data)
        print(r.request.headers)
