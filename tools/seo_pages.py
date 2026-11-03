#!/usr/bin/env python3
"""Builds the indexable search landing pages (one folder per search intent).
Run from the repo root:  python3 tools/seo_pages.py
Edit the PAGES data below, never the generated index.html files by hand.
Prices here must match the homepage/editor DESIGNS and Apps Script PRICES."""
import json, html, os

SITE = "https://littlegasp.com"
CSSV = "14"   # keep in step with ?v= on style.css / site.js everywhere
TODAY = "2026-11-03"

DESIGN = {  # key: (name, price)
  "birthday-cake": ("Birthday Cake", 99), "birthday-wish": ("Make a Wish", 149),
  "apology": ("Mend the Heart", 149), "love-letter": ("Sealed with Love", 149),
  "anniversary": ("Memory Lane", 149), "karwa-chauth": ("Karwa Chauth Moon", 149),
  "diwali": ("Diwali Night", 149), "garba-circle": ("Garba Circle", 149),
  "proposal": ("Ring Hunt", 149), "miss-you": ("Miss You", 149),
}

COMMON_FAQ = [
  ("Can I see it before paying?", "Yes. The editor plays the whole surprise with your own photos and words while you write. You only pay when you're happy with it."),
  ("Do they need to install an app?", "No. It's a private web link that opens in any browser on a phone or laptop. Send it on WhatsApp, Instagram or anywhere else."),
  ("Who can see it?", "Only people who have the link. Customer surprises are hidden from Google and never listed anywhere."),
  ("How long does it stay live?", "At least 12 months from the day you order, so they can open it again whenever they like."),
  ("How do I pay?", "UPI, card or net banking through Razorpay. Your link appears on screen straight away and we email it to you too."),
]

