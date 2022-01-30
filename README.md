# steamprojet
# DataEngineeringProject 
# _TOP50 Steam games
_ Notre projet est un site de présentation des jeux du Top 50 de Steam basé sur Flask, Mongo et Scrapy. Nous allons afficher un tableau dynamique des prix sur la page web, où vous pourrez voir le nombre de jeux avec des prix différents en pourcentage du nombre total de jeux. Après cela, nous avons une brève description des trois meilleurs jeux. Comme certains jeux avec DLC sont comptabilisés comme un seul jeu, nous les avons regroupés pour établir le tableau, de sorte que le nombre final de jeux est inférieur à 50 car nous avons supprimé les doublons.Dans ce tableau, vous pouvez voir le nom du jeu, sa date de sortie et son prix.

```
Étapes de la réalisation de notre projet:
1. Explorer les données via un crawler et sauvegarder les données dans un fichier au format json. data5.json
2. Exécutez app.py et ouvrez le site Web par défaut http://10.188.181.59:8050/ pour afficher notre site Web.
  
  
```

## Docker 
## 1 Scrape 
- Nous avons utilisé scrapy pour obtenir des informations sur chacun des jeux qui est meilleur vendu. Tout d'aboard nous avons créé la model de Item qui contient le nom , date de sortie, Photo et Prix. Selon la langue css du site, nous avons trouvé l'endroit où les informations sont stockées. 
- Allez dans le dossier steam``` cd ./steam```
   Et après run```scrapy runspider steam.py -o data5.json``` in bash
   Nous pouvons obtenir les informations.
- Difficultés rencontrées: 
	- Nous avons essayé d'accèder à la page de détails de chaque jeu utilisant pipeline de scrapy pour obtenir les détails, mais rencontré beaucoup de difficile.
	- Pour les jeu qui nécessitent une vérification de l'âge, il est difficile d'accéder à la page de détails du jeu utilisant scrapy. Il a besoin d'un script pour passer la vérification de l'âge, sinon, inaccessible.
	- Il existe des sites qui sont dynamiques. Ils ne chargent qu'une petite quantité de données au début. Il a besoin de selenium pour meilleur scraper.
## 2 Mongo 
- Nous enregistrons les données au format json, nommé "data5.json". - Nous passons les données dans la base de données mongo via le code concernant mongo dans app.py. Le nom de la base de données est "Steamgame" et nous créons une collection appelée "steam". Le port est le 27017 par défaut.

```
client = MongoClient('mongodb://localhost:27017/')  
database = client['steamgame']  
collection = database['steam']
df_json=pd.read_json("data5.json")  
collection.insert_many(df_json.to_dict(orient='records'))
```

## 3 Flask 
Nous utilisons Echarts et bootstrap pour concevoir notre page d'accueil. Les fichiers js et css des deux sont stockés dans le dossier "static"（flasksteam/static）. Le fichier de mise en page de notre site web est "index.html", qui se trouve dans le dossier 

-Vous pouvez run ```python app.py ``` et ouvrir le site  local pour voir le site.


## 4 Docker
- Nous avons essayé de mettre le projet sur le compose de Docker. Mais à cause de code que nous mélangé la partie de Mongo et Flask, il devient trop difficile de le mettre dans un compose. Et pour la partie de Mongo, nous stocké les donnés dans le fiche local. Donc le Mongodb en Docker est toujour "connextion refused". 
- Quand même, nous avons écrit les fichiers Dockerfile et Docker-compose. J'espère vous montrer ce que nous essayons de faire dans cette section. Et nous avons compris c'est une bonne habitude de créer le code dans un formulaire séparé.



"tamplates". 

## Contact 
* **Hao LI** - _student_ -ESIEE Paris，<hao.li@edu.esiee.fr> 
* **Zhenyu ZHU** - _student_ -ESIEE Paris，<zhenyu.zhu@edu.esiee.fr># steamproject
