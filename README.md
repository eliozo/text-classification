# "Ievads dabiskās valodas apstrādē" kursa mājasdarbs teksta klasificēšanā
> Elizabete Ozoliņa, eo20018 (LU DF, 3.kurss, 2022/2023)

## Īss apraksts par projektu
Šis mājasdarbs teksta klasificēšanā tika veikts izmantojot lekcijā apskatīto nb_experiment.py failu un chatgpt. 
Šī mājasdarba ietvaros tika veikta datu kopas priekšapstrāde (normalizācija), sadalīšana pa kategorijām.

## Izvēlētā datu kopa
Izvēlējos Reuters-21578 datu kopu, kurai bija jāveic priekšapstrāde. Šo datu kopu var iegūt no šīs saites http://www.daviddlewis.com/resources/testcollections/reuters21578/ un, atpakojot vajadzīgo failu, var darboties tālāk.

## Papildus Python faili, ko izveidoju priekšapstrādes vajadzībām

`create_topic_body.py` - šis skripts lasa vairākus .sgm failus (Reuters ziņu rakstus), iegūst tēmas un pamattekstus. Pēc tam tas normalizē tekstu un ieraksta iegūto informāciju all_ten_categories.tsv failā, filtrējot tikai noteiktām iepriekš definētām kategorijām.

`freq_counter.py` - šis skripts lasa vairākus .sgm failus (Reuters ziņu rakstus) un uzskaita to vārdu biežumu, kas atrodami <BODY> teksta tagos. Pēc tam tas ieraksta vārdu biežumu, kur parādās vārdu skaits un vārds.

## No priekšapstrādes iegūtie faili
`all_ten_categories.tsv` - šajā failā ir sašķiroti visi teksti, kuri pieder Reuters-21578 lielākajām kategorijām
`all_training_data.tsv` - šajā failā ir visi teksti, ar visām kategorijām (netiek tālāk izmantots)
`output_freq.tsv` - šajā failā ir atrodami biežākie vārdi, kuri sakārtoti no biežāk līdz retāk sastopamajiem visos Reuters-21578 tekstos

## Komandas
1) `cd` projekta direktorijā
2) `python3 -i nb_experiment.py` faila palaišana interaktīvi
3) `initialise('my_stop_list.txt', 'all_ten_categories.tsv')` inicializē 10 kategoriju saģenerēto failu kopā ar my_stop_list.txt failu
4) `run_training("all_ten_categories.tsv", True)` sāk apmācību
5) `initialise('my_stop_list.txt', 'output_freq.tsv')` inicializē biežākos sastopamos vārdus kopā ar my_stop_list.txt failu
6) `run_validation("all_ten_categories.tsv", 5, 1)` veic validāciju, izveido confusion matrix, salīdzina klasifikatora precizitāti

## Secinājumi/Rezultāti

Uztrenēto modeļu precizitāte:
![image](https://github.com/eliozo/text-classification/assets/71934528/6f67aa44-d801-4524-b75f-a9b91a036e6e)

Pēc šī attēla datiem var saprast, ka modeļa veiktspēja varētu būt labāka. Vidējā precizitāte ir tikai 65%.

Confusion matrica: 
![image](https://github.com/eliozo/text-classification/assets/71934528/8214da1a-d376-46b5-9231-bdac158609eb)





