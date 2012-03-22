import urllib
import re
import sys
import StorageServer
import xbmcaddon

from resources.lib import vice
from resources.lib import utils

### get addon info
__addon__             = xbmcaddon.Addon()
__addonid__           = __addon__.getAddonInfo('id')
__addonidint__        = int(sys.argv[1])

# initialise cache object to speed up plugin operation
page_cache = StorageServer.StorageServer(__addonid__ + 'cached_pages', 1)
video_cache = StorageServer.StorageServer(__addonid__ + 'cached_videos', 24 * 7)

class Main:

    def __init__(self):

        # parse script arguments
        params = utils.getParams()

        # Check if the url param exists
        try:
            
            show_link=urllib.unquote_plus(params["show_link"])
            utils.log('Show Found: %s' % show_link)
            
            # Get the current page number
            pageNum = int(params["page"])
            utils.log('Page Found: %s' % show_link)
            
        except:

            try:
                
                episode_link=urllib.unquote_plus(params["episode_link"])
                utils.log('Episode Found: %s' % episode_link)
            
            except:
                
                for show in vice.get_shows():
                    
                    utils.addDir(show['title'], show['thumb'], show['link'], show['description'])
            
            else:
                
                utils.playVideo(episode_link)
        
        else:
            
            for episode in vice.get_episodes(show_link, pageNum):
                    
                utils.addVideo(episode['title'], episode['link'], episode['thumb'], episode['description'])
            
        # We're done with the directory listing
        utils.endDir()
            

if __name__ == '__main__':
    
    # Main program
    Main()
        