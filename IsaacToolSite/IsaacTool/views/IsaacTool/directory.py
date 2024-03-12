from django.shortcuts import render


def index(response):
    return render(response, "../templates/IsaacTool/directory.html", {"name": "directory"})
