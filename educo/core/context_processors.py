# context_processors.py
def htmx(request):
    # HTMX requests send the HX-Request header.
    return {'is_htmx': request.headers.get('HX-Request') == 'true'}
