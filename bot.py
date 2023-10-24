import telebot
import requests
import json

CHAVE_API = "6057730170:AAFuK-3y89sO8WBF1JkPjSoDhQRCFRWyzI0"


bot = telebot.TeleBot(CHAVE_API)

###############################################

@bot.message_handler(commands=["SPAA"])
def SPAA(mensagem):
   texto = """
   https://goo.gl/maps/RbZ42ivdX88fbeDG6
   """
   bot.reply_to(mensagem, texto)

###############################################

@bot.message_handler(commands=["CAICJ"])
def CAICJ(mensagem):
   texto = """
   https://goo.gl/maps/AQEuCBQiPQBpac3BA
   """
   bot.reply_to(mensagem, texto)

###############################################

@bot.message_handler(commands=["CAICD"])

def CAICD(mensagem):
   texto = """
   https://goo.gl/maps/EbqvZHqLAkdas2xR6
   """
   bot.reply_to(mensagem, texto)

###############################################

@bot.message_handler(commands=["CentroOeste"])

def CentroOeste(mensagem):
   texto = """
   /CAICD - Dr. Rubim de Sá
   /CAICJ - José Carlos Mestrinho
   /SPAA - SPA Alvorada
   """
   bot.reply_to(mensagem, texto)

###############################################
@bot.message_handler(commands=["FMT"])

def FMT(mensagem):
   texto = """
   https://goo.gl/maps/V733AVW2FLTDoAzK8
   """
   bot.reply_to(mensagem, texto)

###############################################

@bot.message_handler(commands=["FHEMOAM"])

def FHEMOAM(mensagem):
   texto = """
   https://goo.gl/maps/7PigbJzqLsityTHy6
   """
   bot.reply_to(mensagem, texto)

###############################################

@bot.message_handler(commands=["HPER"])

def HPER(mensagem):
   texto = """
   https://goo.gl/maps/uyQW9D4XhaQYqGUd9
   """
   bot.reply_to(mensagem, texto)

###############################################

@bot.message_handler(commands=["CentroSul"])

def CentroSul(mensagem):
   texto = """
   /HPER - Hospital Psiquiátrico Eduardo Ribeiro
/FHEMOAM - Fundação de Hematologia e Hemoterapia do Amazonas
   /FMT - Fundação de Medicina Tropical
   
   """

   bot.reply_to(mensagem, texto)

###############################################

@bot.message_handler(commands=["CAIMI"])
def CAIMI(mensagem):
   texto = """
   https://goo.gl/maps/dShNggJBWeGBCFpu8
   """
   bot.reply_to(mensagem, texto)

##############################################

@bot.message_handler(commands=["CAIC"])
def CAIC(mensagem):
   texto = """
   https://goo.gl/maps/an8sq1Ci7TmKxW936
   """
   bot.reply_to(mensagem, texto)

##############################################

@bot.message_handler(commands=["CECON"])

def CECON(mensagem):
   texto = """
   
   https://goo.gl/maps/zDE4sqDjUTwdrJxU8

   """
   bot.reply_to(mensagem, texto)

##############################################

@bot.message_handler(commands=["ZonaOeste"])
def ZonaOeste(mensagem):
   texto = """
   /CAIC - Alberto Carreira
/CAIMI - Ada Rodrigues Viana
/CECON - Fundação CECON
   """
   bot.reply_to(mensagem, texto)

##############################################///////

@bot.message_handler(commands=["ICAM"])
def ICAM(mensagem):
   texto = """
   https://goo.gl/maps/F8ZTPpkb6Hi5FKpn9
   """
   bot.reply_to(mensagem, texto)

##############################################
@bot.message_handler(commands=["HUGV"])

def HUGV(mensagem):
   texto = """
   https://goo.gl/maps/uWU99eCCF3q1pTaq7
   """
   bot.reply_to(mensagem, texto)

##############################################

@bot.message_handler(commands=["_28_Agosto"])
def _28_Agosto(mensagem):
   texto = """
   https://goo.gl/maps/XTkn6kXzvpbpVgEb6
   """
   bot.reply_to(mensagem, texto)


##############################################
# Zona Leste describe text for Hospitals in East Zone

