import tkinter as tk
import numpy as np


def giai_he_phuong_trinh():
  # Lấy dữ liệu từ người dùng
  A = []
  b = []
  for i in range(n):
    A_row = []
    for j in range(n):
      A_row.append(float(entry_A[i][j].get()))
    A.append(A_row)
    b.append(float(entry_b[i].get()))

  # Chuyển dữ liệu thành mảng NumPy
  A = np.array(A)
  b = np.array(b)

  # Kiểm tra xem ma trận A có nghịch đảo không
  if np.linalg.det(A) == 0:
    result_label.config(text="Hệ phương trình không có nghiệm hoặc có vô số nghiệm.")
  else:
    # Tính nghiệm x bằng cách nhân ma trận nghịch đảo của A với vectơ b
    x = np.dot(np.linalg.inv(A), b)
    result_label.config(text="Nghiệm của hệ phương trình:\n" + "\n".join(f"x{i + 1}: {x[i]:.4f}" for i in range(n)))


# Tạo cửa sổ giao diện
root = tk.Tk()
root.title("Giải Hệ Phương Trình Tuyến Tính")

# Nhập số ẩn n
n_label = tk.Label(root, text="Nhập số ẩn n:")
n_label.pack()
n_entry = tk.Entry(root)
n_entry.pack()


# Button để xác nhận số ẩn và tạo các ô nhập dữ liệu
def tao_ung_dung():
  global n, entry_A, entry_b, result_label
  n = int(n_entry.get())

  # Tạo ô nhập dữ liệu cho ma trận A và vectơ b
  entry_A = [[None] * n for _ in range(n)]
  entry_b = [None] * n
  for i in range(n):
    for j in range(n):
      label = tk.Label(root, text=f"A[{i + 1},{j + 1}]:")
      label.pack()
      entry_A[i][j] = tk.Entry(root)
      entry_A[i][j].pack()
    label = tk.Label(root, text=f"b[{i + 1}]:")
    label.pack()
    entry_b[i] = tk.Entry(root)
    entry_b[i].pack()

  # Button để giải hệ phương trình
  solve_button = tk.Button(root, text="Giải Hệ Phương Trình", command=giai_he_phuong_trinh)
  solve_button.pack()

  # Kết quả
  result_label = tk.Label(root, text="")
  result_label.pack()


create_button = tk.Button(root, text="Xác nhận số ẩn", command=tao_ung_dung)
create_button.pack()

root.mainloop()
