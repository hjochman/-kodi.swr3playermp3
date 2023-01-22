# -*- coding: utf-8 -*-


import os,xbmcgui,xbmc,xbmcaddon
import requests as req
import re


title = 'SWR3 MP3 Livestream'
url = 'https://liveradio.swr.de/sw282p3/swr3/play.mp3'
pDialog = xbmcgui.DialogProgress()
pDialog.create(title, 'Initializing script...')

addonID = 'plugin.audio.swr3playermp3'
addon = xbmcaddon.Addon(id = addonID)
addonPath = addon.getAddonInfo('path')
icon = xbmc.translatePath( os.path.join( addonPath , 'icon.png' ) )

pDialog.update(25, 'Get redirect MP3 url',url)

resp = req.head(url, allow_redirects=True)
his = str(resp.history)
xbmc.log(his,xbmc.LOGNOTICE)

pDialog.update(50, 'History',his)

xbmc.log(resp.url,xbmc.LOGNOTICE)

pDialog.update(75, 'MP3 url',resp.url)

pDialog.update(100, 'Starting playback')
xbmcPlayer = xbmc.Player()
playlist = xbmc.PlayList(xbmc.PLAYLIST_MUSIC)
listitem = xbmcgui.ListItem( title, iconImage=icon, thumbnailImage=icon)
playlist.clear()
playlist.add( resp.url, listitem )
pDialog.close()
xbmc.executebuiltin("ActivateWindow(home)")
xbmcPlayer.play(playlist)

