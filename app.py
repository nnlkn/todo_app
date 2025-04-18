import streamlit as st

st.title('🦑To-do App🦑')

# 1. todo 입력칸 제공
# 2. todos(session_state)에 저장
# 3. todos 목록화
# 4. 완료한 todo는 checkbox를 통해 완료처리

# 보기 > 도구 창 > TODO

class Todo:
    def __init__(self, task: str, done: bool = False):
        self.task = task
        self.done = done

    def __repr__(self):
        return f'Todo(task={self.task}, done={self.done}'

def add_todo():
    new_task = st.session_state["new_task"] # 새로운 할 일 추가 (사용자 입력)
    print(f'add_todo: new_task = {new_task}')
    if new_task: # 만약 new task가 존재하면
        new_todo = Todo(new_task) # 새로운 new_todo 객체 만들기
        st.session_state["todos"].append(new_todo) # new_todo에 추가
        st.session_state["new_task"] = "" # 사용자 입력칸 빈칸 처리

def toggle_done(index: int):
    todo = st.session_state["todos"][index]
    todo.done = not todo.done # 반전

# todos 초기화
if "todos" not in st.session_state:
    st.session_state.todos: list[Todo] = []

# 입력창
# - key 매개변수는 session_state 자동 등록 및 관리 --> 사용자 입력값이 new_task로 자동으로 입력
# - on_change 콜백함수는 사용자 입력 후 엔터를 누르면 지정한 함수를 자동 호출
st.text_input("새로운 할일 추가", key="new_task", on_change=add_todo)

# 목록
print(f'todos = {st.session_state["todos"]}')
if st.session_state['todos']:
    for i, todo in enumerate(st.session_state['todos']):
        col1, col2 = st.columns([0.2, 0.8]) # 크기 지정 가능
        col1.checkbox("", value=todo.done, key=f"done_{i}", on_change=toggle_done, args=(i, )) # 체크박스 여부 # 식별자 key 지정
        col2.markdown(f'~~{todo.task}~~' if todo.done else todo.task)
else:
    st.info('할일을 추가해보세요')
