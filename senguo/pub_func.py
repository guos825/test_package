# 此 .py 文件为森果官方公共函数，谢绝外人随意使用
import datetime
import re

from senguo.new_dis_dict import dis_dict


# 特殊字符
class Emoji():
    @classmethod
    def filter_emoji(cls, keyword):
        keyword = re.compile(u'[\U00010000-\U0010ffff]').sub(u'', keyword)
        return keyword

    @classmethod
    def check_emoji(cls, keyword):
        reg_emoji = re.compile(u'[\U00010000-\U0010ffff]')
        has_emoji = re.search(reg_emoji, keyword)
        if has_emoji:
            return True
        else:
            return False

# 处理数字
class NumFunc:
    @staticmethod
    def is_number(number):
        return str(number).replace('.', '', 1).replace('-', '', 1).isdigit()

    @staticmethod
    def is_int(number):
        try:
            int(number)
            return True
        except:
            pass
        return False

    # 处理金额小数位数（1.00处理为1; 1.10处理为1.1; 1.111处理为1.11; 非数字返回0）
    @staticmethod
    def check_float(number, place=2):
        try:
            num = round(float(number), place)
        except:
            num = 0
        if num == int(num):
            num = int(num)
        return num

    # 将数字处理为整数（非数字返回0）
    @staticmethod
    def check_int(number):
        try:
            num = int(number)
        except:
            num = 0
        return num


# 省份城市转换
class ProvinceCityFunc:

    @staticmethod
    def get_city(code):
        try:
            # 直辖市和特别行政区不返回城市名称
            if code in [110000, 120000, 310000, 500000, 810000, 820000]:
                text = ""
            else:
                text = dis_dict.get("city_dict").get(str(code), "")
        except:
            text = ""
        return text

    @staticmethod
    def get_province(code):
        try:
            text = dis_dict.get("province_dict").get(str(code), "")
        except:
            text = ""
        return text

    # 新的省市区转化
    @staticmethod
    def city_to_province(code):
        province_code = int(code / 10000) * 10000
        if dis_dict.get("province_dict").get(str(province_code), None):
            return province_code
        else:
            return 0

    @staticmethod
    def district_to_province(code):
        province_code = int(code / 10000) * 10000
        if dis_dict.get("province_dict").get(str(province_code), None):
            return province_code
        else:
            return 0

    @staticmethod
    def district_to_city(code):
        # 直辖市和特别行政区返回省级编码
        if int(code / 10000) * 10000 in [110000, 120000, 310000, 500000, 810000, 820000]:
            return int(code / 10000) * 10000

        city_code = int(code / 100) * 100
        if dis_dict.get("city_dict").get(str(city_code), None):
            return city_code
        else:
            return 0

    @staticmethod
    def get_district(code):
        try:
            text = dis_dict.get("county_dict").get(str(code), "")
        except:
            text = ""
        return text

    @classmethod
    def get_area_name(cls, code):
        """获取省市县的名称"""
        province = cls.get_province(cls.district_to_province(code))
        city = cls.get_city(cls.district_to_city(code))
        district = cls.get_district(code)
        area_name = province + city + district
        return area_name


# 时间处理
class TimeFunc:

    # 将时间类型换为时间字符串
    @staticmethod
    def time_to_str(time, _type="all"):
        if _type == "all":
            fromat = "%Y-%m-%d %H:%M:%S"
        elif _type == "date":
            fromat = "%Y-%m-%d"
        elif _type == "hour":
            fromat = "%H:%M"
        elif _type == "month":
            fromat = "%m-%d"
        elif _type == "year":
            fromat = "%Y-%m"
        elif _type == "full":
            fromat = "%Y%m%d%H%M"
        elif _type =="no_year":
            fromat = "%m-%d %H:%M:%S"
        elif _type =="time":
            fromat = "%H:%M:%S"
        else:
            fromat = "%Y-%m-%d %H:%M"
        try:
            time_res = time.strftime(fromat)
        except:
            time_res = ""
        return time_res

    # 根据日历星期数获取周开始时间和结束时间
    @staticmethod
    def get_week_by_weeknum(year, weeknum, tzinfo=None):
        # 组装1月4日的日期
        day_jan_4th = datetime.date(year, 1, 4)
        # 今年第一个日历星期的开始日期
        first_week_start = day_jan_4th - datetime.timedelta(days=day_jan_4th.isoweekday()-1)
        # 所求星期的开始时间
        week_start = datetime.datetime.combine(
            first_week_start + datetime.timedelta(weeks=weeknum-1),
            datetime.time(),
        )
        week_end = week_start + datetime.timedelta(weeks=1)
        return week_start, week_end
