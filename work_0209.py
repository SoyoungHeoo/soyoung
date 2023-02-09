import tkinter as tk


def sierpinski(x, y, size):
    if size>=30:
        sierpinski(x, y, size/2)
        sierpinski(x+size/2, y, size/2)
        sierpinski(x+size/4, int(y-size*(3**0.5)/4), size/2)
    else:
        canvas.create_polygon(x, y, x+size, y, x+size/2, y-size*(3**0.5)/2,
                              fill='red', outline='red')


w = 500
radius = 500

if __name__ == "__main__":
    window = tk.Tk()
    window.title("삼각형 모양의 프렉탈")
    canvas = tk.Canvas(window, height=w, width=w, bg="white")

    sierpinski(40, 400, 300)

    canvas.pack()
    window.mainloop()