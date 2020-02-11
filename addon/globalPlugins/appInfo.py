# -*- coding: UTF-8 -*-
# Application Info
# A global plugin for NVDA
# Copyright 2020 Alberto Buffolino, released under GPL
import api
import ui
import addonHandler
import globalPluginHandler
from scriptHandler import getLastScriptRepeatCount

addonHandler.initTranslation()

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def script_announceInfo(self, gesture):
		obj = api.getForegroundObject()
		infos = {}
		try:
			# Translators: dict key spoken below
			infos[_("Executable name")] = obj.appModule.appName
			# Translators: dict key spoken below
			infos[_("Product name")] = obj.appModule.productName
			# Translators: dict key spoken below
			infos[_("Product version")] = obj.appModule.productVersion
		except:
			pass
		if getLastScriptRepeatCount() and infos:
			info = '; '.join(['%s: %s'%(k,v) for k,v in infos.items()])
			if api.copyToClip(info):
				# Translators: message announcing what was copied
				ui.message(_("Application info copied in clipboard"))
		elif infos:
			info = '; '.join(['%s: %s'%(k,v) for k,v in infos.items()])
			ui.message(info)
		else:
			ui.message(_("Application info not available"))
	script_announceInfo.__doc__ = _("Reports application info")

	__gestures = {
		"kb:NVDA+Shift+V": "announceInfo",
	}
