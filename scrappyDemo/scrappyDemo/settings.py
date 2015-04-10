SPIDER_MODULES = ['scrappyDemo.spiders']
NEWSPIDER_MODULE = 'scrappyDemo.spiders'
DEFAULT_ITEM_CLASS = 'scrappyDemo.items.Website'

ITEM_PIPELINES = {'scrappyDemo.pipelines.SendItems':1}
