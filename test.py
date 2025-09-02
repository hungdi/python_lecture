class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "스택 비어잉씀"
        
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "스택 비어잉씀"
        
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    

class TextEditor:
    def __init__(self):
        self.text = ""
        self.undo_stack = Stack()
        self.redo_stack = Stack()

    def append(self, data):
        # 현재 텍스트에 추가
        self.undo_stack.push(self.text)
        self.redo_stack = Stack() # redo 초기화
        self.text += data

    def undo(self):
        if not self.undo_stack.is_empty():
            self.redo_stack.push(self.text)
            self.text = self.undo_stack.pop()
        else:
            print("더 이상 취소할 수 없습니다.")
    
    def redo(self):
        if not self.redo_stack.is_empty():
            self.undo_stack.push(self.text)
            self.text = self.redo_stack.pop()
        else:
            print("더 이상 되돌릴 수 없습니다")

    def display(self):
        print(self.text)




# 아래 코드를 실행합니다.
# TextEditor 클래스 사용 예제
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