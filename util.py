from rich.style import Style
from rich.highlighter import RegexHighlighter

class KeywordHighlighter(RegexHighlighter):
    def __init__(self, keyword):
        super().__init__()
        self.keyword = keyword
        self.highlights = f'(?i)({self.keyword})'
        self.base_style = "bold underline"

    def highlight(self, text):
        text.highlight_regex(re_highlight=self.highlights, style=self.base_style)


def clean_abstract(abstract):
    valid = abstract.split("\\\\")[1:]
    return " ".join(valid)


def add_to_table(df, table, keyword):
    title_style = Style(color="cyan", bold=True)
    highlighter = KeywordHighlighter(keyword)
    for _, row in df.iterrows():
        table.add_row('', highlighter(row['title']), style=title_style)
        table.add_row('', highlighter(row['authors']), style='magenta')
        table.add_row('', row['url'], style='blue')
        table.add_row('', highlighter(clean_abstract(row['abstract'])), style='green')
        table.add_row('')
    return table


def get_until(i, lines, delim, n_skip=0):
    text = lines[i][n_skip:].strip() + ' '
    i += 1
    try:
        while not lines[i].startswith(delim):
            text += lines[i].strip() + ' '
            i += 1
    except IndexError:
        return text
    return text