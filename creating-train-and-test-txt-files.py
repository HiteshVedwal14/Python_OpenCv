'''

Download labelImg and ffmpeg

labelImg is used to label the images by bounding boxes

(base) C:\Users\HITSEH\AppData\Roaming\Python\Python38\labelImg>pyrcc5 -o libs/resurces.py resources.qrc

(base) C:\Users\HITSEH\AppData\Roaming\Python\Python38\labelImg>python labelImg.py

and ffmpeg is used to split video in pictures by desired frames per second

Anaconda prompt

ffmpeg -i video_name.extension -vf fps=4 image-%d.jpeg

'''




# =============================================================================
# Can be used to create own labelled data
# =============================================================================


# Importing needed library
import os


full_path_to_images = 'D:/Python/Yolo/own dataset/myvideo/labelled-data'

# Changing the current directory
# to one with images
os.chdir(full_path_to_images)

# Defining list to write paths in
p = []

# Using os.walk for going through all directories
for current_dir, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.jpeg'):
            # Preparing path to save into train.txt file
            path_to_save_into_txt_files = full_path_to_images + '/' + f

            # Appending the line into the list
            p.append(path_to_save_into_txt_files + '\n')


# Slicing first 15% of elements from the list
# to write into the test.txt file
p_test = p[:int(len(p) * 0.15)]

# Deleting from initial list first 15% of elements
p = p[int(len(p) * 0.15):]


# Creating file train.txt and writing 85% of lines in it
with open('train.txt', 'w') as train_txt:
    # Going through all elements of the list
    for e in p:
        # Writing current path at the end of the file
        train_txt.write(e)

# Creating file test.txt and writing 15% of lines in it
with open('test.txt', 'w') as test_txt:
    # Going through all elements of the list
    for e in p_test:
        # Writing current path at the end of the file
        test_txt.write(e)

# Defining counter for classes
c = 0

with open(full_path_to_images + '/' + 'classes.names', 'w') as names, \
     open(full_path_to_images + '/' + 'classes.txt', 'r') as txt:

    # Going through all lines in txt file and writing them into names file
    for line in txt:
        names.write(line)  

        # Increasing counter
        c += 1

with open(full_path_to_images + '/' + 'labelled_data.data', 'w') as data:
    
    data.write('classes = ' + str(c) + '\n')

    # Location of the train.txt file
    data.write('train = ' + full_path_to_images + '/' + 'train.txt' + '\n')

    # Location of the test.txt file
    data.write('valid = ' + full_path_to_images + '/' + 'test.txt' + '\n')

    # Location of the classes.names file
    data.write('names = ' + full_path_to_images + '/' + 'classes.names' + '\n')

    # Location where to save weights
    data.write('backup = backup')
