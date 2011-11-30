from flask import Flask, request, session, g, redirect, \
                url_for, abort, render_template, flash, \
                make_response

from Termline import app
from PIL import Image, ImageDraw, ImageFont
import tempfile, random, StringIO, string, pprint

def linify (str, w, f, s):
    words = string.split(str, ' ')
    lines = [words[0]]
    curLine = 0
    for i in range(1, len(words)):
        font = ImageFont.truetype(f, s)
        dim = font.getsize( lines[curLine] + words[i] )
        if (dim[0] < w):
            lines[curLine] += ' ' + words[i]
        else: 
            curLine += 1
            lines.append(words[i])
    return lines

def textbox (draw, str, x, y, w, h, bg, fg, font="League Gothic.otf", size=50, box=True, shadow=False, shadowDepth = 2):
    """
        Creates a text centered within the given dimentions of area
        if str is long or height is too small for font,
        font size will be shrunken, however, won't grow to fit
        
        str = text to render
        x, y = position
        w, h = dimetion
        bg = color of box
        fg = color of text
        box = to render box or not
    """
    
    if box:
        draw.rectangle( [(x,y), (x+w,y+h)], fill=bg)

    fontsize = size + 2
    while True:
        fontsize -= 2
        (xx, yy) = ImageFont.truetype(font, fontsize).getsize(str)
        if (xx < w and yy < h):
            break
    
    font = ImageFont.truetype(font, fontsize)
    xx, yy = font.getsize(str)
    if shadow:
        draw.text( ( x+ w/2 - xx/2 + shadowDepth, y + h/2 - yy/2 + shadowDepth ), str, font=font, fill="#333")
        draw.text( ( x+ w/2 - xx/2 , y + h/2 - yy/2 ), str, font=font, fill="white")
    else:
        draw.text( ( x+ w/2 - xx/2 , y + h/2 - yy/2 ), str, font=font, fill=fg)
    

@app.route('/')
def index():
    return render_template('generator.html')

