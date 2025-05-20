import datetime
mire=input("Mire gyűjt Anna?")
darabkutya=int(input("hány kutyát sétáltat?"))
ora=(darabkutya*20)//60
perc=(darabkutya*20)%60
print(f"Anna {ora}:{perc} tölt sétáltatással")
fizu=darabkutya*700
print(f"{darabkutya*700} Ft a fizetése")
if fizu>=5000:
    print(f"Anna {darabkutya} kutyát sétáltatott {ora} óra alatt, ezért {fizu} Ft-ot kapott. Ez már elég a {mire}.")
else:
    print(f"Anna {darabkutya} kutyát sétáltatott {ora} óra alatt, ezért {fizu} Ft-ot kapott. Ez még nem elég a {mire}.")
