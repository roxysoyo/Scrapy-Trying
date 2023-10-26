# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


def clean_movie_class(original_list):
    # Initialize a new empty list
    new_list = []

    for item in original_list:
        # Use strip() to remove whitespace characters and then check if it is an empty string
        stripped_item = item.strip()
        if stripped_item:
            new_list.append(stripped_item)
    return new_list


def clean_movie_introduction(original_paragraphs):
    # Initialize an empty list to store paragraph text
    paragraphs = []

    # 初始化一个空字符串来存储当前段落的文本
    current_paragraph = ""

    # Initialize an empty string to store the text of the current paragraph
    for item in original_paragraphs:
        stripped_item = item.strip()
        if stripped_item:
            current_paragraph += stripped_item
        else:
            if current_paragraph:
                paragraphs.append(current_paragraph)
                current_paragraph = ""

    # If there is text that has not been added to the paragraph list, add the last paragraph
    if current_paragraph:
        current_paragraph = current_paragraph.replace(" ", "")
        paragraphs.append(current_paragraph)
    return paragraphs


class Case1SpiderPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        # clean the movie_class
        former_movie_class = adapter.get("movie_class")
        adapter["movie_class"] = clean_movie_class(former_movie_class)

        # clean the movie_introduction
        former_movie_introduction = adapter.get("movie_introduction")
        adapter["movie_introduction"] = clean_movie_introduction(
            former_movie_introduction
        )
        return item
