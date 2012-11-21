import feedparser

class Gmail:

	def __init__(self, username, password):
		self.u = username
		self.p = password

	def feed_string(self, u, p):
		return "https://" + u + ":" + p + "@mail.google.com/gmail/feed/atom"

	def count(self):
		return int(feedparser.parse(self.feed_string(self.u, self.p))["feed"]["fullcount"])