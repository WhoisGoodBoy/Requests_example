class Human:
    def m(self):
        print('Human')

class Child1(Human):
    def m(self):
        print('Child1')

class Child2(Human):
    def m(self):
        print('Child2')

class Grandchild(Child1,Child2):
    def m(self):
        print('Grandchild')

    def m_from_second_child(self):
        Human.m(self)


grandchild = Grandchild()
grandchild.m()
grandchild.m_from_second_child()