@bot.message_handler(commands=["ZonaSul"])
def ZonaSul(mensagem):
   texto = """
   /_28_Agosto - Hospital e Pronto Socorro 28 de Agosto
   /ICAM - Instituto de Saúde da Criança do Amazonas ICAM
   /HUGV - Hospital Getúlio Vargas
   """
   bot.reply_to(mensagem, texto)

##############################################///////////////


@bot.message_handler(commands=["_Joao_Lucio"])
def _Joao_Lucio(mensagem):
   texto = """
   https://goo.gl/maps/8FBniftkmoyrh56L7
   """
   bot.reply_to(mensagem, texto)

##############################################

@bot.message_handler(commands=["Chapot_Prevost"])
def Chapot_Prevost(mensagem):
   texto = """
   https://goo.gl/maps/e5G3rQrQu6cGBnNR8
   """
   bot.reply_to(mensagem, texto)


##############################################

@bot.message_handler(commands=["Platao_Araujo"])
def Platao_Araujo(mensagem):
   texto = """
   https://goo.gl/maps/W2YrAGXMLZYqzQSm6
   """
   bot.reply_to(mensagem, texto)

##############################################
# Zona Leste describe text for Hospitals in East Zone
@bot.message_handler(commands=["ZonaLeste"])
def ZonaLeste(mensagem):
   texto = """
   /Platao_Araujo - Hospital e Pronto Socorro Platão Araújo
   /_Joao_Lucio - Hospital e Pronto Socorro Dr. João Lúcio 
   /Chapot_Prevost - Hospital Chapot Prévost
   """
   bot.reply_to(mensagem, texto)

##############################################
@bot.message_handler(commands=["Danilo_Correa"])

def Danilo_Correa(mensagem):
   texto = """
   https://goo.gl/maps/VamEAN9uupKaQfJz8
   """

   bot.reply_to(mensagem, texto)

##############################################
# Hospital DR

@bot.message_handler(commands=["Delphina_Rinaldi"])

def Delphina_Rinaldi(mensagem):
   texto = """
   https://goo.gl/maps/MUsi5SZDzzYhsVgG9
   """
   
   bot.reply_to(mensagem, texto)

##############################################
# Hospital FM

@bot.message_handler(commands=["Francisca_Mendes"])

def Francisca_Mendes(mensagem):
   texto = """
   https://goo.gl/maps/pmS2RfPcbByjzhiT7
   """
   bot.reply_to(mensagem, texto)

##############################################

@bot.message_handler(commands=["ZonaNorte"])
# Zona Norte describe text for Hospitals in North Zone

def ZonaNorte(mensagem):
   texto = """
   Aqui estão alguns Hospitais da Zona Norte da cidade De Manaus:
   /Delphina_Rinaldi - Hospital Delphina Rinaldi Abdel Aziz
   /Francisca_Mendes - Hospital Universitário Francisca Mendes
   /Danilo_Correa - SPA e Policlínica - Danilo Corrêa
   """
   bot.reply_to(mensagem, texto)
   

######################################
# Comands 1

@bot.message_handler(commands=["opcao1"])

def opcao1(mensagem):
  texto = """
  Você mora em qual zona?
  /ZonaNorte
  /ZonaLeste
  /ZonaSul
  /ZonaOeste
  /CentroOeste
  /CentroSul
  """
  bot.reply_to(mensagem, texto)

######################################

@bot.message_handler(commands=["_10"])

def _10(mensagem):
   texto = """

   Um oftalmologista é um médico especializado no diagnóstico e tratamento de doenças e distúrbios oculares. Eles são treinados para avaliar e tratar uma ampla variedade de condições oftalmológicas, como miopia, astigmatismo, hipermetropia, catarata, glaucoma, degeneração macular e doenças da retina. Os oftalmologistas também tratam lesões oculares, infecções, inflamações e outras condições que afetam a saúde ocular. Eles usam ferramentas e técnicas especializadas para examinar os olhos e prescrevem óculos, lentes de contato ou medicamentos, conforme necessário. Em casos mais graves, eles também realizam cirurgias oculares para corrigir problemas de visão ou tratar doenças oculares.

   """
   bot.reply_to(mensagem, texto) 

######################################

@bot.message_handler(commands=["_9"])

