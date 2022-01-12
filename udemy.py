import sys
import webbrowser


def url_udemy(course, **args):
    params = {
        'duration': 'long',  # long, short, medium
        'instructional_level': 'all',
        #                       ^ beginner, intermediate, expert, all
        'ratings': '3.0',  # 3.0, 3.5, 4.0, 4.5
        # 'price': 'paid', # free, paid
        'sort': 'newest',  # newest, relevance, most-reviewed
        'lang': 'en',
        'q': course.replace(' ', '%20'),
    }
    params.update(args)
    return 'https://www.udemy.com/courses/search/?{}'.format(
        '&'.join(f'{k}={v}' for k, v in params.items())
    )


def open_url(param):
    webbrowser.open(
        url_udemy(
            param,
            ratings='4.0', lang='pt',
            instructional_level='beginner',
            duration='medium',
            sort='most-reviewed',
            # price='free',
        )
    )


if __name__ == '__main__' and len(sys.argv) > 1:
    open_url(sys.argv[1])
