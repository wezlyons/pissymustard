import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,datetime,os,json,base64,plugintools
import FlawlessTv
import common,xbmcvfs,zipfile,downloader,extract
import xml.etree.ElementTree as ElementTree
reload(sys)
sys.setdefaultencoding('utf8')
SKIN_VIEW_FOR_MOVIES="515"
Bananas = 'cGx1Z2luLnZpZGVvLmZ1dHVyZXN0cmVhbXM='
addonDir = plugintools.get_runtime_path()
global kontroll
background = "YmFja2dyb3VuZC5wbmc=" 
defaultlogo = "ZGVmYXVsdGxvZ28ucG5n" 
hometheater = "aG9tZXRoZWF0ZXIuanBn"
noposter = "bm9wb3N0ZXIuanBn"
theater = "dGhlYXRlci5qcGc="
addonxml = "YWRkb24ueG1s"
addonpy = "ZGVmYXVsdC5weQ=="
icon = "aWNvbi5wbmc="
fanart = "ZmFuYXJ0LmpwZw=="
message = "VU5BVVRIT1JJWkVEIEVESVQgT0YgQURET04h"
#livetv.png = "bGl2ZXR2LnBuZw=="
#Url ="aHR0cDovL29uZXN0cmVhbS5kZG5zLm5ldA=="
#Flawless encode = "aHR0cDovLzE1MS44MC4xMDUuMTg3"
#advanced settings ="c3BlY2lhbDovL3VzZXJkYXRhL2FkdmFuY2Vkc2V0dGluZ3MueG1s"
#Port number 5454="NTQ1NA=="
#Flawless Port 4545="NDU0NQ=="

def run():
    global pnimi
    global televisioonilink
    global filmilink
    global andmelink
    global uuenduslink
    global lehekylg
    global LOAD_LIVE
    global uuendused
    global vanemalukk
    global version
    version = int(get_live("MQ=="))
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    if not kasutajanimi:
        kasutajanimi = "NONE"
        salasona="NONE"
    lehekylg=get_live("aHR0cDovL2ZsYXdsZXNzLWlwdHYubmV0")
    pordinumber=get_live("NDU0NQ==")
	
    uuendused=plugintools.get_setting(sync_data("dXVlbmR1c2Vk"))
    vanemalukk=plugintools.get_setting(sync_data("dmFuZW1hbHVraw=="))
    pnimi = get_live("T25lIFZpZXc=")
    LOAD_LIVE = os.path.join( plugintools.get_runtime_path() , "resources" , "art" )
    plugintools.log(pnimi+get_live("U3RhcnRpbmcgdXA="))
    televisioonilink = get_live("JXM6JXMvZW5pZ21hMi5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmdHlwZT1nZXRfbGl2ZV9jYXRlZ29yaWVz")%(lehekylg,pordinumber,kasutajanimi,salasona)
    filmilink = vod_channels("JXM6JXMvZW5pZ21hMi5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmdHlwZT1nZXRfdm9kX2NhdGVnb3JpZXM=")%(lehekylg,pordinumber,kasutajanimi,salasona)
    andmelink = vod_channels("JXM6JXMvcGFuZWxfYXBpLnBocD91c2VybmFtZT0lcyZwYXNzd29yZD0lcw==")%(lehekylg,pordinumber,kasutajanimi,salasona)
    params = plugintools.get_params()

    if params.get("action") is None:
        peamenyy(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    plugintools.close_item_list()

def peamenyy(params):
    plugintools.log(pnimi+vod_channels("TWFpbiBNZW51")+repr(params))
    load_channels()
    if not lehekylg:
        plugintools.open_settings_dialog()

    channels = kontroll()
    if channels == 1 and FlawlessTv.mode != 5 and FlawlessTv.mode != 1:
        plugintools.set_view( plugintools.LIST )
        plugintools.log(pnimi+vod_channels("TG9naW4gU3VjY2Vzcw=="))
        plugintools.add_item( action=vod_channels("ZXhlY3V0ZV9haW5mbw=="),   title="Account Information", thumbnail=os.path.join(LOAD_LIVE,vod_channels("bXlhY2MucG5n")), folder=True )
        plugintools.add_item( action=vod_channels("c2VjdXJpdHlfY2hlY2s="),  title="PissyMustard TV" , thumbnail=os.path.join(LOAD_LIVE,vod_channels("bGl2ZXR2LnBuZw==")) , folder=True )
        plugintools.add_item( action=vod_channels("ZGV0ZWN0X21vZGlmaWNhdGlvbg=="),   title=vod_channels("T24gRGVtYW5k") , thumbnail=os.path.join(LOAD_LIVE,vod_channels("bXlhY2MucG5n")), folder=True )
        plugintools.add_item( action=vod_channels("bGljZW5zZV9jaGVjaw=="), title="Settings" , thumbnail=os.path.join(LOAD_LIVE,vod_channels("bXlhY2MucG5n")), folder=False )
        #FlawlessTv.AddDir('Extras','Extras',5,FlawlessTv.Images + 'extras.png')
    elif channels != 1 and FlawlessTv.mode != 1:
        plugintools.add_item( action=vod_channels("bGljZW5zZV9jaGVjaw=="), title="Step 1. Insert Login Credentials" , thumbnail=os.path.join(LOAD_LIVE,vod_channels("c2V0dGluZ3MuanBn")), folder=False )	
        plugintools.add_item( action=vod_channels("bGljZW5zZV9jaGVjazI="), title="Step 2. Click Once Login Is Input" , thumbnail=os.path.join(LOAD_LIVE,vod_channels("c2V0dGluZ3MuanBn")), folder=False )	
    if plugintools.get_setting("improve")=="true":
        tseaded = xbmc.translatePath(sync_data("c3BlY2lhbDovL3VzZXJkYXRhL2FkdmFuY2Vkc2V0dGluZ3MueG1s"))
        if not os.path.exists(tseaded):
            file = open( os.path.join(plugintools.get_runtime_path(),vod_channels("cmVzb3VyY2Vz"),sync_data("YWR2YW5jZWRzZXR0aW5ncy54bWw=")) )
            data = file.read()
            file.close()
            file = open(tseaded,"w")
            file.write(data)
            file.close()
            plugintools.message(pnimi, get_live("TmV3IGFkdmFuY2VkIHN0cmVhbWluZyBzZXR0aW5ncyBhZGRlZC4="))

def license_check(params):
    plugintools.log(pnimi+get_live("U2V0dGluZ3MgbWVudQ==")+repr(params))
    plugintools.open_settings_dialog()
def license_check2(params):
    xbmc.executebuiltin('Container.Refresh')
def security_check(params):
    plugintools.log(pnimi+sync_data("TGl2ZSBNZW51")+repr(params))
    request = urllib2.Request(televisioonilink, headers={"Accept" : "application/xml"})
    u = urllib2.urlopen(request)
    tree = ElementTree.parse(u)
    rootElem = tree.getroot()
    for channel in tree.findall(sync_data("Y2hhbm5lbA==")):
        kanalinimi = channel.find(get_live("dGl0bGU=")).text
        kanalinimi = base64.b64decode(kanalinimi)
        kategoorialink = channel.find(vod_channels("cGxheWxpc3RfdXJs")).text
        CatID = channel.find(get_live("Y2F0ZWdvcnlfaWQ=")).text        
        plugintools.add_item( action=get_live("c3RyZWFtX3ZpZGVv"), title=kanalinimi , url=CatID , thumbnail=os.path.join(LOAD_LIVE,sync_data("bGl2ZXR2LnBuZw==")) , fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) ,info_labels=kanalinimi, folder=True )
	                            
    plugintools.set_view( plugintools.LIST )
