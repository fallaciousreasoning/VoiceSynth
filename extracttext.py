import ebooklib
from ebooklib import epub

from bs4 import BeautifulSoup

def extract_text(chapter):
    f = BeautifulSoup(chapter, 'lxml')
    return [line.strip() for line in f.text.splitlines() if line]

def get_chapters(filename):
    book = epub.read_epub(filename)
    chapters = [extract_text(chapter.content) for chapter in book.get_items() if isinstance(chapter, epub.EpubHtml)]
    return chapters

if __name__ == '__main__':
    get_chapters('The Autumn Republic.epub')