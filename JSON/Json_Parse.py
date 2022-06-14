import json
import webbrowser

file = open ('Pizza.json')
array = json.load(file)

f=open('index.html','w',encoding='utf-16')

message='''<html>
<head>
<title>Pizza</title>
</head>

<body>
<h1>Pizza</h1>
'''
for pizza in array:
    name = pizza["name"]
    message+=f"<h2>Name: {name}</h2>"
    message+=f"<h2>INGREDIENTS</h2>"
    for ingredients in pizza["Ingredients"]:
        message+=f'<li>{ingredients["name"]} {ingredients["count"]} {ingredients["unit"]}</li>'
    message+=f"<h2>PREPARATIONS</h2>"
    for Cooking in pizza["Cooking"]:
        message+=f'<li>{Cooking["Time"]} {Cooking["degree"]} degree in {Cooking["Where"]}</li>'
    message+=f"<h2>HOW TO COOK</h2>"
    for Steps in pizza["steps"]:
        message+=f'<li>{Steps["dscription"]}</li>'

message += """
</body>

</html>"""
f.write(message)
f.close()

webbrowser.open_new_tab('index.html')



Moviee = open ('Movies.json')
Movie_array = json.load(Moviee)

f=open('Movies.html','w',encoding='utf-16')
Movies='''<html>
<head>
<title>Movies</title>
</head>

<body>
<h1>Movies</h1>
'''
for Movie in Movie_array[:10]:
    title = Movie["Title"]
    Movies+=f"<h2>Title: {title}</h2>"
    Year = Movie["Year"]
    Movies+=f"<p>Year: {Year}</p>"
    Rated = Movie["Rated"]
    Movies+=f"<p>Rated: {Rated}</p>"
    img = Movie["Poster"]
    Movies+=f"<img src=\"{img}\">"
    Plot =Movie["Plot"]
    Movies+=f"<p>Plot: {Plot}</p>"
    
    

Movies += """
</body>

</html>"""
f.write(Movies)
f.close()

webbrowser.open_new_tab('Movies.html')

