from pprint import pprint
import requests


def get_jokes(number_of_jokes):
    jokes = []
    url = 'https://api.chucknorris.io/jokes/random?category=dev'
    while number_of_jokes > 0:
        response = requests.get(url)
        joke = response.json()
        jokes.append(joke['value'])
        number_of_jokes -= 1

    return jokes


def main():
    fetched_jokes = get_jokes(10)
    pprint(fetched_jokes)
    print(fetched_jokes)
    return fetched_jokes


if __name__ == '__main__':
    main()