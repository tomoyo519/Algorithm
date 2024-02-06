def solution(genres, plays):
    hash = dict()
    hashN = dict()
    for i in range(len(genres)):
        if(genres[i] in hash):
            hash[genres[i]].append((plays[i], i))
            hashN[genres[i]] += plays[i]
        else:
            hash[genres[i]] = [(plays[i], i)]
            hashN[genres[i]] = plays[i]
 
    result = []
    rank = sorted(hashN, key = lambda x: hashN[x], reverse = True)
    for item in rank:
        temp = sorted(hash[item], key = lambda x:(x[0], -x[1]) , reverse = True)
        
        for i in range(2):
            result.append(temp[i][1])
            if len(hash[item])< 2 : break;
                                   
    return result

    