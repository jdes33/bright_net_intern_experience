# Bright Network Technology Internship Experience
This work is for the Google software development challenge.
The idea of the project is to create a simplified command line version of youtube. I was provided with a bunch of tests and hence worked in a TDD fashion.
I completed the work using Python (version 3) and was able to pass all 71 tests.

# Summary of features
## Part 1
 - display number of videos (already provided by Google)
 - show all videos
 - set a video as being 'played'
 - stop a video
 - play a random video
 - pause a video
 - continue a currently paused video
 - show current video (and information about it: title, tags, id, paused status)

## Part 2
 - create playlists
 - add videos to playlists
 - show all playlists
 - show videos within a playlist
 - remove a video from playlist
 - clear playlist
 - delete playlist

## Part 3
 - search for videos by text (using video titles)
 - search for videos by tag

## Part 4
 - allow users to flag videos with a reason
 - allow users to unflag videos

# Running on your own system (windows)
To run this program clone this repository then navigate to the bright_net_intern_experience\google-code-sample\python directory on the command line and enter the following:
```
python -m src.run
```

To run the tess assuming you have pytest installed, in the same directory type:
```
python -m pytest
```
