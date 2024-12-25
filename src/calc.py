from nicegui import ui

# Define the calculator logic
new_operation = True
operation_history = []
history_cleared = False

def add_to_operation(value):
    global new_operation
    if new_operation and result_label.text:
        operation_label.text = result_label.text
        new_operation = False
    current_operation = operation_label.text
    operation_label.text = current_operation + str(value)

def clear_operation():
    global new_operation, history_cleared
    if not history_cleared:
        operation_history.clear()
        history_container.clear()
        history_cleared = True
    else:
        operation_label.text = ''
        result_label.text = ''
        new_operation = True
        history_cleared = False

def backspace_operation():
    current_operation = operation_label.text
    operation_label.text = current_operation[:-1]

def calculate():
    global new_operation, history_cleared
    try:
        result = str(eval(operation_label.text))
    except:
        result = 'Error'
    update_history(operation_label.text + ' = ' + result)
    result_label.text = result
    operation_label.text = result
    new_operation = True
    history_cleared = False

def update_history(operation):
    global operation_history
    operation_history.insert(0, operation)
    if len(operation_history) > 10:
        operation_history.pop()
    history_container.clear()
    with history_container:
        for op in operation_history:
            ui.label(op).style('color: black; font-size: 18px')

# Create the UI elements
with ui.card().classes('dark'):
    with ui.row().classes('justify-center items-center h-screen'):
        with ui.column().classes('dark'):
            ui.label('Calculator').style('color: white; font-size: 24px')
            operation_label = ui.label('').style('color: black; font-size: 18px; background-color: #666; padding: 20px; border-radius: 10px; width: 280px')

            button_layout = [
                ['%', 'C', '⌫'],
                ['1', '2', '3', '/'],
                ['4', '5', '6', '*'],
                ['7', '8', '9', '-'],
                ['0', '.', '=', '+']
            ]

            for row in button_layout:
                with ui.row():
                    for text in row:
                        if text == '=':
                            ui.button(text, on_click=calculate).style('background-color: darkgreen; color: white; width: 50px; height: 50px;')
                        elif text == 'C':
                            ui.button(text, on_click=clear_operation).style('background-color: darkgreen; color: white; width: 50px; height: 50px;')
                        elif text == '⌫':
                            ui.button(text, on_click=backspace_operation).style('background-color: darkgreen; color: white; width: 100px; height: 50px;')
                        elif text in ['/', '*', '-', '+', '%']:
                            ui.button(text, on_click=lambda v=text: add_to_operation(v)).style('background-color: darkgreen; color: white; width: 50px; height: 50px;')
                        elif text != '':
                            ui.button(text, on_click=lambda v=text: add_to_operation(v)).style('background-color: #333; color: white; width: 50px; height: 50px;')

        # Create the result section and history pane to the right of the calculator
        with ui.column().style('background-color: #666; padding: 20px; border-radius: 10px; width: 300px; height: 400px'):
            ui.label('History').style('color: white; font-size: 24px; margin-bottom: 10px')
            with ui.row():
                with ui.column():
                    result_label = ui.label('').style('color: black; font-size: 18px; background-color: #666; padding: 20px; border-radius: 10px; width: 280px')
                with ui.column():
                    history_container = ui.column()

# Enable dark mode
ui.html('''<style>
  body { background-color: #333; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
</style>''')

# Run the application
ui.run(title='NiceGUI Calculator')
