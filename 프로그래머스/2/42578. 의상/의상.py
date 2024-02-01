def solution(clothes):
    hash = dict()
    num_category = []
    for name, category in clothes:
        if category in hash:
            hash[category].append(name);
        else:
            hash[category] = [name];
    print(hash)
    for key in hash:
        num_category.append(len(hash[key]))
    print(num_category)
    answer = 1
    for num in num_category:
        answer = answer * (num+1);
    return answer -1;
            
        