PAGES = [
 dict(slug="digital-surprise-gifts", designs=list(DESIGN), hub=True,
  title="Personalised Interactive Digital Surprises | Little Gasp",
  desc="Make a personalised, interactive digital surprise: a little website they play through, with your photos, notes and letter. Free preview, private link.",
  h1="Personalised, interactive digital surprises",
  lead="Little Gasp is an online platform for making personalised digital surprises. Not a card and not a video: a tiny website the other person plays through on their phone, with your photos, your reasons and your letter hidden inside. You make it in about five minutes, watch the full preview free, then send one private link.",
  plays_title="What makes it different from an e-card",
  plays=["They <b>do</b> something on every screen: light candles, crack a wax seal, mend a broken heart, drive a scooter up memory lane.",
         "Your photos, little notes and letter appear as rewards along the way, so they take their time with every word.",
         "Many designs end with a question you write (\"Dinner on Saturday?\") and send their answer straight to your email.",
         "It works on any phone or laptop browser. Nothing to install, nothing to print, nothing to ship."],
  ideas_title="Pick the surprise that fits the moment",
  ideas=None,
  faq=[("What is a digital surprise?", "A digital surprise is a gift you send as a link instead of a parcel. On Little Gasp it's a small interactive website made just for one person, with your photos and words, that they tap through like a tiny game."),
       ("Is this a good last-minute gift?", "Yes. You can make it in a few minutes and the link is ready the moment you pay, so it works even on the day itself, or when you're in a different city.")],
 ),
 dict(slug="apology-website", designs=["apology"],
  title="Apology Website to Say Sorry | Little Gasp",
  desc="Say sorry with a website they play: they mend a broken heart, read your sorries and tell you how mad they still are. Free preview, private link.",
  h1="An apology website that says sorry properly",
  lead="When a text sorry gets left on seen, send something they'll actually open. <b>Mend the Heart</b> is a personalised sorry website for your girlfriend, boyfriend, husband, wife or best friend. They put a broken heart back together and every piece shows one thing you're sorry for.",
  plays_title="What happens when they open it",
  plays=["A sorry puppy is waiting. One tap and the story begins.",
         "A broken heart lies in pieces. They drag each piece home, and each one shows one of your sorries. Then gold seams fill the cracks.",
         "They wipe the fog off a rainy window to find your photos together.",
         "They shake a jar of paper stars, and each star unfolds into a promise you mean to keep.",
         "They read your letter, then turn the forgive-o-meter from \"Still furious\" to \"All good\". You see where they left it.",
         "You ask your question. If they tap \"Still mad\", the puppy tries chocolate, then flowers, then waits patiently. No pressure.",
         "They order from your make-up menu (pani puri, a movie of their choice, anything you add) and the order comes to your email."],
  ideas_title="What to write in a sorry",
  ideas=["Name the thing. \"I'm sorry I raised my voice on Sunday\" lands better than \"sorry for everything\".",
         "Say why it hurt them, not why you did it. Leave the explanations out of the first message.",
         "Keep each sorry to one line. The heart shows one per piece, so short and true works best.",
         "Promise small, specific things you will actually do: \"I'll call when I'm late.\"",
         "End with an easy next step, like a date or their favourite food, not a demand to be forgiven."],
  faq=[("How do I say sorry to my girlfriend creatively?", "Make it personal and let her take her time. A sorry website like Mend the Heart lets her read each apology at her own pace, see your photos and promises, and answer honestly with the forgive-o-meter instead of replying to a long text."),
       ("Will I know if they forgave me?", "If they move the forgive-o-meter or order from your make-up menu, their answer is emailed to you.")],
 ),
 dict(slug="birthday-surprise-website", designs=["birthday-wish","birthday-cake"],
  title="Birthday Surprise Website | Little Gasp",
  desc="A birthday surprise website they play: candles, a wish, balloons and gifts with your photos, notes and letter inside. Free preview, link in minutes.",
  h1="A birthday surprise website they'll play through",
  lead="Send more than \"HBD 🎂\". Make a personalised birthday website for your girlfriend, boyfriend, wife, husband, best friend or sister. They light the candles, make a wish and find your photos and messages one surprise at a time. Two designs to choose from.",
  plays_title="Two birthday surprises to choose from",
  plays=["<b>Make a Wish</b> (teddy bear party, pink or blue): they light six candles with a match, blow out a wish, pop balloons to read your reasons, unwrap gifts to find your photos, cut the cake to reveal your letter, then answer your question.",
         "<b>Birthday Cake</b> (the simple one): candles, a wish, confetti and a birthday song, then your photos, notes and letter. It ends with a birthday selfie booth that puts a painted crown on their head.",
         "Both play the birthday song, and you can upload your own song instead.",
         "Send the link at midnight and they can open it wherever they are."],
  ideas_title="Birthday message ideas that fit the balloons",
  ideas=["\"You laugh at your own jokes before the punchline and it's my favourite sound.\"",
         "\"Thank you for every 2 am call this year.\"",
         "\"You make ordinary Tuesdays feel like plans.\"",
         "A memory only you two share, in one line, works better than a long paragraph.",
         "End with a question: \"Dinner at our place on Saturday?\""],
  faq=[("What is the best online birthday surprise for a girlfriend or boyfriend far away?", "A birthday surprise website works well for long distance because it arrives instantly as a link, plays on their phone, and carries your photos and voice-like personal notes rather than a generic e-card."),
       ("Can I add our photos?", "Yes. Add up to five photos with captions, plus little reasons, a letter and a question.")],
 ),
 dict(slug="digital-love-letter", designs=["love-letter"],
  title="Digital Love Letter Website | Little Gasp",
  desc="Send a love letter they open: crack the wax seal, unfold your notes and watch a quill write every word. With your photos. Free preview.",
  h1="A digital love letter they open like a real one",
  lead="<b>Sealed with Love</b> turns your words into an interactive love letter website. A dove delivers it, they press the wax seal till it cracks, and a quill writes your letter in front of them. Made for a girlfriend, boyfriend, wife, husband or long-distance partner.",
  plays_title="What happens when they open it",
  plays=["A dove postman flies in with an envelope. They tap it.",
         "They press and hold the wax heart until it cracks, and the envelope really opens.",
         "They drag the folded letter open, and each crease shows one reason you love them.",
         "A quill writes your letter live, word by word.",
         "Pressed flowers turn into polaroids of your photos. Dated memories wait in a keepsake box.",
         "They join stars into a heart and your initials appear. A hidden P.S. shows only when they warm the paper with a candle.",
         "They untie a ribbon to find your question, and can write back with a thumbprint seal. Their reply comes to your email."],
  ideas_title="Love letter ideas",
  ideas=["Start with the moment you knew, in one or two plain sentences.",
         "Write reasons as small true details: \"the way you hum while cooking\".",
         "Put one memory per photo caption, with the date if you remember it.",
         "Save one line for the hidden P.S. Something just for them.",
         "Keep the question simple and kind: \"Will you be mine, again and always?\""],
  faq=[("How do I send a love letter online?", "Write it in the Little Gasp editor, add your photos and reasons, preview it free, then send the private link. They open it in any browser, no app needed."),
       ("Can they reply?", "Yes. At the end they can write back and seal it with a fingerprint heart, and their letter is emailed to you.")],
 ),
 dict(slug="anniversary-surprise-website", designs=["anniversary"],
  title="Anniversary Surprise Website | Little Gasp",
  desc="An anniversary gift they ride through: kick-start the scooter and drive up memory lane, where every milestone is one of your photos. Free preview.",
  h1="An anniversary surprise down memory lane",
  lead="<b>Memory Lane</b> is a personalised anniversary website for a wife, husband, girlfriend or boyfriend. They put on the helmets, kick-start the scooter and ride past every milestone of your story, one photo at a time, with up to 20 photos.",
  plays_title="What happens when they open it",
  plays=["They tap a helmet onto each of you, then swipe the kick lever to start the scooter.",
         "A paper map unfolds with the years you've been together.",
         "They hold the fuel nozzle, and each bar on the gauge is one reason you love them.",
         "They drive up a winding road. Every photo is a milestone with its year and caption.",
         "At the toll gate, each lift of the barrier shows a promise.",
         "You stop for chai, clink glasses, and your letter is written on the chalkboard.",
         "On the bridge they lock a love lock and throw away the key, then ride into forever."],
  ideas_title="Milestone ideas for your photos",
  ideas=["The first photo you ever took together.", "The first trip, even if it was only to Lonavala.",
         "The day you moved in, or the wedding day.", "A silly everyday photo. Those are often the favourites.",
         "This year: \"Still my favourite person to sit in traffic with.\""],
  faq=[("What is a good anniversary gift for my wife online?", "A personalised anniversary website is a thoughtful option because it is made from your own photos and memories, arrives instantly and can be opened again every year."),
       ("How many photos can I add?", "Memory Lane takes up to 20 photos, each with a short caption like \"2019: our first trip\".")],
 ),
 dict(slug="proposal-surprise-website", designs=["proposal"],
  title="Proposal Surprise Website, a Treasure Hunt | Little Gasp",
  desc="Propose with a treasure hunt: they search a dark house with a torch, watch your photos on a projector, then open the ring box. Free preview.",
  h1="A proposal surprise they hunt for",
  lead="<b>Ring Hunt</b> turns your proposal into a little treasure hunt on their phone. They follow a clue map through a dark house with a torch, find your reasons, a sweet note and your letter, watch your photos on an old projector, and open the ring box on the balcony to your question.",
  plays_title="What happens when they open it",
  plays=["They ring the doorbell and a note slides out from under the door.",
         "They unroll a treasure map with four clues marked on it. The map stays one tap away for the whole hunt.",
         "The house is dark, so they search each room with a torch. Warm and cold hints help, and a soft glow appears if they get stuck.",
         "Behind the photo frame: all your reasons. In the cookie jar: a sweet note. Inside a book: your letter. Under the cushion: a film reel.",
         "They follow a trail of rose petals to the balcony door.",
         "An old projector plays your photos as a little film, all by itself.",
         "They tap the ring box, it opens, and your question appears. Their yes is emailed to you."],
  ideas_title="Ideas for a proposal letter",
  ideas=["Start with the first moment you knew, in one plain sentence.",
         "Name small, real things you love: \"how you hum while making chai\".",
         "Use photo captions as tiny chapters of your story, in order.",
         "Keep the question short and in your own words: \"Will you marry me?\" or \"Will you be mine, always?\"",
         "Plan where you'll be when they open it. Many people send the link and wait in the next room with the real ring."],
  faq=[("Can I propose online with a website?", "Yes. Ring Hunt is a personalised proposal website: you add your photos, reasons and letter, preview it free, and send one private link. It works well on its own for long distance, or as the lead-up to a real proposal in person."),
       ("Will I know if they said yes?", "Yes. When they tap \"Yes\" on the balcony, their answer is emailed to you straight away.")],
 ),
 dict(slug="long-distance-relationship-gift", designs=["miss-you"],
  title="Long-Distance Relationship Gift | Little Gasp",
  desc="A long-distance gift: a paper plane flies from your city to theirs with your photos and letter, then lands as a boarding pass to pick the day you meet.",
  h1="A long-distance gift that crosses the miles",
  lead="<b>Miss You</b> is a personalised surprise website for a girlfriend, boyfriend, wife or husband in another city or country. A paper plane carries your message across a painted map from your city to theirs, dropping off a surprise at every stop, and lands as a boarding pass asking when you'll meet.",
  plays_title="What happens when they open it",
  plays=["A night map lights up both your cities, with the real distance between them.",
         "They fly your paper plane along the dotted path. The kilometres count down as it goes.",
         "Stop 1: a rainy window. They wipe the fog to find your photos, one by one.",
         "Stop 2: the phone rings. They pick up, and everything you miss about them arrives as message bubbles.",
         "Stop 3: a parcel. They tear the tape and your letter writes itself in.",
         "At 0 km the plane unfolds into a boarding pass with both cities. They pick the day you meet, and the date comes to your email.",
         "It ends with the two of you together on the map."],
  ideas_title="What to write when you miss someone",
  ideas=["Small things land hardest: \"your voice notes at 1 am\", \"stealing fries off your plate\".",
         "Caption each photo with where you were and what you'll do there next time.",
         "In the letter, talk about the next visit, not only the distance.",
         "Ask a question they can answer with a date: \"When do we meet?\" or \"Which weekend can I steal you?\"",
         "Works across countries too: type any city, or the distance yourself for a small town."],
  faq=[("What is a good gift for a long-distance girlfriend or boyfriend?", "Something personal that arrives instantly. A Miss You surprise website carries your photos, the things you miss and your letter across a map from your city to theirs, so it feels like it travelled to them, and it ends by asking when you'll meet."),
       ("Does it work if we live in different countries?", "Yes. Type both cities and we work out the distance. For a small town, you can type the kilometres yourself.")],
 ),
 dict(slug="karwa-chauth-gift-for-wife", designs=["karwa-chauth"],
  title="Karwa Chauth Gift for Wife, Online | Little Gasp",
  desc="A Karwa Chauth surprise for your wife: she raises the channi to the moon, lights diyas with your reasons and turns the thali for seven promises.",
  h1="A Karwa Chauth surprise for your wife",
  lead="She keeps the fast for you. <b>Karwa Chauth Moon</b> is a personalised surprise website to tell her what it means. She raises the channi to the moon, lights the diyas and turns the puja thali, finding your photos, reasons and seven promises along the way.",
  plays_title="What happens when she opens it",
  plays=["A moonlit window. She raises the channi to see the moon.",
         "She lights the diyas one by one, and each flame shows a reason you love her.",
         "Your photos appear like keepsakes.",
         "She turns the puja thali around the ring. Each round lights a diya and opens one of seven promises.",
         "She reads your letter and answers your question. It ends under the full moon."],
  ideas_title="Promise ideas for the thali",
  ideas=["\"I'll break my fast with you every year.\"", "\"Your chai, made by me, every Sunday.\"",
         "\"I'll listen first and talk second.\"", "\"Every year a new place, just us two.\"",
         "\"I'll always save you the last bite.\""],
  faq=[("What can I gift my wife on Karwa Chauth if I'm away?", "A Karwa Chauth surprise website arrives instantly as a link, so she can open it under the moon wherever you are, with your photos, reasons and promises inside."),
       ("Can I write my own promises?", "Yes. Add up to seven of your own, or use ours.")],
 ),
 dict(slug="diwali-surprise-website", designs=["diwali"],
  title="Diwali & Bhai Dooj Surprise Website | Little Gasp",
  desc="A Diwali surprise they light up: trace a rangoli, launch fireworks that write your wishes, release photo lanterns. For partner, family or Bhai Dooj.",
  h1="A Diwali surprise they light up themselves",
  lead="<b>Diwali Night</b> is a personalised Diwali greeting they play, not just read. For a partner, your family or your brother or sister for Bhai Dooj: they draw a rangoli, light up the sky and find your photos and wishes inside.",
  plays_title="What happens when they open it",
  plays=["They light the diya, then trace a dotted circle to colour a glowing rangoli.",
         "They tap the sky to launch fireworks. Each burst writes one of your wishes in light.",
         "They release lanterns, and each one leaves a polaroid of your photos.",
         "They draw with a sparkler and save the picture.",
         "They read your letter. If you hid a real gift, they scratch the gold foil on a mithai box to find it.",
         "They send a lantern back with their own wish, which comes to your email."],
  ideas_title="Diwali wish ideas",
  ideas=["\"May this year be as bright as your laugh.\"", "For Bhai Dooj: \"Still stealing your sweets, still on your side.\"",
         "For parents: \"Every good thing in me started at home.\"", "Hide the real gift under the foil: a trip, a dinner, a promise."],
  faq=[("Is it only for couples?", "No. Choose partner, family or sibling (Bhai Dooj) and all the wording changes to fit."),
       ("Can I send it to family abroad?", "Yes. It's a link, so it reaches anyone anywhere instantly.")],
 ),
 dict(slug="navratri-garba-surprise", designs=["garba-circle"],
  title="Navratri Surprise, Garba Circle Website | Little Gasp",
  desc="A Navratri surprise: tap the dancing couple to light all nine nights, each opening a photo or reason, then play a dandiya round to the beat.",
  h1="A Navratri surprise for your garba partner",
  lead="<b>Garba Circle</b> is a personalised Navratri website for the person you dance with. They tap the dancing couple to light all nine nights of Navratri, each night opening one of your photos or reasons, then play a dandiya round to the beat.",
  plays_title="What happens when they open it",
  plays=["The circle starts. Each tap on the dancing couple lights the next of nine night colours.",
         "Every night opens a photo, a reason or that night's Devi card.",
         "With all nine lit, a dandiya round begins: tap when the ring closes on the sticks.",
         "Your letter, your question, and a happy ending."],
  ideas_title="Reasons for nine nights",
  ideas=["\"You never miss a step, even when I do.\"", "\"Your laugh in the middle of the circle.\"",
         "\"Every year, my favourite partner.\""],
  faq=[("Can I use our own song?", "Yes. Upload your own MP3 and the dandiya round follows its beat.")],
 ),
]

