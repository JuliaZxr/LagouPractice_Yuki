#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure
import pytest


def test_attach_text():
    allure.attach("这是一个纯文本", attachment_type=allure.attachment_type.TEXT)

def test_attach_html():
    allure.attach("<body>这是一段html body块</body>", "html测试块", attachment_type=allure.attachment_type.HTML)

def test_attach_photo():
    # 当allure报告中图片显示不出来时，请注意图片路径：将\修改为/或者\\
    # 图片应该是attach.file
    allure.attach.file("G:/PycharmProjects/LagouPractice_Yuki/testing/1.jpg", name="这是一张图片", attachment_type=allure.attachment_type.JPG)