def detect_modification(params):
    plugintools.log(pnimi+vod_channels("Vk9EIE1lbnUg")+repr(params))        
    request = urllib2.Request(filmilink, headers={"Accept" : "application/xml"})
    u = urllib2.urlopen(request)
    tree = ElementTree.parse(u)
    rootElem = tree.getroot()
    for channel in tree.findall(sync_data("Y2hhbm5lbA==")):
        filminimi = channel.find(get_live("dGl0bGU=")).text
        filminimi = base64.b64decode(filminimi)
        kategoorialink = channel.find(vod_channels("cGxheWxpc3RfdXJs")).text
        plugintools.add_item( action=vod_channels("Z2V0X215YWNjb3VudA=="), title=filminimi , url=kategoorialink , thumbnail=os.path.join(LOAD_LIVE,sync_data("bGl2ZXR2LnBuZw==")) , fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) , folder=True )
	
    plugintools.set_view( plugintools.LIST )
def stream_video(params):
    plugintools.log(pnimi+sync_data("TGl2ZSBDaGFubmVscyBNZW51IA==")+repr(params))
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    CatID = params.get(get_live("dXJs")) #description
    url = get_live("aHR0cDovL2ZsYXdsZXNzLWlwdHYubmV0OjQ1NDUvZW5pZ21hMi5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmdHlwZT1nZXRfbGl2ZV9zdHJlYW1zJmNhdF9pZD0lcw==")%(kasutajanimi,salasona,CatID)
    request = urllib2.Request(url, headers={"Accept" : "application/xml"})
    u = urllib2.urlopen(request)
    tree = ElementTree.parse(u)
    rootElem = tree.getroot()
    for channel in tree.findall(sync_data("Y2hhbm5lbA==")): #channel
        kanalinimi = channel.find(get_live("dGl0bGU=")).text #title
        kanalinimi = base64.b64decode(kanalinimi)
        kanalinimi = kanalinimi.partition("[")
        striimilink = channel.find(get_live("c3RyZWFtX3VybA==")).text #stream_url
        poo = striimilink
        if "http://flawless-iptv.net/enigma2.php"  in striimilink: 
            poo = striimilink.split(kasutajanimi,1)[1]
            poo = poo.split(salasona,1)[1]
            poo = poo.split("/",1)[1]            
        pilt = channel.find(vod_channels("ZGVzY19pbWFnZQ==")).text #desc_image
        kava = kanalinimi[1]+kanalinimi[2]
        kava = kava.partition("]")
        kava = kava[2]
        kava = kava.partition("   ")
        kava = kava[2]
        shou = get_live("W0NPTE9SIHdoaXRlXSVzIFsvQ09MT1Jd")%(kanalinimi[0])+kava #[COLOR white]%s [/COLOR]
        kirjeldus = channel.find(sync_data("ZGVzY3JpcHRpb24=")).text #description
        if kirjeldus:
           kirjeldus = base64.b64decode(kirjeldus)
           nyyd = kirjeldus.partition("(")
           nyyd = sync_data("Tm93OiA=") +nyyd[0]
           jargmine = kirjeldus.partition(")\n")
           jargmine = jargmine[2].partition("(")
           jargmine = sync_data("TmV4dDog") +jargmine[0] #shou
           kokku = nyyd+jargmine
        else:
           kokku = ""
        if pilt:
           plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=shou , url=poo, thumbnail=pilt, plot=kokku, fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")), extra="", isPlayable=True, folder=False )
        else:
           plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=shou , url=poo, thumbnail=os.path.join(LOAD_LIVE,vod_channels("bGl2ZXR2LnBuZw==")) , plot=kokku, fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) , extra="", isPlayable=True, folder=False )
    plugintools.set_view( plugintools.EPISODES )
    xbmc.executebuiltin(vod_channels("Q29udGFpbmVyLlNldFZpZXdNb2RlKDUwMyk="))
		