HUB_SLUG = "digital-surprise-gifts"
def url(slug): return f"{SITE}/{slug}/"

CSS = """
.lp{max-width:1040px;margin:0 auto}
.lp .hero2{display:grid;gap:28px;align-items:center;border-radius:28px;padding:28px clamp(20px,4vw,44px)}
.lp h1{font-size:clamp(2rem,6vw,3rem);margin:.2em 0 .35em}
.lp .lead{font-size:1.08rem}
.lp .crumbs{font-size:.88rem;color:var(--muted)}.lp .crumbs a{color:var(--muted)}
.lp .acts{display:flex;flex-wrap:wrap;gap:12px;margin-top:18px}
.lp .shot{width:100%;height:auto;border-radius:22px;display:block;box-shadow:var(--shadow)}
.lp .blk{border-radius:28px;padding:28px clamp(20px,4vw,44px);margin-top:22px}
.lp h2{font-size:clamp(1.4rem,4vw,1.8rem);margin-top:0}
.lp ol,.lp ul{padding-left:1.25em}.lp li{margin:.35em 0}
.lp .cards{display:grid;gap:16px;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));margin-top:12px}
.lp .card{border-radius:22px;overflow:hidden;background:var(--glass-strong);border:1px solid var(--edge);text-decoration:none;color:var(--ink);display:flex;flex-direction:column}
.lp .card img{width:100%;height:auto;display:block}
.lp .card b{font:400 1.2rem/1.2 var(--display);padding:12px 16px 2px}
.lp .card span{padding:0 16px 14px;color:var(--muted);font-size:.95rem}
.lp details p{color:var(--muted)}
.lp .more{display:flex;flex-wrap:wrap;gap:10px;margin-top:10px}
.lp .more a{background:#fff;border:1px solid var(--line);border-radius:999px;padding:8px 14px;text-decoration:none;font-weight:600}
@media(min-width:860px){.lp .hero2{grid-template-columns:1.15fr 1fr}}
"""

