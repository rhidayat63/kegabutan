import datetime as dt

def monthReformat(str_date):
    # for this type date format 04 November 2019 18:40:05
    month_list = ['January','February','March','April','May','June','July','August','September','October','November','December']
    temp = str_date.lower()
    for item in month_list:
        if item.lower() in temp:
            temp = temp.replace(item.lower(), str(month_list.index(item) + 1).zfill(2))
            break
    return temp

def dateTrip(date_input):
    try:
        temp = monthReformat(date_input)
        return dt.datetime.strptime(temp, '%d %m %Y %H:%M:%S')
    except:
        return date_input

def combine2List(list1, list2):
    # assumed that both list has same length
    # to make list look like => item1, :, item2
    result = list()
    for i in range(len(list1)):
        result.append([list1[i], ':', list2[i]])
    return result