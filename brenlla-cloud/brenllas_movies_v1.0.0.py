#!/usr/bin/env python
import os
import ntpath
import glob

#moviesPath = "/mnt/usb1.4TB/YouKnow"
moviesPath = "/mnt/usb1.4TB/Kids"
movieInfo = dict()
movies = list()
#htmlFile = "/mnt/usb1.4TB/Brenllas_Cloud/Brenllas_Movie_Collection2.html"
htmlFile = "/mnt/usb1.4TB/Brenllas_Cloud/Kids_Movie_Collection.html"
#collection = "YouKnow"
collection = "Kids"

def print_css_style(html):
    '''
    Prings the page's CSS style.
    '''
    html.write('    <style>\n\
        body {\n\
            background-image: url("background3.png");\n\
        }\n\
        table.movies {\n\
            margin-left:auto;\n\
            margin-right:auto;\n\
            border-spacing: 20px 50px;\n\
        }\n\
    </style>\n\
    <body>\n')

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
    for name in moviesNames:
        movieInfo['movieName']=name
        movieInfo['videoFile']=name+'.mp4'
        movieInfo['subtitles']=name+'.srt'
        movieInfo['coverPic']=name+'.jpg'
        movies.append(movieInfo.copy())
    return movies

if __name__ == "__main__":
    print "Hello World!"
    directories = get_directories_names(moviesPath)
    print '\n'.join(map(str, directories))
    movies = build_up_movies(directories)
    html = open(htmlFile, 'w')
    html.write('<HTML>\n')
    print_css_style(html)
    #### Loop for the movies
    html.write('    <table class="movies">\n')
    i = 1
    html.write('     <tr>\n')
    for movie in movies:
        html.write('      <td><a href="http://192.168.0.106/'+collection+'/'+movie['movieName']+'/'+movie['videoFile']+'"><img src="../'+collection+'/'+movie['movieName']+'/'+movie['coverPic']+'" style="width:182px;height:268px;">\
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
    html.write('</HTML>')
    html.close()
#    content = os.listdir(moviesPath)
#    print '\n'.join(map(str, content))
#    print "#############################"
#    files = get_files_in_directory(moviesPath)
#    files = get_unique_file_names(files)
#    print '\n'.join(map(str, files))
#    movies = build_up_movies(files)
#    print movies
#    html = open(htmlFile, 'w')
#    html.write('<HTML>\n')
#    #### Loop for the movies
#    html.write('    <table>\n')
#    i = 1
#    html.write('     <tr>\n')
#    for movie in movies:
#        html.write('      <td><a href="file://192.168.0.1/volume1/YouKnow/'+movie['videoFile']+'"><img src="YouKnow/'+movie['coverPic']+'" style="width:182px;height:268px;"></a></td>\n')
#        if i == 10:
#            i = 0
#            html.write('        </tr>\n\
#     <tr>\n')
#        i = i +1
#    html.write('        </tr>\n')
#    html.write('    </table>\n')
#    #### End of loop
#    html.write('</HTML>')
#    html.close()

    exit ()
