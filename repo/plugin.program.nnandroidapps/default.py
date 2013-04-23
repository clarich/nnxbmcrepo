import xbmc, xbmcaddon

addon = xbmcaddon.Addon(id='plugin.program.nnandroidapps')

__addon__      = xbmcaddon.Addon()
__author__     = __addon__.getAddonInfo('author')
__scriptid__   = __addon__.getAddonInfo('id')
__scriptname__ = __addon__.getAddonInfo('name')
__cwd__        = __addon__.getAddonInfo('path')
__version__    = __addon__.getAddonInfo('version')
__language__   = __addon__.getLocalizedString

DEBUG = True

if ( __name__ == "__main__" ):
	#xbmc.executebuiltin("xbmc.ActivateWindow(Programs,\"Android Apps\",return)")
	android_apps = xbmc.getLocalizedString(20244)
	xbmc.executebuiltin("xbmc.StartAndroidActivity(Programs,\"" + android_apps + "\",return)")
