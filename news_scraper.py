from user_settings import settings


class NewsScraper:

    @staticmethod
    def get_main_headline(headlines: list):
        try:
            headline = headlines[0].pop()
            if headline is not None:
                return headline
            return headline
        except:
            return None

    @staticmethod
    def handle_article_body(body):
        for tag in body.find_all('aside'):
            tag.decompose()

        for tag in body.find_all('div'):
            tag.decompose()

        for a in body.find_all('a', href=True):
            if 'http' in a['href']:
                a.append(f" [{a['href']}]")

        body = body.text
        body = body.replace(u'\xa0', ' ')  # escape &nbsp

        if settings['separate_text_by_paragraphs']:
            body = body.split('\n\n')  # разделить по абзацам

        return body
