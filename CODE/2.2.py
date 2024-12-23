import numpy as np
import csv

# 1. Đọc dữ liệu từ file CSV
file_path = './DATA/diem_hoc_phan.csv'

# a. Đọc dữ liệu điểm số từ file CSV vào một list
data_list = []
with open(file_path, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    header = next(reader)  # Đọc tiêu đề
    for row in reader:
        data_list.append(row)

# b. Chuyển đổi list này thành một mảng NumPy
data_array = np.array(data_list)

# 2. Quy đổi từ thang điểm 10 sang điểm tín chỉ
def convert_to_grade(score):
    score = float(score)
    if 8.5 <= score <= 10:
        return 'A'
    elif 8.0 <= score <= 8.4:
        return 'B+'
    elif 7.0 <= score < 8:
        return 'B'
    elif 6.5 <= score < 7:
        return 'C+'
    elif 5.5 <= score < 6:
        return 'C'
    elif 5.0 <= score < 5.5:
        return 'D+'
    elif 4.0 <= score < 5:
        return 'D'
    else:
        return 'F'

# Áp dụng quy đổi điểm tín chỉ
grades = []
for row in data_array[:, 2:]:  # Chỉ lấy cột điểm (bỏ id và tên)
    grades.append([convert_to_grade(score) for score in row])
grades_array = np.array(grades)

# 3. Chia tách dữ liệu theo học phần
def split_by_course(data, course_idx):
    return data[:, course_idx]

hp1_scores = data_array[:, 2].astype(float)
hp2_scores = data_array[:, 3].astype(float)
hp3_scores = data_array[:, 4].astype(float)

# 4. Phân tích dữ liệu theo từng học phần
def analyze_scores(scores):
    total = np.sum(scores)
    mean = np.mean(scores)
    std_dev = np.std(scores)
    return total, mean, std_dev

hp1_analysis = analyze_scores(hp1_scores)
hp2_analysis = analyze_scores(hp2_scores)
hp3_analysis = analyze_scores(hp3_scores)

# 5. Phân tích điểm tổng hợp
def count_grades(grades):
    unique, counts = np.unique(grades, return_counts=True)
    return dict(zip(unique, counts))

grade_counts = count_grades(grades_array.flatten())

# Kết quả:
print("Phân tích học phần 1 (HP1):", hp1_analysis)
print("Phân tích học phần 2 (HP2):", hp2_analysis)
print("Phân tích học phần 3 (HP3):", hp3_analysis)
print("Số lượng sinh viên đạt từng loại điểm tín chỉ:", grade_counts)