CARD_TEXT = {
 "apology": ("apology-website", "Say sorry: they mend a broken heart and tell you how mad they still are."),
 "birthday-wish": ("birthday-surprise-website", "A teddy bear's birthday party with candles, balloons and gifts."),
 "birthday-cake": ("birthday-surprise-website", "Candles, a wish, your photos and a birthday selfie with a crown."),
 "love-letter": ("digital-love-letter", "A love letter they open: wax seal, quill and pressed flowers."),
 "anniversary": ("anniversary-surprise-website", "Ride a scooter down memory lane past every photo."),
 "karwa-chauth": ("karwa-chauth-gift-for-wife", "Raise the channi to the moon and turn the thali for seven promises."),
 "diwali": ("diwali-surprise-website", "Rangoli, fireworks and lanterns. For a partner, family or Bhai Dooj."),
 "garba-circle": ("navratri-garba-surprise", "Light all nine nights of Navratri, then a dandiya round."),
 "proposal": ("proposal-surprise-website", "A treasure hunt with a torch, a projector film and a ring box."),
 "miss-you": ("long-distance-relationship-gift", "A paper plane flies to them, with a surprise at every stop."),
}
LINK_NAME = {p["slug"]: p["h1"].replace("A ","").replace("An ","") for p in PAGES}
SHORT = {"digital-surprise-gifts":"All digital surprises","apology-website":"Apology website","birthday-surprise-website":"Birthday surprise website",
 "digital-love-letter":"Digital love letter","anniversary-surprise-website":"Anniversary surprise","proposal-surprise-website":"Proposal surprise website","long-distance-relationship-gift":"Long-distance relationship gift","karwa-chauth-gift-for-wife":"Karwa Chauth gift for wife",
 "diwali-surprise-website":"Diwali & Bhai Dooj surprise","navratri-garba-surprise":"Navratri surprise"}

def esc(s): return html.escape(s, quote=True)
def strip(s):
    import re; return re.sub(r"<[^>]+>", "", s).replace("&amp;","&")

