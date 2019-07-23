'''
@Author: Liam Gardner
@Date: 7/23/2019
Holds the generate map function
'''

import noise
import numpy as np

# THRESHOLD = [-0.25, 0, 0.5]
def GenerateMap(size, scale, threshold, octaves, lacunarity, persistence):
    '''
    generates a map based off multilayered open-simplex noise.
    '''
    octaveOffsets = []
    for i in range(octaves):
        octaveOffsets.append([np.random.randint(-10000, 10000), np.random.randint(-10000, 10000)])

    array = []
    for y in range(0, size):
        for x in range(0, size):
            amplitude = 1
            frequency = 1
            noiseValue = 0
            for i in range(octaves):
                sampleX = frequency * (x + octaveOffsets[i][0]) / scale
                sampleY = frequency * (y + octaveOffsets[i][1]) / scale
            
                noiseValue += amplitude * noise.snoise2(sampleX, sampleY)

                amplitude *= persistence
                frequency *= lacunarity

            array.append(noiseValue)

    array = np.reshape(array, (size,size))
    
    #parses array and creates image based off corresponding data
    image = []
    for y in array:
        image.append([])
        for x in y:
            if x < threshold[0]:
                image[-1].append([200,0,0])
            elif threshold[0] < x < threshold[1]:
                image[-1].append([255,0,0])
            elif threshold[1] < x < threshold[2]:
                image[-1].append([0,255,0])
            elif x > threshold[2]:
                image[-1].append([0,200,0])

    image = np.array(image)

    return image
