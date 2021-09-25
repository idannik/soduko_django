import json
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from soduko.board.sudoku_loader import Sudoku


def get_board(request):
    b = Sudoku().board
    result = {"board": b, "options": [[] * 9 for _ in range(9)]}
    return JsonResponse(result)


def fill_pencil_marks(request):
    data = json.loads(request.body)
    print(data)
    return JsonResponse(data)
