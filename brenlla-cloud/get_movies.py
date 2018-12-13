#!/usr/bin/env python
import os
import ntpath
import glob

moviesPath = "/mnt/tplink_share/volume1/YouKnow"
movieInfo = dict()
movies = list()
htmlFile = "/mnt/tplink_share/volume1/Brenllas_Movie_Collection.html"

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
    Receives a direcotry path and returns a list with all the files in it.
    '''
    return os.listdir(pathToDirectory)

def build_up_movies(moviesNames):
    '''
    Receives a list of movie names and returns
    a list of dicionaries with the movies information.
    '''
    for name in moviesNames:
        movieInfo['movieName']=name
        movieInfo['videoFile']=name+'.mp4'
        movieInfo['subtitles']=name+'.srt'
        movieInfo['coverPic']=name+'.png'
        movies.append(movieInfo.copy())
    return movies

if __name__ == "__main__":
    print "Hello World!"
    content = os.listdir(moviesPath)
    print '\n'.join(map(str, content))
    print "#############################"
    files = get_files_in_directory(moviesPath)
    files = get_unique_file_names(files)
    print '\n'.join(map(str, files))
    movies = build_up_movies(files)
    print movies
    html = open(htmlFile, 'w')
    html.write('<HTML>\n')
    #### Loop for the movies
    html.write('    <table>\n')
    i = 1
    html.write('     <tr>\n')
    for movie in movies:
        html.write('      <td><a href="file://192.168.0.1/volume1/YouKnow/'+movie['videoFile']+'"><img src="YouKnow/'+movie['coverPic']+'" style="width:182px;height:268px;"></a></td>\n')
        if i == 10:
            i = 0
            html.write('        </tr>\n\
     <tr>\n')
        i = i +1
    html.write('        </tr>\n')
    html.write('    </table>\n')
    #### End of loop
    html.write('</HTML>')
    html.close()

    exit ()
