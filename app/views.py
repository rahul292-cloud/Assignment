from django.shortcuts import render, redirect
import requests
import bs4
import lxml
from .models import UrlDetails


def home(request):
    context = {}
    home_templates = 'app/home.html'

    return render(request, home_templates, context)


def postMethod(request):
    print("pass...")
    success_templates = 'app/success.html'
    if request.method == 'POST':
        print(request.POST['noOfWebsite'])
        print(request.POST['website_url'])

        url = str(request.POST['website_url'])
        no = int(request.POST['noOfWebsite'])
        base_url = "https://"
        final_url = base_url + url
        print(final_url)

        res = requests.get(final_url)
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        allWebsites = soup.find('table', class_='table')
        list_of_websites = []
        for website in allWebsites.find_all('tbody'):
            rows = website.find_all('tr')[0:no]
            for row in rows:
                website_url = row.find_all('td')
                urls = website_url[0].find('a', href=True)['href']
                list_of_websites.append(urls)
                print(urls)

                print(website_url[1].text)
                print(website_url[2].text)

                UrlDetails.objects.get_or_create(
                    url=urls,
                    title=website_url[1].text,
                    location=website_url[2].text
                )

        return render(request, success_templates)
