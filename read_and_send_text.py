import os
import json
from collections import Counter

def get_text_files_contents(): # User_Data 폴더 내부의 텍스트 파일들을 읽어 내용이 1.0, 2.0일 경우 배열에 할당후 반환
    folder_path = 'User_Data'
    file_contents = []

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path) and file_name.endswith('.txt'):
            with open(file_path, 'r') as file:
                contents = file.read().strip()
                if contents in ["1.0", "2.0"]:
                    file_contents.append(contents)
    return file_contents


def convert_list_to_json(lst):# 인자로 받은 배열을 json으로 변환. 
    """['1.0', '2.0', '1.0', '2.0', '1.0', '1.0', '1.0', '1.0', '1.0', '1.0']
    -> {"1.0": 8, "2.0": 2}"""
    counts = Counter(lst)
    json_data = {str(key): value for key, value in counts.items()}
    return json.dumps(json_data)

lst = get_text_files_contents()
json_result = convert_list_to_json(lst)
print(json_result)
