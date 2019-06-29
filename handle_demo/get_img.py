import re
import os
print (os.getcwd())
work_dir = os.getcwd()



print ("start ------------")
try:
    # 切分文件匹配
    pattern = r'image[\s\S]*?\n\n'
    file_list = []
    with open(f'{work_dir}/handle_demo/result_2.txt', 'r', encoding='UTF-8') as f:
        content = f.read()

    split_content = re.findall(pattern, content)

    for file_content in split_content:
        file_name = re.search(r'image.*(?=(.jpg)|(.JPG))', file_content)[0]
        file_list.append(file_name)
        with open(f'{work_dir}/handle_demo/original/{file_name}.txt', 'w', encoding='utf-8') as f_file:
            f_file.write(file_content)
    print ('success split')            

    # 单文件匹配
    pattern_1 = re.compile(r'[\w\W]*?right.*[\d+]')
    class_name_pattern = re.compile(r'.*dow')
    score_pattern = re.compile(r'(?<=score:\s)\d.\d+')
    left_pattern = re.compile(r'(?<=left:\s)\d+')
    top_pattern = re.compile(r'(?<=top:\s)\d+')
    right_pattern = re.compile(r'(?<=right:\s)\d+')
    bottom_pattern = re.compile(r'(?<=bottom:\s)\d+')
    for file in file_list:
        new_line = ['classname  score  left  top  right  bottom\n']
        with open(f'{work_dir}/handle_demo/original/{file}.txt', 'r', encoding='UTF-8') as f_original:
            with open(f'{work_dir}/handle_demo/result/{file}.txt', 'w', encoding='UTF-8') as f_result:
                one_file_content = f_original.read()
                one_file_content = re.sub(r'[\w\W]*target.*', '', one_file_content)
                split_one_file = re.findall(pattern_1, one_file_content)
                for one_line in split_one_file:
                    
                    class_name = re.search(class_name_pattern, one_line)[0]
                    score = re.search(score_pattern, one_line)[0]
                    left = re.search(left_pattern, one_line)[0]
                    top = re.search(top_pattern, one_line)[0]
                    right = re.search(right_pattern, one_line)[0]
                    bottom = re.search(bottom_pattern, one_line)[0]
                    new_line.append(f'{class_name} {score} {left} {top} {right} {bottom}\n')
                f_result.writelines(new_line)
except Exception as e:
    print (e)
print ("end---------------")