import json
# from datetime import datetime

def get_all_inf():
    with open('data2.json', encoding='utf8') as f:
        text = json.load(f)
        return text


def get_dates(data):
    list_data = []
    dates = get_all_inf()
    for day in dates:
        if data == day["day_week"]:
            list_data.append(day)
        # if len(list_data) == 0:
        #     raise ValueError
    return list_data


def subject(sub):
    list_sub = []
    subjects = get_all_inf()
    for subs in subjects:
        if sub == subs["discipline"]:
            list_sub.append(subs)
    return list_sub


def subject(s):
    list_sub = []
    subjects = get_all_inf()
    for subs in subjects:
        if s in subs["discipline"]:
            list_sub.append(s)
    return list_sub




# def day_now(datatime):
#     inform = get_all_inf()
#     for day in inform:
#         if day["day_week"] == datatime.data.today().weekday():
#             return day
#
#
# print(day_now(1))
