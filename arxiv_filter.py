import pandas as pd
from rich.console import Console
from rich.table import Table
from rich.style import Style

from util import add_to_table, get_until

console = Console()

with console.status('Reading papers...', spinner='monkey'):
    # --- SETUP ---
    # read keywords and authors from keywords.txt and authors.txt
    with open('keywords.txt', 'r') as file:
        keywords = file.read().splitlines()

    with open('authors.txt', 'r') as file:
        authors = file.read().splitlines()

    # read lines from mail_text.txt
    with open('mail_text.txt', 'r') as file:
        lines = file.readlines()

    # --- PROCESS ---
    results = {
        'title': [],
        'authors': [],
        'abstract': [],
        'url': [],
    }

    for i, line in enumerate(lines):
        if line.startswith('arXiv:'):
            id = line[6:].split(" ")[0].strip()
            results['url'].append(f'https://arxiv.org/abs/{id}')
        elif line.startswith('Title:'):
            results['title'].append(get_until(i, lines, 'Authors:', n_skip=7))
        elif line.startswith('Authors:'):
            results['authors'].append(get_until(i, lines, 'Categories:', n_skip=9))
        elif line.startswith('Categories:'):
            results['abstract'].append(get_until(i, lines, '-----------------------'))
        elif line.startswith("%%--%%--%%--%%--%%--%%--%%--%%--%%--%%--%%--%%--%%--%%--%%--%%--%%--%%--%%--%%"):
            break # only until the updates

    df = pd.DataFrame(results)

    # --- OUTPUT ---
    table = Table(box=None)
    keyword_style = Style(color="red", bold=True)
    table.add_column(max_width=15, justify='center', style=keyword_style)
    table.add_column()

    for keyword in keywords:
        table.add_row(keyword)
        match = df[df['title'].str.contains(keyword, case=False) | df['abstract'].str.contains(keyword, case=False)]
        table = add_to_table(match, table, keyword)

    for author in authors:
        table.add_row(author)
        match = df[df['authors'].str.contains(author, case=False)]
        table = add_to_table(match, table, author)

console.print(table)