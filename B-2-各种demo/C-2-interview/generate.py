"""
1.采用算法：广度优先遍历，但是起点不确定，所以CanGenerate主要是寻找起点，复杂度为O(n),n为i*j 即节点个数
2.get_word函数按照左，左上，上，右上，右，右下，下，左下八个方向进行遍历，采用递归方式，最坏情况下，每条边都要遍历
时间复杂度为O(E),E为边的个数， 需要的队列长度不会超过顶点个数，空间复杂度为O(D),D为顶点个数
总体而言：时间复杂度：O(E),E为边的个数， 空间复杂度O(D)，D为顶点个数
"""


def CanGenerate(letters, word): #寻找起始节点
    max_x = len(letters[0])
    max_y = len(letters)
    first_letter = word[0]
    for i in range(max_y):
        for j in range(max_x):
            if letters[i][j] == first_letter:
                res = get_word(letters, word, 1, i, j, visited_list=[str(i)+str(j)], word_list=[letters[i][j]])
                if ''.join(res) == word:
                    return True
    return False


def get_word(letters, word, m, i, j, visited_list, word_list):
    if ''.join(word_list) == word or len(word_list) >= len(word): #递归出口
        return word_list
    max_x = len(letters[0])
    max_y = len(letters)
    visited_que = [] #已访问的索引值
    que = [] #已访问的节点
    if j-1 >= 0:
        if not str(i)+str(j-1) in visited_list: #左节点
            que.append(letters[i][j-1])
            visited_que.append([i, j-1])
        if i-1 >= 0:
            if not str(i-1) + str(j - 1) in visited_list: #左上
                que.append(letters[i-1][j - 1])
                visited_que.append([i-1, j - 1])
    if i-1 >= 0:
        if not str(i-1) + str(j) in visited_list: #上
            que.append(letters[i-1][j])
            visited_que.append([i-1, j])
        if j+1 < max_y:
            if not str(i-1)+str(j+1) in visited_list: #右上
                que.append(letters[i-1][j+1])
                visited_que.append([i-1, j+1])
    if j+1 < max_y:
        if not str(i) + str(j+1) in visited_list: #右
            que.append(letters[i][j+1])
            visited_que.append([i, j+1])
        if i+1 < max_x:
            if not str(i+1)+str(j+1) in visited_list: #右下
                que.append(letters[i+1][j + 1])
                visited_que.append([i+1, j + 1])
    if i+1 < max_x:
        if not str(i+1) + str(j) in visited_list: #下
            que.append(letters[i+1][j])
            visited_que.append([i+1, j])
        if j - 1 >= 0:
            if not str(i+1) + str(j - 1) in visited_list: #左下
                que.append(letters[i+1][j - 1])
                visited_que.append([i+1, j - 1])
    while len(que) > 0: #能够在相邻方向且没有访问过的节点que队列
        if que[0] == word[m]: #判断当前访问的节点是否与需要的下一个单词一致
            word_list.append(que[0])
            que.pop(0)
            i = visited_que[0][0]
            j = visited_que[0][1]
            visited_que.pop(0)
            visited_list.append(str(i)+str(j))
            print(word_list)
            print(visited_list)
            get_word(letters, word, len(word_list), i, j, visited_list, word_list) #进入下一层访问
            if ''.join(word_list) == word:
                break
        else:
            que.pop(0)
            visited_que.pop(0)
            if not que:
                return word_list.pop() #当前节点的下一层没有符合的，则回溯处理
    return word_list



letters = [ ['A', 'R', 'E'],['I', 'P', 'D'],['E', 'L', 'P'] ]
# word = "ARE"
# word = "APPLEB"
word = "AIELPP"
print(CanGenerate(letters, word))
