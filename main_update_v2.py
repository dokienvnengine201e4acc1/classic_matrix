import time
import os
import random

def matrix():
    try:
        while True:
            row = [str(random.randint(0, 1)) for _ in range(200)]
            print(''.join(row))
            time.sleep(0.05)  # Thêm một chút delay để dễ nhìn
    except KeyboardInterrupt:
        # Người dùng nhấn Ctrl+C => quay về run_matrix để xử lý tiếp
        raise

print("Press Ctrl+C to stop the program.\n")

def run_matrix():
    try:
        os.system("cls" if os.name == "nt" else "clear")
        os.system("color 02")  # Màu xanh matrix
        matrix()
    except KeyboardInterrupt:
        print("\nYou pressed Ctrl+C to stop the program!")
        os.system("color 07")  # Trả lại màu console mặc định
        time.sleep(5)
        os.system("cls" if os.name == "nt" else "clear")

while True:
    ques = input("Do you want run to matrix emu? (Yes/No): ").strip().lower()

    if ques in ["y", "yes"]:
        run_matrix()
        break
    elif ques in ["n", "no"]:
        print("Goodbye! :< ")
        time.sleep(3)
        os.system("cls" if os.name == "nt" else "clear")
        break
    elif ques == "":
        os.system("cls" if os.name == "nt" else "clear")
    else:
        os.system("cls" if os.name == "nt" else "clear")
        print("Invalid input. Please enter Yes (Y) or No (n).")
        time.sleep(2)
        os.system("cls" if os.name == "nt" else "clear")