def build(p):
    slug, ds = p["slug"], p["designs"]
    main = ds[0]
    faq = p["faq"] + COMMON_FAQ
    img = f"/img/cards/{main}.webp"
    og = f"{SITE}/og-image.png" if p.get("hub") else f"{SITE}/{main}/img/share.jpg"
    products = []
    for k in ds:
        n, pr = DESIGN[k]
        products.append({"@type":"Product","name":f"{n} – Little Gasp surprise website","url":f"{SITE}/{k}/",
          "image":f"{SITE}/img/cards/{k}.webp","brand":{"@id":f"{SITE}/#org"},
          "description":strip(CARD_TEXT[k][1]),
          "offers":{"@type":"Offer","price":str(pr),"priceCurrency":"INR","availability":"https://schema.org/InStock","url":f"{SITE}/create/?d={k}"}})
    crumbs = [{"@type":"ListItem","position":1,"name":"Little Gasp","item":SITE+"/"}]
    if not p.get("hub"):
        crumbs.append({"@type":"ListItem","position":2,"name":"Digital surprises","item":url(HUB_SLUG)})
    crumbs.append({"@type":"ListItem","position":len(crumbs)+1,"name":SHORT[slug],"item":url(slug)})
    graph = [
      {"@type":"WebPage","@id":url(slug)+"#page","url":url(slug),"name":p["title"],"description":p["desc"],
       "inLanguage":"en-IN","isPartOf":{"@id":SITE+"/#website"},"about":{"@id":SITE+"/#org"},"dateModified":TODAY,
       "primaryImageOfPage":SITE+img},
      {"@type":"BreadcrumbList","itemListElement":crumbs},
      {"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]},
    ] + products
    ld = json.dumps({"@context":"https://schema.org","@graph":graph}, ensure_ascii=False, indent=1)

    crumb_html = '<a href="/">Little Gasp</a> › ' + ('' if p.get("hub") else f'<a href="/{HUB_SLUG}/">Digital surprises</a> › ') + esc(SHORT[slug])
    if p.get("hub"):
        acts = '<a class="btn" href="/create/">Make a surprise, free preview</a><a class="btn glassy" href="/#designs">See all designs</a>'
        shot = '<img class="shot" src="/img/cards/love-letter.webp" alt="A Little Gasp surprise website playing on a phone" width="1200" height="900">'
    else:
        n, pr = DESIGN[main]
        acts = f'<a class="btn" href="/create/?d={main}">Make yours, free preview</a><a class="btn glassy" href="/{main}/" target="_blank" rel="noopener">Play the demo</a>'
        shot = f'<img class="shot" src="{img}" alt="{esc(n)} surprise website on a phone" width="1200" height="900">'
    price_line = ""
    if not p.get("hub"):
        bits = [f"{DESIGN[k][0]}: ₹{DESIGN[k][1]}" for k in ds]
        price_line = f'<p class="crumbs" style="margin-top:12px">{" · ".join(bits)}, one time. Watch the full preview with your own photos before you pay.</p>'

    plays = "".join(f"<li>{x}</li>" for x in p["plays"])
    listtag = "ul" if p.get("hub") or slug=="birthday-surprise-website" else "ol"
    if p.get("hub"):
        cards = "".join(f'<a class="card" href="/{CARD_TEXT[k][0]}/"><img src="/img/cards/{k}.webp" alt="{esc(DESIGN[k][0])} design" loading="lazy" width="1200" height="900"><b>{esc(DESIGN[k][0])}</b><span>{esc(CARD_TEXT[k][1])}</span></a>' for k in ds)
        ideas = f'<section class="blk glass"><h2>{p["ideas_title"]}</h2><div class="cards">{cards}</div></section>'
    else:
        ideas = f'<section class="blk glass"><h2>{p["ideas_title"]}</h2><ul>{"".join(f"<li>{x}</li>" for x in p["ideas"])}</ul></section>'
    how = ('<section class="blk glass"><h2>How to make one in about five minutes</h2><ol>'
           f'<li>Open the editor and pick {"a design" if p.get("hub") else "<b>"+esc(DESIGN[main][0])+"</b>"}.</li>'
           '<li>Add their name, up to five photos with captions, a few short reasons and your letter.</li>'
           '<li>Watch the live preview play exactly as they will see it.</li>'
           '<li>Pay by UPI or card. Your private link appears instantly and is emailed to you.</li>'
           '<li>Send the link on WhatsApp or Instagram, or save it for midnight.</li></ol></section>')
    faq_html = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q,a in faq)
    more = "".join(f'<a href="/{s}/">{esc(SHORT[s])}</a>' for s in SHORT if s != slug)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(p["title"])}</title>
<meta name="description" content="{esc(p["desc"])}">
<link rel="canonical" href="{url(slug)}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Little Gasp">
<meta property="og:title" content="{esc(p["h1"])}">
<meta property="og:description" content="{esc(p["desc"])}">
<meta property="og:url" content="{url(slug)}">
<meta property="og:image" content="{og}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#FDEFF4">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" type="image/png" sizes="48x48" href="/favicon-48.png">
<link rel="icon" type="image/png" sizes="96x96" href="/favicon-96.png">
<link rel="icon" type="image/png" sizes="192x192" href="/favicon-192.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<script type="application/ld+json">
{ld}
</script>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Caprasimo&family=Figtree:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/style.css?v={CSSV}">
<style>{CSS}</style>
</head>
<body>
<script src="/site.js?v={CSSV}"></script>
<!-- generated by tools/seo_pages.py, edit there -->
<main class="wrap page lp">
<section class="hero2 glass">
 <div>
  <p class="crumbs">{crumb_html}</p>
  <h1>{esc(p["h1"])}</h1>
  <p class="lead">{p["lead"]}</p>
  <div class="acts">{acts}</div>
  {price_line}
 </div>
 {shot}
