from .WBits import WBits
from .event import Event


def _format_str_type(x):
    if isinstance(x, str):
        x = str(x).replace('"', '\\"')
        x = "\"" + x + "\""
    return x


class Control(WBits):
    def __init__(self, index=1):
        WBits.__init__(self)
        self.index = index

    def is_sw1_pressed(self):
        """
        判断按键SW1是否被按下
        :rtype: bool
        """

        command = 'control{}.is_sw1_pressed()'.format(self.index)
        value = self._get_command(command)
        return eval(value)

    def is_sw2_pressed(self):
        """
        判断按键SW2是否被按下
        :rtype: bool
        """

        command = 'control{}.is_sw2_pressed()'.format(self.index)
        value = self._get_command(command)
        return eval(value)

    def is_sw3_at_1(self):
        """
        判断SW3的是否在‘1’的位置（‘1’指的是电路上白色的数字）
        :rtype: bool
        """

        command = 'control{}.is_sw3_at_1()'.format(self.index)
        value = self._get_command(command)
        return eval(value)

    def get_sw4(self):
        """
        获取SW4的位置值
        :rtype: int
        """

        command = 'control{}.get_sw4()'.format(self.index)
        value = self._get_command(command)
        return eval(value)

    def is_m1_connected(self):
        """
        判断获取M1与COM是否导通一般的使用方法是：将连接线插入到控制模块的接头上，实验者一手握住COM线头（黑色），另一手握住M1或M2线头（黄或绿色）。导通时板子上相应指示灯会亮起
        :rtype: bool
        """

        command = 'control{}.is_m1_connected()'.format(self.index)
        value = self._get_command(command)
        return eval(value)

    def is_m2_connected(self):
        """
        判断获取M2与COM是否导通一般的使用方法是：将连接线插入到控制模块的接头上，实验者一手握住COM线头（黑色），另一手握住M1或M2线头（黄或绿色）。导通时板子上相应指示灯会亮起
        :rtype: bool
        """

        command = 'control{}.is_m2_connected()'.format(self.index)
        value = self._get_command(command)
        return eval(value)

    def set_m1_m2_sensitivity(self, limit):
        """
        设置M1和M2灵敏度灵敏度越高，is_m1_connected()和is_m2_connected()越容易返回True

        :param limit: 灵敏度：0~100
        """

        args = []
        args.append(str(limit))
        command = 'control{}.set_m1_m2_sensitivity({})'.format(
            self.index, ",".join(args))
        self._set_command(command)

    def get_m1_value(self):
        """
        获取M1的电阻率
        :rtype: float
        """

        command = 'control{}.get_m1_value()'.format(self.index)
        value = self._get_command(command)
        return eval(value)

    def get_m2_value(self):
        """
        获取M2的电阻率
        :rtype: float
        """

        command = 'control{}.get_m2_value()'.format(self.index)
        value = self._get_command(command)
        return eval(value)

    @property
    def source_sw1(self):
        return self, 'sw1', Event._BOOL_VALUE_TYPE

    @property
    def source_sw2(self):
        return self, 'sw2', Event._BOOL_VALUE_TYPE

    @property
    def source_sw3(self):
        return self, 'sw3', Event._BOOL_VALUE_TYPE

    @property
    def source_sw4(self):
        return self, 'sw4', Event._NUMBER_VALUE_TYPE

    @property
    def source_m1(self):
        return self, 'm1', Event._BOOL_VALUE_TYPE

    @property
    def source_m2(self):
        return self, 'm2', Event._BOOL_VALUE_TYPE

    @property
    def source_m1_value(self):
        return self, 'm1_value', Event._NUMBER_VALUE_TYPE

    @property
    def source_m2_value(self):
        return self, 'm2_value', Event._NUMBER_VALUE_TYPE
