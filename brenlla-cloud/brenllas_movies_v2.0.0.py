#!/usr/bin/env python
import os
import ntpath
import glob

#background-image: url("background3.png");
def print_css_style(html):
    '''
    Prints the page's CSS style.
    '''
    html.write('    <style>\n\
        body {\n\
            /*background-image: url("background3.png");*/\n\
            background-color: black;\n\
        }\n\
        table.movies {\n\
            margin-left:auto;\n\
            margin-right:auto;\n\
            border-spacing: 20px 50px;\n\
        }\n\
        div.back_button{\n\
            box-shadow: 10px 10px 5px grey;\n\
        }\n\
    </style>\n\
    <body>\n\
      <a href="Index.html"><div class="button"><img src="back_button.png"></div></a>\n')

def get_unique_file_names(files):
    '''
    Receives a list of files and returns
    a list of unique file names without
    extension.
    ATTENTION: It is assumed that the only '.'
    in the file name is the one for the file extension.
    '''
    onlyFileNames = list()
    uniqueFileNames = list()
    for file in files:
        onlyFileNames.append(ntpath.basename(file).split('.')[0])
    for file in onlyFileNames:
        if file not in uniqueFileNames:
            uniqueFileNames.append(file)
    return uniqueFileNames

def get_files_in_directory(pathToDirectory):
    '''
    Receives a directory path and returns a list with all the files in it.
    '''
    return os.listdir(pathToDirectory)

def get_directories_names(pathToDirectory):
    '''
    Receives a directory path and returns a list with all the
    names of the directories in it.
    '''
    directoriesNames = list()
    for name in os.listdir(pathToDirectory):
        print "DEBUG: File name = %s" % name
        if os.path.isdir(os.path.join(pathToDirectory, name)):
            print "DEBUG: and is a directory."
            directoriesNames.append(name)
        else:
            print "DEBUG: and is a file."
    return directoriesNames

def build_up_movies(moviesNames):
    '''
    Receives a list of movie names and returns
    a list of dicionaries with the movies information.
    '''
    movies = list()
    movieInfo = dict()
    for name in moviesNames:
        movieInfo['movieName']=name
        movieInfo['videoFile']=name+'.mp4'
        movieInfo['subtitles']=name+'.srt'
        movieInfo['coverPic']=name+'.jpg'
        movies.append(movieInfo.copy())
    return movies

#if __name__ == "__main__":
def generate_movies_page(collection):
    '''
    '''
    movies = list()
    moviesPath = "/mnt/usb4TB/"+collection
    htmlFile = "/mnt/usb4TB/Brenllas_Cloud/"+collection+"_Collection.html"

    directories = get_directories_names(moviesPath)
    directories.sort()
    print '\n'.join(map(str, directories))
    movies = build_up_movies(directories)
    html = open(htmlFile, 'w')
    html.write('<html>\n')
    print_css_style(html)
    #### Loop for the movies
    html.write('    <table class="movies">\n')
    i = 1
    html.write('     <tr>\n')
    for movie in movies:
        html.write('      <td><a href="http://192.168.0.106/'+collection+'/'+movie['movieName']+'/'+movie['videoFile']+'"><img src="../'+collection+'/'+movie['movieName']+'/Cover.jpg" style="width:182px;height:268px;">\
</a></td>\n')
        if i == 8:
            i = 0
            html.write('        </tr>\n')
            html.write('        <tr>\n')
        i = i +1
    html.write('        </tr>\n')
    html.write('    </table>\n')
    #### End of loop
    html.write('    </body>\n')
    html.write('</html>')
    html.close()

if __name__ == "__main__":


    collections = ["YouKnow", "Kids", "Movies", "MayraMovies"]

    for collection in collections:
        print "NOTE: Working on collection: %s" % collection
        generate_movies_page(collection)
    exit()
