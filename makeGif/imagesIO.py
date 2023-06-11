import imageio

# path = '/Users/lap15864-local/temp/Autonomous-Car/report/tu/originV2/'
# filenames = ['f190.png', 'f270png']
# with imageio.get_writer('/path/to/movie.gif', mode='I') as writer:
#     for filename in filenames:
#         image = imageio.imread(filename)
#         writer.append_data(image)


path = '/Users/lap15864-local/temp/Autonomous-Car/report/tu/originV2/'
startIndex = 190
endIndex = 300
with imageio.get_writer('/Users/lap15864-local/temp/Hack-Life/outputs/gifs/movie.gif', mode='I') as writer:
    for index in range(startIndex, endIndex + 1):
        filename = path + 'f' + str(index) + '.png'
        image = imageio.imread(filename)
        writer.append_data(image)