</section>
<section class="blk glass"><h2>{p["plays_title"]}</h2><{listtag}>{plays}</{listtag}></section>
{ideas}
{how}
<section class="blk glass"><h2>Questions people ask</h2>{faq_html}</section>
<section class="blk glass"><h2>More surprise ideas</h2><div class="more">{more}</div>
<h2 style="margin-top:22px">Guides</h2><div class="more">{"".join(f'<a href="/{x["slug"]}/">{esc(x["short"])}</a>' for x in GUIDES)}</div>
<p style="margin-top:16px">Little Gasp is an online gift studio from Mumbai, India, making interactive surprise websites. <a href="/about.html">About us</a>.</p></section>
</main>
</body>
</html>
"""

# ---------- Guides (articles): honest, useful, written by the studio ----------
# Same look as the landing pages. Article + BreadcrumbList + FAQPage JSON-LD, author = the founder.
# No made-up numbers, reviews or customer stories here (site rule 6).
AUTHOR = {"@type":"Person","name":"Aniket Nandkumar Gurav","jobTitle":"Founder, Little Gasp","url":SITE+"/about.html"}
GUIDES = [
 dict(slug="surprise-website-vs-e-card", published="2026-11-03", design="love-letter",
  short="Surprise website vs e-card",
  title="Surprise Website vs E-card vs Video vs Gift | Little Gasp",
  desc="An honest comparison of a surprise website, an e-card, a video message and a physical gift: cost, effort, distance, and which one fits your moment.",
  h1="Surprise website vs e-card, video message or a physical gift",
  lead="You want to make someone feel special and you have four obvious options. Each one is good at something different. Here is an honest side-by-side, including when a surprise website is <b>not</b> the right pick.",
  table=(["", "E-card", "Video message", "Physical gift", "Surprise website"],
   [["What it costs", "Often free or low cost", "Free if you record it yourself", "The gift, plus wrapping and delivery", "₹99 or ₹149 on Little Gasp"],
    ["Time to make", "A few minutes", "Minutes to hours, retakes included", "Shopping time, plus days for delivery", "About five minutes"],
    ["Reaches another city", "Instantly", "Instantly", "Days, and only if delivery reaches them", "Instantly"],
    ["What they do with it", "Read it once", "Watch it once", "Hold it, use it, keep it", "Play through it: tap, swipe, unwrap"],
    ["Your photos and words", "One message", "Your face and voice", "A note card, at most", "Up to 5 photos, 6 notes and a full letter"],
    ["Can they answer you", "No", "Only by replying separately", "No", "Yes, many designs send their answer to your email"],
    ["Feels personal", "Depends on what you write", "Very, if you are comfortable on camera", "Very, if you choose well", "Very: your words, your photos, their name"]]),
  sections=[
   ("When an e-card is enough", "<p>For a colleague's birthday or a quick festival wish to many people, an e-card is fine. It's fast, and nobody expects more.</p>"),
   ("When a video message is better", "<p>If you are comfortable on camera, nothing beats your own face and voice. A video works especially well for grandparents and family who would rather see you than read.</p>"),
   ("When a physical gift wins", "<p>If you're in the same city and they've been wanting something specific, give them the thing. A surprise website doesn't replace a hug or a present they can hold. It works well alongside one, though: send the link the night before and hand over the gift the next day.</p>"),
   ("When a surprise website is the right pick", "<ul><li>You're in a different city or country, or the day has already started.</li><li>You have more to say than fits in a card, but writing a long text feels flat.</li><li>You want them to take their time with every line, not scroll past it.</li><li>You're asking something (sorry, a date, a question) and want an honest answer back.</li></ul>"),
   ("Our honest take", "<p>We make surprise websites, so we're not neutral. But the reason we started is simple: a message they <i>do</i> something with stays with them longer than one they just read. If that's not what your moment needs, pick one of the other three. You can try any of our designs free before deciding.</p>"),
  ],
  faq=[("Is a surprise website better than an e-card?", "It depends on the moment. An e-card is quicker and fine for light occasions. A surprise website takes about five minutes, holds your photos, notes and a full letter, and they play through it, so it suits birthdays, anniversaries, apologies and long distance."),
       ("Can I send a surprise website with a physical gift?", "Yes. Many people send the link at midnight and give the gift in person later. The website carries the words; the gift carries the hug."),
       ("Do I need technical skills to make a surprise website?", "No. On Little Gasp you pick a design, type your words, add photos and watch the preview. There's no coding and nothing to install.")]),
 dict(slug="long-distance-surprise-ideas", published="2026-11-03", design="miss-you",
  short="Long-distance surprise guide",
  title="How to Surprise a Long-Distance Partner | Little Gasp",
  desc="A step-by-step guide to planning a surprise for a long-distance partner: timing across cities, what to say, photos to pick, and a plan to meet next.",
  h1="How to plan a surprise for a long-distance partner",
  lead="Distance makes the small things big. A good long-distance surprise isn't about how much you spend. It's about timing, words they can come back to, and a clear sign that you're planning to close the gap.",
  steps=[("Pick the moment, in their time zone", "Midnight on their birthday, the morning of a hard exam, the night before your anniversary. If they're abroad, work out their local time and set an alarm for yours."),
         ("Choose photos that tell a story", "Pick three to five photos in order: the first time you met, a trip, an ordinary day, the last time you said goodbye. Write one line under each one."),
         ("Write what you miss, specifically", "\"I miss you\" is true but vague. \"I miss your voice when you're half asleep on a call\" is the one they'll remember. Write five or six of these, one line each."),
         ("Add one letter, not ten texts", "Put the longer feelings in one letter. Start with their name, say what this distance has been like for you, and end with what you're looking forward to."),
         ("End with a plan, not just a wish", "The best long-distance surprises end with something real: a date you'll meet, a call booked for tonight, or a question like \"When do we meet?\" that they can answer."),
         ("Send it, then stay reachable", "Don't send it and go to sleep. Be around for the reply, the call, or the voice note that follows.")],
  sections=[
   ("Small ideas that work across any distance", "<ul><li>Order their favourite food to their door at dinner time, then video-call and eat together.</li><li>Watch the same film at the same time and keep a call open.</li><li>Send a voice note for each day you're apart until you meet.</li><li>Send a letter they can open again on bad days. On Little Gasp, <b>Miss You</b> sends a paper plane from your city to theirs, with a stop for your photos, your reasons and your letter, and it lands as a boarding pass where they pick the day you meet.</li></ul>"),
  ],
  faq=[("What is a good surprise for a long-distance boyfriend or girlfriend?", "Something they can open at the right moment and come back to: your photos in order, specific things you miss, a letter, and a plan to meet. A surprise website like Miss You puts all of that in one link that reaches them instantly."),
       ("How do I make a long-distance birthday special?", "Send something at midnight their time, order a small treat to their door, stay on a call while they open it, and end with a date for when you'll celebrate together.")]),
 dict(slug="how-to-write-an-apology", published="2026-11-03", design="apology",
  short="How to write an apology",
  title="How to Write an Apology That Lands | Little Gasp",
  desc="What to write in an apology to your partner or friend: name what you did, own how it felt for them, skip the excuses, promise something small and real.",
  h1="What to write in an apology that actually lands",
  lead="A sorry that doesn't land usually fails in the same few ways: it's vague, it explains too much, or it asks to be forgiven too soon. Here's a simple way to write one that's honest and easy to accept.",
  steps=[("Name exactly what you did", "\"I'm sorry I cancelled on Saturday at the last minute\" works. \"Sorry for everything\" sounds like you don't know what went wrong."),
         ("Say how it felt for them", "\"You'd planned the whole evening and I made you feel like it didn't matter.\" This shows you understand, which is most of what they're waiting for."),
         ("Leave out the explanation, for now", "Reasons can wait for a calmer conversation. In the first message, an explanation reads like an excuse."),
         ("Don't add a \"but\"", "\"I'm sorry, but you also…\" cancels the sorry. If something needs talking about, talk about it later, separately."),
         ("Promise something small and real", "\"Next time I'll tell you a day before, not an hour before\" is believable. \"It will never happen again\" usually isn't."),
         ("Let them take their time", "Don't ask \"are we okay?\" in the same message. Give them a way to answer when they're ready.")],
  sections=[
   ("Lines you can adapt", "<ul><li>\"I'm sorry I snapped at you in front of your friends. You didn't deserve that.\"</li><li>\"I forgot something that mattered to you, and I'm sorry.\"</li><li>\"I should have listened instead of trying to fix it.\"</li><li>\"I'll call when I'm running late, every time.\"</li></ul>"),
   ("If a text gets left on seen", "<p>Sometimes the same words land better in a different format. <b>Mend the Heart</b> on Little Gasp lets them put a broken heart back together, with one of your sorries on each piece, then tell you honestly how they feel on a forgive-o-meter. It never pushes for a yes: \"I need a minute\" is always an answer.</p>"),
  ],
  faq=[("How do I apologise to my girlfriend or boyfriend after a fight?", "Wait until you're both calmer, then name what you did, say how it made them feel, skip the excuses and promise one small specific change. Give them time to answer instead of asking to be forgiven straight away."),
       ("Should I explain why I did it?", "Not in the first apology. Explanations sound like excuses at that point. Once they feel heard, a calm conversation about why is much easier.")]),
]

GCSS = """
.lp .byline{font-size:.92rem;color:var(--muted);margin-top:6px}
.lp .tw{overflow-x:auto;-webkit-overflow-scrolling:touch;margin-top:8px}
.lp table{border-collapse:collapse;width:100%;min-width:640px;font-size:.95rem}
.lp th,.lp td{text-align:left;vertical-align:top;padding:10px 12px;border-bottom:1px solid var(--line)}
.lp thead th{font-weight:700;background:rgba(255,255,255,.55)}
.lp tbody th{font-weight:600;color:var(--muted);white-space:nowrap}
.lp td:last-child,.lp th:last-child{background:rgba(255,200,87,.16)}
.lp .cmp{display:none}
@media(max-width:700px){.lp .tw{display:none}.lp .cmp{display:grid;gap:12px}
 .lp .opt{border:1px solid var(--line);border-radius:18px;padding:14px 16px;background:rgba(255,255,255,.5)}
 .lp .opt.ours{background:rgba(255,200,87,.18)}
 .lp .opt h3{margin:0 0 6px;font-size:1.15rem}
 .lp .opt dl{margin:0;display:grid;grid-template-columns:42% 1fr;gap:8px 12px;font-size:.92rem;line-height:1.35}
 .lp .opt dt{color:var(--muted);font-weight:600;font-size:.84rem}.lp .opt dd{margin:0}}