@app.route('/generate', methods=['POST', 'GET']) 
def generate():

    theme1 = ['#1B1B2C','#21214C','#3635A8','#7B7BD1','#B6B5D1']
    theme2 = ['#0E3D59','#88A61B','#F29F05','#F25C05','#F25C05']
    theme3 = ['#2D4973','#306C85','#306C85','#339994','#339994']
    theme = theme1 + theme2 + theme3
    # random.shuffle(theme)
    # print theme[0], theme[1], theme[2], theme[3], theme[4]

    # uwtheme = ['#009AA6', '#E98300', '#57068C', '#57068C', '#E0249A', '#0073CF']
     
    c = {}
    # bg should be dark
    cdark = [random.randrange(30,50),random.randrange(40,60),random.randrange(50,70)]
    random.shuffle( cdark )
    c['bg'] = tuple(cdark)
    c['bg'] = "#FECB00"
    # fg should be bright
    cbright = [random.randrange(100,150),random.randrange(120,150),random.randrange(120,150)]
    c['fg'] = tuple(cbright)
    c['fg'] = "#000000"

    # work and school bg and fg are inverted
    # should pick opposite for high contrast
    # cc = [random.randrange(30,70),random.randrange(200,220),random.randrange(20,50)]
    cc = [random.randrange(30,70),random.randrange(200,220),random.randrange(80,120)]
    random.shuffle(cc)
    c1 = tuple(cc)
    cc2 = [255-cc[0], 255-cc[1], 255-cc[2]]
    random.shuffle(cc2)
    c2 = tuple(cc2)
    
    c1 = "#24221F"
    c2 = "#5E7C88"
    c['workbg'] = c1
    c['workfg'] = '#e5e5e5'
    
    c['schoolbg'] = c2
    c['schoolfg'] = '#e5e5e5'
    
    pprint.pprint(c)

    c['font'] = "League Gothic.otf"
    c['m100'] = "Museo_Slab_100.otf"
    c['m300'] = "Museo_Slab_300.otf"
    c['m500'] = "Museo_Slab_500.otf"
    c['m700'] = "Museo_Slab_700.otf"
    c['m900'] = "Museo_Slab_900.otf"
    c['size'] = 48
    
    c['width'] = 960
    c['height'] = 760
    c['margin'] = 50

    img = Image.new('RGBA', (c['width'], c['height']), c['bg'])
    draw = ImageDraw.Draw(img)

    name = request.values.get('name', 'Hoon')
    study = request.values.get('study', 'Engineering')
    school = request.values.get('school', 'University of Waterloo')
    
    textIntro = "Hello. My name is %s. I study %s @ %s. Here is my timeline." % (name, study, school)
    
    font = ImageFont.truetype(c['font'], c['size'])
    smallfont = ImageFont.truetype(c['font'], c['size']/2)
    m300 = ImageFont.truetype(c['m300'], c['size'])
    m500 = ImageFont.truetype(c['m500'], c['size'])
    draw.setfont(font)

    terms = []
    terms.append({ 'type':"title", 'title': "Winter", "year": " ", "term": "1" })
    terms.append({ 'type':"title", 'title': "Spring", "year": " ", "term": "2" })
    terms.append({ 'type':"title", 'title': "Fall", "year": " ", "term": "3" })
    for key in sorted(request.values.iterkeys()):
        keysplit = string.split(key,'-')
        if (len(keysplit) is 2 and len(request.values.get(key)) is not 0):
            terms.append({'title': request.values.get(key), "year": keysplit[0], "term": keysplit[1] })
    
    # terms.append({ 'type':"school", 'title': "1A", "year": "2008", "term": "3" })
    # terms.append({ 'type':"school", 'title': "1B", "year": "2009", "term": "1" })
    # terms.append({ 'type':"work", 'title': "Indigo", "year": "2009", "term": "2" })
    # terms.append({ 'type':"school", 'title': "2A", "year": "2009", "term": "3" })
    # terms.append({ 'type':"work", 'title': "Shoppers", "year": "2010", "term": "1" })
    # terms.append({ 'type':"school", 'title': "2B", "year": "2010", "term": "2" })
    # terms.append({ 'type':"work", 'title': "Telus", "year": "2010", "term": "3" })
    # terms.append({ 'type':"school", 'title': "3A", "year": "2011", "term": "1" })
    # terms.append({ 'type':"work", 'title': "Facebook", "year": "2011", "term": "2" })
    # terms.append({ 'type':"school", 'title': "3B", "year": "2011", "term": "3" })
    # terms.append({ 'type':"work", 'title': "Microsoft is gonna be awesome", "year": "2012", "term": "1" })
    # terms.append({ 'type':"school", 'title': "4A", "year": "2012", "term": "2" })
    # terms.append({ 'type':"work", 'title': "Hire ME", "year": "2012", "term": "3" })

    t = {}
    for term in terms:
        if not t.has_key(term['year']):
            t[term['year']] = {}
        t[term['year']][term['term']] = term['title']

    
    both = (True, False)
    leftspread = random.choice(both);
    
    if leftspread:
        boundleft = 0
        boxw = (c['width'] - c['margin'] - 100) /3
        yearx = boxw*3 + 25
    else:
        boundleft = c['margin'] + 100
        boxw = (c['width'] - c['margin'] - 100) /3
        yearx = 25
    boxh =  50
    curWidth = 200
    curHeight = 250

    for year in sorted(t.iterkeys()):
        # this is for blank terms
        draw.rectangle([(boundleft,curHeight), (boundleft+boxw*3,curHeight+boxh)], fill='#ddd') 
        # year label
        textbox( draw, year, yearx, curHeight, 100, boxh, None, 'white', font=c['m500'], box=False, shadow=True, shadowDepth = 1)
        for term in sorted(t[year].iterkeys()):
            # draw
            # school term
            if len(t[year][term]) < 4:
                # school term
                # draw.rectangle([(200*int(term),curHeight), (200*int(term)+200,curHeight+50)], fill=c['schoolbg'])
                # draw.text((200*int(term)+20,curHeight), t[year][term], fill=c['schoolfg'])
                # def textbox(str, x, y, w, h, bg, fg, font="League Gothic.otf", size=50, box=True):
                textbox( draw, t[year][term], boundleft+boxw*int(term)-boxw, curHeight, boxw, boxh, c['schoolbg'], c['schoolfg'], font=c['m500'], shadow=True)
            else:
                # work term
                # draw.rectangle([(200*int(term),curHeight), (200*int(term)+200,curHeight+50)], fill=c['workbg'])
                # draw.text((200*int(term)+20,curHeight), t[year][term], fill=c['workfg'])
                textbox( draw, t[year][term], boundleft+boxw*int(term)-boxw, curHeight, boxw, boxh, c['workbg'], c['workfg'], font=c['m500'], shadow=True)
            # if last term, new line
            if term is "3":
                curHeight += boxh+15

    # lines = linify(textIntro, c['width']-c['margin']*2, c['font'], c['size'])
    lines = linify(textIntro, 800, c['m500'], c['size'])
    
    height = c['margin']
    for line in lines:
        draw.text((c['margin'],height), line, font=m500, fill=c['fg'])
        height += 50

    tagline = "%s's timeline is generated @ http://termline.me" % name
    smallm300 = ImageFont.truetype(c['m300'], 24)
    xx, yy = smallm300.getsize(tagline)
    draw.text( (c['width']-xx-c['margin']/2, c['height']-yy-c['margin']/4), tagline, font=smallm300, fill=c['fg'])

    out = StringIO.StringIO()
    img.save(out, "png")

    r = make_response(out.getvalue())
    r.headers["Content-Type"] = "image/png"
    return r
