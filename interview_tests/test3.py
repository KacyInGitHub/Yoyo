# -*- coding:utf-8 -*-
# author: lining3
# date: 2020/11/18 3:03 下午
# file: test3.py
# IDE: PyCharm


class JsonDiff:
    def __init__(self, json1, json2):
        self.path = '#'
        self.data_cmp_res = []
        self.frame_cmp_res = []
        self.compare(json1, json2, self.path)

    def compare(self, json1, json2, path):
        try:
            if not isinstance(json1, (list, tuple, dict)):
                if not json1 == json2:
                    msg = f"{path}:json1 value{str(json1)}, json2 value{str(json2)}"
                    self.data_cmp_res.append(msg)
            elif isinstance(json1, (list, tuple)):
                if not isinstance(json2, (list, tuple)):
                    raise IndexError(f"json2 数据格式错误")
                if len(json1) >= len(json2):
                    for i, v in enumerate(json1):
                        try:
                            if i < len(json2):
                                self.compare(v, json2[i], f'{path}[{i}]')
                            else:
                                raise IndexError(f"json2 缺少数据:{path}[{i}]")
                        except Exception as e:
                            if IndexError:
                                self.frame_cmp_res.append(f"json2 结构或数据缺失: {e.args}")
                            else:
                                self.frame_cmp_res.append("未知异常")
                else:
                    for i, v in enumerate(json2):
                        try:
                            if i < len(json1):
                                self.compare(v, json1[i], f'{path}[{i}]')
                            else:
                                raise IndexError(f"json1 缺少数据:{path}[{i}]")
                        except Exception as e:
                            if IndexError:
                                self.frame_cmp_res.append(f"json1 结构或数据缺失: {e.args}")
                            else:
                                self.frame_cmp_res.append("未知异常")
            else:
                if not isinstance(json2, dict):
                    raise IndexError(f"json2 不是dict:{path}")
                if len(json1) >= len(json2):
                    for k, v in json1.items():
                        try:
                            if k in json2.keys():
                                self.compare(v, json2.get(k), f"{path}.{str(k)}")
                            else:
                                raise IndexError(f"json2 缺失数据:{path}.{str(k)}")
                        except Exception as e:
                            if IndexError:
                                self.frame_cmp_res.append(f"结构或数据缺失:{e.args}")
                            else:
                                self.frame_cmp_res.append(f"未知异常:{e.args}")
                else:
                    for k, v in json2.items():
                        try:
                            if k in json1.keys():
                                self.compare(json1.get(k), v, f"{path}.{str(k)}")
                            else:
                                raise IndexError(f"json1 缺失数据:{path}.{str(k)}")
                        except Exception as e:
                            if IndexError:
                                self.frame_cmp_res.append(f"结构或数据缺失:{e.args}")
                            else:
                                self.frame_cmp_res.append(f"未知异常:{e.args}")
        except Exception as e:
            self.frame_cmp_res.append(f"未知异常{e.args}")
