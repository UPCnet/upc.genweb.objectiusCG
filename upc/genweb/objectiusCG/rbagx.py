# -*- coding: utf-8 -*-
#
# rbagx.py ;  Autor : Carles Bruguera <carles@plentysolutions.eu>
#
# Script per re-executar archgenxml sobre un egg.
# Renombra tots els arxius necessaris per adaptar els Productes de archgenxml a l'espai de noms del nostre egg
#

import os
import subprocess

def sar(a,b,f):
    fin = open(f)
    fout = open('%s.replaced' % f, "wt")
    for line in fin:
        fout.write( line.replace(a,b) )
    fin.close()
    fout.close()
    os.rename('%s.replaced' % f, f)
    print 'INFO S\'ha reemplaçat la cadena "%s" per "%s" en l\'arxiu %s' % (a,b,f)
    return

def searchEggName():
    path = os.getcwd()
    while not os.path.exists('%s/setup.py' % path):
        path = '/'.join(path.split('/')[:-1])
    return '.'.join(os.getcwd().replace(path,'').split('/')[1:])
#VARIABLES

EGG_NAME = searchEggName()
EGG_TITLE = 'Genweb UPC ObjectiusCG'
AGX_NAME = EGG_NAME.split('.')[-1]
CONTENT_DIRS = ['content']
CONTENT_EXCLUDE_FILES = ['__init__.py','interfaces.py']

#Fem la llista de tipus
types=[]
for dirs in CONTENT_DIRS:
    if os.path.exists(dirs):
        types = types + [ dict(name=a[:-3],path=dirs) for a in os.listdir(dirs) if a.endswith('.py') and a not in CONTENT_EXCLUDE_FILES ]
    
    
replaces = [

    ('PROJECTNAME = "%s"' % AGX_NAME, 
     'PROJECTNAME = "%s"' % EGG_NAME, 
     ['config.py']),

    ('Products.%s' % AGX_NAME,
     EGG_NAME,
     ['setuphandlers.py','config.py','profiles/default/import_steps.xml',] + ['%s/%s.py' % (a['path'],a['name']) for a in types ]),

    ("i18n_domain='%s'" % AGX_NAME,
     "i18n_domain='%s'" % EGG_NAME,
     ['%s/%s.py' % (a['path'],a['name']) for a in types ]),

    ('i18n_domain="%s"' % AGX_NAME,
     'i18n_domain="%s"' % EGG_NAME,
     ['configure.zcml','profiles.zcml']),
     
    ('product">%s' % AGX_NAME,
     'product">%s' % EGG_NAME,
     # AQUI busquem els .py, pero modifiquem els xml, ja que podrien haver-hi alguns xml de tipus que no fossin generats per archgen
     ['profiles/default/types/%s.xml' % (a['name']) for a in types if os.path.exists('profiles/default/types/%s.xml' % (a['name']))]),

    ('title="%s"' % AGX_NAME,
     'title="%s"' % EGG_TITLE,
     ['profiles.zcml']),
     
    ('Project-Id-Version: %s' % AGX_NAME,
     'Project-Id-Version: %s' % EGG_TITLE,
     ['i18n/generated.pot']),

    ('Domain: %s' % AGX_NAME,
     'Domain: %s' % EGG_NAME,
     ['i18n/generated.pot']),

     
    ('%s/' % AGX_NAME,
     '%s:' % EGG_NAME,
     ['profiles/default/skins.xml']),

]

#rebuild

removes = ['profiles/default/skins.xml']
for re in removes:
    if os.path.exists(re):
        os.remove(re)
        print "INFO Esborrant arxiu %s" % re
        
xmi_file = [fi for fi in os.listdir('model') if fi.endswith('xmi')][-1]

os.chdir('/'.join(os.getcwd().split('/')[:-1]))
print 'INFO Executant "archgenxml %s/model/%s' % (AGX_NAME,xmi_file)
subprocess.call(['archgenxml','%s/model/%s' % (AGX_NAME,xmi_file)])
os.chdir('%s/%s' % (os.getcwd(),AGX_NAME))

#rename
for a,b,files in replaces:
  for filename in files:
    sar(a,b,filename)
