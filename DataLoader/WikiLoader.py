import wikipedia
import requests
import json
import DSELoader
import logging

log = logging.getLogger()
log.setLevel('INFO')
logging.disable("DEBUG")

handler = logging.StreamHandler()

handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))
log.addHandler(handler)


queueWikiPages = []
queueWikiPagesJson = []

class WikiPage:

    def __init__(self,title,links,category,content,parent,lang):

        self.title=title
        self.links=links
        self.category=[category]
        self.content=content
        self.parent=parent
        self.lang=lang

def AddWikiPageQueue(pageIn) :
    currWikiPageJson =  json.dumps(vars(pageIn),sort_keys=True, indent=4)
    queueWikiPagesJson.append(currWikiPageJson)
    queueWikiPages.append(pageIn)

def LoadWikiPageQueue(queueIn,langIn):
    wikipedia.set_lang(langIn)
    counter = 0
    while counter != len(queueIn):
        try:
            currWikiPage=wikipedia.page(title=queueIn[counter])
            print currWikiPage.title
            print currWikiPage.parent_id
            counter = counter + 1
            AddWikiPageQueue(currWikiPage)
        except:
            print "[BOOM] Error on Getting WikiPage that page, continue to next page"

            counter = counter+1

def GetRandomPages(maxPagesIn,langIn):
    wikipedia.set_lang(langIn)
    randonPages = wikipedia.random(maxPagesIn)
    return randonPages

def SetWikiLanguages():
    curr_lang = wikipedia.languages()
    return curr_lang

def PrintPages(PagesIn,langIn):
    wikipedia.set_lang(langIn)
    for p in PagesIn: print p

def get_wikipedia_basic_info(titles):
    atts = {'prop': 'info', 'action': 'query', 'format': 'json',
      'inprop': 'protection|watchers',
      'titles': titles
    }
    resp = requests.get('http://en.wikipedia.org/w/api.php', params = atts)

    return resp.json()

def print_wiki_object(cuuPage):
    print cuuPage.title
    print cuuPage.url
    print cuuPage.categories
    print cuuPage.content
    print cuuPage.parent_id

def insertQueueDSE(queueIn, sessionIn, langIn):

    prepared = sessionIn.prepare("""
        INSERT INTO solrdemo.wikipages (title, links, category,parent,content,lang)
        VALUES (?, ?, ?,?,?,?)
        """)

    counter = 0
    while counter != len(queueIn):
        currPage = queueIn[counter]
        sessionIn.execute(prepared, (currPage.title, currPage.url, currPage.categories,str(currPage.parent_id),currPage.content,langIn))
        counter = counter+1

def main():

    #print wikipedia.summary("Wikipedia")
    #print wikipedia.summary("GitHub")
    #curr_lang=wikipedia.languages()
    #print wikipedia.random(pages=10)

    curr_lang = SetWikiLanguages()
    enPages = GetRandomPages(10,'en')
    frPages = GetRandomPages(10,'fr')
    ruPages = GetRandomPages(10,'ru')
    esPages = GetRandomPages(10,'es')
    dePages = GetRandomPages(10,'de')

    currCluster = DSELoader.setupCluster()
    currSession = DSELoader.connect(currCluster)

    LoadWikiPageQueue(enPages,'en')
    insertQueueDSE(queueWikiPages,currSession,'en')

    LoadWikiPageQueue(frPages,'fr')
    insertQueueDSE(queueWikiPages,currSession,'fr')

    LoadWikiPageQueue(ruPages,'ru')
    insertQueueDSE(queueWikiPages,currSession,'ru')

    LoadWikiPageQueue(esPages,'es')
    insertQueueDSE(queueWikiPages,currSession,'es')

    LoadWikiPageQueue(dePages,'de')
    insertQueueDSE(queueWikiPages,currSession,'de')

if __name__ == "__main__":
    main()