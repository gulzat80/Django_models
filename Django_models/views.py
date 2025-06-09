from django.shortcuts import render
from .models import Fruit

def index(request):
    selected_fruits = Fruit.objects.filter(price__lte=100)
    total_price = sum(f.price for f in selected_fruits)
    result = ""
    change = 0

    if request.method == "POST":
        money = int(request.POST.get("money", 0))
        if money > total_price:
            change = money - total_price
            result = f"Кайтарым: {change} сом. Соодаңыз үчүн рахмат!"
        elif money < total_price:
            result = "Сиз берген акча жетишсиз."
        else:
            result = "Соодаңыз үчүн рахмат!"

    context = {
        "fruits": selected_fruits,
        "total": total_price,
        "result": result
    }
    return render(request, "index.html", context)