def _9(mensagem):
   texto = """

   Um infectologista é um médico especializado no diagnóstico e tratamento de doenças infecciosas causadas por bactérias, vírus, fungos e outros agentes infecciosos. Eles estudam o modo de transmissão das doenças, o impacto na saúde pública e as medidas de prevenção e controle de infecções. Os infectologistas são responsáveis por tratar uma ampla variedade de doenças infecciosas, incluindo HIV/AIDS, tuberculose, hepatite, meningite, pneumonia, entre outras. Eles trabalham em estreita colaboração com outros profissionais de saúde, como microbiologistas e epidemiologistas, para identificar e controlar surtos de doenças infecciosas e garantir o melhor tratamento possível para os pacientes.


   """
   bot.reply_to(mensagem, texto)  

######################################

@bot.message_handler(commands=["_8"])

def _8(mensagem):
   texto = """

Um cirurgião é um médico especializado em realizar cirurgias para tratar doenças, lesões ou deformidades físicas. Eles são treinados para avaliar e tratar uma ampla variedade de condições médicas, desde procedimentos simples, como remover um cisto ou uma verruga, até procedimentos complexos, como cirurgia cardíaca ou neurocirurgia. Os cirurgiões devem ser habilidosos em técnicas cirúrgicas e ter um profundo conhecimento da anatomia do corpo humano. Eles também devem ter habilidades de comunicação para orientar os pacientes antes e depois da cirurgia, e trabalhar em equipe com outros profissionais de saúde para garantir o melhor resultado possível para o paciente.

   """
   bot.reply_to(mensagem, texto)  


######################################

@bot.message_handler(commands=["_7"])

def _7(mensagem):
   texto = """

   Um pediatra é um médico especializado no cuidado da saúde de crianças, desde o nascimento até a adolescência. Eles são treinados para diagnosticar e tratar uma ampla variedade de problemas de saúde infantil, desde doenças comuns, como resfriados e gripes, até doenças crônicas, como diabetes e asma. Além disso, os pediatras também se concentram no desenvolvimento físico, emocional e comportamental das crianças, e oferecem orientações aos pais e cuidadores sobre cuidados infantis, incluindo nutrição, vacinação e prevenção de lesões.

   """
   bot.reply_to(mensagem, texto)  

######################################

@bot.message_handler(commands=["_6"])

def _6(mensagem):
   texto = """
   Um ortopedista é um médico especializado no diagnóstico e tratamento de lesões e doenças do sistema musculoesquelético, incluindo ossos, músculos, tendões, ligamentos e articulações. Eles são treinados para avaliar e tratar uma ampla variedade de problemas ortopédicos, como fraturas ósseas, luxações articulares, artrite, escoliose e lesões esportivas. Além disso, os ortopedistas podem realizar cirurgias ortopédicas, como a substituição de articulações, reparação de ligamentos rompidos e fusão óssea.
   """
   bot.reply_to(mensagem, texto)  

######################################

@bot.message_handler(commands=["_5"])

def _5(mensagem):
   texto = """
   Um dermatologista é um médico especializado no diagnóstico e tratamento de doenças da pele, cabelos e unhas. Eles são treinados para avaliar e tratar uma ampla variedade de problemas dermatológicos, como acne, psoríase, eczema, rosácea, câncer de pele e infecções fúngicas. Além disso, os dermatologistas podem realizar procedimentos dermatológicos, como biópsias de pele, remoção de verrugas e tratamentos a laser para rejuvenescimento da pele.
   """
   bot.reply_to(mensagem, texto)  

######################################

@bot.message_handler(commands=["_4"])

def _4(mensagem):
   texto = """
Um urologista é um médico especializado no diagnóstico e tratamento de doenças do sistema urinário masculino e feminino, bem como do sistema reprodutivo masculino. Eles são treinados para avaliar e tratar uma ampla variedade de problemas urológicos, como infecções do trato urinário, cálculos renais, incontinência urinária, câncer de próstata e disfunção erétil. Além disso, os urologistas podem realizar cirurgias urológicas, como a remoção de tumores da bexiga e próstata, e a correção de anomalias congênitas.   """
   bot.reply_to(mensagem, texto)  

######################################