.lp ol.steps{counter-reset:s;list-style:none;padding:0}
.lp ol.steps li{counter-increment:s;position:relative;padding-left:46px;margin:14px 0}
.lp ol.steps li::before{content:counter(s);position:absolute;left:0;top:0;width:32px;height:32px;border-radius:50%;background:var(--butter);display:grid;place-items:center;font-weight:700}
.lp ol.steps b{display:block}
"""

def fdate(d):
    import datetime; return datetime.date.fromisoformat(d).strftime("%-d %B %Y")

def build_guide(g):
    slug, k = g["slug"], g["design"]
    n, pr = DESIGN[k]
    faq = g["faq"]
    crumbs = [{"@type":"ListItem","position":1,"name":"Little Gasp","item":SITE+"/"},
              {"@type":"ListItem","position":2,"name":"Digital surprises","item":url(HUB_SLUG)},
              {"@type":"ListItem","position":3,"name":g["short"],"item":url(slug)}]
    art = {"@type":"Article","@id":url(slug)+"#article","mainEntityOfPage":url(slug),"headline":g["h1"],"description":g["desc"],
           "image":f"{SITE}/{k}/img/share.jpg","datePublished":g["published"],"dateModified":TODAY,"inLanguage":"en-IN",
           "author":AUTHOR,"publisher":{"@id":SITE+"/#org"},"isPartOf":{"@id":SITE+"/#website"}}
    if "steps" in g:
        howto = {"@type":"HowTo","name":g["h1"],"step":[{"@type":"HowToStep","position":i+1,"name":a,"text":b} for i,(a,b) in enumerate(g["steps"])]}
    else: howto = None
    graph = [art, {"@type":"BreadcrumbList","itemListElement":crumbs},
             {"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]}]
    if howto: graph.append(howto)
    ld = json.dumps({"@context":"https://schema.org","@graph":graph}, ensure_ascii=False, indent=1)
    body = ""
    if "table" in g:
        head, rows = g["table"]
        th = "".join(f"<th scope=\"col\">{esc(h)}</th>" for h in head)
        trs = "".join("<tr><th scope=\"row\">"+esc(r[0])+"</th>"+"".join(f"<td>{esc(c)}</td>" for c in r[1:])+"</tr>" for r in rows)
        cards = "".join(f'<div class="opt{" ours" if j==len(head)-1 else ""}"><h3>{esc(head[j])}</h3><dl>' + "".join(f"<dt>{esc(r[0])}</dt><dd>{esc(r[j])}</dd>" for r in rows) + "</dl></div>" for j in range(1, len(head)))
        body += f'<section class="blk glass"><h2>Side by side</h2><div class="tw"><table><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div><div class="cmp">{cards}</div></section>'
    if "steps" in g:
        lis = "".join(f"<li><b>{esc(a)}</b>{esc(b)}</li>" for a,b in g["steps"])
        body += f'<section class="blk glass"><h2>Step by step</h2><ol class="steps">{lis}</ol></section>'
    for h, t in g["sections"]:
        body += f'<section class="blk glass"><h2>{esc(h)}</h2>{t}</section>'
    faq_html = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q,a in faq)
    more = "".join(f'<a href="/{s}/">{esc(SHORT[s])}</a>' for s in SHORT) 
    gmore = "".join(f'<a href="/{x["slug"]}/">{esc(x["short"])}</a>' for x in GUIDES if x["slug"] != slug)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(g["title"])}</title>
<meta name="description" content="{esc(g["desc"])}">
<link rel="canonical" href="{url(slug)}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Little Gasp">
<meta property="og:title" content="{esc(g["h1"])}">
<meta property="og:description" content="{esc(g["desc"])}">
<meta property="og:url" content="{url(slug)}">
<meta property="og:image" content="{SITE}/{k}/img/share.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#FDEFF4">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" type="image/png" sizes="48x48" href="/favicon-48.png">
<link rel="icon" type="image/png" sizes="96x96" href="/favicon-96.png">
<link rel="icon" type="image/png" sizes="192x192" href="/favicon-192.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<script type="application/ld+json">
{ld}
</script>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Caprasimo&family=Figtree:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/style.css?v={CSSV}">
<style>{CSS}{GCSS}</style>
</head>
<body>
<script src="/site.js?v={CSSV}"></script>
<!-- generated by tools/seo_pages.py, edit there -->
<main class="wrap page lp">
<section class="hero2 glass">
 <div>
  <p class="crumbs"><a href="/">Little Gasp</a> › <a href="/{HUB_SLUG}/">Digital surprises</a> › {esc(g["short"])}</p>
  <h1>{esc(g["h1"])}</h1>
  <p class="byline">By <a href="/about.html">Aniket Gurav</a>, founder of Little Gasp, Mumbai · Updated {fdate(TODAY)}</p>
  <p class="lead">{g["lead"]}</p>
  <div class="acts"><a class="btn" href="/create/?d={k}">Try {esc(n)}, free preview</a><a class="btn glassy" href="/{k}/" target="_blank" rel="noopener">Play the demo</a></div>
 </div>
 <img class="shot" src="/img/cards/{k}.webp" alt="{esc(n)} surprise website on a phone" width="1200" height="900">
</section>
{body}
<section class="blk glass"><h2>Questions people ask</h2>{faq_html}</section>
<section class="blk glass"><h2>More guides</h2><div class="more">{gmore}</div>
<h2 style="margin-top:22px">Surprise ideas</h2><div class="more">{more}</div>
<p style="margin-top:16px">Little Gasp is an online gift studio from Mumbai, India, making interactive surprise websites. <a href="/about.html">About us</a>.</p></section>
</main>
</body>
</html>
"""

