#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/21 21:40
# @Author  : Yuki
import pystache


class TestMustache:
    def test_mustache(self):
        pystache.render(
            "Hi {{person}}!",
            {"person": "Yuki"}
        )