def get_myaccount(params):
        plugintools.log(pnimi+get_live("Vk9EIGNoYW5uZWxzIG1lbnUg")+repr(params))
        if vanemalukk == "true":
           pealkiri = params.get(sync_data("dGl0bGU="))
           vanema_lukk(pealkiri)
        purl = params.get(get_live("dXJs"))
        request = urllib2.Request(purl, headers={"Accept" : "application/xml"})
        u = urllib2.urlopen(request)
        tree = ElementTree.parse(u)
        rootElem = tree.getroot()
        for channel in tree.findall(sync_data("Y2hhbm5lbA==")):
            pealkiri = channel.find(get_live("dGl0bGU=")).text
            pealkiri = base64.b64decode(pealkiri)
            pealkiri = pealkiri.encode("utf-8")
            striimilink = channel.find(sync_data("c3RyZWFtX3VybA==")).text
            pilt = channel.find(sync_data("ZGVzY19pbWFnZQ==")).text
            kirjeldus = channel.find(vod_channels("ZGVzY3JpcHRpb24=")).text
            if kirjeldus:
               kirjeldus = base64.b64decode(kirjeldus) 
            if pilt:
               plugintools.add_item( action="restart_service", title=pealkiri , url=striimilink, thumbnail=pilt, plot=kirjeldus, fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) , extra="", isPlayable=True, folder=False )
            else:
               plugintools.add_item( action="restart_service", title=pealkiri , url=striimilink, thumbnail=os.path.join("bGl2ZXR2LnBuZw=="), plot=kirjeldus, fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) , extra="", isPlayable=True, folder=False )
        plugintools.set_view( plugintools.EPISODES )
        xbmc.executebuiltin('Container.SetViewMode(503)')
	
def run_cronjob(params):
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    lopplink = params.get("url")
    if "http://"  not in lopplink: 
        lopplink = get_live("aHR0cDovLzE1MS44MC4xMDUuMTg3OjQ1NDUvZW5pZ21hLnBocC9saXZlLyVzLyVzLyVz")%(kasutajanimi,salasona,lopplink)
        lopplink = lopplink[:-2]
        lopplink = lopplink + "m3u8"
    listitem = xbmcgui.ListItem(path=lopplink)
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)

def sync_data(channel):
    video = base64.b64decode(channel)
    return video

def restart_service(params):
    lopplink = params.get(vod_channels("dXJs"))
    plugintools.play_resolved_url( lopplink )

