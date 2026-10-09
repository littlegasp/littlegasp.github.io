/* Little Gasp – writing ideas for the editor.
   The buyer picks who it's for; the editor offers these as tap-to-use suggestions.
   Lookup order for every field: occasion[relation] → occasion[group] → occasion[kind] → common[...] (same order).
   Letters: first line is the greeting ({to} becomes their name); no sign-off, every design adds its own.
   Keep reasons ≤ 40 characters and captions ≤ 30: some designs show them in small spaces. */
window.LG_REL = {
  wife:      { label: "Wife",        group: "partner", kind: "partner", g: "her", hello: "My love" },
  husband:   { label: "Husband",     group: "partner", kind: "partner", g: "him", hello: "My love" },
  girlfriend:{ label: "Girlfriend",  group: "partner", kind: "partner", g: "her", hello: "My love" },
  boyfriend: { label: "Boyfriend",   group: "partner", kind: "partner", g: "him", hello: "My love" },
  mom:       { label: "Mom",         group: "mom",     kind: "parent",  g: "her", hello: "Maa" },
  dad:       { label: "Dad",         group: "dad",     kind: "parent",  g: "him", hello: "Papa" },
  sister:    { label: "Sister",      group: "sibling", kind: "sibling", g: "her", hello: "Hey you" },
  brother:   { label: "Brother",     group: "sibling", kind: "sibling", g: "him", hello: "Hey you" },
  bestie:    { label: "Best friend", group: "friend",  kind: "friend",  g: "",    hello: "Hey you" }
};