def build_llms():
    lines = ["# Little Gasp", "",
     "> Little Gasp (littlegasp.com) is an online gift studio from Mumbai, India. It makes personalised, interactive surprise websites: the buyer adds photos, short notes and a letter, watches the full preview free, pays once, and sends one private link that the other person taps and plays through on a phone or laptop.", "",
     "- No app needed; the link opens in any browser and stays live for at least 12 months.",
     "- Customer surprise pages are private (only people with the link) and hidden from search engines.",
     "- Payment by UPI, card or net banking through Razorpay; the link appears instantly and is emailed.",
     "- Buyers can upload their own song (MP3/M4A) on every design.",
     "- Founder: Aniket Nandkumar Gurav, Mumbai. Instagram @littlegasp.co. Email littlegasp.orders@gmail.com.", "",
     "## Designs (one-time price in INR)", ""]
    for k,(n,pr) in DESIGN.items():
        lines.append(f"- [{n}]({SITE}/{k}/): {strip(CARD_TEXT[k][1])} ₹{pr}. Occasion page: {url(CARD_TEXT[k][0])}")
    lines += ["", "## Surprise ideas by occasion", ""]
    for p in PAGES: lines.append(f"- [{SHORT[p['slug']]}]({url(p['slug'])}): {p['desc']}")
    lines += ["", "## Guides", ""]
    for g in GUIDES: lines.append(f"- [{g['h1']}]({url(g['slug'])}): {g['desc']}")
    lines += ["", "## Company", "", f"- [About Little Gasp]({SITE}/about.html)", f"- [Make a surprise (editor)]({SITE}/create/)",
              f"- [Terms]({SITE}/terms.html)", f"- [Refunds]({SITE}/refund.html)", f"- [Privacy]({SITE}/privacy.html)", f"- [Contact]({SITE}/contact.html)", ""]
    return "\n".join(lines)

if __name__ == "__main__":
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    for p in PAGES:
        d = os.path.join(root, p["slug"]); os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "index.html"), "w").write(build(p))
        print("wrote", p["slug"])
    for g in GUIDES:
        d = os.path.join(root, g["slug"]); os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "index.html"), "w").write(build_guide(g))
        print("wrote guide", g["slug"])
    open(os.path.join(root, "llms.txt"), "w").write(build_llms()); print("wrote llms.txt")
