import datetime as dt
import make

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

def combine2List(list1, delimeter, list2):
    # assumed that both list has same length
    # to make list look like => item1, :, item2
    result = list()
    for i in range(len(list1)):
        result.append([list1[i], delimeter, list2[i]])
    return result

def gridDisplay(list_, column=1):
    # ex: gridDisplay([a,b,c,d,e,f,g], column=2)
    # result:
    # [a, c, e, g]
    # [b, d, f,]
    result = list()
    size = len(list_)
    item_per_column = int(math.ceil(float(size) / column))
    start = 0
    end = start + item_per_column
    # initializing
    for i in range(item_per_column):
        result.append(list())
    
    # put the actual data
    while start + item_per_column < size:
        index = 0
        for i in range(start, end):
            if isinstance(list_[i], (list, tuple)):
                result[index].extend(list_[i])
            else:
                result[index].append(list_[i])
            index += 1
        start = end
        end = start + item_per_column
    
    index = 0
    for i in range(start, size):
        if isinstance(list_[i], (list, tuple)):
            result[index].extend(list_[i])
        else:
            result[index].append(list_[i])
        index += 1
    return result