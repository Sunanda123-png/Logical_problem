"""Write a Python script to concatenate the following dictionaries to create a new one."""


def concat_dic(dic1, dic2,dic3):
    dic = {}
    for element in (dic1, dic2, dic3):
        dic.update(element)
    return dic

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
print(concat_dic(dic1,dic2,dic3))