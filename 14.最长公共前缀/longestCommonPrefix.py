def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""
    if len(strs) == 1:
        return strs[0]
    flag = True
    j = 0
    common_prefix = []
    while flag:

        for i in range(1, len(strs)):
            if strs[i-1] and strs[i]:
                if len(strs[i-1])>=j+1 and len(strs[i])>=j+1:

                    if strs[i][j] == strs[i-1][j]:
                        continue
                    else:
                        flag = False
                        break
                else:
                    flag = False
                    break
            else:
                flag = False
                break
        if flag:
            common_prefix.append(strs[0][j])
            j += 1
    if common_prefix:
        return ''.join(common_prefix)
    else:
        return ""

# 44ms算法
def longestCommonPrefix1(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        if len(strs) == 0:
            return ""
        for each in zip(*strs):
            if len(set(each)) == 1:
                res += each[0]
            else:
                return res
        return res

strs = ["c","c"]
print(longestCommonPrefix1(strs))