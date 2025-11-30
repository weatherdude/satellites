import cv2
from satellites_api import above,sat_position
from PIL import Image
from PIL import ImageDraw

# constants
lat = 52.262297
lon = 10.522219
altitude = 75
search_angle = 70
category = 1 # brightest satellites
sec = 1 # retrieve position for next x sec
key = ""

# define functions
def coords_from_zenith_azimuth(rows,cols,zenith,azimuth):
    import math
    # rows: number of rows in image
    # cols: number of columns in image
    # zenith: zenith angle (°)
    # azimuth: azimuth angle (°) - 0° = north , 90° = east

    center_px = (math.floor(rows/2),math.floor(cols/2))
    tau = rows/180 # scale factor (px/°)

    d = zenith * tau # distance in px
    azimuth_rad = (azimuth-90) / 180 * math.pi

    x = math.floor(center_px[0] + d * math.cos(azimuth_rad))
    y = math.floor(center_px[1] + d * math.sin(azimuth_rad))

    return x,y


# main part
path = r'C:\Users\Admin\Documents\UFO\Satellites\sky_circle.png'

image = cv2.imread(path, 1)
rows,cols,channels = image.shape

img1 = Image.open(path)

path = r"C:\Users\Admin\Documents\UFO\Satellites\satellite_icon.png"
img2 = Image.open(path)

# get satellites above location
data = above(lat,lon,altitude,search_angle,category,key)

ids = []
sat_names = []
for i in range(0,len(data["above"])):
    ids.append(data["above"][i]["satid"])
    sat_names.append(data["above"][i]["satname"])

# get positions of each satellite above
azimuths = []
elevations = []
zeniths = []
for i in range(0,len(ids)):
    data2 = sat_position(ids[i],lat,lon,altitude,sec,key)

    azimuths.append(data2["positions"][0]["azimuth"])
    elevations.append(data2["positions"][0]["elevation"])
    zeniths.append(90-elevations[i])

    # get pixel coordinates
    x,y = coords_from_zenith_azimuth(rows,cols,zeniths[i],azimuths[i])

    try:
        # Pasting img2 image on top of img1
        # starting at coordinates (0, 0)
        img1.paste(img2, (x,y), mask = img2)

        # Call draw Method to add 2D graphics in an image
        I1 = ImageDraw.Draw(img1)
        # Add Text to an image
        sat_name = sat_names[i]
        I1.text((x, y + 48), sat_name, fill=(0, 0, 0))
    except:
        continue #print("No satellites above.")
# Displaying the image
img1.show()
img1.save("satellites_result.png")

# # Window name in which image is displayed
# window_name = 'Image'
# # Displaying the image
# cv2.imshow(window_name, image)
# k = cv2.waitKey(0) & 0xFF # hack to get cv2.imshow going
# if k == 27:         # wait for ESC key to exit
#     cv2.destroyAllWindows()

