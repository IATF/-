#encoding:utf-8
# author: sunfei
# create date: 2019-06-27

"""这是一个数组模块，class: PyArray()
"""


class PyArray(object):
    """
    这是一个数组
    """
    def __init__(self, data_type, init_data=None):
        self._type = data_type
        if init_data is None:
            self._init_data = []
        else:
            self._init_data = init_data
        if not isinstance(self._init_data, list):
            raise ValueError("初始数组必须为list。")

    def __setitem__(self, key, value):
        self._init_data[key] = value

    def __getitem__(self, item):
        return self._init_data[item]

    def __iter__(self):
        for item in self._init_data:
            yield item

    def __len__(self):
        return len(self._init_data)

    def __str__(self):
        return repr(self._init_data)

    def insert(self, index, value):
        if not isinstance(value, self._type):
            raise ValueError(f"请指定一个有效的值，值得类型只能是{self._type}")
        if index < len(self) and index >= 0:
            self._init_data.insert(index, value)
        elif index == len(self):
            self._init_data.append(value)
        else:
            raise ValueError("请指定一个有效的index")


if __name__ == "__main__":
    my_array = PyArray(int)
    my_array.insert(0, 2)
    print(my_array)
