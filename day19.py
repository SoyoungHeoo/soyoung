import tkinter as tk

memos = [None for _ in range(100)]
memos[0], memos[1] = 0, 1

def fibo_memo_recu(n) :
	'''
	재귀함수 사용한 피보나치 수열 처리 함수
	:param n:
	:return:
	'''
	global memos
	if n <= 1 :
		return memos[n]

	if memos[n] is not None: # 전역 메모리 memos에 이전에 계산한 결과 값이 존재하면
		return memos[n]

	memos[n] = fibo_memo_recu(n-2) + fibo_memo_recu(n-1)
	return memos[n]


def fact_recu(n):
	if n == 1:
		return 1
	else:
		return (n * fact_recu(n-1))


def factorial_input():
	lbl_results.config(text=f"계산기 출력 결과 : {fact_recu(int(en_num_input.get()))}")


def fibonacci_input():
	lbl_results.config(text=f"계산기 출력 결과 : {fibo_memo_recu(int(en_num_input.get()))}")


## 그래픽
win = tk.Tk()
win.title("Calculator") # 피보나치, 팩토리얼 계산기.
win.geometry("180x240")

en_num_input = tk.Entry() # 텍스트 입력 상자
lbl_results = tk.Label(text="계산기 출력 결과: ")
btn_fact = tk.Button(text="팩토리얼", command = factorial_input) # 이벤트 발생 버튼
btn_fibo = tk.Button(text="피보나치", command = fibonacci_input) # 이벤트 발생 버튼

en_num_input.pack()
lbl_results.pack()
btn_fact.pack(fill="x")
btn_fibo.pack(fill="x")
win.mainloop()
