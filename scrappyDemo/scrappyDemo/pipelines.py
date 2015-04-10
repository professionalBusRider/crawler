from scrapy.exceptions import DropItem

class SendItems(object):
	#called on every item of the pipeline
	#ret: Item xor DropItem
	def process_item(self, item, spider):
		print
		print
		print item['url']
		print
		print
		return item
