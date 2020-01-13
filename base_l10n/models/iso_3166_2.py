# -*- coding: utf-8 -*-

# https://github.com/olahol/iso-3166-2.json/blob/master/data/eQuest.csv
# Successfull implementation requires regular updates

iso_3166_2 = """AF,,,Afghanistan
,AF-BDS,,Badakhshān
,AF-BDG,,Bādghīs
,AF-BGL,,Baghlān
,AF-BAL,,Balkh
,AF-BAM,,Bāmīān
,AF-FRA,,Farāh
,AF-FYB,,Fāryāb
,AF-GHA,,Ghaznī
,AF-GHO,,Ghowr
,AF-HEL,,Helmand
,AF-HER,,Herāt
,AF-JOW,,Jowzjān
,AF-KAB,,Kabul (Kābol)
,AF-KAN,,Kandahār
,AF-KAP,,Kāpīsā
,AF-KNR,,Konar (Kunar)
,AF-KDZ,,Kondoz (Kunduz)
,AF-LAG,,Laghmān
,AF-LOW,,Lowgar
,AF-NAN,,Nangrahār (Nangarhār)
,AF-NIM,,Nīmrūz
,AF-ORU,,Orūzgān (Urūzgā
,AF-PIA,,Paktīā
,AF-PKA,,Paktīkā
,AF-PAR,,Parwān
,AF-SAM,,Samangān
,AF-SAR,,Sar-e Pol
,AF-TAK,,Takhār
,AF-WAR,,Wardak (Wardag)
,AF-ZAB,,Zābol (Zābul)
AL,,,Albania
,AL-BR,,Berat
,AL-BU,,Bulqizë
,AL-DL,,Delvinë
,AL-DV,,Devoll
,AL-DI,,Dibër
,AL-DR,,Durrës
,AL-EL,,Elbasan
,AL-FR,,Fier
,AL-GR,,Gramsh
,AL-GJ,,Gjirokastër
,AL-HA,,Has
,AL-KA,,Kavajë
,AL-ER,,Kolonjë
,AL-KO,,Korcë
,AL-KR,,Krujë
,AL-KC,,Kucovë
,AL-KU,,Kukës
,AL-LA,,Laç
,AL-LE,,Lezhë
,AL-LB,,Librazhd
,AL-LU,,Lushnjë
,AL-MM,,Malësia e Madhe
,AL-MK,,Mallakastër
,AL-MT,,Mat
,AL-MR,,Mirditë
,AL-PQ,,Peqin
,AL-PR,,Përmet
,AL-PG,,Pogradec
,AL-PU,,Pukë
,AL-SR,,Sarandë
,AL-SK,,Skrapar
,AL-SH,,Shkodër
,AL-TE,,Tepelenë
,AL-TR,,Tiranë
,AL-TP,,Tropojë
,AL-VL,,Vlorë
DZ,,,Algeria
,DZ-01,,Adrar
,DZ-44,,Aïn Defla
,DZ-46,,Aïn Témouchent
,DZ-16,,Alger
,DZ-05,,Batna
,DZ-08,,Béchar
,DZ-06,,Béjaïa
,DZ-07,,Biskra
,DZ-09,,Blida
,DZ-34,,Bordj Bou Arréridj
,DZ-10,,Bouira
,DZ-35,,Boumerdès
,DZ-02,,Chlef
,DZ-25,,Constantine
,DZ-17,,Djelfa
,DZ-32,,El Bayadh
,DZ-39,,El Oued
,DZ-36,,El Tarf
,DZ-47,,Ghardaïa
,DZ-24,,Guelma
,DZ-33,,Illizi
,DZ-18,,Jijel
,DZ-40,,Khenchela
,DZ-03,,Laghouat
,DZ-29,,Mascara
,DZ-26,,Médéa
,DZ-43,,Mila
,DZ-27,,Mostaganem
,DZ-28,,Msila
,DZ-45,,Naama
,DZ-31,,Oran
,DZ-30,,Ouargla
,DZ-04,,Oum el Bouaghi
,DZ-48,,Relizane
,DZ-20,,Saïda
,DZ-19,,Sétif
,DZ-22,,Sidi Bel Abbès
,DZ-21,,Skikda
,DZ-41,,Souk Ahras
,DZ-11,,Tamanghasset
,DZ-12,,Tébessa
,DZ-14,,Tiaret
,DZ-37,,Tindouf
,DZ-42,,Tipaza
,DZ-38,,Tissemsilt
,DZ-15,,Tizi Ouzou
,DZ-13,,Tlemcen
AS,,,American Samoa
,AS-AS,,American Samoa
AD,,,Andorra
,AD-AD,,Andorra
AO,,,Angola
,AO-BGO,,Bengo
,AO-BGU,,Benguela
,AO-BIE,,Bié
,AO-CAB,,Cabinda
,AO-CCU,,Cuando-Cubango
,AO-CNO,,Cuanza Norte
,AO-CUS,,Cuanza Sul
,AO-CNN,,Cunene
,AO-HUA,,Huambo
,AO-HUI,,Huíla
,AO-LUA,,Luanda
,AO-LNO,,Lunda Norte
,AO-LSU,,Lunda Sul
,AO-MAL,,Malange
,AO-MOX,,Moxico
,AO-NAM,,Namibe
,AO-UIG,,Uíge
,AO-ZAI,,Zaïre
AI,,,Anguilla
,AI-AI,,Anguilla
AQ,,,Antarctica
,AQ-AQ,,Antarctica
AG,,,Antigua & Barbuda
,AG-AG,,Antigua & Barbuda
AR,,,Argentina
,AR-C,,Capital federal
,AR-B,,Buenos Aires
,AR-K,,Catamarca
,AR-X,,Córdoba
,AR-W,,Corrientes
,AR-H,,Chaco
,AR-U,,Chubut
,AR-E,,Entre Ríos
,AR-P,,Formosa
,AR-Y,,Jujuy
,AR-L,,La Pampa
,AR-F,,La Rioja
,AR-M,,Mendoza
,AR-N,,Misiones
,AR-Q,,Neuquén
,AR-R,,Río Negro
,AR-A,,Salta
,AR-J,,San Juan
,AR-D,,San Luis
,AR-Z,,Santa Cruz
,AR-S,,Santa Fe
,AR-G,,Santiago del Estero
,AR-V,,Tierra del Fuego
,AR-T,,Tucumán
AM,,,Armenia
,AM-ER,,Erevan
,AM-AG,,Aragacotn
,AM-AR,,Ararat
,AM-AV,,Armavir
,AM-GR,,Geģark'unik'
,AM-KT,,Kotayk'
,AM-LO,,Loŕy
,AM-SH,,Širak
,AM-SU,,Syunik'
,AM-TV,,Tavuš
,AM-VD,,Vayoc Jor
AW,,,Aruba
,AW-AW,,Aruba
AU,,,Australia
,AU-NSW,,New South Wales
,AU-QLD,,Queensland
,AU-SA,,South Australia
,AU-TAS,,Tasmania
,AU-VIC,,Victoria
,AU-WA,,Western Australia
,AU-ACT,,Australian Capital Territory
,AU-NT,,Northern Territory
AT,,,Austria
,AT-1,,Burgenland
,AT-2,,Kärnten
,AT-3,,Niederösterreich
,AT-4,,Oberösterreich
,AT-5,,Salzburg
,AT-6,,Steiermark
,AT-7,,Tirol
,AT-8,,Vorarlberg
,AT-9,,Wien
AZ,,,Azerbaijan
,AZ-MM,,Naxçivan
,AZ-AB,,Äli Bayramli
,AZ-BA,,Baki
,AZ-GA,,Gäncä
,AZ-LA,,Länkäran
,AZ-MI,,Mingäçevir
,AZ-NA,,Naftalan
,AZ-SA,,Şäki
,AZ-SM,,Sumqayit
,AZ-SS,,Şuşa
,AZ-XA,,Xankändi
,AZ-YE,,Yevlax
,AZ-ABS,,Abşeron
,AZ-AGC,,Ağcabädi
,AZ-AGM,,Ağdam
,AZ-AGS,,Ağdas
,AZ-AGA,,Ağstafa
,AZ-AGU,,Ağsu
,AZ-AST,,Astara
,AZ-BAB,,Babäk
,AZ-BAL,,Balakän
,AZ-BAR,,Bärdä
,AZ-BEY,,Beyläqan
,AZ-BIL,,Biläsuvar
,AZ-CAB,,Cäbrayil
,AZ-CAL,,Cälilabad
,AZ-CUL,,Culfa
,AZ-DAS,,Daşkäsän
,AZ-DAV,,Däväçi
,AZ-FUZ,,Füzuli
,AZ-GAD,,Gädäbäy
,AZ-GOR,,Goranboy
,AZ-GOY,,Göyçay
,AZ-HAC,,Haciqabul
,AZ-IMI,,Imişli
,AZ-ISM,,Ismayilli
,AZ-KAL,,Kälbäcär
,AZ-KUR,,Kürdämir
,AZ-LAC,,Laçin
,AZ-LAN,,Länkäran
,AZ-LER,,Lerik
,AZ-MAS,,Masalli
,AZ-NEF,,Neftçala
,AZ-OGU,,Oğuz
,AZ-ORD,,Ordubad
,AZ-QAB,,Qäbälä
,AZ-QAX,,Qax
,AZ-QAZ,,Qazax
,AZ-QOB,,Qobustan
,AZ-QBA,,Quba
,AZ-QBI,,Qubadlı
,AZ-QUS,,Qusar
,AZ-SAT,,Saatli
,AZ-SAB,,Sabirabad
,AZ-SAD,,Sädäräk
,AZ-SAH,,Şahbuz
,AZ-SAK,,Şäki
,AZ-SAL,,Salyan
,AZ-SMI,,Şamaxı
,AZ-SKR,,Şämkir
,AZ-SMX,,Samux
,AZ-SAR,,Şärur
,AZ-SIY,,Siyäzän
,AZ-SUS,,Şuşa
,AZ-TAR,,Tärtär
,AZ-TOV,,Tovuz
,AZ-UCA,,Ucar
,AZ-XAC,,Xaçmaz
,AZ-XAN,,Xanlar
,AZ-XIZ,,Xizi
,AZ-XCI,,Xocalı
,AZ-XVD,,Xocavänd
,AZ-YAR,,Yardimli
,AZ-YEV,,Yevlax
,AZ-ZAN,,Zängılan
,AZ-ZAQ,,Zaqatala
,AZ-ZAR,,Zärdab
BS,,,Bahamas
,BS-AC,,Acklins and Crooked Islands
,BS-BI,,Bimini
,BS-CI,,Cat Island
,BS-EX,,Exuma
,BS-FP,,Freeport
,BS-FC,,Fresh Creek
,BS-GH,,Governor's Harbour
,BS-GT,,Green Turtle Cay
,BS-HI,,Harbour Island
,BS-HR,,High Rock
,BS-IN,,Inagua
,BS-KB,,Kemps Bay
,BS-LI,,Long Island
,BS-MH,,Marsh Harbour
,BS-MG,,Mayaguana
,BS-NP,,New Providence
,BS-NB,,Nicholls Town and Berry Islands
,BS-RI,,Ragged Island
,BS-RS,,Rock Sound
,BS-SP,,Sandy Point
,BS-SR,,San Salvador and Rum Cay
BH,,,Bahrain
,BH-01,,Al Ḩadd
,BH-03,,Al Manāmah
,BH-10,,Al Minţaqah al Gharbīyah
,BH-07,,Al Minţaqah al Wusţa
,BH-05,,Al Minţaqah ash Shamālīyah
,BH-02,,Al Muḩarraq
,BH-09,,Ar Rifā‘
,BH-04,,Jidd Ḩafş
,BH-12,,Madīnat Ḩamad
,BH-08,,Madīnat ‘Īsá
,BH-11,,Minţaqat Juzur Ḩawār
,BH-06,,Sitrah
BD,,,Bangladesh
,BD-1,,Barisal bibhag
,,BD-1B,Barisal anchal
,,BD-1Q,Patuakhali anchal
,BD-2,,Chittagong bibhag
,,BD-2A,Bandarban anchal
,,BD-2D,Chittagong anchal
,,BD-2E,Chittagong Hill Tracts
,,BD-2F,Comilla anchal
,,BD-2O,Noakhali anchal
,,BD-2T,Sylhet anchal
,BD-3,,Dhaka bibhag
,,BD-3G,Dhaka anchal
,,BD-3I,Faridpur anchal
,,BD-3J,Jamalpur anchal
,,BD-3N,Mymensingh anchal
,,BD-3U,Tangail anchal
,BD-4,,Khulna bibhag
,,BD-4K,Jessore anchal
,,BD-4L,Khulna anchal
,,BD-4M,Khustia anchal
,BD-5,,Rajshahi bibhag
,,BD-5C,Bogra anchal
,,BD-5H,Dinajpur anchal
,,BD-5P,Pabna anchal
,,BD-5R,Rajshahi anchal
,,BD-5S,Rangpur anchal
BB,,,Barbados
,BB-BB,,Barbados
BY,,,Belarus
,BY-BR,,Brestskaya voblasts'
,BY-HO,,Homyel'skaya voblasts’
,BY-HR,,Hrodnenskaya voblasts'
,BY-MA,,Mahilyowskaya voblasts'
,BY-MI,,Minskaya voblasts'
,BY-VI,,Vitsyebskaya voblasts'
BE,,,Belgium
,BE-BRU,,"Bruxelles-Capitale, Region de (fr), Brussels Hoofdstedelijk Gewest (nl)"
,BE-VLG,,Vlaamse Gewest (nl)
,,BE-VAN,Antwerpen (nl)
,,BE-VLI,Limburg (nl)
,,BE-VOV,Oost-Vlaanderen (nl)
,,BE-VBR,Vlaams Brabant (nl)
,,BE-VWV,West-Vlaanderen (nl)
,BE-WAL,,"Wallonne, Region (fr)"
,,BE-WBR,Brabant Wallon (fr)
,,BE-WHT,Hainaut (fr)
,,BE-WLG,Liège (fr)
,,BE-WLX,Luxembourg (fr)
,,BE-WNA,Namur (fr)
BZ,,,Belize
,BZ-BZ,,Belize
,BZ-CY,,Cayo
,BZ-CZL,,Corozal
,BZ-OW,,Orange Walk
,BZ-SC,,Stann Creek
,BZ-TOL,,Toledo
BJ,,,Benin
,BJ-AK,,Atakora
,BJ-AQ,,Atlantique
,BJ-BO,,Borgou
,BJ-MO,,Mono
,BJ-OU,,Ouémé
,BJ-ZO,,Zou
BM,,,Bermuda
,BM-BM,,Bermuda
BT,,,Bhutan
,BT-33,,Bumthang
,BT-12,,Chhukha
,BT-22,,Dagana
,BT-GA,,Gasa
,BT-13,,Ha
,BT-44,,Lhuentse
,BT-42,,Monggar
,BT-11,,Paro
,BT-43,,Pemagatshel
,BT-23,,Punakha
,BT-45,,Samdrup Jongkha
,BT-14,,Samtse
,BT-31,,Sarpang
,BT-15,,Thimphu
,BT-41,,Trashigang
,BT-TY,,Trashi Yangtse
,BT-32,,Trongsa
,BT-21,,Tsirang
,BT-24,,Wangdue Phodrang
,BT-34,,Zhemgang
BO,,,Bolivia
,BO-C,,Cochabamba
,BO-H,,Chuquisaca
,BO-B,,El Beni
,BO-L,,La Paz
,BO-O,,Oruro
,BO-N,,Pando
,BO-P,,Potosi
,BO-S,,Santa Cruz
,BO-T,,Tarija
BA,,,Bosnia & Herzegovina
,BA-BIH,,Federacija Bosna i Hercegovina
,BA-SRP,,Republika Srpska
BW,,,Botswana
,BW-CE,,Central [Serowe-Palapye]
,BW-CH,,Chobe
,BW-GH,,Ghanzi
,BW-KG,,Kgalagadi
,BW-KL,,Kgatleng
,BW-KW,,Kweneng
,BW-NG,,Ngamiland [North-West]
,BW-NE,,North-East
,BW-SE,,South-East
,BW-SO,,Southern [Ngwaketse]
BV,,,Bouvet Island
,BV-BV,,Bouvet Island
BR,,,Brazil
,BR-DF,,Distrito Federal
,BR-AC,,Acre
,BR-AL,,Alagoas
,BR-AP,,Amapá
,BR-AM,,Amazonas
,BR-BA,,Bahia
,BR-CE,,Ceará
,BR-ES,,Espírito Santo
,BR-GO,,Goiás
,BR-MA,,Maranhāo
,BR-MT,,Mato Grosso
,BR-MS,,Mato Grosso do Sul
,BR-MG,,Minas Gerais
,BR-PA,,Pará
,BR-PB,,Paraíba
,BR-PR,,Paraná
,BR-PE,,Pernambuco
,BR-PI,,Piauí
,BR-RJ,,Rio de Janeiro
,BR-RN,,Rio Grande do Norte
,BR-RS,,Rio Grande do Sul
,BR-R0,,Rondônia
,BR-RR,,Roraima
,BR-SC,,Santa Catarina
,BR-SP,,São Paulo
,BR-SE,,Sergipe
,BR-TO,,Tocantins
IO,,,British Indian Ocean Territory
,IO-IO,,British Indian Ocean Territory
BN,,,Brunei Darussalam
,BN-BE,,Belait
,BN-BM,,Brunei-Muara
,BN-TE,,Temburong
,BN-TU,,Tutong
BG,,,Bulgaria
,BG-02,,Burgas
,BG-09,,Haskovo
,BG-04,,Loveč
,BG-05,,Montana
,BG-06,,Plovdiv
,BG-07,,Ruse
,BG-08,,Sofija
,BG-01,,Sofija-Grad
,BG-03,,Varna
BF,,,Burkina Faso
,BF-BAL,,Balé
,BF-BAM,,Bam
,BF-BAN,,Banwa
,BF-BAZ,,Bazèga
,BF-BGR,,Bougouriba
,BF-BLG,,Boulgou
,BF-BLK,,Boulkiemdé
,BF-COM,,Comoé
,BF-GAN,,Ganzourgou
,BF-GNA,,Gnagna
,BF-GOU,,Gourma
,BF-HOU,,Houet
,BF-IOB,,Ioba
,BF-KAD,,Kadiogo
,BF-KEN,,Kénédougou
,BF-KMD,,Komondjari
,BF-KMP,,Kompienga
,BF-KOS,,Kossi
,BF-KOP,,Koulpélogo
,BF-KOT,,Kouritenga
,BF-KOW,,Kourwéogo
,BF-LER,,Léraba
,BF-LOR,,Loroum
,BF-MOU,,Mouhoun
,BF-NAO,,Nahouri
,BF-NAM,,Namentenga
,BF-NAY,,Nayala
,BF-NOU,,Noumbiel
,BF-OUB,,Oubritenga
,BF-OUD,,Oudalan
,BF-PAS,,Passoré
,BF-PON,,Poni
,BF-SNG,,Sanguié
,BF-SMT,,Sanmatenga
,BF-SEN,,Séno
,BF-SIS,,Sissili
,BF-SOM,,Soum
,BF-SOR,,Sourou
,BF-TAP,,Tapoa
,BF-TUI,,Tui
,BF-YAG,,Yagha
,BF-YAT,,Yatenga
,BF-ZIR,,Ziro
,BF-ZON,,Zondoma
,BF-ZOU,,Zoundwéogo
BI,,,Burundi
,BI-BB,,Bubanza
,BI-BJ,,Bujumbura
,BI-BR,,Bururi
,BI-CA,,Cankuzo
,BI-CI,,Cibitoke
,BI-GI,,Gitega
,BI-KR,,Karuzi
,BI-KY,,Kayanza
,BI-KI,,Kirundo
,BI-MA,,Makamba
,BI-MU,,Muramvya
,BI-MY,,Muyinga
,BI-NG,,Ngozi
,BI-RT,,Rutana
,BI-RY,,Ruyigi
KH,,,Cambodia
,KH-23,,Krong Kaeb [Krŏng Kêb]
,KH-18,,Krong Preah Sihanouk [Krŏng Preăh Sihanouk]
,KH-12,,Phnom Penh [Phnum Pénh]
,KH-2,,Baat Dambang [Bătdâmbâng]
,KH-1,,Banteay Mean Chey [Bântéay Méanchey]
,KH-3,,Kampong Chaam [Kâmpóng Cham]
,KH-4,,Kampong Chhnang [Kâmpóng Chhnăng]
,KH-5,,Kampong Spueu [Kâmpóng Spœ]
,KH-6,,Kampong Thum [Kâmpóng Thum]
,KH-7,,Kampot [Kâmpôt]
,KH-8,,Kandaal [Kândal]
,KH-10,,Kracheh [Krâchéh]
,KH-11,,Mond01 Kiri [Môndól Kiri]
,KH-22,,Otdar Mean Chey [Ŏtdâr Méanchey]
,KH-15,,Pousaat [Poŭthĭsăt]
,KH-13,,Preah Vihear [Preăh Vihéar]
,KH-14,,Prey Veaeng [Prey Vêng]
,KH-16,,Rotanak Kiri [Rôtânôkiri]
,KH-17,,Siem Reab [Siĕmréab]
,KH-19,,Stueng Traeng [Stœng Trêng]
,KH-20,,Svaay Rieng [Svay Riĕng]
,KH-21,,Taakaev [Takêv]
CM,,,Cameroon
,CM-AD,,Adamaoua
,CM-CE,,Centre
,CM-ES,,Est
,CM-EN,,Far North
,CM-LT,,Littoral
,CM-NO,,North
,CM-NW,,North-West
,CM-SU,,South
,CM-SW,,South-West
,CM-OU,,West
CA,,,Canada
,CA-AB,,Alberta
,CA-BC,,British Columbia (Colombie-Britannique)
,CA-MB,,Manitoba
,CA-NB,,New Brunswick (Nouveau-Brunswick)
,CA-NL,,Newfoundland and Labrador (Terre-Neuve)
,CA-NS,,Nova Scotia (Nouvelle-Écosse)
,CA-ON,,Ontario
,CA-PE,,Prince Edward Island (Île-du-Prince-Édouard)
,CA-QC,,Quebec (Québec)
,CA-SK,,Saskatchewan
,CA-NT,,Northwest Territories (Territoires du Nord-Ouest)
,CA-NU,,Nunavut
,CA-YT,,Yukon Territory (Teritoire du Yukon)
CV,,,Cape Verde
,CV-B,,Ilhas de Barlavento
,,CV-BV,Boa Vista
,,CV-PA,Paul
,,CV-PN,Porto Novo
,,CV-RG,Ribeira Grande
,,CV-SL,Sal
,,CV-SN,Sāo Nicolau
,,CV-SV,Sāo Vicente
,CV-S,,Ilhas de Sotavento
,,CV-BR,Brava
,,CV-FO,Fogo
,,CV-MA,Maio
,,CV-PR,Praia
,,CV-CA,Santa Catarina
,,CV-CR,Santa Cruz
,,CV-TA,Tarrafal
KY,,,Cayman Islands
,KY-KY,,Cayman Islands
CF,,,Central African Republic
,CF-BGF,,Bangui
,CF-BB,,Bamingui-Bangoran
,CF-BK,,Basse-Kotto
,CF-HK,,Haute-Kotto
,CF-HM,,Haut-Mbomou
,CF-KG,,Kémo
,CF-LB,,Lobaye
,CF-HS,,Mambéré-Kadéï
,CF-MB,,Mbomou
,CF-KB,,Nana-Grébizi
,CF-NM,,Nana-Mambéré
,CF-MP,,Ombella-Mpoko
,CF-UK,,Ouaka
,CF-AC,,Ouham
,CF-OP,,Ouham-Pendé
,CF-SE,,Sangha-Mbaéré
,CF-VK,,Vakaga
TD,,,Chad
,TD-BA,,Batha
,TD-BI,,Biltine
,TD-BET,,Borkou-Ennedi-Tibesti
,TD-CB,,Chari-Baguirmi
,TD-GR,,Guéra
,TD-KA,,Kanem
,TD-LC,,Lac
,TD-LO,,Logone-Occidental
,TD-LR,,Logone-Oriental
,TD-MK,,Mayo-Kébbi
,TD-MC,,Moyen-Chari
,TD-OD,,Ouaddaï
,TD-SA,,Salamat
,TD-TA,,Tandjilé
CL,,,Chile
,CL-AI,,Aisén del General Carlos Ibáñiez del Campo
,CL-AN,,Antofagasta
,CL-AR,,Araucanía
,CL-AT,,Atacama
,CL-BI,,Bío-Bío
,CL-CO,,Coquimbo
,CL-LI,,Libertador General Bernardo O'Higgins
,CL-LL,,Los Lagos
,CL-MA,,Magallanes
,CL-ML,,Maule
,CL-RM,,Regíon Metropolitana de Santiago
,CL-TA,,Tarapacá
,CL-VS,,Valparaiso
CN,,,China
,CN-11,,Beijing
,CN-50,,Chongqing
,CN-31,,Shanghai
,CN-12,,Tianjin
,CN-34,,Anhui
,CN-35,,Fujian
,CN-62,,Gansu
,CN-44,,Guangdong
,CN-52,,Guizhou
,CN-46,,Hainan
,CN-13,,Hebei
,CN-23,,Heilongjiang
,CN-41,,Henan
,CN-42,,Hubei
,CN-43,,Hunan
,CN-32,,Jiangsu
,CN-36,,Jiangxi
,CN-22,,Jilin
,CN-21,,Liaoning
,CN-63,,Qinghai
,CN-61,,Shaanxi
,CN-37,,Shandong
,CN-14,,Shanxi
,CN-51,,Sichuan
,CN-71,,Taiwan
,CN-53,,Yunnan
,CN-33,,Zhejiang
,CN-45,,Guangxi
,CN-15,,Nei Monggol
,CN-64,,Ningxia
,CN-65,,Xinjiang
,CN-54,,Xizang
,CN-91,,Hong Kong
CX,,,Christmas Island
,CX-CX,,Christmas Island
CC,,,Cocos (Keeling) Islands
,CC-CC,,Cocos (Keeling) Islands
CO,,,Colombia
,CO-DC,,Distrito Capital de Santa Fe de Bogota
,CO-AMA,,Amazonas
,CO-ANT,,Antioguia
,CO-ARA,,Arauca
,CO-ATL,,Atlántico
,CO-BOL,,Bolívar
,CO-BOY,,Boyacá
,CO-CAL,,Caldas
,CO-CAQ,,Caquetá
,CO-CAS,,Casanare
,CO-CAU,,Cauca
,CO-CES,,Cesar
,CO-COR,,Córdoba
,CO-CUN,,Cundinamarca
,CO-CHO,,Chocó
,CO-GUA,,Guainía
,CO-GUV,,Guaviare
,CO-HUI,,Huila
,CO-LAG,,La Guajira
,CO-MAG,,Magdalena
,CO-MET,,Meta
,CO-NAR,,Nariño
,CO-NSA,,Norte de Santander
,CO-PUT,,Putumayo
,CO-QUI,,Quindío
,CO-RIS,,Risaralda
,CO-SAP,,"San Andrés, Providencia y Santa Catalina"
,CO-SAN,,Santander
,CO-SUC,,Sucre
,CO-TOL,,Tolima
,CO-VAC,,Valle del Cauca
,CO-VAU,,Vaupés
,CO-VID,,Vichada
KM,,,Comoros
,KM-A,,Anjouan (Ndzouani)
,KM-G,,Grande Comore (Ngazidja)
,KM-M,,Mohéli (Moili)
CG,,,Congo
,CG-BZV,,Brazzaville
,CG-11,,Bouenza
,CG-8,,Cuvette
,CG-15,,Cuvette-Ouest
,CG-5,,Kouilou
,CG-2,,Lékoumou
,CG-7,,Likouala
,CG-9,,Niari
,CG-14,,Plateaux
,CG-12,,Pool
,CG-13,,Sangha
CD,,,Zaire
,CD-KN,,Kinshasa
,CD-BN,,Bandundu
,CD-BC,,Bas-Congo
,CD-EQ,,Équateur
,CD-HC,,Haut-Congo
,CD-KW,,Kasai-Occidental
,CD-KE,,Kasai-Oriental
,CD-KA,,Katanga
,CD-MA,,Maniema
,CD-NK,,Nord-Kivu
,CD-SK,,Sud-Kivu
CK,,,Cook Islands
,CK-CK,,Cook Islands
CR,,,Costa Rica
,CR-A,,Alajuela
,CR-C,,Cartago
,CR-G,,Guanacaste
,CR-H,,Heredia
,CR-L,,Limón
,CR-P,,Puntarenas
,CR-SJ,,San José
CI,,,Cote D'ivoire (Ivory Coast)
,CI-06,,18 Montagnes (Région des)
,CI-16,,Agnébi (Région de l')
,CI-09,,Bas-Sassandra (Région du)
,CI-10,,Denguélé (Région du)
,CI-02,,Haut-Sassandra (Région du)
,CI-07,,Lacs (Région des)
,CI-01,,Lagunes (Région des)
,CI-12,,Marahoué (Région de la)
,CI-05,,Moyen-Comoé (Région du)
,CI-11,,Nzi-Comoé (Région)
,CI-03,,Savanes (Région des)
,CI-15,,Sud-Bandama (Région du)
,CI-13,,Sud-Comoé (Région du)
,CI-04,,Vallée du Bandama (Région de la)
,CI-14,,Worodougou (Région du)
,CI-08,,Zanzan (Région du)
HR,,,Croatia (Hrvatska)
,HR-07,,Bjelovarsko-bilogorska županija
,HR-12,,Brodsko-posavska županija
,HR-19,,Dubrovačko-neretvanska županija
,HR-18,,Istarska županija
,HR-04,,Karlovačka županija
,HR-06,,Koprivničkco-križevačka županija
,HR-02,,Krapinsko-zagorska županija
,HR-09,,Ličko-senjska županija
,HR-20,,Medjimurska županija
,HR-14,,Osječko-baranjska županija
,HR-11,,Požeško-slavonska županija
,HR-08,,Primorsko-goranska županija
,HR-03,,Sisaško-moslavačka županija
,HR-17,,Splitsko-dalmatinska županija
,HR-15,,Šibensko-kninska županija
,HR-05,,Varaždinska županija
,HR-10,,Virovitičko-podravska županija
,HR-16,,Vukovarsko-srijemska županija
,HR-13,,Zadarska županija
,HR-01,,Zagrebačka županija
CU,,,Cuba
,CU-09,,Camagüey
,CU-03,,Ciudad de La Habana
,CU-12,,Granma
,CU-14,,Guantánamo
,CU-11,,Holguín
,CU-02,,La Habana
,CU-10,,Las Tunas
,CU-04,,Matanzas
,CU-01,,Pinar del Río
,CU-07,,Sancti Spíritus
,CU-13,,Santiago de Cuba
,CU-05,,Villa Clara
,CU-99,,Isla de la Juventud
CY,,,Cyprus
,CY-04,,Ammochostos (Mağusa)
,CY-06,,Keryneia (Girne)
,CY-03,,Larnaka
,CY-01,,Lefkosia (Lefkoşa)
,CY-02,,Lemesos (Leymosun)
,CY-05,,Pafos (Baf)
CZ,,,Czech Republic
,CZ-PRG,,Praha
,CZ-CJC,,Jihočeský kraj
,CZ-CJM,,Jihomoravský kraj
,CZ-CSC,,Severočeský kraj
,CZ-CSM,,Severomoravský kraj
,CZ-CST,,Středočeský kraj
,CZ-CVC,,Východočeský kraj
,CZ-CZC,,Západočeský kraj
DK,,,Denmark
,DK-147,,Frederiksberg
,DK-101,,Kǿbenhavn
,DK-040,,Bornholm
,DK-020,,Frederiksborg
,DK-042,,Fyn
,DK-015,,Kǿbenhavn
,DK-080,,Nordjylland
,DK-055,,Ribe
,DK-065,,Ringkǿbing
,DK-025,,Roskilde
,DK-035,,Storstrǿm
,DK-050,,Sǿnderjylland
,DK-060,,Vejle
,DK-030,,Vestsjælland
,DK-076,,Viborg
,DK-070,,Århus
DJ,,,Djibouti
,DJ-AS,,Ali Sabieh
,DJ-DI,,Dikhil
,DJ-DJ,,Djibouti
,DJ-OB,,Obock
,DJ-TA,,Tadjoura
DM,,,Dominica
,DM-DM,,Dominica
DO,,,Dominican Republic
,DO-DN,,Distrito National (Santo Domingo)
,DO-AZ,,Azua
,DO-BR,,Bahoruco
,DO-BH,,Barahona
,DO-DA,,Dajabón
,DO-DU,,Duarte
,DO-SE,,El Seibo
,DO-EP,,La Estrelleta [Elías Piña]
,DO-HM,,Hato Mayor
,DO-IN,,Independencia
,DO-AL,,La Altagracia
,DO-RO,,La Romana
,DO-VE,,La Vega
,DO-MT,,María Trinidad Sánchez
,DO-MN,,Monseñor Nouel
,DO-MC,,Monte Cristi
,DO-MP,,Monte Plata
,DO-PN,,Pedernales
,DO-PR,,Peravia
,DO-PP,,Puerto Plata
,DO-SC,,Salcedo
,DO-SM,,Samaná
,DO-SZ,,Sanchez Ramírez
,DO-CR,,San Cristóbal
,DO-JU,,San Juan
,DO-PM,,San Pedro de Macorís
,DO-ST,,Santiago
,DO-SR,,Santiago Rodríguez
,DO-VA,,Valverde
TP,,,East Timor
,TP-TP,,East Timor
EC,,,Ecuador
,EC-A,,Azuay
,EC-B,,Bolívar
,EC-F,,Cañar
,EC-C,,Carchi
,EC-X,,Cotopaxi
,EC-H,,Chimborazo
,EC-O,,El Oro
,EC-E,,Esmeraldas
,EC-W,,Galápagos
,EC-G,,Guayas
,EC-I,,Imbabura
,EC-L,,Loja
,EC-R,,Los Ríos
,EC-M,,Manabí
,EC-S,,Morona-Santiago
,EC-N,,Napo
,EC-Y,,Pastaza
,EC-P,,Pichincha
,EC-U,,Sucumbíos
,EC-T,,Tungurahua
,EC-Z,,Zarnora-Chinchipe
EG,,,Egypt
,EG-DK,,Ad Daqahlīyah
,EG-BA,,Al Baḩr al Aḩmar
,EG-BH,,Al Buḩayrah
,EG-FYM,,Al Fayyūm
,EG-GH,,Al Gharbīyah
,EG-ALX,,Al Iskandarīyah
,EG-IS,,Al Ismā‘īlīyah
,EG-GZ,,Al Jīzah
,EG-MNF,,Al Minūfīyah
,EG-MN,,Al Minyā
,EG-C,,Al Qāhirah
,EG-KB,,Al Qalyūbīyah
,EG-WAD,,Al Wādī al Jadīd
,EG-SHR,,Ash Sharqīyah
,EG-SUZ,,As Suways
,EG-ASN,,Aswān
,EG-AST,,Asyūţ
,EG-BNS,,Banī Suwayf
,EG-PTS,,Būr Sa‘īd
,EG-DT,,Dumyāţ
,EG-JS,,Janūb Sīnā'
,EG-KFS,,Kafr ash Shaykh
,EG-MT,,Maţrūḩ
,EG-KN,,Qinā
,EG-SIN,,Shamāl Sīnā'
,EG-SHG,,Sūhāj
SV,,,El Salvador
,SV-AH,,Ahuachapán
,SV-CA,,Cabañas
,SV-CU,,Cuscatlán
,SV-CH,,Chalatenango
,SV-LI,,La Libertad
,SV-PA,,La Paz
,SV-UN,,La Unión
,SV-MO,,Morazán
,SV-SM,,San Miguel
,SV-SS,,San Salvador
,SV-SA,,Santa Ana
,SV-SV,,San Vicente
,SV-SO,,Sonsonate
,SV-SU,,Usulután
GQ,,,Equatorial Guinea
,GQ-C,,Región Continental
,,GQ-CS,Centro Sur
,,GQ-KN,Kie-Ntem
,,GQ-LI,Litoral
,,GQ-WN,Wele-Nzás
,GQ-I,,Región Insular
,,GQ-AN,Annobón
,,GQ-BN,Bioko Norte
,,GQ-BS,Bioko Sur
ER,,,Eritrea
,ER-AG,,Akele Guzai [Akalä Guzay]
,ER-AS,,Asmara [Asmära]
,ER-BA,,Barka
,ER-DE,,Denkalia [Dänkali]
,ER-GS,,Gash-Setit [Gaš enna Sätit]
,ER-HA,,Hamasien [Hamasén]
,ER-SA,,Sahel
,ER-SM,,Semhar [Sämhar]
,ER-SN,,Senhit [Sänhet]
,ER-SR,,Seraye [Särayé]
EE,,,Estonia
,EE-37,,Harjumaa
,EE-39,,Hiiumaa
,EE-44,,Ida-Virumaa
,EE-49,,Jōgevamaa
,EE-51,,Järvamaa
,EE-57,,Läänemaa
,EE-59,,Lääne-Virumaa
,EE-65,,Pōlvamaa
,EE-67,,Pärnumaa
,EE-70,,Raplamaa
,EE-74,,Saaremaa
,EE-78,,Tartumaa
,EE-82,,Valgamaa
,EE-84,,Viljandimaa
,EE-86,,Vōrumaa
ET,,,Ethiopia
,ET-AA,,Addis Ababa [Addis Abeba]
,ET-AF,,Afar
,ET-AM,,Amara [Amhara]
,ET-BE,,Benshangul-Gumaz [Bénishangul]
,ET-GA,,Gambela Peoples [Gambéla]
,ET-HA,,Harari People [Harer]
,ET-OR,,Oromia [Oromo]
,ET-SO,,Somali
,ET-SN,,"Southern Nations, Nationalities and Peoples"
,ET-TI,,Tigrai [Tegré]
FK,,,Falkland Islands (Malvinas)
,FK-FK,,Falkland Islands (Malvinas)
FO,,,Faroe Islands
,FO-FO,,Faroe Islands
FJ,,,Fiji
,FJ-C,,Central
,FJ-E,,Eastern
,FJ-N,,Northern
,FJ-W,,Western
,FJ-R,,Rotuma
FI,,,Finland
,FI-AL,,Ahvenanmaan lääni
,FI-ES,,Etelä-Suomen lääni
,FI-IS,,Itä-Suomen lääni
,FI-LL,,Lapin lääni
,FI-LS,,Länsi-Suomen lääni
,FI-OL,,Oulun lääni
FR,,,France
,FR-A,,Alsace
,,FR-67,Bas-Rhin
,,FR-68,Haut-Rhin
,FR-B,,Aquitaine
,,FR-79,Deux-Sèvres
,,FR-24,Dordogne
,,FR-33,Gironde
,,FR-40,Landes
,,FR-47,Lot-et-Garonne
,,FR-64,Pyrénées-Atlantiques
,FR-C,,Auvergne
,,FR-03,Allier
,,FR-15,Cantal
,,FR-43,Haute-Loire
,,FR-63,Puy-de-Dôme
,FR-P,,Basse-Normandie
,,FR-14,Calvados
,,FR-50,Manche
,,FR-61,Orne
,FR-D,,Bourgogne
,,FR-21,Côte-d'Or
,,FR-58,Nièvre
,,FR-71,Saône-et-Loire
,,FR-89,Yonne
,FR-E,,Bretagne
,,FR-22,Cotes-d'Armor
,,FR-29,Finistère
,,FR-35,Ille-et-Vilaine
,,FR-56,Morbihan
,FR-F,,Centre
,,FR-18,Cher
,,FR-28,Eure-et-Loir
,,FR-36,Indre
,,FR-37,Indre-et-Loire
,,FR-41,Loir-et-Cher
,,FR-45,Loiret
,FR-G,,Champagne-Ardenne
,,FR-08,Ardennes
,,FR-10,Aube
,,FR-52,Haute-Marne
,,FR-51,Marne
,FR-H,,Corse
,,FR-2A,Corse-du-Sud
,,FR-2B,Haute-Corse
,FR-I,,Franche-Comté
,,FR-25,Doubs
,,FR-70,Haute-Saône
,,FR-39,Jura
,,FR-90,Territoire de Belfort
,FR-Q,,Haute-Normandie
,,FR-27,Eure
,,FR-76,Seine-Maritime
,FR-J,,Île-de-France
,,FR-91,Essonne
,,FR-92,Hauts-de-Seine
,,FR-75,Paris
,,FR-77,Seine-et-Marne
,,FR-93,Seine-Saint-Denis
,,FR-94,Val-de-Marne
,,FR-95,Val-d'Oise
,,FR-78,Yvelines
,FR-K,,Languedoc-Roussillon
,,FR-11,Aude
,,FR-30,Gard
,,FR-34,Hérault
,,FR-48,Lozère
,,FR-66,Pyrénées-Orientales
,FR-L,,Limousin
,,FR-19,Corrèze
,,FR-23,Creuse
,,FR-87,Haute-Vienne
,FR-M,,Lorraine
,,FR-54,Meurthe-et-Moselle
,,FR-55,Meuse
,,FR-57,Moselle
,,FR-88,Vosges
,FR-N,,Midi-Pyrénées
,,FR-09,Ariège
,,FR-12,Aveyron
,,FR-32,Gers
,,FR-31,Haute-Garonne
,,FR-65,Hautes-Pyrénées
,,FR-46,Lot
,,FR-81,Tarn
,,FR-82,Tarn-et-Garonne
,FR-O,,Nord-Pas-de-Calais
,,FR-59,Nord
,,FR-62,Pas-de-Calais
,FR-R,,Pays de la Loire
,,FR-44,Loire-Atlantique
,,FR-49,Maine-et-Loire
,,FR-53,Mayenne
,,FR-72,Sarthe
,,FR-85,Vendée
,FR-S,,Picardie
,,FR-02,Aisne
,,FR-60,Oise
,,FR-80,Somme
,FR-T,,Poitou-Charentes
,,FR-16,Charente
,,FR-17,Charente-Maritime
,,FR-86,Vienne
,FR-U,,Provence-Alpes-Côte d'Azur
,,FR-04,Alpes-de-Haute-Provence
,,FR-06,Alpes-Maritimes
,,FR-13,Bauches-du-Rhône
,,FR-05,Hautes-Alpes
,,FR-83,Var
,,FR-84,Vaucluse
,FR-V,,Rhône-Alpes
,,FR-01,Ain
,,FR-07,Ardèche
,,FR-26,Drôme
,,FR-74,Haute-Savoie
,,FR-38,Isère
,,FR-42,Loire
,,FR-69,Rhône
,,FR-73,Savoie
,FR-GP,,Guadeloupe
,FR-GF,,Guyane (francaise)
,FR-MQ,,Martinique
,FR-RE,,Réunion
,FR-YT,,Mayotte
,FR-PM,,Saint-Pierre-et-Miquelon
,FR-NC,,Nouvelle-Calédonie
,FR-PF,,Polynésie française
,FR-TF,,Terres Australes
,FR-WF,,Wallis et Futuna
GF,,,French Guiana
,GF-GF,,French Guiana
PF,,,French Polynesia
,PF-PF,,French Polynesia
TF,,,French Southern Territories
,TF-TF,,French Southern Territories
GA,,,Gabon
,GA-1,,Estuaire
,GA-2,,Haut-Ogooué
,GA-3,,Moyen-Ogooué
,GA-4,,Ngounié
,GA-5,,Nyanga
,GA-6,,Ogooué-Ivindo
,GA-7,,Ogooué-Lolo
,GA-8,,Ogooué-Maritime
,GA-9,,Woleu-Ntem
GM,,,Gambia
,GM-B,,Banjul
,GM-L,,Lower River
,GM-M,,MacCarthy Island
,GM-N,,North Bank
,GM-U,,Upper River
,GM-W,,Western
GE,,,Georgia
,GE-AB,,Ap'khazet'is Avtonomiuri Respublika [Abkhazia]
,GE-AJ,,Acharis Avtonomiuri Respublika [Ajaria]
,GE-BUS,,Bat'umi
,GE-CHI,,Chiat'ura
,GE-GAG,,Gagra
,GE-GOR,,Gori
,GE-KUT,,K'ut'aisi
,GE-PTI,,P'ot'i
,GE-RUS,,Rust'avi
,GE-SUI,,Sokhumi
,GE-TBS,,T'bilisi
,GE-TQI,,Tqibuli
,GE-TQV,,Tqvarch'eli
,GE-TSQ,,Tsqalmbo
,GE-ZUG,,Zugdidi
,GE-01,,Abashis Raioni
,GE-02,,Adigenis Raioni
,GE-03,,Akhalgoris Raioni
,GE-04,,Akhalk'alak'is Raioni
,GE-05,,Akhalts'ikhis Raioni
,GE-06,,Akhmetis Raioni
,GE-07,,Ambrolauris Raioni
,GE-08,,Aspindzis Raioni
,GE-09,,Baghdat'is Raioni
,GE-10,,Bolnisis Raioni
,GE-11,,Borjomis Raioni
,GE-12,,Ch'khorotsqus Raioni
,GE-13,,Ch'okhatauris Raioni
,GE-14,,Dedop'listsqaros Raioni
,GE-15,,Dmanisis Raioni
,GE-16,,Dushet'is Raioni
,GE-17,,Galis Raioni
,GE-18,,Gardabnis Raioni
,GE-19,,Goris Raioni
,GE-20,,Gudaut'is Raioni
,GE-21,,Gulrip'shis Raioni
,GE-22,,Gurjaanis Raioni
,GE-23,,Javis Raioni
,GE-24,,K'arelis Raioni
,GE-25,,Kaspis Raioni
,GE-26,,K'edis Raioni
,GE-27,,Kharagaulis Raioni
,GE-28,,Khashuris Raioni
,GE-29,,Khelvach'auris Raioni
,GE-30,,Khobis Raioni
,GE-31,,Khonis Raioni
,GE-32,,Khulos Raioni
,GE-33,,K'obuletis Raioni
,GE-34,,Lagodekhis Raioni
,GE-35,,Lanch'khut'is Raioni
,GE-36,,Lentekhis Raioni
,GE-37,,Marneulis Raioni
,GE-38,,Martvilis Raioni
,GE-39,,Mestiis Raioni
,GE-40,,Mts'khet'is Raioni
,GE-41,,Ninotsmindis Raioni
,GE-42,,Och'amch'iris Raioni
,GE-43,,Onis Raioni
,GE-44,,Ozurget'is Raioni
,GE-45,,Qazbegis Raioni
,GE-46,,Qvarlis Raioni
,GE-47,,Sach'kheris Raioni
,GE-48,,Sagarejos Raioni
,GE-49,,Samtrediis Raioni
,GE-50,,Senakis Raioni
,GE-51,,Shuakhevis Raioni
,GE-52,,Sighnaghis Raioni
,GE-53,,Sokhumis Raioni
,GE-54,,T'elavis Raioni
,GE-55,,T'erjolis Raioni
,GE-56,,T'et'ritsqaros Raioni
,GE-57,,T'ianet'is Raioni
,GE-58,,Ts'ageris Raioni
,GE-59,,Tsalenjikhis Raioni
,GE-60,,Tsalkis Raioni
,GE-61,,Vanis Raioni
,GE-62,,Zestap'onis Raioni
,GE-63,,Zugdidis Raioni
DE,,,Germany
,DE-BW,,Baden-Württemberg
,DE-BY,,Bayern
,DE-BE,,Berlin
,DE-BB,,Brandenburg
,DE-HB,,Bremen
,DE-HH,,Hamburg
,DE-HE,,Hessen
,DE-MV,,Mecklenburg-Vorpommern
,DE-NI,,Niedersachsen
,DE-NW,,Nordrhein-Westfalen
,DE-RP,,Rheinland-Pfalz
,DE-SL,,Saarland
,DE-SN,,Sachsen
,DE-ST,,Sachsen-Anhalt
,DE-SH,,Schleswig-Holstein
,DE-TH,,Thüringen
GH,,,Ghana
,GH-AH,,Ashanti
,GH-BA,,Brong-Ahafo
,GH-CP,,Central
,GH-EP,,Eastern
,GH-AA,,Greater Accra
,GH-NP,,Northern
,GH-UE,,Upper East
,GH-UW,,Upper West
,GH-TV,,Volta
,GH-WP,,Western
GI,,,Gibraltar
,GI-GI,,Gibraltar
GB,,,United Kingdom
,GB-CHA,,Channel Islands
,,GB-GSY,Guernsey [Guernesey]
,,GB-JSY,Jersey
,GB-ENG,,England
,,GB-BDG,Barking and Dagenham
,,GB-BNE,Barnet
,,GB-BNS,Barnsley
,,GB-BAS,Bath and North East Somerset
,,GB-BDF,Bedfordshire
,,GB-BEX,Bexley
,,GB-BIR,Birmingham (City of)
,,GB-BBD,Blackburn with Darwen
,,GB-BPL,Blackpool
,,GB-BOL,Bolton
,,GB-BMH,Bournemouth
,,GB-BRC,Bracknell Forest
,,GB-BRD,Bradford (City of)
,,GB-BEN,Brent
,,GB-BNH,Brighton and Hove
,,GB-BST,"Bristol, City of"
,,GB-BRY,Bromley
,,GB-BKM,Buckinghamshire
,,GB-BUR,Bury
,,GB-CLD,Calderdale
,,GB-CAM,Cambridgeshire
,,GB-CMD,Camden
,,GB-CHS,Cheshire
,,GB-CON,Cornwall
,,GB-COV,Coventry (City of)
,,GB-CRY,Croydon
,,GB-CMA,Cumbria
,,GB-DAL,Darlington
,,GB-DER,Derby (City of)
,,GB-DBY,Derbyshire
,,GB-DEV,Devon
,,GB-DNC,Doncaster
,,GB-DOR,Dorset
,,GB-DUD,Dudley
,,GB-DUR,Durharn
,,GB-EAL,Ealing
,,GB-ERY,East Riding of Yorkshire
,,GB-ESX,East Sussex
,,GB-ENF,Enfield
,,GB-ESS,Essex
,,GB-GAT,Gateshead
,,GB-GLS,Gloucestershire
,,GB-GRE,Greenwich
,,GB-HCK,Hackney
,,GB-HAL,Haiton
,,GB-HMF,Hammersmith and Fulham
,,GB-HAM,Hampshire
,,GB-HRY,Haringey
,,GB-HRW,Harrow
,,GB-HPL,Hartlepool
,,GB-HAV,Havering
,,GB-HEF,"Herefordshire, County of"
,,GB-HRT,Hertfordshire
,,GB-HIL,Hillingdon
,,GB-HNS,Hounslow
,,GB-IOW,Isle of Wight
,,GB-IOS,Isles of Scilly
,,GB-ISL,Islington
,,GB-KEC,Kensington and Chelsea
,,GB-KEN,Kent
,,GB-KHL,"Kingston upon Hull, City of"
,,GB-KTT,Kingston upon Thames
,,GB-KIR,Kirklees
,,GB-KWL,Knowsley
,,GB-LBH,Lambeth
,,GB-LAN,Lancashire
,,GB-LDS,Leeds (City of)
,,GB-LCE,Leitester (City of)
,,GB-LEC,Leicestershire
,,GB-LEW,Lewisham
,,GB-LIN,Lincolnshire
,,GB-LIV,Liverpool (City of)
,,GB-LND,"London, City of"
,,GB-LUT,Luton
,,GB-MAN,Manchester (City of)
,,GB-MDW,Medway
,,GB-MRT,Merton
,,GB-MDB,Middlesbrough
,,GB-MIK,Milton Keynes
,,GB-NET,Newcastle upon Tyne (City of)
,,GB-NWM,Newham
,,GB-NFK,Norfolk
,,GB-NEL,North East Lincolnshire
,,GB-NLN,North Lincolnshire
,,GB-NSM,North Somerset
,,GB-NTY,North Tyneside
,,GB-NYK,North Yorkshire
,,GB-NTH,Northamptonshire
,,GB-NBL,Northumberland
,,GB-NGM,Nottingham (City of)
,,GB-NTT,Nottinghamshire
,,GB-OLD,Oldham
,,GB-OXF,Oxfordshire
,,GB-PTE,Peterborough
,,GB-PLY,Plymouth (City of)
,,GB-POL,Poole
,,GB-POR,Portsmouth (City of)
,,GB-RDG,Reading
,,GB-RDB,Redbridge
,,GB-RCC,Redcar and Cleveland
,,GB-RIC,Richmond upon Thames
,,GB-RCH,Rochdale
,,GB-ROT,Rotherharn
,,GB-RUT,Rutland
,,GB-SHN,St. Helens
,,GB-SLF,Salford (City of)
,,GB-SAW,Sandweil
,,GB-SFT,Sefton
,,GB-SHF,Sheffield (City of)
,,GB-SHR,Shropshire
,,GB-SLG,Slough
,,GB-SOL,Solihull
,,GB-SOM,Somerset
,,GB-SGC,South Gloucestershire
,,GB-STY,South Tyneside
,,GB-STH,Southampton (City of)
,,GB-SOS,Southend-on-Sea
,,GB-SWK,Southwark
,,GB-STS,Staffordshire
,,GB-SKP,Stockport
,,GB-STT,Stockton-On-Tees
,,GB-STE,Stoke-on-Trent (City of)
,,GB-SFK,Suffolk
,,GB-SND,Sunderland (City of)
,,GB-SRY,Surrey
,,GB-STN,Sutton
,,GB-SWD,Swindon
,,GB-TAM,Tameside
,,GB-TFW,Telford and Wrekin
,,GB-THR,Thurrock
,,GB-TOB,Torbay
,,GB-TWH,Tower Hamlets
,,GB-TRF,Trafford
,,GB-WKF,Wakefield (City of)
,,GB-WLL,Walsall
,,GB-WFT,Waltham Forest
,,GB-WND,Wandsworth
,,GB-WRT,Warrington
,,GB-WAR,Warwickshire
,,GB-WBK,West Berkshire
,,GB-WSX,West Sussex
,,GB-WSM,Westminster (City of)
,,GB-WGN,Wigan
,,GB-WIL,Wiltshire
,,GB-WNM,Windsor and Maidenhead
,,GB-WRL,Wirral
,,GB-WOK,Wokingham
,,GB-WLV,Wolverhampton
,,GB-WOR,Worcestershire
,,GB-YOR,York (City of)
,GB-IOM,,Isle of Man
,GB-NIR,,Northern Ireland
,,GB-ANT,Antrim
,,GB-ARD,Ards
,,GB-ARM,Armagh
,,GB-BLA,Ballymena
,,GB-BLY,Ballymoney
,,GB-BNB,Banbridge
,,GB-BFS,Belfast (City of)
,,GB-CKF,Carrickfergus
,,GB-CSR,Castlereagh
,,GB-CLR,Coleraine
,,GB-CKT,Cookstown
,,GB-CGV,Craigavon
,,GB-DRY,Derry (City of)
,,GB-DOW,Down
,,GB-DGN,Dungannon
,,GB-FER,Fermanagh
,,GB-LRN,Larne
,,GB-LMV,Limavady
,,GB-LSB,Lisburn
,,GB-MFT,Magherafelt
,,GB-MYL,Moyle
,,GB-NYM,Newry and Mourne
,,GB-NTA,Newtownabbey
,,GB-NDN,North Down
,,GB-OMH,Omagh
,,GB-STB,Strabane
,GB-SCT,,Scotland
,,GB-ABE,Aberdeen City
,,GB-ABD,Aberdeenshire
,,GB-ANS,Angus
,,GB-AGB,Argyll and Bute
,,GB-CLK,Clackmannanshire
,,GB-DGY,Dumfries and Galloway
,,GB-DND,Dundee City
,,GB-EAY,East Ayrshire
,,GB-EDU,East Dunbartonshire
,,GB-ELN,East Lothian
,,GB-ERW,East Renfrewshire
,,GB-EDH,"Edinburgh, City of"
,,GB-ELS,Eilean Siar
,,GB-FAL,Falkirk
,,GB-FIF,Fife
,,GB-GLG,Glasgow City
,,GB-HLD,Highland
,,GB-IVC,Inverclyde
,,GB-MLN,Midlothian
,,GB-MRY,Moray
,,GB-NAY,North Ayrshire
,,GB-NLK,North Lanarkshire
,,GB-ORK,Orkney Islands
,,GB-PKN,Perth and Kinross
,,GB-RFW,Renfrewshire
,,GB-SCB,"Scottish Borders, The"
,,GB-ZET,Shetland Islands
,,GB-SAY,South Ayrshire
,,GB-SLK,South Lanarkshire
,,GB-STG,Stirling
,,GB-WDU,West Dunbartonshire
,,GB-WLN,West Lothian
,GB-WLS,,Wales [Cymru]
,,GB-BGW,Blaenau Gwent
,,GB-BGE,Bridgend [Pen-y-bont ar Ogwr GB-POG]
,,GB-CAY,Caerphilly [Caerffili GB-CAF]
,,GB-CRF,Cardiff (City of) [Caerdydd GB-CRD]
,,GB-CMN,Carmarthenshire [Sir Gaerfyrddin GB-GFY]
,,GB-CGN,Ceredigion [Sir Ceredigion]
,,GB-CWY,Conwy
,,GB-DEN,Denbighshire [Sir Ddinbych GB-DDB]
,,GB-FLN,Flintshire [Sir y Fflint GB-FFL]
,,GB-GWN,Gwynedd
,,GB-AGY,Isle of Anglesey [Sir Ynys Man GB-YNM]
,,GB-MTY,Merthyr Tydfil [Merthyr Tudful GB-MTU]
,,GB-MON,Monmouthshire [Sir Fynwy GB-FYN]
,,GB-NTL,Neath Port Talbot [Castell-nedd Port Talbot GB-CTL]
,,GB-NWP,Newport [Casnewydd GB-CNW]
,,GB-PEM,Pembrokeshire [Sir Benfro CB-BNF]
,,GB-POW,Powys
,,GB-RCT,"Rhondda, Cynon, Taff [Rhondda, Cynon, Taf]"
,,GB-SWA,Swansea (City of) [Abertawe GB-ATA]
,,GB-TOF,Torfaen [Tor-faen]
,,GB-VGL,"Vale of Glamorgan, The [Bro Morgannwg GB-BMG]"
,,GB-WRX,Wrexham [Wrecsam GB-WRC]
GR,,,Greece
,GR-I,,Anatoliki Makedonia kai Thraki
,,GR-52,Drama
,,GR-71,Evros
,,GR-55,Kavalla
,,GR-73,Rodopi
,,GR-72,Xanthi
,GR-IX,,Attiki
,,GR-A1,Attiki
,GR-VII,,Dytiki Ellada
,,GR-13,Achaïa
,,GR-01,Aitolia-Akarnania
,,GR-14,Ileia
,GR-III,,Dytiki Makedonia
,,GR-63,Florina
,,GR-51,Grevena
,,GR-56,Kastoria
,,GR-58,Kozani
,GR-VI,,Ionioi Nisoi
,,GR-23,Kefallinia
,,GR-22,Kerkyra
,,GR-24,Lefkas
,,GR-21,Zakynthos
,GR-IV,,Ipeiros
,,GR-31,Arta
,,GR-33,Ioannina
,,GR-34,Preveza
,,GR-32,Thesprotia
,GR-II,,Kentriki Makedonia
,,GR-64,Chalkidiki
,,GR-53,Imathia
,,GR-57,Kilkis
,,GR-59,Pella
,,GR-61,Pieria
,,GR-62,Serrai
,,GR-54,Thessaloniki
,GR-XIII,,Kriti
,,GR-94,Chania
,,GR-91,Irakleion
,,GR-92,Lasithion
,,GR-93,Rethymnon
,GR-XII,,Notio Aigaio
,,GR-81,Dodekanisos
,,GR-82,Kyklades
,GR-X,,Peloponnisos
,,GR-11,Argolis
,,GR-12,Arkadia
,,GR-15,Korinthia
,,GR-16,Lakonia
,,GR-17,Messinia
,GR-VIII,,Sterea Ellada
,,GR-05,Evrytania
,,GR-04,Evvoia
,,GR-07,Fokis
,,GR-06,Fthiotis
,,GR-03,Voiotia
,GR-V,,Thessalia
,,GR-41,Karditsa
,,GR-42,Larisa
,,GR-43,Magnisia
,,GR-44,Trikala
,GR-XI,,Voreio Aigaio
,,GR-85,Chios
,,GR-83,Lesvos
,,GR-84,Samos
GL,,,Greenland
,GL-GL,,Greenland
GD,,,Grenada
,GD-GD,,Grenada
GP,,,Guadeloupe
,GP-GP,,Guadeloupe
GU,,,Guam
,GU-GU,,Guam
GT,,,Guatemala
,GT-AV,,Alta Verapaz
,GT-BV,,Baja Verapaz
,GT-CM,,Chimaltenango
,GT-CQ,,Chiquimula
,GT-PR,,El Progreso
,GT-ES,,Escuintla
,GT-GU,,Guatemala
,GT-HU,,Huehuetenango
,GT-IZ,,Izabal
,GT-JA,,Jalapa
,GT-JU,,Jutiapa
,GT-PE,,Petén
,GT-QZ,,Quezaltenango
,GT-QC,,Quiché
,GT-RE,,Retalhuleu
,GT-SA,,Sacatepéquez
,GT-SM,,San Marcos
,GT-SR,,Santa Rosa
,GT-SO,,Sololá
,GT-SU,,Suchitepéquez
,GT-TO,,Totonicapán
,GT-ZA,,Zacapa
GN,,,Guinea
,GN-B,,"Bake, Gouvernorat de"
,,GN-BF,Boffa
,,GN-BK,Boké
,,GN-FR,Fria
,,GN-GA,Gaoual
,,GN-KD,Koundara
,GN-C,,"Conakry, Gouvernorat de"
,GN-F,,"Faranah, Gouvernorat de"
,,GN-DB,Dabola
,,GN-DI,Dinguiraye
,,GN-FA,Faranah
,,GN-KS,Kissidougou
,GN-K,,"Kankan, Gouvernorat de"
,,GN-KA,Kankan
,,GN-KE,Kérouané
,,GN-KO,Kouroussa
,,GN-MD,Mandiana
,,GN-SI,Siguiri
,GN-D,,"Kindia, Gouvernorat de"
,,GN-CO,Coyah
,,GN-DU,Dubréka
,,GN-FO,Forécariah
,,GN-KD,Kindia
,,GN-TE,Télimélé
,GN-L,,"Labé, Gouvernorat de"
,,GN-KB,Koubia
,,GN-LA,Labé
,,GN-LE,Lélouma
,,GN-ML,Mali
,,GN-TO,Tougué
,GN-M,,"Mamou, Gouvernorat de"
,,GN-DL,Dalaba
,,GN-MM,Mamou
,,GN-PI,Pita
,GN-N,,"Nzérékoré, Gouvernorat de"
,,GN-BE,Beyla
,,GN-GU,Guékédou
,,GN-LO,Lola
,,GN-MC,Macenta
,,GN-NZ,Nzérékoré
,,GN-YO,Yomou
GW,,,Guinea-Bissau
,GW-BS,,Bissau
,GW-BA,,Bafatá
,GW-BM,,Biombo
,GW-BL,,Bolama
,GW-CA,,Cacheu
,GW-GA,,Gabú
,GW-OI,,Oio
,GW-QU,,Quinara
GY,,,Guyana
,GY-BA,,Barima-Waini
,GY-CU,,Cuyuni-Mazaruni
,GY-DE,,Demerara-Mahaica
,GY-EB,,East Berbice-Corentyne
,GY-ES,,Essequibo Islands-West Demerara
,GY-MA,,Mahaica-Berbice
,GY-PM,,Pomeroon-Supenaam
,GY-PT,,Potaro-Siparuni
,GY-UD,,Upper Demerara-Berbice
,GY-UT,,Upper Takutu-Upper Essequibo
HT,,,Haiti
,HT-AR,,Artibonite
,HT-CE,,Centre
,HT-GA,,Grande-Anse
,HT-ND,,Nord
,HT-NE,,Nord-Est
,HT-NO,,Nord-Ouest
,HT-OU,,Ouest
,HT-SD,,Sud
,HT-SE,,Sud-Est
HM,,,Heard & McDonald Islands
,HM-HM,,Heard & McDonald Islands
VA,,,Vatican City (Holy See)
,VA-VA,,Vatican City (Holy See)
HN,,,Honduras
,HN-AT,,Atlántida
,HN-CL,,Colón
,HN-CM,,Comayagua
,HN-CP,,Copán
,HN-CR,,Cortés
,HN-CH,,Choluteca
,HN-EP,,El Paraíso
,HN-FM,,Francisco Morazán
,HN-GD,,Gracias a Dios
,HN-IN,,Intibucá
,HN-IB,,Islas de la Bahía
,HN-LP,,La Paz
,HN-LE,,Lempira
,HN-OC,,Ocotepeque
,HN-OL,,Olancho
,HN-SB,,Santa Bárbara
,HN-VA,,Valle
,HN-YO,,Yoro
HK,,,Hong Kong
,HK-HK,,Hong Kong
HU,,,Hungary
,HU-BU,,Budapest
,HU-BK,,Bács-Kiskun
,HU-BA,,Baranya
,HU-BE,,Békés
,HU-BZ,,Borsod-Abaúj-Zemplén
,HU-CS,,Csongrád
,HU-FE,,Fejér
,HU-GS,,Gyór-Moson-Sopron
,HU-HB,,Hajdú-Bihar
,HU-HE,,Heves
,HU-JN,,Jasz-Nagykun-Szolnok
,HU-KE,,Komárom-Esztergom
,HU-NO,,Nógrád
,HU-PE,,Pest
,HU-SO,,Somogy
,HU-SZ,,Szabolcs-Szatmár-Bereg
,HU-TO,,Tolna
,HU-VA,,Vas
,HU-VE,,Veszprém
,HU-ZA,,Zala
,HU-BC,,Békéscsaba
,HU-DE,,Debrecen
,HU-DU,,Dunaújváros
,HU-EG,,Eger
,HU-GY,,Gyór
,HU-HV,,Hódmezóvásárhely
,HU-KV,,Kaposvár
,HU-KM,,Kecskemét
,HU-MI,,Miskolc
,HU-NK,,Nagykanizsa
,HU-NY,,Nyíregyháza
,HU-PS,,Pécs
,HU-ST,,Salgótarján
,HU-SN,,Sopron
,HU-SD,,Szeged
,HU-SF,,Székesfehérvár
,HU-SS,,Szekszárd
,HU-SK,,Szolnok
,HU-SH,,Szombathely
,HU-TB,,Tatabánya
,HU-VM,,Veszprém
,HU-ZE,,Zalaegerszeg
IS,,,Iceland
,IS-7,,Austurland
,IS-1,,Höfudborgarsvædi utan Reykjavíkur
,IS-6,,Nordurland eystra
,IS-5,,Nordurland vestra
,IS-0,,Reykjavīk
,IS-8,,Sudurland
,IS-2,,Sudurnes
,IS-4,,Vestfirdir
,IS-3,,Vesturland
IN,,,India
,IN-AP,,Andhra Pradesh
,IN-AR,,Arunachal Pradesh
,IN-AS,,Assam
,IN-BR,,Bihar
,IN-GA,,Goa
,IN-GJ,,Gujarat
,IN-HR,,Haryana
,IN-HP,,Himachal Pradesh
,IN-JK,,Jammu and Kashmir
,IN-KA,,Karnataka
,IN-KL,,Kerala
,IN-MP,,Madhya Pradesh
,IN-MH,,Maharashtra
,IN-MN,,Manipur
,IN-ML,,Meghalaya
,IN-MZ,,Mizoram
,IN-NL,,Nagaland
,IN-OR,,Orissa
,IN-PB,,Punjab
,IN-RJ,,Rajasthan
,IN-SK,,Sikkim
,IN-TN,,Tamil Nadu
,IN-TR,,Tripura
,IN-UP,,Uttar Pradesh
,IN-WB,,West Bengal
,IN-AN,,Andaman and Nicobar Islands
,IN-CH,,Chandigarh
,IN-DN,,Dadra and Nagar Haveli
,IN-DD,,Daman and Diu
,IN-DL,,Delhi
,IN-LD,,Lakshadweep
,IN-PY,,Pondicherry
ID,,,Indonesia
,ID-IJU,,Irian Jaya
,,ID-IJ,Irian Jaya
,ID-JWU,,Jawa
,,ID-JB,Jawa Barat
,,ID-JT,Jawa Tengah
,,ID-JI,Jawa Timur
,,ID-JK,Jakarta Raya
,,ID-YO,Yogyakarta
,ID-KAU,,Kalimantan
,,ID-KB,Kalimantan Barat
,,ID-KS,Kalimantan Selatan
,,ID-KT,Kalimantan Tengah
,,ID-KI,Kalimantan Timur
,ID-MAU,,Maluku
,,ID-MA,Maluku
,ID-NUU,,Nusa Tenggara
,,ID-BA,Bali
,,ID-NB,Nusa Tenggara Barat
,,ID-NT,Nusa Tenggara Timur
,,ID-TT,Timor Timur
,ID-SLU,,Sulawesi
,,ID-SN,Sulawesi Selatan
,,ID-ST,Sulawesi Tengah
,,ID-SG,Sulawesi Tenggara
,,ID-SA,Sulawesi Utara
,ID-SMU,,Sumatera
,,ID-BE,Bengkulu
,,ID-JA,Jambi
,,ID-LA,Lampung
,,ID-RI,Riau
,,ID-SB,Sumatera Barat
,,ID-SS,Sumatera Selatan
,,ID-SU,Sumatera Utara
,,ID-AC,Aceh
IR,,,Iran
,IR-03,,Ardabīl
,IR-02,,Āzarbāyjān-e-Gharbī
,IR-01,,Āzarbāyjān-e-Sharqī
,IR-06,,Būshehr
,IR-08,,Chahār Maḩāll vā Bakhtīārī
,IR-04,,Eşfahān
,IR-14,,Fārs
,IR-19,,Gīlān
,IR-24,,Hamadān
,IR-23,,Hormozgān
,IR-05,,Īlām
,IR-15,,Kermān
,IR-17,,Kermānshāhān
,IR-09,,Khorāsān
,IR-10,,Khūzestān
,IR-18,,Kohkīlūyeh va Būyer Aḩmadī
,IR-16,,Kordestān
,IR-20,,Lorestān
,IR-22,,Markazī
,IR-21,,Māzandarān
,IR-26,,Qom
,IR-12,,Semnān
,IR-13,,Sīstān va Balūchestān
,IR-07,,Tehrān
,IR-25,,Yazd
,IR-11,,Zanjān
IQ,,,Iraq
,IQ-AN,,Al Anbār
,IQ-BA,,Al Başrah
,IQ-MU,,Al Muthanná
,IQ-QA,,Al Qādisīyah
,IQ-NA,,An Najaf
,IQ-AR,,Arbīl
,IQ-SU,,As Sulaymānīyah
,IQ-TS,,At Ta'mīm
,IQ-BB,,Bābil
,IQ-BG,,Baghdād
,IQ-DA,,Dahūk
,IQ-DQ,,Dhī Qār
,IQ-DI,,Diyālá
,IQ-KA,,Karbalā'
,IQ-MA,,Maysān
,IQ-NI,,Nīnawá
,IQ-SD,,Şalāḩ ad Dīn
,IQ-WA,,Wāsiţ
IE,,,Ireland
,IE-CP,,Connaught (Connacht)
,,IE-G,Galway (Gaillimh)
,,IE-LM,Leitrim (Liatroim)
,,IE-MO,Mayo (Maigh Eo)
,,IE-RN,Roscommon (Ros Comáin)
,,IE-SO,Sligo (Sligeach)
,IE-LP,,Leinster (Laighin)
,,IE-CW,Carlow (Ceatharlach)
,,IE-D,Dublin (Baile Átha Cliath)
,,IE-KE,Kildare (Cill Dara)
,,IE-KK,Kilkenny (Cill Chainnigh)
,,IE-LS,Laois (Laois)
,,IE-LD,Longford (An Longfort)
,,IE-LH,Louth (Lú)
,,IE-MH,Meath (An Mhí)
,,IE-OY,Offaly (Uíbh Fhailí)
,,IE-WH,Westmeath (An Iarmhí)
,,IE-WX,Wexford (Loch Garman)
,,IE-WW,Wicklow (Cill Mhantáin)
,IE-M,,Munster (An Mhumhain)
,IE-UP,,Ulster (Ulaidh)
,,IE-CN,Cavan (An Cabhán)
,,IE-DL,Donegal (Dún na nGall)
,,IE-MN,Monaghan (Muineachán)
IL,,,Israel
,IL-D,,HaDarom (El Janūbī)
,IL-M,,HaMerkaz (El Awsat)
,IL-2,,HaZafon (Esh Shamālī)
,IL-HA,,Hefa (Heifā)
,IL-TA,,Tel-Aviv (Tell Abīb)
,IL-JM,,Yerushalayim (Al Quds)
IT,,,Italy
,IT-65,,Abruzzo
,,IT-CH,Chieti
,,IT-AQ,L'Aquila
,,IT-PE,Pescara
,,IT-TE,Teramo
,IT-77,,Basilicata
,,IT-MT,Matera
,,IT-PZ,Potenza
,IT-78,,Calabria
,,IT-CZ,Catanzaro
,,IT-CS,Cosenza
,,IT-KR,Crotone
,,IT-RC,Reggio Calabria
,,IT-W,Vibo Valentia
,IT-72,,Campania
,,IT-AV,Avellino
,,IT-BN,Benevento
,,IT-CE,Caserta
,,IT-NA,Napoli
,,IT-SA,Salerno
,IT-45,,Emilia-Romagna
,,IT-BO,Bologna
,,IT-FE,Ferrara
,,IT-FO,Forlì
,,IT-MO,Modena
,,IT-PR,Parma
,,IT-PC,Piacenza
,,IT-RA,Ravenna
,,IT-RE,Reggio Emilia
,,IT-RN,Rimini
,IT-36,,Friuli-Venezia Giulia
,,IT-GO,Gorizia
,,IT-PN,Pordenone
,,IT-TS,Trieste
,,IT-UD,Udine
,IT-62,,Lazio
,,IT-FR,Frosinone
,,IT-LT,Latina
,,IT-RI,Rieti
,,IT-RM,Roma
,,IT-VT,Viterbo
,IT-42,,Liguria
,,IT-GE,Genova
,,IT-IM,Imperia
,,IT-SP,La Spezia
,,IT-SV,Savona
,IT-25,,Lombardia
,,IT-BG,Bergamo
,,IT-BS,Brescia
,,IT-CO,Como
,,IT-CR,Cremona
,,IT-LC,Lecco
,,IT-LO,Lodi
,,IT-MN,Mantova
,,IT-MI,Milano
,,IT-PV,Pavia
,,IT-SO,Sondrio
,,IT-VA,Varese
,IT-57,,Marche
,,IT-AN,Ancona
,,IT-AP,Ascoli Piceno
,,IT-MC,Macerata
,,IT-PS,Pesaro
,IT-67,,Molise
,,IT-CB,Campobasso
,,IT-IS,Isernia
,IT-21,,Piemonte
,,IT-AL,Alessandria
,,IT-AT,Asti
,,IT-BI,Biella
,,IT-CN,Cuneo
,,IT-NO,Novara
,,IT-TO,Torino
,,IT-VB,Verbano-Cusio-Ossola
,,IT-VC,Vercelli
,IT-75,,Puglia
,,IT-BA,Bari
,,IT-BR,Brindisi
,,IT-FG,Foggia
,,IT-LE,Lecce
,,IT-TA,Taranto
,IT-88,,Sardegna
,,IT-CA,Cagliari
,,IT-NU,Nuoro
,,IT-OR,Oristano
,,IT-SS,Sassari
,IT-82,,Sicilia
,,IT-AG,Agrigento
,,IT-CL,Caltanissetta
,,IT-CT,Catania
,,IT-EN,Enna
,,IT-ME,Mesaina
,,IT-PA,Palermo
,,IT-RG,Ragusa
,,IT-SR,Siracusa
,,IT-TP,Trapani
,IT-52,,Toscana
,,IT-AR,Arezzo
,,IT-FI,Firenze
,,IT-GR,Grosseto
,,IT-LI,Livorno
,,IT-LU,Lucca
,,IT-MS,Massa
,,IT-PI,Pisa
,,IT-PT,Pistoia
,,IT-PO,Prato
,,IT-SI,Siena
,IT-32,,Trentino-Alte Adige (Trentino-Südtirol)
,,IT-BZ,Bolzano (Bozen)
,,IT-TN,Trento
,IT-55,,Umbria
,,IT-PG,Perugia
,,IT-TR,Terni
,IT-23,,Valle d'Aosta (Vallée d'Aoste)
,,IT-AO,Aosta (Aoste)
,IT-34,,Veneto
,,IT-BL,Belluno
,,IT-PD,Padova
,,IT-RO,Rovigo
,,IT-TV,Treviso
,,IT-VE,Venezia
,,IT-VR,Verona
,,IT-VI,Vicenza
JM,,,Jamaica
,JM-13,,Clarendon
,JM-09,,Hanover
,JM-01,,Kingston
,JM-12,,Manchester
,JM-04,,Portland
,JM-02,,Saint Andrew
,JM-06,,Saint Ann
,JM-14,,Saint Catherine
,JM-11,,Saint Elizabeth
,JM-08,,Saint James
,JM-05,,Saint Mary
,JM-03,,Saint Thomas
,JM-07,,Trelawny
,JM-10,,Westmoreland
JP,,,Japan
,JP-23,,Aiti [Aichi]
,JP-05,,Akita
,JP-02,,Aomori
,JP-38,,Ehime
,JP-21,,Gihu [Gifu]
,JP-10,,Gunma
,JP-34,,Hirosima [Hiroshima]
,JP-01,,Hokkaidô [Hokkaido]
,JP-18,,Hukui [Fukui]
,JP-40,,Hukuoka [Fukuoka]
,JP-07,,Hukusima [Fukushima]
,JP-28,,Hyôgo [Hyogo]
,JP-08,,Ibaraki
,JP-17,,Isikawa [Ishikawa]
,JP-03,,Iwate
,JP-37,,Kagawa
,JP-46,,Kagosima [Kagoshima]
,JP-14,,Kanagawa
,JP-39,,Kôti [Kochi]
,JP-43,,Kumamoto
,JP-26,,Kyôto [Kyoto]
,JP-24,,Mie
,JP-04,,Miyagi
,JP-45,,Miyazaki
,JP-20,,Nagano
,JP-42,,Nagasaki
,JP-29,,Nara
,JP-15,,Niigata
,JP-44,,Ôita [Oita]
,JP-33,,Okayama
,JP-47,,Okinawa
,JP-27,,Ôsaka [Osaka]
,JP-41,,Saga
,JP-11,,Saitama
,JP-25,,Siga [Shiga]
,JP-22,,Sizuoka [Shizuoka]
,JP-12,,Tiba [Chiba]
,JP-09,,Totigi [Tochigi]
,JP-36,,Tokusima [Tokushima]
,JP-13,,Tôkyô [Tokyo]
,JP-31,,Tottori
,JP-16,,Toyama
,JP-30,,Wakayama
,JP-06,,Yamagata
,JP-35,,Yamaguti [Yamaguchi]
,JP-19,,Yamanasi [Yamanashi]
JO,,,Jordan
,JO-AJ,,‘Ajlūn
,JO-AQ,,Al 'Aqaba
,JO-BA,,Al Balqā'
,JO-KA,,Al Karak
,JO-MA,,Al Mafraq
,JO-AM,,‘Ammān
,JO-AT,,Aţ Ţafīlah
,JO-AZ,,Az Zarqā'
,JO-IR,,Irbid
,JO-JA,,Jarash
,JO-MN,,Ma‘ān
,JO-MD,,Mādaba
KZ,,,Kazakhstan
,KZ-ALA,,Almaty
,KZ-BAY,,Bayqonyr (Baykonyr)
,KZ-ALM,,Almaty oblysy (Almatinskaya oblast')
,KZ-AKM,,Aqmola oblysy (Akmolinskaya oblast')
,KZ-AKT,,Aqtöbe oblysy (Aktyubinskaya oblast')
,KZ-ATY,,Atyraü oblysy (Atyrauskaya oblast')
,KZ-ZAP,,Batys Kazakstan oblysy (Zapadno-Kazakhstanskaya oblast')
,KZ-MAN,,Mangghystaū oblysy (Mangystauskaya oblast')
,KZ-YUZ,,Ongtüstik Kazakstan oblysy (Yuzhno-Kazakhstanskaya oblast')
,KZ-PAV,,Pavlodar oblysy (Pavlodarskaya oblast')
,KZ-KAR,,Qaraghandy oblysy (Karagandinskaya oblast')
,KZ-KUS,,Qostanay oblysy (Kustanayskaya oblast')
,KZ-KZY,,Qyzylorda oblysy (Kzylordinskaya oblast')
,KZ-VOS,,Shyghys Kazakstan oblysy (Vostochno-Kazakhstanskaya oblast')
,KZ-SEV,,Soltüstik Kazakstan oblysy (Severo-Kazakhstanskaya oblast')
,KZ-ZHA,,Zhambyl oblysy (Zhambylskaya Oblast')
KE,,,Kenya
,KE-110,,Nairobi Municipality
,KE-200,,Central (Kati)
,KE-300,,Coast (Pwani)
,KE-400,,Eastern (Mashariki)
,KE-500,,North-Eastern (Kaskazini Mashariki)
,KE-600,,Nyanza
,KE-700,,Rift Valley
,KE-900,,Western (Magharibi)
KI,,,Kiribati
,KI-G,,Gilbert Islands
,KI-L,,Line Islands
,KI-P,,Phoenix Islands
KP,,,Korea (North)
,KP-KAE,,Kaesong-si
,KP-NAM,,Nampo-si
,KP-PYO,,Pyongyang-si
,KP-CHA,,Chagang-do
,KP-HAB,,Hamgyongbuk-do
,KP-HAN,,Hamgyongnam-do
,KP-HWB,,Hwanghaebuk-do
,KP-HWN,,Hwanghaenam-do
,KP-KAN,,Kangwon-do
,KP-PYB,,Pyonganbuk-do
,KP-PYN,,Pyongannam-do
,KP-YAN,,Yanggang-do
KR,,,Korea (South)
,KR-11,,Seoul Teugbyeolsi [ Seoul-T’ŭkpyŏlshi]
,KR-26,,Busan Gwang'yeogsi [Pusan-Kwangyŏkshi]
,KR-27,,Daegu Gwang'yeogsi [Taegu-Kwangyŏkshi)
,KR-30,,Daejeon Gwang'yeogsi [Taejŏn-Kwangyŏkshi]
,KR-29,,Gwangju Gwang'yeogsi [Kwangju-Kwangyŏkshi]
,KR-28,,Incheon Gwang'yeogsi [Inchŏn-Kwangyŏkshi]
,KR-31,,Ulsan Gwang'yeogsi [Ulsan-Kwangyŏkshi]
,KR-43,,Chungcheongbugdo [Ch'ungch'ŏngbuk-do]
,KR-44,,Chungcheongnamdo [Ch'ungch'ŏngnam-do]
,KR-42,,Gang'weondo [Kang-won-do]
,KR-41,,Gyeonggido [Kyŏnggi-do]
,KR-47,,Gyeongsangbugdo [Kyŏngsangbuk-do]
,KR-48,,Gyeongsangnamdo [Kyŏngsangnam-do]
,KR-49,,Jejudo [Cheju-do]
,KR-45,,Jeonrabugdo [Chŏllabuk-do)
,KR-46,,Jeonranamdo [Chŏllanam-do]
KW,,,Kuwait
,KW-AH,,Al Aḩmadi
,KW-FA,,Al Farwānīyah
,KW-JA,,Al Jahrah
,KW-KU,,Al Kuwayt
,KW-HA,,Ḩawallī
KG,,,Kyrgyzstan
,KG-C,,Chu (Chuyskaya oblast')
,KG-J,,Jalal-Abad (Dzhalal-Abadskaya oblast')
,KG-N,,Naryn (Narynskaya Oblast’)
,KG-O,,Osh (Oshskaya oblast')
,KG-T,,Talas (Talasskaya oblast')
,KG-Y,,Ysyk-Köl (Issyk-Kul'skaya oblast')
LA,,,Laos
,LA-VT,,Vientiane
,LA-AT,,Attapu [Attopeu]
,LA-BK,,Bokèo
,LA-BL,,Bolikhamxai [Borikhane]
,LA-CH,,Champasak [Champassak]
,LA-HO,,Houaphan
,LA-KH,,Khammouan
,LA-LM,,Louang Namtha
,LA-LP,,Louangphabang [Louang Prabang]
,LA-OU,,Oudômxai [Oudomsai]
,LA-PH,,Phôngsali [Phong Saly]
,LA-SL,,Salavan [Saravane]
,LA-SV,,Savannakhét
,LA-VI,,Vientiane
,LA-XA,,Xaignabouli [Sayaboury]
,LA-XE,,Xékong [Sékong]
,LA-XI,,Xiangkhoang [Xieng Khouang]
LV,,,Latvia
,LV-AI,,Aizkraukles Aprinkis
,LV-AL,,Alūksnes Aprinkis
,LV-BL,,Balvu Aprinkis
,LV-BU,,Bauskas Aprinkis
,LV-CE,,Cēsu Aprinkis
,LV-DA,,Daugavpils Aprinkis
,LV-DO,,Dobeles Aprinkis
,LV-GU,,Gulbenes Aprinkis
,LV-JL,,Jelgavas Aprinkis
,LV-JK,,Jēkabpils Aprinkis
,LV-KR,,Krāslavas Aprinkis
,LV-KU,,Kuldīgas Aprinkis
,LV-LM,,Limbažu Aprinkis
,LV-LE,,Liepājas Aprinkis
,LV-LU,,Ludzas Aprinkis
,LV-MA,,Madonas Aprinkis
,LV-OG,,Ogres Aprinkis
,LV-PR,,Preilu Aprinkis
,LV-RE,,Rēzeknes Aprinkis
,LV-RI,,Rīgas Aprinkis
,LV-SA,,Saldus Aprinkis
,LV-TA,,Talsu Aprinkis
,LV-TU,,Tukuma Aprinkis
,LV-VK,,Valkas Aprinkis
,LV-VM,,Valmieras Aprinkis
,LV-VE,,Ventspils Aprinkis
,LV-DGV,,Daugavpils
,LV-JEL,,Jelgava
,LV-JUR,,Jūrmala
,LV-LPX,,Liepāja
,LV-REZ,,Rēzekne
,LV-RIX,,Rīga
,LV-VEN,,Ventspils
LB,,,Lebanon
,LB-BA,,Beiroût (Bayrūt)
,LB-BI,,El Béqaa (Al Biqā')
,LB-JL,,Jabal Loubnâne (Jabal Lubnān)
,LB-AS,,Loubnâne ech Chemâli (Ash Shamāl)
,LB-JA,,Loubnâne ej Jnoûbi (Al Janūb)
,LB-NA,,Nabatîyé (An Nabaţīyah
LS,,,Lesotho
,LS-D,,Berea
,LS-B,,Butha-Buthe
,LS-C,,Leribe
,LS-E,,Mafeteng
,LS-A,,Maseru
,LS-F,,Mohale's Hoek
,LS-J,,Mokhotlong
,LS-H,,Qacha's Nek
,LS-G,,Quthing
,LS-K,,Thaba-Tseka
LR,,,Liberia
,LR-BM,,Bomi
,LR-BG,,Bong
,LR-GB,,Grand Bassa
,LR-CM,,Grand Cape Mount
,LR-GG,,Grand Gedeh
,LR-GK,,Grand Kru
,LR-LO,,Lofa
,LR-MG,,Margibi
,LR-MY,,Maryland
,LR-MO,,Montserrado
,LR-NI,,Nimba
,LR-RI,,Rivercess
,LR-SI,,Sinoe
LY,,,Libya
,LY-BU,,Al Buţnān
,LY-JA,,Al Jabal al Akhḑar
,LY-JG,,Al Jabal al Gharbī
,LY-Ju,,Al Jufrah
,LY-WA,,Al Wāḩah
,LY-Wu,,Al Wusţá
,LY-ZA,,Az Zāwiyah
,LY-BA,,Banghāzī
,LY-FA,,Fazzān
,LY-MI,,Mişrātah
,LY-NA,,Naggaza
,LY-SF,,Sawfajjin
,LY-TB,,Ţarābulus
LI,,,Liechtenstein
,LI-LI,,Liechtenstein
LT,,,Lithuania
,LT-AL,,Alytaus Apskritis
,LT-KU,,Kauno Apskritis
,LT-KL,,Klaipėdos Apskritis
,LT-MR,,Marijampolės Apskritis
,LT-PN,,Panevėžio Apskritis
,LT-SA,,Šiauliu Apskritis
,LT-TA,,Tauragės Apskritis
,LT-TE,,Telšiu Apskritis
,LT-UT,,Utenos Apskritis
,LT-VL,,Vilniaus Apskritis
LU,,,Luxembourg
,LU-D,,Diekirch
,LU-G,,Grevenmacher
,LU-L,,Luxembourg (Luxemburg)
MO,,,Macau
,MO-MO,,Macau
MK,,,Macedonia
,MK-MK,,Macedonia
MG,,,Madagascar
,MG-T,,Antananarivo
,MG-D,,Antsiranana
,MG-F,,Fianarantsoa
,MG-M,,Mahajanga
,MG-A,,Toamasina
,MG-U,,Toliara
MW,,,Malawi
,MW-C,,Central
,,MW-DE,Dedza
,,MW-DO,Dowa
,,MW-KS,Kasungu
,,MW-LI,Lilongwe
,,MW-MC,Mchinji
,,MW-NK,Nkhotakota
,,MW-NU,Ntcheu
,,MW-NI,Ntchisi
,,MW-SA,Salima
,MW-N,,Northern
,,MW-CT,Chitipa
,,MW-KR,Karonga
,,MW-MZ,Mzimba
,,MW-NB,Nkhata Bay
,,MW-RU,Rumphi
,MW-S,,Southern
,,MW-BL,Blantyre
,,MW-CK,Chikwawa
,,MW-CR,Chiradzulu
,,MW-MH,Machinga
,,MW-MG,Mangochi
,,MW-MU,Mulanje
,,MW-MW,Mwanza
,,MW-NS,Nsanje
,,MW-TH,Thyolo
,,MW-ZO,Zomba
MY,,,Malaysia
,MY-W,,Wilayah Persekutuan Kuala Lumpur
,MY-L,,Wilayah Persekutuan Labuan
,MY-J,,Johor
,MY-K,,Kedah
,MY-D,,Kelantan
,MY-M,,Melaka
,MY-N,,Negeri Sembilan
,MY-C,,Pahang
,MY-A,,Perak
,MY-R,,Perlis
,MY-P,,Pulau Pinang
,MY-SA,,Sabah
,MY-SK,,Sarawak
,MY-B,,Selangor
,MY-T,,Terengganu
MV,,,Maldives
,MV-MLE,,Male
,MV-02,,Alif
,MV-20,,Baa
,MV-17,,Dhaalu
,MV-14,,Faafu
,MV-27,,Gaaf Alif
,MV-28,,Gaafu Dhaalu
,MV-29,,Gnaviyani
,MV-07,,Haa Alif
,MV-23,,Haa Dhaalu
,MV-26,,Kaafu
,MV-05,,Laamu
,MV-03,,Lhaviyani
,MV-12,,Meemu
,MV-25,,Noonu
,MV-13,,Raa
,MV-01,,Seenu
,MV-24,,Shaviyani
,MV-08,,Thaa
,MV-04,,Vaavu
ML,,,Mali
,ML-BKO,,Bamako
,ML-7,,Gao
,ML-1,,Kayes
,ML-8,,Kidal
,ML-2,,Koulikoro
,ML-5,,Mopti
,ML-4,,Ségou
,ML-3,,Sikasso
,ML-6,,Tombouctou
MT,,,Malta
,MT-MT,,Malta
MH,,,Marshall Islands
,MH-L,,Ralik chain
,,MH-ALL,Ailinglapalap
,,MH-EBO,Ebon
,,MH-ENI,Eniwetok
,,MH-JAL,Jaluit
,,MH-KIL,Kili
,,MH-KWA,Kwajalein
,,MH-LAE,Lae
,,MH-LIB,Lib
,,MH-NMK,Namorik
,,MH-NMU,Namu
,,MH-RON,Rongelap
,,MH-UJA,Ujae
,,MH-UJL,Ujelang
,,MH-WTH,Wotho
,MH-T,,Ratak chain
,,MH-ALK,Ailuk
,,MH-ARN,Arno
,,MH-AUR,Aur
,,MH-LIK,Likiep
,,MH-MAJ,Majuro
,,MH-MAL,Maloelap
,,MH-MEJ,Mejit
,,MH-MIL,Mili
,,MH-UTI,Utirik
,,MH-WTJ,Wotje
MQ,,,Martinique
,MQ-MQ,,Martinique
MR,,,Mauritania
,MR-NKC,,Nouakchott
,MR-07,,Adrar
,MR-03,,Assaba
,MR-05,,Brakna
,MR-08,,Dakhlet Nouādhibou
,MR-04,,Gorgol
,MR-10,,Guidimaka
,MR-01,,Hodh ech Chargui
,MR-02,,Hodh el Gharbi
,MR-12,,Inchiri
,MR-09,,Tagant
,MR-11,,Tiris Zemmour
,MR-06,,Trarza
MU,,,Mauritius
,MU-BR,,Beau Bassin-Rose Hill
,MU-CU,,Curepipe
,MU-PL,,Port Louis
,MU-QB,,Quatre Bornes
,MU-VP,,Vacoas-Phoenix
,MU-BL,,Black River
,MU-FL,,Flacq
,MU-GP,,Grand Port
,MU-MO,,Moka
,MU-PA,,Pamplemousses
,MU-PW,,Plaines Wilhems
,MU-RR,,Rivière du Rempart
,MU-SA,,Savanne
,MU-AG,,Agalega Islands
,MU-CC,,Cargados Carajos Shoals [Saint Brandon Islands]
,MU-RO,,Rodrigues Island
YT,,,Mayotte
,YT-YT,,Mayotte
MX,,,Mexico
,MX-DIF,,Distrito Federal
,MX-AGU,,Aguascalientes
,MX-BCN,,Baja California
,MX-BCS,,Baja California Sur
,MX-CAM,,Campeche
,MX-COA,,Coahuila
,MX-COL,,Colima
,MX-CHP,,Chiapas
,MX-CHH,,Chihuahua
,MX-DUR,,Durango
,MX-GRO,,Guerrero
,MX-GUA,,Guanajuato
,MX-HID,,Hidalgo
,MX-JAL,,Jalisco
,MX-MEX,,México
,MX-MIC,,Michoacán
,MX-MOR,,Morelos
,MX-NAY,,Nayarit
,MX-NLE,,Nuevo León
,MX-OAX,,Oaxaca
,MX-PUE,,Puebla
,MX-QUE,,Queretaro
,MX-ROO,,Quintana Roo
,MX-SLP,,San Luis Potosí
,MX-SIN,,Sinaloa
,MX-SON,,Sonora
,MX-TAB,,Tabasco
,MX-TAM,,Tamaulipas
,MX-TLA,,Tlaxcala
,MX-VER,,Veracruz
,MX-YUC,,Yucatán
,MX-ZAC,,Zacatecas
FM,,,Micronesia
,FM-TRK,,chuuk
,FM-KSA,,Kosrae
,FM-PNI,,Pohnpei
,FM-YAP,,Yap
MD,,,Moldova
,MD-BAL,,Bălţi
,MD-CAH,,Cahul
,MD-CHI,,Chişinău
,MD-DUB,,Dubăsari
,MD-ORH,,Orhei
,MD-RIB,,Rîbniţa
,MD-SOC,,Soroca
,MD-TIG,,Tighina
,MD-TIR,,Tiraspol
,MD-UNG,,Ungheni
,MD-ANE,,Anenii Noi
,MD-BAS,,Basarabeasca
,MD-BRI,,Brinceni
,MD-CHL,,Cahul
,MD-CAM,,Camenca
,MD-CAN,,Cantemir
,MD-CAI,,Căinari
,MD-CAL,,Călăraşi
,MD-CAS,,Căuşeni
,MD-CIA,,Ciadîr-Lunga
,MD-CIM,,Cimişlia
,MD-COM,,Comrat
,MD-CRI,,Criuleni
,MD-DON,,Donduşeni
,MD-DRO,,Drochia
,MD-DBI,,Dubăsari
,MD-EDI,,Edineţ
,MD-FAL,,Făleşti
,MD-FLO,,Floreşti
,MD-GLO,,Glodeni
,MD-GRI,,Grigoriopol
,MD-HIN,,Hînceşti
,MD-IAL,,Ialoveni
,MD-LEO,,Leova
,MD-NIS,,Nisporeni
,MD-OCN,,Ocniţa
,MD-OHI,,Orhei
,MD-REZ,,Rezina
,MD-RIT,,Rîbniţa
,MD-RIS,,Rîşcani
,MD-SIN,,Sîngerei
,MD-SLO,,Slobozia
,MD-SOA,,Soroca
,MD-STR,,Străşeni
,MD-SOL,,Şoldăneşti
,MD-STE,,Ştefan Vodă
,MD-TAR,,Taraclia
,MD-TEL,,Teleneşti
,MD-UGI,,Ungheni
,MD-VUL,,Vulcăneşti
MC,,,Monaco
,MC-MC,,Monaco
MN,,,Mongolia
,MN-1,,Ulaanbaatar
,MN-073,,Arhangay
,MN-069,,Bayanhongor
,MN-071,,Bayan-Ölgiy
,MN-067,,Bulgan
,MN-037,,Darhan uul
,MN-061,,Dornod
,MN-063,,Dornogovĭ
,MN-059,,Dundgovĭ
,MN-057,,Dzavhan
,MN-065,,Govĭ-Altay
,MN-064,,Govĭ-Sümber
,MN-039,,Hentiy
,MN-043,,Hovd
,MN-041,,Hövsgöl
,MN-053,,Ömnögovĭ
,MN-035,,Orhon
,MN-055,,Övörhangay
,MN-049,,Selenge
,MN-051,,Sühbaatar
,MN-047,,Töv
,MN-046,,Uvs
MS,,,Montserrat
,MS-MS,,Montserrat
MA,,,Morocco
,MA-CE,,Centre
,,MA-AZI,Azilal
,,MA-BEM,Beni Mellal
,,MA-BES,Ben Slimane
,,MA-BOM,Boulemane
,,MA-CAS,Casablanca [Dar el Beïda]
,,MA-JDI,El Jadida
,,MA-KHO,Khouribga
,,MA-SET,Settat
,MA-CN,,Centre-Nord
,,MA-HOC,Al Hoceïma
,,MA-FES,Fès
,,MA-SEF,Sefrou
,,MA-TAO,Taounate
,,MA-TAZ,Taza
,MA-CS,,Centre-Sud
,,MA-HAJ,El Hajeb
,,MA-ERR,Errachidia
,,MA-IFR,Ifrane
,,MA-KHN,Khenifra
,,MA-MEK,Meknès
,MA-ES,,Est
,,MA-BER,Berkane
,,MA-FIG,Figuig
,,MA-IRA,Jrada
,,MA-NAD,Nador
,,MA-OUJ,Oujda
,MA-NO,,Nord-Ouest
,,MA-CHE,Chefchaouene
,,MA-KEN,Kénitra
,,MA-KHE,Khemisset
,,MA-LAR,Larache
,,MA-RBA,Rabat-Salé
,,MA-SIK,Sidi Kacem
,,MA-TNG,Tanger
,,MA-TET,Tétouan
,MA-SU,,Sud
,,MA-AGD,Agadir
,,MA-BAH,Aït Baha
,,MA-MEL,Aït Melloul
,,MA-ASZ,Assa-Zag
,,MA-BOD,Boujdour (EH)
,,MA-ESM,Es Semara (EH)
,,MA-GUE,Guelmim
,,MA-LAA,Laayoune (EH)
,,MA-OUA,Ouarzazate
,,MA-OUD,Oued ed Dahab (EH)
,,MA-TNT,Tan-Tan
,,MA-TAR,Taroudannt
,,MA-TAT,Tata
,,MA-TIZ,Tiznit
,MA-TS,,Tensift
,,MA-HAO,Al Haouz
,,MA-CHI,Chichaoua
,,MA-ESI,Essaouira
,,MA-KES,Kelaat Sraghna
,,MA-MAR,Marrakech
,,MA-SAF,Safi
MZ,,,Mozambique
,MZ-MPM,,Maputo
,MZ-P,,Cabo Delgado
,MZ-G,,Gaza
,MZ-I,,Inhambane
,MZ-B,,Manica
,MZ-L,,Maputo
,MZ-N,,Nampula
,MZ-A,,Niassa
,MZ-S,,Sofala
,MZ-T,,Tete
,MZ-Q,,Zambézia
MM,,,Myanmar
,MM-07,,Ayeyarwady
,MM-02,,Bago
,MM-03,,Magway
,MM-04,,Mandalay
,MM-01,,Sagaing
,MM-05,,Tanintharyi
,MM-06,,Yangon
,MM-14,,Chin
,MM-11,,Kachin
,MM-12,,Kayah
,MM-13,,Kayin
,MM-15,,Mon
,MM-16,,Rakhine
,MM-17,,Shan
NA,,,Namibia
,NA-CA,,Caprivi
,NA-ER,,Erongo
,NA-HA,,Hardap
,NA-KA,,Karas
,NA-KH,,Khomas
,NA-KU,,Kunene
,NA-OW,,Ohangwena
,NA-OK,,Okavango
,NA-OH,,Omaheke
,NA-OS,,Omusati
,NA-ON,,Oshana
,NA-OT,,Oshikoto
,NA-OD,,Otjozondjupa
NR,,,Nauru
,NR-NR,,Nauru
NP,,,Nepal
,NP-1,,Madhyamanchal
,,NP-BA,Bagmati
,,NP-JA,Janakpur
,,NP-NA,Narayani
,NP-2,,Madhya Pashchimanchal
,,NP-BH,Bheri
,,NP-KA,Karnali
,,NP-RA,Rapti
,NP-3,,Pashchimanchal
,,NP-DH,Dhawalagiri
,,NP-GA,Gandaki
,,NP-LU,Lumbini
,NP-4,,Purwanchal
,,NP-KO,Kosi [Koshi]
,,NP-ME,Mechi
,,NP-SA,Sagarmatha
,NP-5,,Sudur Pashchimanchal
,,NP-MA,Mahakali
,,NP-SE,Seti
NL,,,Netherlands
,NL-DR,,Drenthe
,NL-FL,,Flevoland
,NL-FR,,Friesland
,NL-GE,,Gelderland
,NL-GR,,Groningen
,NL-LI,,Limburg
,NL-NB,,Noord-Brabant
,NL-NH,,Noord-Holland
,NL-OV,,Overijssel
,NL-UT,,Utrecht
,NL-ZE,,Zeeland
,NL-ZH,,Zuid-Holland
AN,,,Netherlands Antilles
,AN-AN,,Netherlands Antilles
NC,,,New Caledonia
,NC-NC,,New Caledonia
NZ,,,New Zealand
,NZ-N,,North Island
,,NZ-AUK,Auckland
,,NZ-BOP,Bay of Plenty
,,NZ-GIS,Gisborne
,,NZ-HKB,Hawkes's Bay
,,NZ-MWT,Manawatu-Wanganui
,,NZ-NTL,Northland
,,NZ-TKI,Taranaki
,,NZ-WKO,Waikato
,,NZ-WGN,Wellington
,NZ-S,,South Island
,,NZ-CAN,Canterbury
,,NZ-MBH,Marlborough
,,NZ-NSN,Nelson
,,NZ-OTA,Otago
,,NZ-STL,Southland
,,NZ-TAS,Tasman
,,NZ-WTC,West Coast
NI,,,Nicaragua
,NI-BO,,Boaco
,NI-CA,,Carazo
,NI-CI,,Chinandega
,NI-CO,,Chontales
,NI-ES,,Estelí
,NI-GR,,Granada
,NI-JI,,Jinotega
,NI-LE,,León
,NI-MD,,Madriz
,NI-MN,,Manaqua
,NI-MS,,Masaya
,NI-MT,,Matagalpa
,NI-NS,,Nueva Segovia
,NI-SJ,,Río San Juan
,NI-RI,,Rivas
,NI-ZE,,Zelaya
NE,,,Niger
,NE-8,,Niamey
,NE-1,,Agadez
,NE-2,,Diffa
,NE-3,,Dosso
,NE-4,,Maradi
,NE-5,,Tahoua
,NE-6,,Tillaberi
,NE-7,,Zinder
NG,,,Nigeria
,NG-FC,,Abuja Capital Territory
,NG-AB,,Abia
,NG-AD,,Adamawa
,NG-AK,,Akwa Ibom
,NG-AN,,Anambra
,NG-BA,,Bauchi
,NG-BE,,Benue
,NG-BO,,Borno
,NG-CR,,Cross River
,NG-DE,,Delta
,NG-ED,,Edo
,NG-EN,,Enugu
,NG-IM,,Imo
,NG-JI,,Jigawa
,NG-KD,,Kaduna
,NG-KN,,Kano
,NG-KT,,Katsina
,NG-KE,,Kebbi
,NG-KO,,Kogi
,NG-KW,,Kwara
,NG-LA,,Lagos
,NG-NI,,Niger
,NG-OG,,Ogun
,NG-ON,,Ondo
,NG-OS,,Osun
,NG-OY,,Oyo
,NG-PL,,Plateau
,NG-RI,,Rivers
,NG-SO,,Sokoto
,NG-TA,,Taraba
,NG-YO,,Yobe
NU,,,Niue
,NU-NU,,Niue
NF,,,Norfolk Island
,NF-NF,,Norfolk Island
MP,,,Northern Mariana Islands
,MP-MP,,Northern Mariana Islands
NO,,,Norway
,NO-02,,Akershus
,NO-09,,Aust-Agder
,NO-06,,Buskerud
,NO-20,,Finnmark
,NO-04,,Hedmark
,NO-12,,Hordaland
,NO-15,,Møre og Romsdal
,NO-18,,Nordland
,NO-17,,Nord-Trøndelag
,NO-05,,Oppland
,NO-03,,Oslo
,NO-11,,Rogaland
,NO-14,,Sogn og Fjordane
,NO-16,,Sør-Trøndelag
,NO-08,,Telemark
,NO-19,,Troms
,NO-10,,Vest-Agder
,NO-07,,Vestfold
,NO-01,,Østfold
,NO-22,,Jan Mayen (Arctic Region)
,NO-21,,Svalbard (Arctic Region)
OM,,,Oman
,OM-DA,,Ad Dākhilīyah
,OM-BA,,Al Bāţinah
,OM-JA,,Al Janūbīyah [Zufār]
,OM-WU,,Al Wusţā
,OM-SH,,Ash Sharqīyah
,OM-ZA,,Az Zāhirah
,OM-MA,,Masqaţ
,OM-MU,,Musandam
PK,,,Pakistan
,PK-IS,,Islamabad
,PK-BA,,Baluchistan (Balochistān)
,PK-NW,,North-West Frontier
,PK-PB,,Punjab
,PK-SD,,Sind (Sindh)
,PK-TA,,Federally Administered Tribal Areas
,PK-JK,,Azad Kashmir
,PK-NA,,Northern Areas
PW,,,Palau
,PW-PW,,Palau
PA,,,Panama
,PA-1,,Botas del Toro
,PA-2,,Coclé
,PA-3,,Colón
,PA-4,,Chiriquī
,PA-5,,Darién
,PA-6,,Herrera
,PA-7,,Los Santos
,PA-8,,Panamá
,PA-9,,Veraguas
,PA-0,,Comarca de San Blas
PG,,,Papua New Guinea
,PG-NCD,,National Capital District (Port Moresby)
,PG-CPM,,Central
,PG-CPK,,Chimbu
,PG-EHG,,Eastern Highlands
,PG-EBR,,East New Britain
,PG-ESW,,East Sepik
,PG-EPW,,Enga
,PG-GPK,,Gulf
,PG-MPM,,Madang
,PG-MRL,,Manus
,PG-MBA,,Milne Bay
,PG-MPL,,Morobe
,PG-NIK,,New Ireland
,PG-NPP,,Northern
,PG-NSA,,North Solomons
,PG-SAN,,Sandaun [West Sepik]
,PG-SHM,,Southern Highlands
,PG-WPD,,Western
,PG-WHM,,Western Highlands
,PG-WBK,,West New Britain
PY,,,Paraguay
,PY-ASU,,Asunción
,PY-16,,Alto Paraguay
,PY-10,,Alto Parang
,PY-13,,Amambay
,PY-19,,Boquerón
,PY-5,,Caaguazú
,PY-6,,Caazapá
,PY-14,,Canindeyú
,PY-11,,Central
,PY-1,,Concepción
,PY-3,,Cordillera
,PY-4,,Guairá
,PY-7,,Itapúa
,PY-8,,Misiones
,PY-12,,Neembucú
,PY-9,,Paraguarī
,PY-15,,Presidente Hayes
,PY-2,,San Pedro
PE,,,Peru
,PE-CAL,,El Callao
,PE-AMA,,Amazonas
,PE-ANC,,Ancash
,PE-APU,,Apurímac
,PE-ARE,,Arequipa
,PE-AYA,,Ayacucho
,PE-CAJ,,Cajamarca
,PE-CUS,,Cuzco [Cusco]
,PE-HUV,,Huancavelica
,PE-HUC,,Huánuco
,PE-ICA,,Ica
,PE-JUN,,Junín
,PE-LAL,,La Libertad
,PE-LAM,,Lambayeque
,PE-LIM,,Lima
,PE-LOR,,Loreto
,PE-MDD,,Madre de Dios
,PE-MOQ,,Moquegua
,PE-PAS,,Pasco
,PE-PIU,,Piura
,PE-PUN,,Puno
,PE-SAM,,San Martín
,PE-TAC,,Tacna
,PE-TUM,,Tumbes
,PE-UCA,,Ucayali
PH,,,Philippines
,PH-PH,,Philippines
PN,,,Pitcairn
,PN-PN,,Pitcairn
PL,,,Poland
,PL-BP,,Biała Podlaska
,PL-BK,,Białystok
,PL-BB,,Bielsko
,PL-BY,,Bydgoszcz
,PL-CH,,Chełm
,PL-CI,,Ciechanów
,PL-CZ,,Czestochowa
,PL-EL,,Elblag
,PL-GD,,Gdańsk
,PL-GO,,Gorzów
,PL-JG,,Jelenia Gera
,PL-KL,,Kalisz
,PL-KA,,Katowice
,PL-KI,,Kielce
,PL-KN,,Konin
,PL-KO,,Koszalin
,PL-KR,,Kraków
,PL-KS,,Krosno
,PL-LG,,Legnica
,PL-LE,,Leszno
,PL-LU,,Lublin
,PL-LO,,Łomia
,PL-LD,,Łódź
,PL-NS,,Nowy Sacz
,PL-OL,,Olsztyn
,PL-OP,,Opole
,PL-OS,,Ostrołeka
,PL-PI,,Piła
,PL-PT,,Piotrków
,PL-PL,,Płock
,PL-PO,,Poznań
,PL-PR,,Przemyśl
,PL-RA,,Radom
,PL-RZ,,Rzeszów
,PL-SE,,Siedlce
,PL-SI,,Sieradz
,PL-SK,,Skierniewice
,PL-SL,,Słupsk
,PL-SU,,Suwałki
,PL-SZ,,Szczecin
,PL-TG,,Tarnobrzeg
,PL-TA,,Tarnów
,PL-TO,,Toruń
,PL-WB,,Wałbrzych
,PL-WA,,Warszawa
,PL-WL,,Włocławek
,PL-WR,,Wrocław
,PL-ZA,,Zamość
,PL-ZG,,Zielona Góra
PT,,,Portugal
,PT-01,,Aveiro
,PT-02,,Beja
,PT-03,,Braga
,PT-04,,Bragança
,PT-05,,Castelo Branco
,PT-06,,Coimbra
,PT-07,,Évora
,PT-08,,Faro
,PT-09,,Guarda
,PT-10,,Leiria
,PT-11,,Lisboa
,PT-12,,Portalegre
,PT-13,,Porto
,PT-14,,Santarém
,PT-15,,Setúbal
,PT-16,,Viana do Castelo
,PT-17,,Vila Real
,PT-18,,Viseu
,PT-20,,Regiāo Autónoma dos Açores
,PT-30,,Regiāo Autónoma da Madeira
PR,,,Puerto Rico
,PR-PR,,Puerto Rico
QA,,,Qatar
,QA-DA,,Ad Dawḩah
,QA-GH,,Al Ghuwayrīyah
,QA-JU,,Al Jumaylīyah
,QA-KH,,Al Khawr
,QA-WA,,Al Wakrah
,QA-RA,,Ar Rayyān
,QA-JB,,Jarīyān al Bāţnah
,QA-MS,,Madīnat ash Shamāl
,QA-US,,Umm Şalāl
RE,,,Reunion
,RE-RE,,Reunion
RO,,,Romania
,RO-B,,Bucureşti
,RO-AB,,Alba
,RO-AR,,Arad
,RO-AG,,Argeş
,RO-BC,,Bacău
,RO-BH,,Bihor
,RO-BN,,Bistriţa-Năsăud
,RO-BT,,Botoşani
,RO-BV,,Braşov
,RO-BR,,Brăila
,RO-BZ,,Buzău
,RO-CS,,Caraş-Severin
,RO-CL,,Călăraşi
,RO-CJ,,Cluj
,RO-CT,,Constanţa
,RO-CV,,Covasna
,RO-DB,,Dâmboviţa
,RO-DJ,,Dolj
,RO-GL,,Galaţi
,RO-GR,,Giurgiu
,RO-GJ,,Gorj
,RO-HR,,Harghita
,RO-HD,,Hunedoara
,RO-IL,,Ialomiţa
,RO-IS,,Iaşi
,RO-MM,,Maramureş
,RO-MH,,Mehedinţi
,RO-MS,,Mureş
,RO-NT,,Neamţ
,RO-OT,,Olt
,RO-PH,,Prahova
,RO-SM,,Satu Mare
,RO-SJ,,Sălaj
,RO-SB,,Sibiu
,RO-SV,,Suceava
,RO-TR,,Teleorman
,RO-TM,,Timiş
,RO-TL,,Tulcea
,RO-VS,,Vaslui
,RO-VL,,Vâlcea
,RO-VN,,Vrancea
RU,,,Russian Federation
,RU-AD,,"Adygeya, Respublika"
,RU-AL,,"Altay, Respublika"
,RU-BA,,"Bashkortostan, Respublika"
,RU-BU,,"Buryatiya, Respublika"
,RU-CE,,Chechenskaya Respublika
,RU-CU,,Chuvashskaya Respublika
,RU-DA,,"Dagestan, Respublika"
,RU-IN,,Ingushskaya Respublika
,RU-KB,,Kabardino-Balkarskaya Respublika
,RU-KL,,"Kalmykiya, Respublika"
,RU-KC,,Karachayevo-Cherkesskaya Respublika
,RU-KR,,"Kareliya, Respublika"
,RU-KK,,"Khakasiya, Respublika"
,RU-KO,,"Komi, Respublika"
,RU-ME,,"Mariy El, Respublika"
,RU-MO,,"Mordoviya, Respublika"
,RU-SA,,"Sakha, Respublika [Yakutiya]"
,RU-SE,,"Severnaya Osetiya, Respublika [Alaniya]"
,RU-TA,,"Tatarstan, Respublika"
,RU-TY,,"Tyva, Respublika [Tuva]"
,RU-UD,,Udmurtskaya Respublika
,RU-ALT,,Altayskiy kray
,RU-KHA,,Khabarovskiy kray
,RU-KDA,,Krasnodarskiy kray
,RU-KYA,,Krasnoyarskiy kray
,RU-PRI,,Primorskiy kray
,RU-STA,,Stavropol 'skiy kray
,RU-AMU,,Amurskaya Oblast'
,RU-ARK,,Arkhangel'skaya Oblast'
,RU-AST,,Astrakhanskaya Oblast'
,RU-BEL,,Belgorodskaya Oblast'
,RU-BRY,,Bryanskaya Oblast'
,RU-CHE,,Chelyabinskaya Oblast'
,RU-CHI,,Chitinskaya Oblast'
,RU-IRK,,Irkutskaya Oblast'
,RU-IVA,,Ivanovskaya Oblast'
,RU-KGD,,Kaliningradskaya Oblast'
,RU-KLU,,Kaluzhskaya Oblast'
,RU-KAM,,Kamchatskaya Oblast'
,RU-KEM,,Kemerovskaya Oblast'
,RU-KIR,,Kirovskaya Oblast'
,RU-KOS,,Kostromskaya Oblast'
,RU-KGN,,Kurganskaya Oblast'
,RU-KRS,,Kurskaya Oblast'
,RU-LEN,,Leningradskaya Oblast'
,RU-LIP,,Lipetskaya Oblast'
,RU-MAG,,Magadanskaya Oblast'
,RU-MOS,,Moskovskaya Oblast'
,RU-MUR,,Murmanskaya Oblast'
,RU-NIZ,,Nizhegorodskaya Oblast'
,RU-NGR,,Novgorodskaya Oblast'
,RU-NVS,,Novosibirskaya Oblast'
,RU-OMS,,Omskaya Oblast'
,RU-ORE,,Orenburgskaya Oblast'
,RU-ORL,,Orlovskaya Oblast'
,RU-PNZ,,Penzenskaya Oblast'
,RU-PER,,Permskaya Oblast'
,RU-PSK,,Pskovskaya Oblast'
,RU-ROS,,Rostovskaya Oblast'
,RU-RYA,,Ryazanskaya Oblast'
,RU-SAK,,Sakhalinskaya Oblast'
,RU-SAM,,Samarskaya Oblast’
,RU-SAR,,Saratovskaya Oblast'
,RU-SMO,,Smolenskaya Oblast'
,RU-SVE,,Sverdlovskaya Oblast'
,RU-TAM,,Tambovskaya Oblast'
,RU-TOM,,Tomskaya Oblast’
,RU-TUL,,Tul'skaya Oblast'
,RU-TVE,,Tverskaya Oblast'
,RU-TYU,,Tyumenskaya Oblast'
,RU-ULY,,Ul'yanovskaya Oblast'
,RU-VLA,,Vladimirskaya Oblast'
,RU-VGG,,Volgogradskaya Oblast'
,RU-VLG,,Vologodskaya Oblast'
,RU-VOR,,Voronezhskaya Oblast'
,RU-YAR,,Yaroslavskaya Oblast'
,RU-MOW,,Moskva
,RU-SPE,,Sankt-Peterburg
,RU-YEV,,Yevreyskaya avtonomnaya oblast'
,RU-AGB,,Aginskiy Buryatskiy avtonomnyy okrug
,RU-CHU,,Chukotskiy avtonomnyy okrug
,RU-EVE,,Evenkiyskiy avtonomnyy okrug
,RU-KHM,,Khanty-Mansiyskiy avtonomnyy okrug
,RU-KOP,,Komi-Permyatskiy avtonomnyy okrug
,RU-KOR,,Koryakskiy avtonomnyy okrug
,RU-NEN,,Nenetskiy avtonomnyy okrug
,RU-TAY,,Taymyrskiy (Dolgano-Nenetskiy) avtonomnyy okrug
,RU-UOB,,Ust’-Ordynskiy Buryatskiy avtonomnyy okrug
,RU-YAN,,Yamalo-Nenetskiy avtonomnyy okrug
RW,,,Rwanda
,RW-C,,Butare
,RW-I,,Byumba
,RW-E,,Cyangugu
,RW-D,,Gikongoro
,RW-G,,Gisenyi
,RW-B,,Gitarama
,RW-J,,Kibungo
,RW-F,,Kibuye
,RW-K,,Kigali-Rural (Kigali y’ Icyaro)
,RW-L,,Kigali-Ville (Kilgali Ngari)
,RW-M,,Mutara
,RW-H,,Ruhengeri
SH,,,St. Helena
,SH-SH,,Saint Helena
,SH-AC,,Ascension
,SH-TA,,Tristan da Cunha
KN,,,Saint Kitts & Nevis
,KN-KN,,Saint Kitts & Nevis
LC,,,Saint Lucia
,LC-LC,,Saint Lucia
PM,,,St. Pierre & Miquelon
,PM-PM,,St. Pierre & Miquelon
VC,,,St. Vincent & the Grenadines
,VC-VC,,St. Vincent & the Grenadines
WS,,,Samoa
,WS-AA,,A'ana
,WS-AL,,Aiga-i-le-Tai
,WS-AT,,Atua
,WS-FA,,Fa'asaleleaga
,WS-GE,,Gaga'emauga
,WS-GI,,Gagaifomauga
,WS-PA,,Palauli
,WS-SA,,Satupa'itea
,WS-TU,,Tuamasaga
,WS-VF,,Va'a-o-Fonoti
,WS-VS,,Vaisigano
SM,,,San Marino
,SM-SM,,San Marino
ST,,,Sao Tome & Principe
,ST-P,,Príncipe
,ST-S,,Sāo Tomé
SA,,,Saudi Arabia
,SA-11,,Al Bāḩah
,SA-08,,Al Ḩudūd ash Shamālīyah
,SA-12,,Al Jawf
,SA-03,,Al Madīnah
,SA-05,,Al Qaşim
,SA-O1,,Ar Riyāḑ
,SA-04,,Ash Sharqīyah
,SA-14,,‘Asīr
,SA-06,,Ḩā'il
,SA-09,,Jīzān
,SA-02,,Makkah
,SA-10,,Najrān
,SA-07,,Tabūk
SN,,,Senegal
,SN-DK,,Dakar
,SN-DB,,Diourbel
,SN-FK,,Fatick
,SN-KL,,Kaolack
,SN-KD,,Kolda
,SN-LG,,Louga
,SN-SL,,Saint-Louis
,SN-TC,,Tambacounda
,SN-TH,,Thiès
,SN-ZG,,Ziguinchor
SC,,,Seychelles
,SC-SC,,Seychelles
SL,,,Sierra Leone
,SL-W,,Western Area (Freetown)
,SL-E,,Eastern
,SL-N,,Northern
,SL-S,,Southern
SG,,,Singapore
,SG-SG,,Singapore
SK,,,Slovak Republic
,SK-BC,,Banskobystrický kraj
,SK-BL,,Bratislavský kraj
,SK-KI,,Košický kraj
,SK-NI,,Nitriansky kraj
,SK-PV,,Prešovský kraj
,SK-TC,,Trenčiansky kraj
,SK-TA,,Trnavský kraj
,SK-ZI,,Žilinský kraj
SI,,,Slovenia
,SI-07,,Dolenjska
,SI-09,,Gorenjska
,SI-11,,Goriška
,SI-03,,Koroška
,SI-10,,Notranjsko-kraška
,SI-12,,Obalno-kraška
,SI-08,,Osrednjeslovenska
,SI-02,,Podravska
,SI-01,,Pomurska
,SI-04,,Savinjska
,SI-06,,Spodnjeposavska
,SI-05,,Zasavska
SB,,,Solomon Islands
,SB-CT,,Capital Territory (Honiara)
,SB-CE,,Central
,SB-GU,,Guadalcanal
,SB-IS,,Isabel
,SB-MK,,Makira
,SB-ML,,Malaita
,SB-TE,,Temotu
,SB-WE,,Western
SO,,,Somalia
,SO-AW,,Awdal
,SO-BK,,Bakool
,SO-BN,,Banaadir
,SO-BR,,Bari
,SO-BY,,BaY
,SO-GA,,Galguduud
,SO-GE,,Gedo
,SO-HI,,Hiiraan
,SO-JD,,Jubbada Dhexe
,SO-JH,,Jubbada Hoose
,SO-MU,,Mudug
,SO-NU,,Nugaal
,SO-SA,,Sanaag
,SO-SD,,Shabeellaha Dhexe
,SO-SH,,Shabeellaha Hoose
,SO-SO,,Sool
,SO-TO,,Togdheer
,SO-WO,,Woqooyi Galbeed
ZA,,,South Africa
,ZA-EC,,Eastern Cape (Oos-Kaap)
,ZA-FS,,Free State (Vrystaat)
,ZA-GT,,Gauteng
,ZA-NL,,Kwazulu-Natal
,ZA-MP,,Mpumalanga
,ZA-NC,,Northern Cape (Noord-Kaap)
,ZA-NP,,Northern Province (Noordelike Provinsie)
,ZA-NW,,North-West (Noord-Wes)
,ZA-WC,,Western Cape (Wes-Kaap)
GS,,,S.Georgia & S.Sandwich Islands
,GS-GS,,S.Georgia & S.Sandwich Islands
ES,,,Spain
,ES-AN,,Andalucía
,,ES-AL,Almería
,,ES-CA,Cádiz
,,ES-CO,Córdoba
,,ES-GR,Granada
,,ES-H,Huelva
,,ES-J,Jaén
,,ES-MA,Málaga
,,ES-SE,Sevilla
,ES-AR,,Aragón
,,ES-HU,Huesca
,,ES-TE,Teruel
,,ES-Z,Zaragoza
,ES-O,,"Asturias, Principado de"
,,ES-O,Asturias
,ES-CN,,Canarias
,,ES-GC,Las Palmas
,,ES-TF,Santa Cruz De Tenerife
,ES-S,,Cantabria
,,ES-S,Cantabria
,ES-CM,,Castilla-La Mancha
,,ES-AB,Albacete
,,ES-CR,Ciudad Real
,,ES-CU,Cuenca
,,ES-GU,Guadalajara
,,ES-TO,Toledo
,ES-CL,,Castilla y León
,,ES-AV,Ávila
,,ES-BU,Burgos
,,ES-LE,León
,,ES-P,Palencia
,,ES-SA,Salamanca
,,ES-SG,Segovia
,,ES-SO,Soria
,,ES-VA,Valladolid
,,ES-ZA,Zamora
,ES-CT,,Cataluña
,,ES-B,Barcelona
,,ES-GE,Gerona
,,ES-L,Lérida
,,ES-T,Tarragona
,ES-EX,,Extremadura
,,ES-BA,Badajoz
,,ES-CC,Cáceres
,ES-GA,,Galicia
,,ES-C,La Coruña
,,ES-LU,Lugo
,,ES-OR,Orense
,,ES-PO,Pontevedra
,ES-PM,,Islas Baleares
,,ES-PM,Baleares
,ES-LO,,La Rioja
,,ES-LO,La Rioja
,ES-M,,"Madrid, Comunidad de"
,,ES-M,Madrid
,ES-MU,,"Murcia, Región de"
,,ES-MU,Murcia
,ES-NA,,"Navarra, Comunidad Foral de"
,,ES-NA,Navarra
,ES-PV,,País Vasco
,,ES-VI,Álava
,,ES-SS,Guipúzcoa
,,ES-BI,Vizcaya
,ES-VC,,"Valenciana, Comunidad"
,,ES-A,Alicante
,,ES-CS,Castellón
,,ES-V,Valencia
LK,,,Sri Lanka
,LK-1,,Basnahira Palata (Western Province)
,,LK-11,Colombo
,,LK-12,Gampaha
,,LK-13,Kalutara
,LK-3,,Dakunu Palata (Southern Province)
,,LK-31,Galle
,,LK-33,Hambantota
,,LK-32,Matara
,LK-2,,Madhyama Palata (Central Province)
,,LK-21,Kandy
,,LK-22,Matale
,,LK-23,Nuwara Eliya
,LK-5,,Negenahira Palata (Eastern Province)
,,LK-52,Arnpara
,,LK-51,Batticaloa
,,LK-53,Trincomalee
,LK-9,,Sabaragamuwa Palata
,,LK-92,Kegalla
,,LK-91,Ratnapura
,LK-7,,Uturumeda Palata (North Central Province)
,,LK-71,Anuradhapura
,,LK-72,Polonnaruwa
,LK-4,,Uturu Palata (Northern Province)
,,LK-41,Jaffna
,,LK-42,Kilinochchi
,,LK-43,Mannar
,,LK-45,Mullaittivu
,,LK-44,Vavuniya
,LK-8,,Uva Palata
,,LK-81,Badulla
,,LK-82,Monaragala
,LK-6,,Wayamba Palata (North Western Province)
,,LK-61,Kurunegala
,,LK-62,Puttalam
SD,,,Sudan
,SD-23,,A‘ālī an Nīl
,SD-26,,Al Baḩr al Aḩmar
,SD-18,,Al Buḩayrāt
,SD-07,,Al Jazīrah
,SD-03,,Al Kharţūm
,SD-06,,Al Qaḑārif
,SD-22,,Al Waḩdah
,SD-04,,An Nīl
,SD-08,,An Nīl al Abyaḑ
,SD-24,,An Nīl al Azraq
,SD-01,,Ash Shamālīyah
,SD-17,,Baḩr al Jabal
,SD-16,,Gharb al Istiwā'īyah
,SD-14,,Gharb Baḩr al Ghazāl
,SD-12,,Gharb Dārfūr
,SD-10,,Gharb Kurdufān
,SD-11,,Janūb Dārfūr
,SD-13,,Janūb Kurdufān
,SD-20,,Jūnqalī
,SD-05,,Kassalā
,SD-15,,Shamāl Baḩr al Ghazāl
,SD-02,,Shamāl Dārfūr
,SD-09,,Shamāl Kurdufān
,SD-19,,Sharq al Istiwā'iyah
,SD-25,,Sinnār
,SD-21,,Wārāb
SR,,,Suriname
,SR-BR,,Brokopondo
,SR-CM,,Commewijne
,SR-CR,,Coronie
,SR-MA,,Marowijne
,SR-NI,,Nickerie
,SR-PR,,Para
,SR-PM,,Paramaribo
,SR-SA,,Saramacca
,SR-SI,,Sipaliwini
,SR-WA,,Wanica
SJ,,,Svalbard & Jan Mayen Islands
,SJ-SJ,,Svalbard & Jan Mayen Islands
SZ,,,Swaziland
,SZ-HH,,Hhohho
,SZ-LU,,Lubombo
,SZ-MA,,Manzini
,SZ-SH,,Shiselweni
SE,,,Sweden
,SE-K,,Blekinge län
,SE-W,,Dalarnas län
,SE-I,,Gotlands län
,SE-X,,Gävleborgs län
,SE-N,,Hallands län
,SE-Z,,Jämtlands län
,SE-F,,Jönköpings län
,SE-H,,Kalmar län
,SE-G,,Kronobergs län
,SE-BD,,Norrbottens län
,SE-M,,Skåne län
,SE-AB,,Stockholms län
,SE-D,,Södermanlands län
,SE-C,,Uppsala län
,SE-S,,Värmlands län
,SE-AC,,Västerbottens län
,SE-Y,,Västernorrlands län
,SE-U,,Västmanlands län
,SE-O,,Västra Götalands län
,SE-T,,Örebro län
,SE-E,,Östergötlands län
CH,,,Switzerland
,CH-AG,,Aargau
,CH-AR,,Appenzell Ausser-Rhoden
,CH-AI,,Appenzell Inner-Rhoden
,CH-BL,,Basel-Landschaft
,CH-BS,,Basel-Stadt
,CH-BE,,Bern
,CH-FR,,Freiburg
,CH-GE,,Geneve
,CH-GL,,Glarus
,CH-GR,,Graubünden
,CH-JU,,Jura
,CH-LU,,Luzern
,CH-NE,,Neuchatel
,CH-NW,,Nidwalden
,CH-OW,,Obwalden
,CH-SG,,Sankt Gallen
,CH-SH,,Schaffhausen
,CH-SZ,,Schwyz
,CH-SO,,Solothurn
,CH-TG,,Thurgau
,CH-TI,,Ticino
,CH-UR,,Uri
,CH-VS,,Wallis
,CH-VD,,Vaud
,CH-ZG,,Zug
,CH-ZH,,Zürich
SY,,,Syria
,SY-HA,,Al Ḩasakah
,SY-LA,,Al Lādhiqīyah
,SY-QU,,Al Qunayţirah
,SY-RA,,Ar Raqqah
,SY-SU,,As Suwaydā'
,SY-DR,,Dar’ā
,SY-DY,,Dayr az Zawr
,SY-DI,,Dimashq
,SY-HL,,Ḩalab
,SY-HM,,Ḩamāh
,SY-HI,,Ḩimş
,SY-ID,,Idlib
,SY-RD,,Rīf Dimashq
,SY-TA,,Ţarţūs
TW,,,Taiwan
,TW-KHH,,Kaohsiung
,TW-TPE,,Taipei
,TW-CYI,,Chiayi
,TW-HSZ,,Hsinchu
,TW-KEE,,Keelung
,TW-TXG,,Taichung
,TW-TNN,,Tainan
,TW-CHA,,Changhua
,TW-HUA,,Hualien
,TW-ILA,,Ilan
,TW-MIA,,Miaoli
,TW-NAN,,Nantou
,TW-PEN,,Penghu
,TW-PIF,,Pingtung
,TW-TTT,,Taitung
,TW-TAO,,Taoyuan
,TW-YUN,,Yunlin
TJ,,,Tajikistan
,TJ-KR,,Karategin
,TJ-KT,,Khatlon
,TJ-LN,,Leninabad
,TJ-GB,,Gorno-Badakhshan
TZ,,,Tanzania
,TZ-01,,Arusha
,TZ-02,,Dar-es-Salaam
,TZ-03,,Dodoma
,TZ-04,,Iringa
,TZ-05,,Kagera
,TZ-06,,Kaskazini Pemba (Pemba North)
,TZ-07,,Kaskazini Unguja (Zanzibar North)
,TZ-08,,Kigoma
,TZ-09,,Kilimanjaro
,TZ-10,,Kusini Pemba (Pemba South)
,TZ-11,,Kusini Unguja (Zanzibar South)
,TZ-12,,Lindi
,TZ-13,,Mara
,TZ-14,,Mbeya
,TZ-15,,Mjini Magharibi (Zanzibar West)
,TZ-16,,Morogoro
,TZ-17,,Mtwara
,TZ-18,,Mwanza
,TZ-19,,Pwani (Coast)
,TZ-20,,Rukwa
,TZ-21,,Ruvuma
,TZ-22,,Shinyanga
,TZ-23,,Singida
,TZ-24,,Tabora
,TZ-25,,Tanga
TH,,,Thailand
,TH-10,,Krung Thep Maha Nakhon [Bangkok]
,TH-S,,Phatthaya
,TH-37,,Amnat Charoen
,TH-15,,Ang Thong
,TH-31,,Buri Ram
,TH-24,,Chachoengsao
,TH-18,,Chai Nat
,TH-36,,Chaiyaphum
,TH-22,,Chanthaburi
,TH-50,,Chiang Mai
,TH-57,,Chiang Rai
,TH-20,,Chon Buri
,TH-86,,Chumphon
,TH-46,,Kalasin
,TH-62,,Kamphaeng Phet
,TH-71,,Kanchanaburi
,TH-40,,Khon Kaen
,TH-81,,Krabi
,TH-52,,Lampang
,TH-51,,Lamphun
,TH-42,,Loei
,TH-16,,Lop Buri
,TH-58,,Mae Hong Son
,TH-44,,Maha Sarakham
,TH-49,,Mukdahan
,TH-26,,Nakhon Nayok
,TH-73,,Nakhon Pathom
,TH-48,,Nakhon Phanom
,TH-30,,Nakhon Ratchasima
,TH-60,,Nakhon Sawan
,TH-80,,Nakhon Si Thammarat
,TH-55,,Nan
,TH-96,,Narathiwat
,TH-39,,Nong Bua Lam Phu
,TH-43,,Nong Khai
,TH-12,,Nonthaburi
,TH-13,,Pathum Thani
,TH-94,,Pattani
,TH-82,,Phangnga
,TH-93,,Phatthalung
,TH-56,,Phayao
,TH-67,,Phetchabun
,TH-76,,Phetchaburi
,TH-66,,Phichit
,TH-65,,Phitsanulok
,TH-54,,Phrae
,TH-14,,Phra Nakhon Si Ayutthaya
,TH-83,,Phuket
,TH-25,,Prachin Buri
,TH-77,,Prachuap Khiri Khan
,TH-85,,Ranong
,TH-70,,Ratchaburi
,TH-21,,Rayong
,TH-45,,Roi Et
,TH-27,,Sa Kaeo
,TH-47,,Sakon Nakhon
,TH-11,,Samut Prakan
,TH-74,,Samut Sakhon
,TH-75,,Samut Songkhram
,TH-19,,Saraburi
,TH-91,,Satun
,TH-17,,Sing Buri
,TH-33,,Si Sa Ket
,TH-90,,Songkhla
,TH-64,,Sukhothai
,TH-72,,Suphan Buri
,TH-84,,Surat Thani
,TH-32,,Surin
,TH-63,,Tak
,TH-92,,Trang
,TH-23,,Trat
,TH-34,,Ubon Ratchathani
,TH-41,,Udon Thani
,TH-61,,Uthai Thani
,TH-53,,Uttaradit
,TH-95,,Yala
,TH-35,,Yasothon
TG,,,Togo
,TG-C,,Centre
,TG-K,,Kara
,TG-M,,Maritime (Région)
,TG-P,,Plateaux
,TG-S,,Savannes
TK,,,Tokelau
,TK-TK,,Tokelau
TO,,,Tonga
,TO-TO,,Tonga
TT,,,Trinidad & Tobago
,TT-CTT,,Couva-Tabaquite-Talparo
,TT-DMN,,Diego Martin
,TT-ETO,,Eastern Tobago
,TT-PED,,Penal-Debe
,TT-PRT,,Princes Town
,TT-RCM,,Rio Claro-Mayaro
,TT-SGE,,Sangre Grande
,TT-SJL,,San Juan-Laventille
,TT-SIP,,Siparia
,TT-TUP,,Tunapuna-Piarco
,TT-WTO,,Western Tobago
,TT-ARI,,Arima
,TT-CHA,,Chaguanas
,TT-PTF,,Point Fortin
,TT-POS,,Port of Spain
,TT-SFO,,San Fernando
TN,,,Tunisia
,TN-31,,Béja
,TN-13,,Ben Arous
,TN-23,,Bizerte
,TN-81,,Gabès
,TN-71,,Gafsa
,TN-32,,Jendouba
,TN-41,,Kairouan
,TN-42,,Kasserine
,TN-73,,Kebili
,TN-12,,L'Ariana
,TN-33,,Le Kef
,TN-53,,Mahdia
,TN-82,,Medenine
,TN-52,,Monastir
,TN-21,,Nabeul
,TN-61,,Sfax
,TN-43,,Sidi Bouzid
,TN-34,,Siliana
,TN-51,,Sousse
,TN-83,,Tataouine
,TN-72,,Tozeur
,TN-11,,Tunis
,TN-22,,Zaghouan
TR,,,Turkey
,TR-01,,Adana
,TR-02,,Adiyaman
,TR-03,,Afyon
,TR-04,,Ağrı
,TR-68,,Aksaray
,TR-05,,Amasya
,TR-06,,Ankara
,TR-07,,Antalya
,TR-75,,Ardahan
,TR-08,,Artvin
,TR-09,,Aydin
,TR-10,,Balıkesir
,TR-74,,Bartın
,TR-72,,Batman
,TR-69,,Bayburt
,TR-11,,Bilecik
,TR-12,,Bingöl
,TR-13,,Bitlis
,TR-14,,Bolu
,TR-15,,Burdur
,TR-16,,Bursa
,TR-17,,Çanakkale
,TR-18,,Çankırı
,TR-19,,Çorum
,TR-20,,Denizli
,TR-21,,Diyarbakır
,TR-22,,Edirne
,TR-23,,Elaziğ
,TR-24,,Erzincan
,TR-25,,Erzurum
,TR-26,,Eskişehir
,TR-27,,Gaziantep
,TR-28,,Giresun
,TR-29,,Gümüşhane
,TR-30,,Hakkari
,TR-31,,Hatay
,TR-76,,Iğdir
,TR-32,,Isparta
,TR-33,,İçel
,TR-34,,İstanbul
,TR-35,,İzmir
,TR-46,,Kahramanmaraş
,TR-78,,Karabük
,TR-70,,Karaman
,TR-36,,Kars
,TR-37,,Kastamonu
,TR-38,,Kayseri
,TR-71,,Kırıkkale
,TR-39,,Kırklareli
,TR-40,,Kırşehir
,TR-79,,Kilis
,TR-41,,Kocaeli
,TR-42,,Konya
,TR-43,,Kütahya
,TR-44,,Malatya
,TR-4S,,Manisa
,TR-47,,Mardin
,TR-48,,Muğla
,TR-49,,Muş
,TR-SO,,Nevşehir
,TR-51,,Niğde
,TR-52,,Ordu
,TR-53,,Rize
,TR-54,,Sakarya
,TR-SS,,Samsun
,TR-56,,Siirt
,TR-57,,Sinop
,TR-S8,,Sivas
,TR-63,,Şanlıurfa
,TR-73,,Şirnak
,TR-59,,Tekirdağ
,TR-60,,Tokat
,TR-61,,Trabzon
,TR-62,,Tunceli
,TR-64,,Uşak
,TR-65,,Van
,TR-77,,Yalova
,TR-66,,Yozgat
,TR-67,,Zonguldak
TM,,,Turkmenistan
,TM-A,,Ahal
,TM-B,,Balkan
,TM-D,,Daşhowuz
,TM-L,,Lebap
,TM-M,,Mary
TC,,,Turks & Caicos Islands
,TC-TC,,Turks & Caicos Islands
TV,,,Tuvalu
,TV-TV,,Tuvalu
UG,,,Uganda
,UG-APA,,Apac
,UG-ARU,,Arua
,UG-BUN,,Bundibugyo
,UG-BUS,,Bushenyi
,UG-GUL,,Gulu
,UG-HOI,,Hoima
,UG-IGA,,Iganga
,UG-JIN,,Jinja
,UG-KBL,,Kabale
,UG-KBR,,Kabarole
,UG-KLG,,Kalangala
,UG-KLA,,Kampala
,UG-KLI,,Kamuli
,UG-KAP,,Kapchorwa
,UG-KAS,,Kasese
,UG-KLE,,Kibaale
,UG-KIB,,Kiboga
,UG-KIS,,Kisoro
,UG-KIT,,Kitgum
,UG-KOT,,Kotido
,UG-KUM,,Kumi
,UG-LIR,,Lira
,UG-LUW,,Luwero
,UG-MSK,,Masaka
,UG-MSI,,Masindi
,UG-MBL,,Mbale
,UG-MBR,,Mbarara
,UG-MOR,,Moroto
,UG-MOY,,Moyo
,UG-MPI,,Mpigi
,UG-MUB,,Mubende
,UG-MUK,,Mukono
,UG-NEB,,Nebbi
,UG-NTU,,Ntungamo
,UG-PAL,,Pallisa
,UG-RAK,,Rakai
,UG-RUK,,Rukungiri
,UG-SOR,,Soroti
,UG-TOR,,Tororo
UA,,,Ukraine
,UA-71,,Cherkas'ka Oblast'
,UA-74,,Chernihivs'ka Oblast'
,UA-77,,Chernivets'ka Oblast'
,UA-12,,Dnipropetrovs'ka Oblast'
,UA-14,,Donets'ka Oblast'
,UA-26,,Ivano-Frankivs'ka Oblast'
,UA-63,,Kharkivs'ka Oblast'
,UA-65,,Khersons'ka Oblast'
,UA-68,,Khmel'nyts'ka Oblast'
,UA-35,,Kirovohrads'ka Oblast'
,UA-32,,Kyïvs'ka Oblast'
,UA-09,,Luhans'ka Oblast'
,UA-46,,L'vivs'ka Oblast'
,UA-48,,Mykolaïvs'ka Oblast'
,UA-51,,Odes'ka Oblast'
,UA-53,,Poltavs'ka Oblast'
,UA-56,,Rivnens'ka Oblast'
,UA-59,,Sums'ka Oblast'
,UA-61,,Ternopil's'ka Oblast'
,UA-05,,Vinnyts'ka Oblast'
,UA-07,,Volyns'ka Oblast'
,UA-21,,Zakarpats'ka Oblast'
,UA-23,,Zaporiz'ka Oblast'
,UA-18,,Zhytomyrs'ka Oblast'
,UA-43,,Respublika Krym
,UA-30,,Kyïv
,UA-40,,Sevastopol'
AE,,,United Arab Emirates
,AE-AZ,,Abū Zaby (Abu Dhabi)
,AE-AJ,,‘Ajmān
,AE-FU,,Al Fujayrah
,AE-SH,,Ash Shāriqah (Sharjah)
,AE-DU,,Dubayy (Dubai)
,AE-RK,,R'as al Khaymah
,AE-UQ,,Umm al Qaywayn
US,,,United States
,US-AL,,Alabama
,US-AK,,Alaska
,US-AZ,,Arizona
,US-AR,,Arkansas
,US-CA,,California
,US-CO,,Colorado
,US-CT,,Connecticut
,US-DE,,Delaware
,US-FL,,Florida
,US-GA,,Georgia
,US-HI,,Hawaii
,US-ID,,Idaho
,US-IL,,Illinois
,US-IN,,Indiana
,US-IA,,Iowa
,US-KS,,Kansas
,US-KY,,Kentucky
,US-LA,,Louisiana
,US-ME,,Maine
,US-MD,,Maryland
,US-MA,,Massachusetts
,US-MI,,Michigan
,US-MN,,Minnesota
,US-MS,,Mississippi
,US-MO,,Missouri
,US-MT,,Montana
,US-NE,,Nebraska
,US-NV,,Nevada
,US-NH,,New Hampshire
,US-NJ,,New Jersey
,US-NM,,New Mexico
,US-NY,,New York
,US-NC,,North Carolina
,US-ND,,North Dakota
,US-OH,,Ohio
,US-OK,,Oklahoma
,US-OR,,Oregon
,US-PA,,Pennsylvania
,US-RI,,Rhode Island
,US-SC,,South Carolina
,US-SD,,South Dakota
,US-TN,,Tennessee
,US-TX,,Texas
,US-UT,,Utah
,US-VT,,Vermont
,US-VA,,Virginia
,US-WA,,Washington
,US-WV,,West Virginia
,US-WI,,Wisconsin
,US-WY,,Wyoming
,US-DC,,District of Columbia
,US-AS,,American Samoa
,US-GU,,Guam
,US-MP,,Northern Mariana Islands
,US-PR,,Puerto Rico
,US-UM,,United States Minor Outlying Islands
,US-VI,,"Virgin Islands, U.S."
UY,,,Uruguay
,UY-AR,,Artigas
,UY-CA,,Canelones
,UY-CL,,Cerro Largo
,UY-CO,,Colonia
,UY-DU,,Durazno
,UY-FS,,Flores
,UY-FD,,Florida
,UY-LA,,Lavalleja
,UY-MA,,Maldonado
,UY-MO,,Montevideo
,UY-PA,,Paysandú
,UY-RN,,Río Negro
,UY-RV,,Rivera
,UY-RO,,Rocha
,UY-SA,,Salto
,UY-SJ,,San José
,UY-SO,,Soriano
,UY-TA,,Tacuarembó
,UY-TT,,Treinta y Tres
UZ,,,Uzbekistan
,UZ-QR,,"Qoraqalpoghiston Respublikasi (Karakalpakstan, Respublika)"
,UZ-AN,,Andijon (Andizhan)
,UZ-BU,,Bukhoro (Bukhara)
,UZ-FA,,Farghona (Fergana)
,UZ-JI,,Jizzakh (Dzhizak)
,UZ-KH,,Khorazm (Khorezm)
,UZ-NG,,Namangan
,UZ-NW,,Nawoiy (Navoi)
,UZ-QA,,Qashqadaryo (Kashkadar'ya)
,UZ-SA,,Samarqand (Samarkand)
,UZ-SI,,Sirdaryo (Syrdar'ya)
,UZ-SU,,Surkhondaryo (Surkhandar'ya)
,UZ-TO,,Toshkent (Tashkent)
VU,,,Vanuatu
,VU-MAP,,Malampa
,VU-PAM,,Pénama
,VU-SAM,,Sanma
,VU-SEE,,Shéfa
,VU-TAE,,Taféa
,VU-TOB,,Torba
VE,,,Venezuela
,VE-A,,Distrito Federal
,VE-B,,Anzoátegui
,VE-C,,Apure
,VE-D,,Aragua
,VE-E,,Barinas
,VE-F,,Bolívar
,VE-G,,Carabobo
,VE-H,,Cojedes
,VE-I,,Falcón
,VE-J,,Guárico
,VE-K,,Lara
,VE-L,,Mérida
,VE-M,,Miranda
,VE-N,,Monagas
,VE-O,,Nueva Esparta
,VE-P,,Portuguesa
,VE-R,,Sucre
,VE-S,,Táchira
,VE-T,,Trujillo
,VE-U,,Yaracuy
,VE-V,,Zulia
,VE-Z,,Amazonas
,VE-Y,,Delta Amacuro
,VE-W,,Dependencias Federales
VN,,,Viet Nam
,VN-44,,An Giang
,VN-53,,Bat Can
,VN-54,,Bat Giang
,VN-55,,Bat Lieu
,VN-56,,Bat Ninh
,VN-43,,Ba Ria - Vung Tau
,VN-50,,Ben Tre
,VN-31,,Binh Dinh
,VN-57,,Binh Duong
,VN-58,,Binh Phuoc
,VN-40,,Binh Thuan
,VN-59,,Ca Mau
,VN-48,,Can Tho
,VN-04,,Cao Bang
,VN-33,,Dac Lac
,VN-60,,"Da Nang, thanh pho"
,VN-39,,Dong Nai
,VN-45,,Dong Thap
,VN-30,,Gia Lai
,VN-03,,Ha Giang
,VN-61,,Hai Duong
,VN-62,,"Hai Phong, thanh pho"
,VN-63,,Ha Nam
,VN-64,,"Ha Noi, thu do"
,VN-15,,Ha Tay
,VN-23,,Ha Tinh
,VN-14,,Hoa Binh
,VN-65,,"Ho Chi Minh, thanh po [Sai Gon]"
,VN-66,,Hung Yen
,VN-34,,Khanh Hoa
,VN-47,,Kien Giang
,VN-28,,Kon Turn
,VN-01,,Lai Chau
,VN-35,,Lam Dong
,VN-09,,Lang Son
,VN-02,,Lao Cai
,VN-41,,Long An
,VN-67,,Nam Dinh
,VN-22,,Nghe An
,VN-18,,Ninh Binh
,VN-36,,Ninh Thuan
,VN-68,,Phu Tho
,VN-32,,Phu Yen
,VN-24,,Quang Ninh
,VN-27,,Quang Nam
,VN-29,,Quang Ngai
,VN-25,,Quang Tri
,VN-52,,Sec Trang
,VN-05,,Son La
,VN-37,,Tay Ninh
,VN-20,,Thai Binh
,VN-69,,Thai Nguyen
,VN-21,,Thanh Hoa
,VN-26,,Thua Thien-Hue
,VN-46,,Tien Giang
,VN-51,,Tra Vinh
,VN-07,,Tuyen Quang
,VN-49,,Vinh Long
,VN-70,,Vinh Yen
,VN-06,,Yen Bai
VG,,,Virgin Islands (British)
,VG-VG,,Virgin Islands (British)
VI,,,Virgin Islands (U.S.)
,VI-VI,,Virgin Islands (U.S.)
WF,,,Wallis & Futuna Islands
,WF-WF,,Wallis & Futuna Islands
EH,,,Western Sahara
,EH-EH,,Western Sahara
YE,,,Yemen
,YE-AB,,Abyān
,YE-AD,,‘Adan
,YE-BA,,Al Bayḑā'
,YE-HU,,Al Ḩudaydah
,YE-JA,,Al Jawf
,YE-MR,,Al Mahrah
,YE-MW,,Al Maḩwit
,YE-DH,,Dhamār
,YE-HD,,Ḩaḑramawt
,YE-HJ,,Ḩajjah
,YE-IB,,Ibb
,YE-LA,,Laḩij
,YE-MA,,Ma'rib
,YE-SD,,Şa'dah
,YE-SN,,Şan‘ā'
,YE-SH,,Shabwah
,YE-TA,,Ta‘izz
YU,,,Yugoslavia
,YU-CG,,Crna Gora
,YU-SR,,Srbija
,YU-KM,,Kosovo-Metohija
,YU-VO,,Vojvodina
ZM,,,Zambia
,ZM-02,,Central
,ZM-08,,Copperbelt
,ZM-03,,Eastern
,ZM-04,,Luapula
,ZM-09,,Lusaka
,ZM-05,,Northern
,ZM-06,,North-Western
,ZM-07,,Southern
,ZM-01,,Western
ZW,,,Zimbabwe
,ZW-BU,,Bulawayo
,ZW-HA,,Harare
,ZW-MA,,Manicaland
,ZW-MC,,Mashonaland Central
,ZW-ME,,Mashonaland East
,ZW-MW,,Mashonaland West
,ZW-MV,,Masvingo
,ZW-MN,,Matabeleland North
,ZW-MS,,Matabeleland South
,ZW-MI,,Midlands"""
