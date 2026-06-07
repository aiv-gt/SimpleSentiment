from django.shortcuts import render
from textblob import TextBlob

def home(request):

    result = ""
    sentence = ""

    if request.method == "POST":

        sentence = request.POST.get("sentence")

        polarity = TextBlob(sentence).sentiment.polarity

        if polarity > 0:
            result = "Positive"
        elif polarity < 0:
            result = "Negative"
        else:
            result = "Neutral"

    return render(
        request,
        "home.html",
        {
            "result": result,
            "sentence": sentence
        }
    )