from nicegui import ui

rooms = []
accordion_visible = False  # State to track accordion visibility

def create_room(room_name, room_description):
    rooms.append({'name': room_name, 'description': room_description, 'documents': []})
    show_rooms()

def refresh_rooms():
    rooms_column.clear()
    with rooms_column:
        for room in rooms:
            with ui.card().style('background-color: #333; color: #fff;'):
                ui.label(f'Room Name: {room["name"]}')
                ui.label(f'Description: {room["description"]}')
                for doc in room['documents']:
                    ui.label(f'Document: {doc["name"]}').style('color: #fff;')
                ui.button('Add Document', on_click=lambda room=room: add_document(room)).style('background-color: #555; color: #fff;')
        ui.button('Add Room', on_click=show_add_room_page).style('background-color: #555; color: #fff; margin-top: 10px;')

def add_document(room):
    with ui.dialog() as dialog:
        with ui.card().style('background-color: #333; color: #fff;'):
            doc_name = ui.input('Document Name').style('margin-bottom: 10px; color: #fff;')
            doc_url = ui.input('Document URL').style('margin-bottom: 10px; color: #fff;')
            ui.button('Upload', on_click=lambda: (room['documents'].append({'name': doc_name.value, 'url': doc_url.value}), dialog.close())).style('background-color: #555; color: #fff;')

def update_header(page_name):
    header_text.set_text(f"Home Management System - {page_name}")

def show_dashboard():
    update_header("Dashboard")
    main_column.clear()
    with main_column:
        ui.label('This is the Dashboard page.').style('color: #fff;')

def show_rooms():
    update_header("Rooms")
    main_column.clear()
    with main_column:
        global rooms_column
        rooms_column = ui.column()
        refresh_rooms()

def show_add_room_page():
    update_header("Add Room")
    main_column.clear()
    with main_column:
        room_name = ui.input('Room Name').style('width: 100%; margin-bottom: 10px; color: #fff;')
        room_description = ui.input('Room Description').style('width: 100%; margin-bottom: 10px; color: #fff;')
        ui.button('Create Room', on_click=lambda: create_room(room_name.value, room_description.value)).style('background-color: #555; color: #fff; width: 100%;')

def show_settings():
    update_header("Settings")
    main_column.clear()
    with main_column:
        ui.label('This is the Settings page.').style('color: #fff;')

def toggle_accordion():
    global accordion_visible
    accordion_visible = not accordion_visible
    render_navigation()

def render_navigation():
    nav_column.clear()
    with nav_column:
        ui.button('Dashboard', on_click=show_dashboard).classes('dark-button')
        ui.button('Rooms', on_click=toggle_accordion).classes('dark-button')
        if accordion_visible:
            ui.button('Add Room', on_click=show_add_room_page).classes('dark-button')
        ui.button('Settings', on_click=show_settings).classes('dark-button')

# Custom CSS for dark mode, header, footer, and navigation menu
dark_mode_css = '''
body {
    background-color: #121212;
    color: #fff;
    margin: 0;
    padding: 0;
}
.ui-row {
    background-color: #121212;
    color: #fff;
}
.ui-column {
    background-color: #1e1e1e;
}
.dark-card {
    background-color: #333;
    color: #fff;
}
.dark-button {
    background-color: #555;
    color: #fff;
    width: 100%;
    border: none;
    margin: 0;
    padding: 10px 0;
}
.dark-label {
    color: #fff;
}
.ui-input {
    color: #fff;
}
.header, .footer {
    background-color: #333;
    color: #fff;
    padding: 10px;
    text-align: center;
    font-size: 20px;
    width: 100%;
}
.footer {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
}
'''

with ui.column().style('height: 100vh; margin: 0; padding: 0;'):
    header_text = ui.label("Home Management System - Dashboard").classes('header')

    with ui.row().style('flex: 1; margin: 0; padding: 0;').classes('ui-row'):
        with ui.column().style('width: 200px; margin: 0; padding: 0;').classes('ui-column') as nav_column:
            render_navigation()

        main_column = ui.column().style('flex-grow: 1;').classes('ui-column')

    footer_text = ui.label("© 2024 Home Management System").classes('footer')

show_dashboard()

# Add custom CSS to the application
ui.add_head_html(f'<style>{dark_mode_css}</style>')

ui.run()
