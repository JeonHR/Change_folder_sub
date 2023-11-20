import os

def rename_files_in_folder(folder_path):
    # 폴더 내 모든 파일과 폴더 목록 가져오기
    items = os.listdir(folder_path)

    for item in items:
        item_path = os.path.join(folder_path, item)

        # 폴더인 경우 재귀적으로 함수 호출
        if os.path.isdir(item_path): ## 
            rename_files_in_folder(item_path)

        # 파일인 경우 이름 변경
        elif os.path.isfile(item_path):
            folder_name = os.path.basename(folder_path)
            filename, file_extension = os.path.splitext(item)
            new_filename = f"{filename}_{folder_name}{file_extension}"
            new_item_path = os.path.join(folder_path, new_filename)

            # 이름 변경
            os.rename(item_path, new_item_path)
            print(f"이름 변경: {item} -> {new_filename}")

# 폴더 경로 지정
folder_path = "./"

# 함수 호출
rename_files_in_folder(folder_path)
