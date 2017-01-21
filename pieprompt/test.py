# -*- coding: utf-8 -*-
import importlib.util


spec = importlib.util.spec_from_file_location("piepompt.part", "/home/markl/.config/pieprompt/hipart.py")
foo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(foo)
