from random import shuffle

sample_data = [
    {
        "id": 404,
        "name": "Second",
        "parentCategoryId": 0,
    },
    {
        "id": 401,
        "name": "First",
        "parentCategoryId": 0,
    },
    
    {
        "id": 403,
        "name": "First - 2",
        "parentCategoryId": 401,
    },
    {
        "id": 402,
        "name": "First - 1",
        "parentCategoryId": 401,
    },
    {
        "id": 600,
        "name": "First - 3",
        "parentCategoryId": 401,
    },
    {
        "id": 702,
        "name": "Second - 2",
        "parentCategoryId": 404,
    },
    {
        "id": 405,
        "name": "Second - 1",
        "parentCategoryId": 404,
    },
    {
        "id": 407,
        "name": "Second - 1 - 2",
        "parentCategoryId": 405,
    },
    {
        "id": 406,
        "name": "Second - 1 - 1",
        "parentCategoryId": 405,
    },
    # TODO: 재귀함수를 이용하여 정렬해야 함
    {
        "id": 409,
        "name": "Second - 1 - 1 - 1",
        "parentCategoryId": 406,
    },
    {
        "id": 410,
        "name": "Second - 1 - 1 - 2",
        "parentCategoryId": 409,
    },
]

def sort_by_id(d_list:list):
    for i in range(len(d_list)):
        for j in range(i+1, len(d_list)):
            if d_list[j]["id"] < d_list[i]["id"]:
                temp = d_list[j]
                d_list[j] = d_list[i]
                d_list[i] = temp
    return d_list

def merge(parent_list:list, child_list:dict, pre=[]):
    sorted_list = []
    for parent in parent_list:
        if parent not in pre:
            sorted_list.append(parent)
            pre.append(parent)
        temp = sort_by_id(child_list[str(parent["id"])])
        for item in temp:
            if item in parent_list:
                pre.extend(sorted_list)
                temp = merge(parent_list[parent_list.index(item):], child_list, pre)
                sorted_list.extend(temp)
            else:
                if item not in sorted_list and item not in pre:
                    sorted_list.append(item)
    return sorted_list

def main():
    # 샘플 데이터 랜덤하게 섞기
    shuffle(sample_data)

    # 알고리즘 시작
    sorted_list = []
    parent_list = []
    pid_list    = []
    child_temp  = {}
    for item in sample_data:
        if item["parentCategoryId"] == 0:
            parent_list.append(item)
            pid_list.append(item["id"])
        else:
            p_id = str(item["parentCategoryId"])
            try:
                child_temp[p_id]
            except:
                child_temp[p_id] = []
            child_temp[p_id].append(item)
            if item["parentCategoryId"] not in pid_list:
                for temp_item in sample_data:
                    if temp_item["id"] == item["parentCategoryId"]:
                        parent_list.append(temp_item)
                        pid_list.append(temp_item["id"])
    
    sort_by_id(parent_list)
    sorted_list = merge(parent_list, child_temp)
            
    # 출력
###############################################################################
    # for item in parent_list:
    #     print(item)
    # print("------------------------------------------------------------")
    # for pid in child_temp:
    #     for item in child_temp[pid]:
    #         print(item)
    print("------------------------------------------------------------")
    for item in sorted_list:
        print(item)
    print("------------------------------------------------------------")
    print(len(sample_data), "/", len(sorted_list))
###############################################################################


if __name__ == "__main__":
    main()