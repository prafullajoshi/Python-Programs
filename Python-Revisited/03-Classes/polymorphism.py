from abc import ABC, abstractmethod


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


def draw(controls):
    for control in controls:
        control.draw()      # depending on type of control object this draw method takes different forms


textBox = TextBox()
ddl = DropDownList()
# draw(textBox)
# draw(ddl)

draw([textBox, ddl])
