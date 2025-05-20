import datetime
mire=input("Mire gyűjt Anna?")
darabkutya=int(input("hány kutyát sétáltat?"))
ora=(darabkutya*20)//60
perc=(darabkutya*20)%60
print(f"Anna {ora}:{perc} tölt sétáltatással")
fizu=darabkutya*700
print(f"{darabkutya*700} Ft a fizetése")
if fizu>=5000:
    print(f"Anna {mire} gyűjtött, és egy hétvége melóval sikerült megvennie")
else:
    print(f"Anna {mire} gyűjtött, és egy hétvége melóval nem sikerült megvennie")