window.LG_IDEAS = {
  common: {
    reasons: {
      partner: ["The way you laugh at my worst jokes","You make ordinary days feel special","Your hugs fix everything","You remember the little things","You believe in me more than I do","Our 2 a.m. chats","You make anywhere feel like home","Your terrible singing in the car","You never let me eat alone"],
      mom: ["Your hugs still fix everything","You know when I'm not okay","Your dal tastes like home","You never stopped believing in me","You taught me to be kind","Your 'have you eaten?' calls","The strongest person I know","You made every birthday special"],
      dad: ["You taught me to ride a cycle","Your quiet, solid support","Your jokes (I secretly love them)","You worked hard so I could dream","You can fix anything","Your advice I pretend not to need","My first hero","The way you're proud of me"],
      sibling: ["You always had my back at home","Our fights over the TV remote","You know all my secrets","Partner in crime since day one","You steal my clothes, I steal yours","You make family dinners louder","My first best friend","You'll always be my favourite"],
      friend: ["You get my jokes before I finish","Our 'one last chai' that lasts hours","You never judge, only roast","You show up, every single time","Our inside jokes nobody gets","The sibling I got to choose","You make bad days better","Every trip is better with you"]
    },
    captions: {
      partner: ["Our first photo together","The day I knew","My favourite person","Us, being us","That trip we still talk about","Look at that smile","Home, in one picture","Best day ever"],
      parent: ["My first home","Your smile, my sunshine","Look at us!","Then and now","Forever my favourite","Our kitchen chats"],
      sibling: ["Partners in crime","Back when you were nicer","Still fighting, still family","That one family trip","Look how cute we were"],
      friend: ["Us, since forever","Peak friendship moment","The trip we'll never forget","Chai and chaos","Evidence of our madness"]
    }
  },

  birthday: {
    letters: {
      partner: [
        ["Sweet", "{to},", "Happy birthday to the person who makes every day feel like a celebration.", "Thank you for your laugh, your patience, and the way you make even Monday mornings better.", "I hope this year gives you everything you've given me, and then some.", "I'm so lucky I get to love you."],
        ["Funny", "{to},", "Another year older, and somehow still out of my league.", "Thank you for putting up with my jokes, my snacks and my 'five more minutes'.", "Today you get the last slice of cake. Tomorrow, no promises.", "Happy birthday, my favourite human."],
        ["Heartfelt", "{to},", "I don't say it enough, so I'm saying it here, where you can play it again and again.", "You make me braver, softer and happier than I ever was before you.", "Whatever this year brings, you won't face any of it alone.", "Happy birthday. I love you, today and every day after."]
      ],
      mom: [
        ["Sweet", "{to},", "Happy birthday to the woman who made me who I am.", "Thank you for every tiffin, every late-night wait, and every time you believed in me first.", "I hope today you finally let someone else do the fussing.", "I love you more than I ever say out loud."],
        ["Funny", "{to},", "Happy birthday to the only person who can find anything in this house.", "Thank you for every 'have you eaten?' and every 'wear a sweater'. You were right. Mostly.", "Today: no cooking, no worrying, only cake."],
        ["Heartfelt", "{to},", "Everything good in me started with you.", "You gave up so much so I could have more, and you never once made me feel it.", "I hope I make you as proud as you make me.", "Happy birthday. I love you."]
      ],
      dad: [
        ["Sweet", "{to},", "Happy birthday to my first hero.", "Thank you for every early morning, every lesson, and every time you quietly made things okay.", "I hope this year is as kind to you as you've always been to us."],
        ["Funny", "{to},", "Happy birthday to the man whose jokes get worse every year, and whom we love more every year.", "Thank you for fixing everything, from bicycles to bad days.", "Today, the TV remote is all yours."],
        ["Heartfelt", "{to},", "I don't think I've ever really said thank you.", "For the hard work you never talked about, and the worries you kept to yourself so we didn't have to.", "Everything I am, I learned watching you.", "Happy birthday. I love you."]
      ],
      sibling: [
        ["Sweet", "{to},", "Happy birthday to my first best friend.", "Thank you for every secret kept, every fight forgiven, and every time you took my side.", "Growing up with you was the best part.", "Love you, even when you steal my stuff."],
        ["Funny", "{to},", "Happy birthday to the person who knows exactly how annoying I am, and stayed anyway.", "Thank you for taking the blame (sometimes) and the last piece of cake (always).", "Congratulations on getting older. I'm still the favourite."],
        ["Heartfelt", "{to},", "We fight, we make up, we fight again. And still, you're the first person I'd call.", "Thank you for being my partner in crime and my safe place, both at once.", "I hope this year is everything you deserve.", "Happy birthday. I'm proud of you."]
      ],
      friend: [
        ["Sweet", "{to},", "Happy birthday to the friend who feels like family.", "Thank you for every long call, every 'one last chai', and every time you showed up.", "Here's to another year of us."],
        ["Funny", "{to},", "Happy birthday to the only person who knows all my secrets. Please keep it that way.", "Thank you for the laughs, the roasts and the terrible advice I always follow.", "Another year older, still not wiser. Never change."],
        ["Heartfelt", "{to},", "Some people come into your life and just stay. I'm so glad you're one of them.", "You've seen me at my worst and stayed for the best.", "I hope this year is as wonderful as you are.", "Happy birthday."]
      ]
    },
    asks: {
      partner: [["Birthday dinner, just us, this Saturday?", "I'll pick you up at 8. Dress nice."], ["Can I take you somewhere special this weekend?", "Pack a small bag. It's a surprise."], ["Will you let me spoil you all day today?", "Breakfast first. Then everything else."]],
      parent: [["Lunch together this Sunday, my treat?", "Your favourite place. I've booked a table."], ["Will you let me cook for you tonight?", "No arguments. You just sit and relax."], ["Family movie night, your pick?", "Popcorn's on me."]],
      sibling: [["Birthday treat on me, anywhere you want?", "Fine. Even the expensive place."], ["Movie and pizza this weekend?", "I'll even let you choose the movie."]],
      friend: [["Birthday night out, all of us?", "Saturday, 8 pm. Wear something fancy."], ["Chai and a long drive this weekend?", "I'll bring the playlist. You bring the gossip."]]
    }
  },

  karwa: {
    reasons: {
      wife: ["You fast for me, every single year","Your mehendi-coloured hands","The way you wait for the moon","You make every festival feel like home"],
      husband: ["You make my fast feel worth it","You bring me water at moonrise","You're my moon, honestly","You keep me strong all day"]
    },
    captions: { partner: ["Our first Karwa Chauth","Waiting for the moon","My moon, my sky","Us, every year"] },
    letters: {
      wife: [
        ["Sweet", "{to},", "Today you go without food and water, all for me. I don't take that lightly.", "Thank you for loving me this deeply, this patiently, every single day.", "When the moon comes out tonight, I'll be the lucky one looking at you.", "You are my whole sky."],
        ["Funny", "{to},", "You fast all day, and I can't even skip one snack. That's how I know you're the stronger one.", "Thank you for your love, your patience and your amazing hunger tolerance.", "Tonight, the first bite is mine to feed you. Then all the food you want."],
        ["Heartfelt", "{to},", "Every Karwa Chauth, I watch you wait for the moon, and I fall for you all over again.", "You pray for my long life. I pray I deserve you for all of it.", "Thank you for choosing me, every year, every day.", "I love you, today and always."]
      ],
      husband: [
        ["Sweet", "{to},", "Today I'll fast from sunrise to moonrise, and I'll do it with a smile, because it's for you.", "Thank you for making every day feel safe and full of love.", "When I look at you through the chhalni tonight, I'll be thanking God for you.", "You are my moon."],
        ["Funny", "{to},", "Fair warning: I'll be very hungry and very cranky till the moon shows up.", "Please be on time tonight, and bring snacks.", "But honestly? I'd wait for the moon a hundred times if it meant a lifetime with you."],
        ["Heartfelt", "{to},", "I fast today for your long life, but really, I pray for our life together.", "Thank you for your patience, your laughter and your hand that always finds mine.", "May we see a hundred more moons, side by side.", "I love you."]
      ]
    },
    asks: {
      wife: [["Dinner on the terrace once the moon is out?", "I've ordered all your favourites. You've earned it."], ["Can I feed you the first bite tonight?", "Then dessert, and then more dessert."], ["Shall we watch the moon together tonight?", "I'll be home early. Promise."]],
      husband: [["Will you break my fast with me tonight?", "Be home before the moon. I'll be waiting."], ["Dinner together after moonrise?", "Then you're cooking. Kidding, I'll order in."]]
    }
  },

  garba: {
    reasons: {
      partner: ["You out-dance me every single night","Your smile in the garba circle","You still hold my hand in the crowd"],
      friend: ["Our matching chaniya choli plans","Dancing till the last aarti with you"]
    },
    captions: { partner: ["Our first garba night","Twirling together","Nine nights, one us"], friend: ["Garba gang","Dandiya night chaos"] },
    letters: {
      partner: [
        ["Sweet", "{to},", "Nine nights, nine colours, and my favourite one is always you.", "Thank you for twirling with me, laughing with me and holding my hand when the circle gets crowded.", "This Navratri, every step is for you."],
        ["Funny", "{to},", "You dance like a pro. I dance like a dandiya that lost its partner.", "Thank you for never letting me embarrass myself alone.", "See you in the circle. I'll be the one stepping on your toes."],
        ["Heartfelt", "{to},", "Every year the dhol beats, the lights glow, and I find myself looking only at you.", "You make every festival feel like home.", "Happy Navratri. Here's to many more nights of dancing together."]
      ],
      friend: [
        ["Sweet", "{to},", "Navratri isn't Navratri without you.", "Thank you for the matching outfits, the late nights and the laughs that last longer than the music.", "Let's dance till the last aarti, like always."],
        ["Funny", "{to},", "Reminder: you promised to teach me the new steps. You did not. I'm still waiting.", "Thank you for being my garba partner, my outfit consultant and my photographer.", "See you in the circle!"]
      ]
    },
    asks: {
      partner: [["Will you be my dandiya partner this Navratri?", "Then tonight we dance till the last aarti."], ["Garba tonight, matching outfits?", "I've already picked the colours."]],
      friend: [["Garba tonight, all of us together?", "Meet at 8. Don't be late this time."], ["Will you be my dandiya partner this year?", "Practice session tomorrow, no excuses."]]
    }
  },

  diwali: {
    reasons: {
      partner: ["You light up more than any diya","Your rangoli, my favourite art"],
      parent: ["Your Diwali faral is the best","You kept every tradition alive for us"],
      sibling: ["Fighting over the last laddoo","Bursting crackers together, always"],
      friend: ["Our Diwali card nights","You make every festival louder"]
    },
    captions: { partner: ["Our Diwali glow","Diyas and us"], parent: ["Diwali at home","Every Diwali with you"], sibling: ["Bhai Dooj, us","Crackers crew"], friend: ["Diwali gang","Festival mode on"] },
    letters: {
      partner: [
        ["Sweet", "{to},", "Of all the lights this Diwali, you're still the brightest.", "Thank you for filling our home with warmth, laughter and way too many sweets.", "Here's to a year as bright as your smile.", "Happy Diwali, my love."],
        ["Funny", "{to},", "This Diwali I promise to help with the cleaning. Mostly by staying out of the way.", "Thank you for making every festival fun, even when I ruin the rangoli.", "Happy Diwali! Save me a kaju katli."],
        ["Heartfelt", "{to},", "Every diya we light, I quietly wish for one thing: more years with you.", "You turned my life from ordinary to bright.", "Happy Diwali. I love you."]
      ],
      parent: [
        ["Sweet", "{to},", "Every Diwali, our home glows because of you.", "Thank you for the faral, the new clothes, the early-morning rituals and every tradition you kept alive for us.", "Happy Diwali. I love you."],
        ["Heartfelt", "{to},", "Wherever I go, my favourite Diwali will always be the one at home with you.", "Thank you for every lamp you lit for us, in the house and in our lives.", "Happy Diwali."]
      ],
      sibling: [
        ["Sweet", "{to},", "Happy Diwali and Bhai Dooj to my favourite troublemaker.", "Thank you for every fight, every secret and every time you had my back.", "I'm lucky you're mine. Now, where's my gift?"],
        ["Heartfelt", "{to},", "Growing up, you were my first friend and my first fight.", "Today I just want to say thank you for being there, always.", "Happy Bhai Dooj. Love you."]
      ],
      friend: [
        ["Sweet", "{to},", "Happy Diwali to the friend who makes every celebration brighter.", "Thank you for the card nights, the sweets and the laughs.", "Here's to another year of us."],
        ["Funny", "{to},", "Happy Diwali! May your year be bright, your sweets be endless, and your card game finally improve.", "Thank you for being my favourite chaos."]
      ]
    },
    asks: {
      partner: [["Diwali dinner with my family this year?", "They already love you. Mom's making your favourite."], ["Will you light the first diya with me?", "Tonight at 7. I'll have everything ready."], ["Diwali shopping date this weekend?", "My treat. Even the sweets."]],
      parent: [["Can I come home for Diwali this year?", "I'm booking my ticket today."], ["Diwali dinner, all of us together?", "I'll bring the sweets."]],
      sibling: [["Bhai Dooj at mine this year?", "I'll make your favourite. Bring my gift."], ["Diwali shopping together, like old times?", "My treat. Don't get used to it."]],
      friend: [["Diwali card party at mine?", "Saturday night. Bring sweets and your luck."], ["Rangoli and crackers together this year?", "I'll get the colours. You get the snacks."]]
    }
  },

  apology: {
    reasons: {
      partner: ["I'm sorry I didn't listen","I'm sorry I made you feel small","I'm sorry I picked my phone over you","I'm sorry I said things I didn't mean","I'm sorry I wasn't there","I'm sorry I got so defensive","I'm sorry I took you for granted","I'm sorry. No excuses."],
      parent: ["I'm sorry I raised my voice","I'm sorry I didn't call more","I'm sorry I took you for granted","I'm sorry I said things I didn't mean","I'm sorry I made you worry","I'm sorry. No excuses."],
      sibling: ["I'm sorry I raised my voice","I'm sorry I said things I didn't mean","I'm sorry I wasn't there for you","I'm sorry I made it about me","I'm sorry. No excuses."],
      friend: ["I'm sorry I went quiet on you","I'm sorry I wasn't there when it mattered","I'm sorry I made it about me","I'm sorry I cancelled again","I'm sorry I said things I didn't mean","I'm sorry. No excuses."]
    },
    captions: { partner: ["Us, before I messed up","Our best day","Worth fixing"], parent: ["You, always there","My safe place"], sibling: ["Still my favourite","Us, always"], friend: ["Us, always","Worth fixing"] },
    letters: {
      partner: [
        ["Sincere", "{to},", "I've been thinking about what happened, and you were right.", "I don't want to win arguments with you. I want to be on your side, even when I'm the problem.", "No excuses this time. Just me, saying sorry, and meaning it."],
        ["Short", "{to},", "I messed up. I know it, and I'm sorry.", "You deserve someone who listens, and I want to be that person.", "Please give me the chance to show you."],
        ["Light", "{to},", "I'm sorry. Also, I miss you. Mostly the first one, but a lot of the second.", "I know a website doesn't fix it, but I hope it shows I'm really trying.", "Can we talk tonight? I'll listen this time, properly."]
      ],
      parent: [
        ["Sincere", "{to},", "I'm sorry for how I spoke to you. You didn't deserve that.", "You've always been there for me, and I forgot to be there for you.", "I love you, and I'll do better."],
        ["Short", "{to},", "I know I hurt you, and I've felt terrible about it ever since.", "Thank you for always forgiving me, even when I don't make it easy.", "I'm sorry. Really."]
      ],
      sibling: [
        ["Sincere", "{to},", "I'm sorry for what I said. You didn't deserve it.", "We fight a lot, but this one was on me.", "You're my favourite person to annoy, and I don't want to lose that."],
        ["Light", "{to},", "Okay, I was wrong. Please screenshot this, it won't happen again.", "But seriously, I'm sorry. I hate it when we don't talk.", "Truce?"]
      ],
      friend: [
        ["Sincere", "{to},", "I'm sorry. I went quiet and I made it about me, and that wasn't fair to you.", "You've always shown up for me. I want to do the same.", "Chai's on me. Can we talk?"],
        ["Short", "{to},", "Our friendship matters more to me than being right.", "I'm sorry for what I said. I didn't mean it, and I hate that I hurt you.", "I miss you. Can we fix this?"]
      ]
    },
    asks: {
      partner: [["Coffee tomorrow, my treat, and I'll listen this time?", "Thank you. I'll be there at 6, with your favourite."], ["Can we start over tonight?", "Thank you. I'll make it right, I promise."], ["Can I take you to dinner and say it properly?", "Thank you. 8 pm, your favourite place."]],
      parent: [["Can I come over and say sorry in person?", "Thank you. I'll be there this evening."], ["Will you forgive me?", "Thank you. I love you."]],
      sibling: [["Truce? Pizza's on me.", "Thank you. Extra cheese, as always."], ["Will you forgive me?", "Thank you. Love you, even when we fight."]],
      friend: [["Chai tomorrow, my treat?", "Thank you. Same place, 5 pm."], ["Friends again?", "Thank you. I missed you."]]
    }
  }
};
