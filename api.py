import webapp2
import json

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('<html>')
        self.response.write('<head><title>DVBSE service API</title></head>')
        self.response.write('<body>')
        self.response.write('<h1>DVBStreamExplorer Service API</h1>')
        self.response.write('You need <a href=\"http://www.dvbstreamexplorer.com/dvbse/dvbse.php\">DVBStreamExplorer</a> to produce service XML file.')
        self.response.write('You need <a href=\"https://dvbseserviceproc.codeplex.com/\">DVBStreamExplorer Service File Processor</a> to to send service data encoded in JSON to this service ')
        self.response.write('</body>')
        self.response.write('</html>')
        
    def post(self):
      self.handlerequest()

    def put(self):
      self.handlerequest()
    
    def handlerequest(self):
        list = json.JSONDecoder().decode(self.request.body)
        # validate a few, but not all possible properties.
        for service in list:
          if 'name' not in service:
            self.response.status = 500
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('property name not found')
            return
            
          if 'provider' not in service:
            self.response.status = 500
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('provider name not found')
            return

application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)