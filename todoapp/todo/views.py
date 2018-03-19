from django.shortcuts import render

def get_todo_index(request):
    return render(request, "todo/index.html")
    
def edit_todo_item(request, id):
    return render(request, "todo/edit.html")
    
def delete_todo_item(request, id):
    return render(request, "todo/delete.html")
    
def toggle_todo_item(request, id):
    return render(request, "todo/toggle.html")