def grab_epg():
    req = urllib2.Request(andmelink)
    req.add_header(sync_data("VXNlci1BZ2VudA==") , vod_channels("S29kaSBwbHVnaW4gYnkgTWlra00="))
    response = urllib2.urlopen(req)
    link=response.read()
    jdata = json.loads(link.decode('utf8'))
    response.close()
    if jdata:
       plugintools.log(pnimi+sync_data("amRhdGEgbG9hZGVkIA=="))
       return jdata
def kontroll():
    randomstring = grab_epg()
    kasutajainfo = randomstring[sync_data("dXNlcl9pbmZv")]
    kontroll = kasutajainfo[get_live("YXV0aA==")]
    return kontroll
def get_live(channel):
    video = base64.b64decode(channel)
    return video
def execute_ainfo(params):
    plugintools.log(pnimi+get_live("TXkgYWNjb3VudCBNZW51IA==")+repr(params))
    andmed = grab_epg()
    kasutajaAndmed = andmed[sync_data("dXNlcl9pbmZv")]
    seis = kasutajaAndmed[get_live("c3RhdHVz")]
    aegub = kasutajaAndmed[sync_data("ZXhwX2RhdGU=")]
    if aegub:
       aegub = datetime.datetime.fromtimestamp(int(aegub)).strftime('%d/%m/%Y %H:%M')
    else:
       aegub = vod_channels("TmV2ZXI=")
    leavemealone = kasutajaAndmed[get_live("bWF4X2Nvbm5lY3Rpb25z")]
    polarbears = kasutajaAndmed[sync_data("dXNlcm5hbWU=")]
    plugintools.add_item( action="",   title=sync_data("W0NPTE9SID0gd2hpdGVdVXNlcjogWy9DT0xPUl0=")+polarbears , thumbnail=os.path.join(LOAD_LIVE,vod_channels("bGl2ZXR2LnBuZw==")) , fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) , folder=False )
    plugintools.add_item( action="",   title=sync_data("W0NPTE9SID0gd2hpdGVdU3RhdHVzOiBbL0NPTE9SXQ==")+seis , thumbnail=os.path.join(LOAD_LIVE,vod_channels("bGl2ZXR2LnBuZw==")) , fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) , folder=False )
    plugintools.add_item( action="",   title=get_live("W0NPTE9SID0gd2hpdGVdRXhwaXJlczogWy9DT0xPUl0=")+aegub , thumbnail=os.path.join(LOAD_LIVE,vod_channels("bGl2ZXR2LnBuZw==")) , fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) , folder=False )
    plugintools.add_item( action="",   title=vod_channels("W0NPTE9SID0gd2hpdGVdTWF4IGNvbm5lY3Rpb25zOiBbL0NPTE9SXQ==")+leavemealone , thumbnail=os.path.join(LOAD_LIVE,vod_channels("bGl2ZXR2LnBuZw==")) , fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) , folder=False )
    #plugintools.add_item( action="",   title=vod_channels("U2lnbiB1cCBhdCBGdXR1cmVTdHJlYW1zLnRr") , thumbnail=os.path.join(LOAD_LIVE,vod_channels("bXlhY2MucG5n")) , fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) , folder=False )
	
    plugintools.set_view( plugintools.LIST )
def vanema_lukk(name):
        plugintools.log(pnimi+sync_data("UGFyZW50YWwgbG9jayA="))
        a = 'XXX', 'Adult', 'Adults','ADULT','ADULTS','adult','adults','Porn','PORN','porn','Porn','xxx'
        if any(s in name for s in a):
           xbmc.executebuiltin((u'XBMC.Notification("Parental Lock", "Channels may contain adult content", 2000)'))
           text = plugintools.keyboard_input(default_text="", title=get_live("UGFyZW50YWwgbG9jaw=="))
           if text==plugintools.get_setting(sync_data("dmFuZW1ha29vZA==")):
              return
           else:
              exit()
        else:
           name = ""
def DownloaderClass(url,dest):
    dp = xbmcgui.DialogProgress()
    dp.create(sync_data("R2V0dGluZyB1cGRhdGU="),get_live("RG93bmxvYWRpbmc="))
    urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
def check_user():
    plugintools.message(get_live("RVJST1I="),vod_channels("VU5BVVRIT1JJWkVEIEVESVQgT0YgQURET04h"))
    sys.exit()
def _pbhook(numblocks, blocksize, filesize, url=None,dp=None):
    try:
        percent = min((numblocks*blocksize*100)/filesize, 100)
        print percent
        dp.update(percent)
    except:
        percent = 100
        dp.update(percent)
    if dp.iscanceled(): 
        print "DOWNLOAD CANCELLED"
        dp.close()
def load_channels():
    statinfo = os.stat(LOAD_LIVE+"/"+get_live("YmFja2dyb3VuZC5wbmc="))

def vod_channels(channel):
    video = base64.b64decode(channel)
    return video
run()
