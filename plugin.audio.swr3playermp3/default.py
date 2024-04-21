# -*- coding: utf-8 -*-


import os,xbmcgui,xbmc,xbmcaddon,xbmcvfs
import requests as req
import re


title = 'SWR3 MP3 Livestream'
url = 'https://liveradio.swr.de/sw282p3/swr3/play.mp3'
pDialog = xbmcgui.DialogProgress()
pDialog.create(title, 'Initializing script...')

addonID = 'plugin.audio.swr3playermp3'
addon = xbmcaddon.Addon(id = addonID)
addonPath = addon.getAddonInfo('path')
icon = xbmcvfs.translatePath( os.path.join( addonPath , 'icon.png' ) )


xbmc.log(url,xbmc.LOGINFO)
pDialog.update(25, 'Get redirect MP3 url')

resp = req.head(url, allow_redirects=True)
his = str(resp.history)
xbmc.log(his,xbmc.LOGINFO)

pDialog.update(50, 'History read')

xbmc.log(resp.url,xbmc.LOGINFO)

pDialog.update(75, 'MP3 url found')

pDialog.update(100, 'Starting playback')
xbmcPlayer = xbmc.Player()
playlist = xbmc.PlayList(xbmc.PLAYLIST_MUSIC)
listitem = xbmcgui.ListItem( title)
listart = "{ 'icon':'%s', 'thumb': '%s' }" % (icon, icon)
listitem.setArt( listart )
playlist.clear()
playlist.add( resp.url, listitem )
pDialog.close()
xbmc.executebuiltin("ActivateWindow(home)")
xbmcPlayer.play(playlist)

