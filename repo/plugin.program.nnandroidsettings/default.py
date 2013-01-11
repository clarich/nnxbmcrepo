import xbmc, xbmcaddon

addon = xbmcaddon.Addon(id='plugin.program.nnandroidsettings')

__addon__      = xbmcaddon.Addon()
__author__     = __addon__.getAddonInfo('author')
__scriptid__   = __addon__.getAddonInfo('id')
__scriptname__ = __addon__.getAddonInfo('name')
__cwd__        = __addon__.getAddonInfo('path')
__version__    = __addon__.getAddonInfo('version')
__language__   = __addon__.getLocalizedString

DEBUG = True

# This is a "drop in" replacement for:
#     PlayMedia("androidapp://sources/apps/com.android.calendar",return)

# ToDo: Good way to do the following:
#     androidapp://sources/apps/com.android.calendar.png

if ( __name__ == "__main__" ):
	try:
		package = "com.android.settings"
		xbmc.executebuiltin('XBMC.StartActivity("com.android.settings")')
		print "KmN: After execute built in"
	except Exception as e:
		print "KmN: Exception!"
		print e
