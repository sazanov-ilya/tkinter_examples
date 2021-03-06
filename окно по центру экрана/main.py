#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import Tk, Frame, BOTH


class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.parent.title("Окно по центру экрана")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()

    def centerWindow(self):
        # значения ширины и высоты окна нашего приложения
        w = 290
        h = 150

        # определяем ширину и высоту экрана
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        # рассчитываем необходимые координаты «x» и «y»
        x = (sw - w) / 2
        y = (sh - h) / 2
        # метод geometry(), чтобы центрировать окно на экране
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))


def main():
    root = Tk()
    ex = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()