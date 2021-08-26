from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from soduko.board.SudokuLoader import Sudoku


def get_board(request, board_id):
    b = Sudoku(board_id).board
    result = {}
    result["board"] = b
    result["options"] = [[] * 9 for _ in range(9)]
    return JsonResponse(result)
