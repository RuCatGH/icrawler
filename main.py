from icrawler.builtin import GoogleImageCrawler, GreedyImageCrawler

def google_img_downloader():
    filters = dict(
        type='photo',
        color='color',
        size='icon'
        # license='noncommercial, commercial',
        # date=((2020, 1, 1), (2022, 5, 14)) 
    )
    crawler = GoogleImageCrawler(storage={'root_dir': r'C:\Users\Vladimir\Desktop\img'}, downloader_threads=10)


    crawler.crawl(
        keyword='Cat',
        max_num=1,
        min_size=(1000,1000),
        overwrite=True,
        filters=filters,
        file_idx_offset='auto',

    )

def greedy_crowler():
    greedy_crawler = GreedyImageCrawler(storage={'root_dir': './img/'},downloader_threads=10)
    greedy_crawler.crawl(domains='https://pikabu.ru/story/20_samyikh_populyarnyikh_dinozavrov_s_kartinkami_8064374', max_num=10,
                     min_size=(700,700), max_size=None)

def main():
    google_img_downloader()

if __name__ == '__main__':
    main()
