# Semestrální projekt STIN
## Zadání
### Cílem projektu je vytvořit chat bota, který musí umět:
1. Přijmout a zpracovat vstupní data (3 otázky)
2. Vygenerovat výstupní data (odpovědi na zadané otázky)

### Jazyk komunikace:  
 Anglický jazyk

### Formáty otázek:
1. Jméno bota
2. Čas
3. Momentální kurz České Koruny vůči Euru

### Příklady koverzace:  
1. Q: "What's your name?" A: "My name is Bot, nice to meet You."  
2. Q: "What time is now?" A: "Now is 12:03:53."  
3. Q: "Show me exchange rate of EUR." A: "Current exchange rate of EUR is 24,420 Kc."

### Funkční vlastnosti:
1. Pokud bude otázka obsahovat "your" a "name", bot odpoví svým jménem.
2. Pokud bude otázka obsahovat "time" a "now", bot odpoví serverovým časem.
3. Pokud bude otázka obsahovat "eur", bot stáhne výpis kurzu ze stránek ČNB, extrahuje z něj kurz eura a vypíše ho.
4. Pokud bude otázka obsahovat klíčová slova z různých formátů otázek, bot odpoví na všechny s následujícím pořadí: Jméno, Datum, Kurz.  (klíčové slovo - slovo, které bude bot hledat, aby vygeneroval odpověď, slovo v uvozovkách)

## Use case diagram:
<img src="./STIN_chatbot.png" alt="Use case diagram" width="950" height="500">
