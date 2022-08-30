from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, кг': 0.3,
        'сыр, кг': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def omlet_view(request):
    servings = int(request.GET.get("servings", 1))
    recipe = {key: round(float(val)*servings, 4) for key, val in DATA['omlet'].items()}
    context = {
        'recipe': recipe
    }
    return render(request, 'calculator/index.html', context)


def pasta_view(request):
    servings = int(request.GET.get("servings", 1))
    recipe = {key: round(float(val) * servings, 4) for key, val in DATA['pasta'].items()}
    context = {
        'recipe': recipe
    }
    return render(request, 'calculator/index.html', context)

def buter_view(request):
    servings = int(request.GET.get("servings", 1))
    recipe = {key: round(float(val) * servings, 4) for key, val in DATA['buter'].items()}
    context = {
        'recipe': recipe
    }
    return render(request, 'calculator/index.html', context)


