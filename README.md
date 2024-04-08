# Komanda_34_MIP
Pirmais praktiskais darbs, Mākslīgā Intelekta Pamati

## Papildu prasības programmatūrai 

Spēles sākumā spēles programmatūra gadījuma ceļā saģenerē 5 skaitļus diapazonā no 20000 līdz 30000, bet tādus, kas sākotnēji dalās ar 3, 2 un 4. Cilvēks-spēlētājs izvēlas, ar kuru no saģenerētajiem skaitļiem viņš vēlas sākt spēli. 

## Spēles apraksts 
Spēles sākumā ir dots cilvēka-spēlētāja izvēlētais skaitlis.
Abiem spēlētājiem ir 0 punktu.

Spēlētāji izdara gājienus pēc kārtas, katrā gājienā dalot pašreizējā brīdī esošu skaitli ar 2,3 vai 4.
Skaitli ir iespējams sadalīt tikai tajā gadījumā, ja rezultātā veidojas vesels skaitlis.

Ja dalīšanas rezultātā veidojas pāra skaitlis, tad no pretinieka punktiem tiek atņemts 1 punkts, ja nepāra skaitlis, tad paša spēlētāja punkti tiek palielināti par 1 punktu. 

Spēle beidzas, kā tikko ir iegūts skaitlis, kas ir mazāks vai vienāds ar 10. Ja spēlētāju punktu skaits ir vienāds, tad rezultāts ir neizšķirts. Pretējā gadījumā uzvar spēlētājs, kam ir vairāk punktu. 

## Komandas ieviestās prasības
Ne vienmēr saģenerētu skaitli būs iespējams sadalīt tik tālu, kad skaitlis ir mazāks par 10, kā rezultātā spēle beidzas, kad nav vairs iespējams sadalīt skaitli tālāk ar 2, 3 vai 4, nevis, kad skaitlis ir mazāks par 10 (ja skaitlis ir mazāks par 10, bet to ir iespējams sadalīt, tad arī spēle beidzas sakarā ar sākotnējiem noteikumiem).
