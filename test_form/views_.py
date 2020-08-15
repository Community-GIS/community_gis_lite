from django.shortcuts import render

from test_form.form import FlavourSuggestionForm


def suggest(request):
    if request.method == 'POST':
        form = FlavourSuggestionForm(request.POST)
        if form.is_valid():
            flavour = form.save()
            return render(request, 'test_form/thankyou.html', {
                'flavour': flavour,
            })
    else:
        form = FlavourSuggestionForm()

    return render(request, 'test_form/suggest.html', {
        'form': form,
    })