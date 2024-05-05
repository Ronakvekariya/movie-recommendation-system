from flask import Flask , render_template,request
import pickle

app = Flask(__name__)

movies_dic = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommned' , methods = ['POST'])
def movie_recommned():
    movie_name = request.form.get('movie')

    index = movies_dic['title']
    counter = 0

    for i in index:
        if movie_name.lower() == i.lower():
            break
        else:
            counter = counter + 1
    
    print(similarity[counter])
    distance = sorted(list(enumerate(similarity[counter])),reverse=True,key = lambda x:x[1])[1:6]

    movies = []

    for i in distance:
        movies.append(index[i[0]])



    return render_template("display.html" , result = movies)
    

if __name__ == '__main__':
    app.run(debug=True)