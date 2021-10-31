import webbrowser
import tkinter as tk
import urllib.request


class Sadbot:
    def window(self):
        root = tk.Tk()
        root.geometry('480x660')
        root.title('SadBot')

        return root


    def screen(self):
        urllib.request.urlretrieve("https://i.imgur.com/XU0nB3s.png", "SadBot.png")
        img = tk.PhotoImage(file="SadBot.png")
        img = img.zoom(25)
        img = img.subsample(50)
        screen = tk.Label(root, image=img).pack()

        return screen, img


    def close_window(self):
        root.destroy()


    def program(self, arg):
        if arg == 1:
            sentence.set('Do you want to give up?')
            button_left['text'] = 'YES'
            button_right['text'] = 'NO'
            button_left['command'] = self.give_up
            button_right['command'] = self.go_away

        elif arg == 2:
            sentence.set('Do you think your life can still be saved?')
            button_left['text'] = 'YES'
            button_right['text'] = 'NO'
            button_left['command'] = self.go_away
            button_right['command'] = self.kys


    def give_up(self):
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ?autoplay=1')
        sentence.set('Did Rick Astley help you?')
        button_left['text'] = 'YES'
        button_right['text'] = 'NO'
        button_left['command'] = self.go_away
        button_right['command'] = self.nothing


    def kys(self):
        webbrowser.open('https://letmegooglethat.com/?q=how+to+kill+yourself')
        sentence.set('Did this solution help you?')
        button_left['text'] = 'YES'
        button_right['text'] = 'NO'
        button_left['command'] = self.go_away
        button_right['command'] = self.nothing


    def go_away(self):
        sentence.set('So what are you still doing here?')
        button_left['text'] = 'Exit'
        button_right['text'] = 'Exit'
        button_left['command'] = root.quit
        button_right['command'] = root.quit


    def nothing(self):
        sentence.set('I am sorry, nothing will help you anymore')
        button_left['text'] = 'Exit'
        button_right['text'] = 'Exit'
        button_left['command'] = root.quit
        button_right['command'] = root.quit


sadbot = Sadbot()


if __name__ == '__main__':
    root = sadbot.window()

    sentence = tk.StringVar()
    sentence.set('What is your problem?')
    txt = tk.Label(root, textvariable=sentence, height='5').pack()

    screen = sadbot.screen()

    button_left = tk.Button(root, text='Bad day', command=lambda: sadbot.program(arg=1), width='20', height='5')
    button_left.pack()
    button_left.place(x=20, y=540)
    button_right = tk.Button(root, text='Existence', command=lambda: sadbot.program(arg=2), width='20', height='5')
    button_right.pack()
    button_right.place(x=270, y=540)

    root.mainloop()