@bot.message_handler(commands=["_3"])

def _3(mensagem):
   texto = """
   Um ginecologista é um médico especializado no diagnóstico e tratamento de doenças do sistema reprodutivo feminino, incluindo órgãos genitais internos e externos. Eles são treinados para avaliar e tratar uma ampla variedade de problemas ginecológicos, como infecções, endometriose, miomas uterinos e câncer de colo de útero. Além disso, os ginecologistas podem realizar exames ginecológicos de rotina, prescrever contraceptivos, ajudar em questões de fertilidade e cuidados pré-natais durante a gestação.
   """
   bot.reply_to(mensagem, texto)  

######################################

@bot.message_handler(commands=["_2"])

def _2(mensagem):
   texto = """
   Um cardiologista é um médico especializado no diagnóstico e tratamento de doenças do coração e do sistema cardiovascular. Eles são treinados para avaliar e tratar uma ampla variedade de problemas cardíacos, como arritmias, doenças coronárias, insuficiência cardíaca e doenças das válvulas cardíacas. Além disso, os cardiologistas podem realizar procedimentos diagnósticos e terapêuticos, como eletrocardiogramas, ecocardiogramas e angioplastia coronariana.
   """
   bot.reply_to(mensagem, texto)    
######################################

@bot.message_handler(commands=["_1"])

def _1(mensagem):
  texto = """
  
Um clínico geral é um médico que se especializa em cuidados de saúde abrangentes e não especializados para pacientes de todas as idades, independentemente de gênero ou condição médica específica. Eles são treinados para diagnosticar e tratar uma ampla gama de condições médicas comuns e coordenar o cuidado do paciente com outros especialistas, quando necessário.
  
  """
  bot.reply_to(mensagem, texto)

######################################
# Comands 2

@bot.message_handler(commands=["opcao2"])

def opcao2(mensagem):
  texto = """
  Aqui estão alguns especialistas, cada descrição irá dizer qual
  sera o mais indicado para você (clique para saber os detalhes):
  /_1 Clínico Geral
  /_2 Cardiologista
  /_3 Ginecologista
  /_4 Urologista
  /_5 Dermatologita
  /_6 Ortopedistaa
  /_7 Pediatra
  /_8 Cirurgião
  /_9 Infectologista
  /_10 Oftalmologista
  """
  bot.reply_to(mensagem, texto)

########################################

@bot.message_handler(commands=["MALARIA"])

def MALARIA(mensagem):
   texto = """
A malária é uma doença infecciosa que é transmitida pela picada de mosquitos infectados com parasitas do gênero Plasmodium. Quando esses parasitas entram no corpo humano, eles se multiplicam nos glóbulos vermelhos e causam sintomas como febre, calafrios, fadiga e dor de cabeça. A malária é mais comum em áreas tropicais e subtropicais e pode ser fatal se não tratada adequadamente. A prevenção da malária envolve o uso de medidas de controle de mosquitos, como o uso de mosquiteiros tratados com inseticida, bem como o uso de medicamentos profiláticos e tratamentos antimaláricos.

   """
   bot.reply_to(mensagem, texto)

########################################

@bot.message_handler(commands=["RAIVA"])

def RAIVA(mensagem):
   texto = """
   O vírus da raiva é um vírus transmitido principalmente por mordidas de animais infectados, como cães, gatos, morcegos e outros mamíferos. O vírus ataca o sistema nervoso central e pode levar a sintomas graves, incluindo febre, dor de cabeça, agitação, convulsões e paralisia. Se não tratada rapidamente, a raiva é quase sempre fatal. A prevenção da raiva envolve a vacinação pré-exposição em pessoas com alto risco de exposição ao vírus, como veterinários e trabalhadores da fauna, e a vacinação pós-exposição após a exposição a um animal suspeito de estar infectado. O tratamento imediato após a exposição inclui a limpeza da ferida e a administração da vacina e imunoglobulina antirrábica. A raiva é uma doença grave e é importante tomar medidas para prevenir a exposição ao vírus sempre que possível.
   """
   bot.reply_to(mensagem, texto)

########################################

@bot.message_handler(commands=["CHAGAS"])

