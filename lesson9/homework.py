"""
1*. Переписать код из homework6 используя ООП
2. Реализовать класс "очередь"
https://en.wikipedia.org/wiki/Queue_(abstract_data_type)
- в качестве инициализации принимает размер очереди, если параметр не указан,
то очередь - бесконечная
- выдать сообщение об ошибке, если в полную очередь добавить элемент нельзя,
или из пустой очереди достать элемент
3. Реализовать класс "стек"
https://en.wikipedia.org/wiki/Stack_(abstract_data_type)
- в качестве инициализации принимает размер стека, если параметр не указан,
то стек - бесконечный
- выдать сообщение об ошибке, если в полный стек добавить элемент нельзя,
или из пустого стека достать элемент
"""

class Queue:
    def __init__(self, size = None):
        self.size = size
        self.count = []

        def check(self):
         if self.size > len(self.count):
             return True
            else:
             return False

        def printer(self):
                print("size is {self.size} , count is {count.size}".format)

        def add(self,obj):
            if check is True:
                self.count.append(obj)
            else:
                raise Exception('smth with obj')

class Stack:
    def __init__(self, size = None):
        self.size = size
        self.value = []

        def printer(self):
            print("size is{}, steck is{}".format(self.size,self.value))

            def check(self):
                if self.size > len(self.value):
                    return True
                else:
                    return False

            def add(self, obj):
                if check is True:
                    self.value.append(obj)
                else:
                    return False

                def get(self):
                    if self.value == 0:
                        raise Exception("empty")
                    else:
                        del self.__value[-1]
                    t = self.value[-1]
                    return t










