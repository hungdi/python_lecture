class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    

class TextEditor:
    def __init__(self):
        self.text = ""
        self.undo_stack = Stack()
        self.redo_stack = Stack()

    def display(self):
        print(self.text)

    def append(self, new_text):
        self.undo_stack.push(self.text)
        self.text += new_text
        self.redo_stack = Stack()

    def undo(self):
        # 실행 취소 기능을 수행
        if not self.undo_stack.is_empty():
            self.redo_stack.push(self.text)
            self.text = self.undo_stack.pop()
        else:
            print("더 이상 되돌릴 수 없습니다")
    
    def redo(self):
        # 다시 실행 기능을 수행합니다.
        if not self.redo_stack.is_empty():
            self.undo_stack.push(self.text)
            self.text = self.redo_stack.pop()
        else:
            print("더 이상 다시 실행할 수 없습니다")
    

editor = TextEditor()

print("---1. 'Hello' 입력---")
editor.append("Hello")
editor.display() # 예상 출력: Hello

print("\n---2. ' World' 입력---")
editor.append(" World")
editor.display() # 예상 출력: Hello World

print("\n---3. 실행 취소 (undo)---")
editor.undo()
editor.display() # 예상 출력: Hello

print("\n---4. 다시 실행 (redo)---")
editor.redo()
editor.display() # 예상 출력: Hello World

print("\n---5. 다시 실행 (redo) 실패---")
editor.redo() # redo_stack이 비어있으므로 아무 변화 없음
editor.display() # 예상 출력: Hello World

print("\n---6. ' Python' 입력 (redo 스택 초기화)---")
editor.append(" Python")
editor.display() # 예상 출력: Hello World Python

print("\n---7. 다시 실행 (redo) 실패---")
editor.redo() # 새로운 append가 발생했으므로 redo 스택은 비어있음
editor.display() # 예상 출력: Hello World Python