def CHAGAS(mensagem):
   texto = """
A doença de Chagas, também conhecida como tripanossomíase americana, é uma doença infecciosa causada pelo parasita Trypanosoma cruzi. A doença é transmitida por insetos conhecidos como triatomíneos ou barbeiros, que vivem em áreas rurais e suburbanas da América Latina. Os sintomas da doença de Chagas variam, mas podem incluir febre, inchaço nos gânglios linfáticos, fadiga, dor de cabeça, vômito e diarreia. Em alguns casos, a doença pode causar danos aos órgãos internos, incluindo o coração e o sistema digestivo, levando a complicações graves e até a morte. A prevenção da doença de Chagas inclui o controle de insetos vetores, bem como a triagem de doadores de sangue e transplante de órgãos para garantir que o parasita não seja transmitido através desses meios. O tratamento da doença de Chagas envolve medicamentos antiparasitários e, em alguns casos, terapias para tratar complicações. A doença de Chagas é um importante problema de saúde pública em muitos países da América Latina e é considerada uma doença negligenciada.
   """
   bot.reply_to(mensagem, texto)

########################################

@bot.message_handler(commands=["DENGUE"])

def DENGUE(mensagem):
   texto = """
   A dengue é uma doença viral transmitida por mosquitos do gênero Aedes, principalmente o Aedes aegypti. Os sintomas incluem febre alta, dor de cabeça, dor atrás dos olhos, dores musculares e nas articulações, erupções cutâneas e náuseas. Em casos graves, a dengue pode levar a complicações potencialmente fatais, como dengue hemorrágica ou síndrome do choque da dengue. A prevenção da dengue envolve medidas de controle de mosquitos, como a eliminação de criadouros de mosquitos e o uso de repelentes. Não há tratamento específico para a dengue, mas a gestão dos sintomas e o tratamento de complicações são importantes. A dengue é comum em áreas tropicais e subtropicais e é um importante problema de saúde pública em muitos países.
   """
   bot.reply_to(mensagem, texto)

########################################

@bot.message_handler(commands=["COVID"])

def COVID(mensagem):
   texto = """
   A COVID-19 é uma doença infecciosa causada pelo coronavírus SARS-CoV-2. Os sintomas incluem febre, tosse, fadiga e falta de ar, e em casos graves, a doença pode levar à hospitalização e até à morte. A COVID-19 se espalha principalmente de pessoa para pessoa através de gotículas respiratórias quando uma pessoa infectada tosse, espirra ou fala. As medidas de prevenção incluem o distanciamento físico, uso de máscaras, lavagem frequente das mãos e vacinação. O tratamento da COVID-19 varia de acordo com a gravidade dos sintomas, mas pode incluir suporte respiratório, medicamentos antivirais e corticosteroides. A pandemia de COVID-19 teve um impacto significativo na saúde pública global, economias e na vida cotidiana das pessoas em todo o mundo.
   """
   bot.reply_to(mensagem, texto)

########################################
@bot.message_handler(commands=["opcao3"])

def opcao3(mensagem):
   texto = """
   Aqui estão algumas doenças:
   /COVID - COVID19
   /DENGUE - Dengue
   /MALARIA - Malária
   /CHAGAS - Doença de Chagas
   /RAIVA - Virús da Raiva
   """
   bot.reply_to(mensagem, texto)

########################################

@bot.message_handler(commands=["opcao4"])

def opcao4(mensagem):
   texto = """
   SAMU - 192
   SIATE- 193
   """
   bot.reply_to(mensagem, texto)

########################################
# Main menu, describe: welcome to bot support
def verificar(mensagem):
    return True

@bot.message_handler(func=verificar) #  Criar um decorator: dar uma nova caracteristica, ou seja executar a função no momento certo

def responder(mensagem): 

  texto = """
  Olá, eu sou suporte médico. Em que posso ajudar? :)
  /opcao1 Hospitais próximos de minha casa.
  /opcao2 Descrever alguns médicos especialista.
  /opcao3 Me fale um pouco sobre algumas doenças.
  /opcao4 Números de Emergências.
  ^^^^Clique nas palavras azuis para escolher as opções
  Responder outra coisa não irá funcionar!!!
  
  """
  bot.reply_to(mensagem, texto)


bot.polling()

