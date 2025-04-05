from openai import OpenAI
import requests
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import markdown

from chat.forms import SummaryForm

def deepseek_page(request):
    form = SummaryForm()
    with open("chat/t.txt", mode='r', encoding='utf-8') as f:
        r = f.read()
    md = markdown.Markdown(extensions=["fenced_code"])
    content = md.convert(r)
    return render(request, "chat/index.html", {'form': form, 'markdown_content': content})

def call_deepseek1(request):
    query = request.GET.get("query", "")  # Get query from the input field

    if not query:
        return HttpResponse("<p class='text-red-500'>Query cannot be empty.</p>")

    client = OpenAI(api_key=settings.DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")
    prompt = ""
    with open("chat/prompt.txt", mode='r', encoding='utf-8') as f:
        # print(f.read())
        prompt = f.read()

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "Respect the following rule:"},
            {"role": "system", "content": prompt},
            {"role": "user", "content": f"topis is {query}" },
        ],
        stream=False,
        response_format={
            'type': 'json_object'
        }
    )

    
    print(response)
    if response:
        data = response.choices[0].message.content
        return HttpResponse(f"<pre class='text-green-500'>{data}</pre>")
    else:
        return HttpResponse("<p class='text-red-500'>Error fetching data.</p>")


def call_deepseek(request):
    if request.method == 'GET':
        form = SummaryForm(request.GET)
        
        # Check if the form is valid
        if form.is_valid():
            topic = form.cleaned_data['topic']
            specific_aspect = form.cleaned_data['specific_aspect']
            summary_length = form.cleaned_data['summary_length']
            tone = form.cleaned_data['tone']

            # Prepare prompt for OpenAI
            prompt = f"Generate a {summary_length} summary about the topic '{topic}'"
            if specific_aspect:
                prompt += f" focusing on {specific_aspect}."
            prompt += f" The tone should be {tone}."

            # Call OpenAI API
            client = OpenAI(api_key=settings.DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": "Respect the following rule:"},
                    {"role": "system", "content": "Provide a clear, concise, and relevant response."},
                    {"role": "user", "content": prompt}
                ],
                stream=False,
                response_format={'type': 'text'}
            )

            # Process response and return it to the user
            if response:
                data = response.choices[0].message.content
                return HttpResponse(f"<pre class='text-green-500'>{data}</pre>")
            else:
                return HttpResponse("<p class='text-red-500'>Error fetching data.</p>")

        else:
            return HttpResponse("<p class='text-red-500'>Invalid form submission. Please fill out all required fields.</p>")

    return HttpResponse("<p class='text-red-500'>Invalid request method.</p>")