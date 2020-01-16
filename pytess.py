from PIL import Image

import pytesseract

def test(img):

    ans = ""
    ans = pytesseract.image_to_string(Image.open(img), lang="transliterate")
    #ans = ans.encode('utf-8')
    return ans#.encode('utf-8')

