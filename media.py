import webbrowser

class Movie():
	def __init__(self, item):
		self.id = item['id']
		self.title = item['snippet']['localized']['title']
		if 'contentRating' in item['contentDetails'] and 'mpaaRating' in item['contentDetails']['contentRating']:
			self.rating = item['contentDetails']['contentRating']['mpaaRating'].replace('mpaa','')
		else:
			self.rating = 'Not Available'
		self.storyline = item['snippet']['localized']['description'].encode('ascii',errors='ignore')
		#turns the youtube search result img url into the web_poster URL -- couldn't find any part of the API that returned this directly
		self.poster_image_url = item['snippet']['thumbnails']['default']['url'].replace('default.jpg', 'movieposter.jpg')
		#this includes the full embed code for the youtube player, not just the URL
		self.trailer_youtube_url = item['player']['embedHtml']
		self.duration = item['contentDetails']['duration'].replace('PT','')
		#the next lines prep the html for each movie card (thumbnail+title) and each details pane (Youtube trailer, description, etc)
		#normally, I'd separate these out as discreet methods, and only call them on those instances that I was definitely going to 
		#insert in the final html, but in this case, I know I'm including all Movie instances, so I kept these in init.
		self.cardHTML = open('elements/titleCard.html').read().format(self)
		self.paneHTML = open('elements/detailPane.html').read().format(self)
		#TODO -- figure out how to change the above format function to use kwargs from a dict of self so I don't have to
		#use the silly 0. notation in the template.
