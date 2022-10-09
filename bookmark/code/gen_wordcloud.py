# coding=utf-8

import os
import json
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator

filepath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

fontpath = os.path.join(filepath, 'font', 'sarasa-ui-sc-regular.ttf')
jiebapath = os.path.join(filepath, 'jieba.json')


def main():

    with open(jiebapath,'r',encoding='utf-8') as f:
        contents = json.load(f)

    bookmark_cloud = WordCloud(font_path=fontpath,
                   background_color="white",
                   max_words=2000,
                   #    mask=back_coloring,  # 设置背景图片
                   max_font_size=100,
                   random_state=42,
                   width=1000, height=860, margin=2,
                   )
    

    bookmark_cloud.generate_from_frequencies(contents)

    plt.figure()
    plt.imshow(bookmark_cloud)
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    main()
