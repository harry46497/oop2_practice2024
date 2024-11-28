class SayHello:
    def init____(self, target="World"):
        self.target = target

    def say(self):
        print(f"Hello, {self.target}!!")
if __name__ == '__main__':
    app = SayHello()
    app.say()
    app = SayHello("Someone")
    app.say()