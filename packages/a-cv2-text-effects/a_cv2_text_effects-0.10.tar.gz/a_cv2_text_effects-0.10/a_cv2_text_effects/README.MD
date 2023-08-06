# Text effects for OpenCV



```python
$pip install a-cv2-text-effects

import os
from a_cv_imwrite_imread_plus import open_image_in_cv,save_cv_image
from a_cv2_text_effects import (
    put_ttf_font_multiline_in_box_at_exact_center_location_with_exact_size,
    put_ttf_font_multiline_at_exact_center_location_with_exact_size,
    put_ttf_font_multiline_at_exact_location_with_exact_size,
    put_ttf_font_multiline_in_box_at_exact_location_with_exact_size,
    put_ttf_font_in_circle_at_exact_location_with_exact_size,
    put_ttf_font_in_box_at_exact_location_with_exact_size,
    put_ttf_font_at_exact_location_with_exact_size,
    putTrueTypeText,
    center_text_at_certain_size_at_a_specific_point,
    center_of_text_at_certain_size_at_a_specific_point_with_boxes,
)

img = open_image_in_cv(
    "https://raw.githubusercontent.com/hansalemaos/screenshots/main/merg6.png"
)
maxwidth = 150
maxheight = 150

(
    imgresult1,
    ptLowerLeftTextOriginX2,
    ptLowerLeftTextOriginY2,
    intFontFace2,
    fltFontScale2,
    intFontThickness2,
    textSize2,
) = center_of_text_at_certain_size_at_a_specific_point_with_boxes(
    img,
    "Number 1",
    maxwidth,
    maxheight,
    wheretoput=(200, 200),
    color=(255, 255, 0),
    add_thickness_each=10,
    rectangle_border_size=5,
    rectangle_border_colors=((244, 255, 0), (244, 0, 255)),
)

(
    imgresult2,
    ptLowerLeftTextOriginX,
    ptLowerLeftTextOriginY,
    intFontFace,
    fltFontScale,
    intFontThickness,
    textSize,
) = center_text_at_certain_size_at_a_specific_point(
    img,
    "Number 2",
    maxwidth,
    maxheight,
    wheretoput=(100, 100),
    color=(255, 255, 0),
    add_thickness_each=10,
)

imgresult3 = putTrueTypeText(
    img=img,
    text="Number 3",
    org=(100, 100),
    fontFace=r"C:\Windows\Fonts\ANTQUAB.TTF",
    fontScale=56,
    color=(255, 255, 0),
)


ia = put_ttf_font_at_exact_location_with_exact_size(
    image=img,
    text="Number 4",
    coords=(59, 300),
    color=(100, 0, 100),
    font=r"C:\Windows\Fonts\ANTQUAB.TTF",
    maxwidth=300,
    maxheight=100,
    fonttransparency=100,
)

ia1 = put_ttf_font_in_box_at_exact_location_with_exact_size(
    image=img,
    text="Number 5",
    coords=(59, 300),
    color=(100, 0, 100),
    font=r"C:\Windows\Fonts\ANTQUAB.TTF",
    maxwidth=300,
    maxheight=100,
    fonttransparency=0,
    boxtransparency=0.7,
    boxcolor=(255, 0, 0),
)

ia2 = put_ttf_font_in_circle_at_exact_location_with_exact_size(
    image=img,
    text="Number 6",
    coords=(59, 300),
    color=(100, 0, 100),
    font=r"C:\Windows\Fonts\ANTQUAB.TTF",
    maxwidth=300,
    maxheight=100,
    fonttransparency=50,
    circletransparency=0.2,
    circlecolor=(255, 0, 0),
)


ia3 = put_ttf_font_multiline_in_box_at_exact_location_with_exact_size(
    image=img,
    textwithnewline="Number 7\nNumber 7\nNumber 7",
    coords=(59, 10),
    color=(100, 0, 100),
    font=r"C:\Windows\Fonts\ANTQUAB.TTF",
    maxwidth=600,
    maxheight=600,
    fonttransparency=50,
    boxtransparency=0.2,
    boxcolor=(255, 0, 0),
    boxborder=20,
)


ia4 = put_ttf_font_multiline_at_exact_location_with_exact_size(
    image=img,
    textwithnewline="Number 8\nNumber 8\nNumber 8",
    coords=(59, 10),
    color=(100, 0, 100),
    font=r"C:\Windows\Fonts\ANTQUAB.TTF",
    maxwidth=600,
    maxheight=600,
    fonttransparency=50,
)


ia5 = put_ttf_font_multiline_at_exact_center_location_with_exact_size(
    image=img,
    textwithnewline="Number 9\nNumber 9\nNumber 9",
    coords=(300, 300),
    color=(255, 255, 210),
    font=r"C:\Windows\Fonts\ANTQUAB.TTF",
    maxwidth=300,
    maxheight=100,
    fonttransparency=-1,
)


ia6 = put_ttf_font_multiline_in_box_at_exact_center_location_with_exact_size(
    image=img,
    textwithnewline="Number 10\nNumber 10\nNumber 10",
    coords=(300, 300),
    color=(255, 255, 210),
    font=r"C:\Windows\Fonts\ANTQUAB.TTF",
    maxwidth=300,
    maxheight=100,
    fonttransparency=50,
    boxtransparency=0.2,
    boxcolor=(255, 0, 0),
    boxborder=20,
)


allimgs=    [
        imgresult1,
        imgresult2,
        imgresult3,
        ia["result"],
        ia1["result"],
        ia2["result"],
        ia3["result"],
        ia4["result"],
        ia5["result"],
        ia6["result"],

    ]
for i,b in enumerate(allimgs):
    save_cv_image(os.path.join('f:\\alltextimgs',str(i).zfill(6) + '.png'), b)

```


<img src="https://github.com/hansalemaos/screenshots/raw/main/texteffects/000000.png"/>


<img src="https://github.com/hansalemaos/screenshots/raw/main/texteffects/000000.png"/>



<img src="https://github.com/hansalemaos/screenshots/raw/main/texteffects/000001.png"/>



<img src="https://github.com/hansalemaos/screenshots/raw/main/texteffects/000002.png"/>



<img src="https://github.com/hansalemaos/screenshots/raw/main/texteffects/000003.png"/>



<img src="https://github.com/hansalemaos/screenshots/raw/main/texteffects/000004.png"/>



<img src="https://github.com/hansalemaos/screenshots/raw/main/texteffects/000005.png"/>



<img src="https://github.com/hansalemaos/screenshots/raw/main/texteffects/000006.png"/>



<img src="https://github.com/hansalemaos/screenshots/raw/main/texteffects/000007.png"/>



<img src="https://github.com/hansalemaos/screenshots/raw/main/texteffects/000008.png"/>



<img src="https://github.com/hansalemaos/screenshots/raw/main/texteffects/000009.png"/>