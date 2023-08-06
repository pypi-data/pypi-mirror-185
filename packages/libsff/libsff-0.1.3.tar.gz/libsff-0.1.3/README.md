# sfflib

sfflib is an opensource, miltiplatform Scanlation File Format (sff) parser made for [CanScanlate](https://github.com/NandeMD/CanScanlate/tree/man).

[.sff](test.sffx) files are basically xml files with some custom tags.

Below is the basic sff file:
```xml
<Document>
    <Metadata>
        <Script>Scanlation Script File v0.1.0</Script>
        <App></App>
        <Info>Made by NandeMD.</Info>
        <TLLength>0</TLLength>
        <PRLength>0</PRLength>
        <CMLength>0</CMLength>
        <BalloonCount>0</BalloonCount>
        <LineCount>0</LineCount>
    </Metadata>
    <Baloon type="Square" has_image="No">
        <text>
            şşşşşşşşşşşşşşşşşşşşşşşşşşşşşşşşşşşşşşşşşşşşşşşşşşşş
        </text>
        <text>
            şşşşşşşşşşşşşşşşşşşşşşşşşşşşşşşşşşşşşşşşşşşşşşşşşşşş
        </text>
  </Baloon>
</Document>
```

# Installing

**Python 3.8 or higher is required!**

```bash
# Linux/MacOS
python3 -m pip install -U libssf

# Windows
py -m pip install -U libsff
```

# Example
```python
from libsff import Document, Balloon, Out
from random import randint

# open a test image
with open("testimg.jpg", "rb") as file:
    imagefile = file.read()

# Create a blank document object
doc = Document.create_blank()

# Generate random 100 balloons
for _ in range(100):
    # Randomize imge
    has_image = randint(0, 1)

    # Add a Balloon object to our document
    docasd.add_balloon(
        Balloon(
            tl_content=[
                "Hi, this is tl line 1",
                "Hi, this is tl line 2"
            ],
            btype=randint(0, 4),
            has_img=has_image, # Yes, this is int
            balloon_img=imagefile if has_image else b"",
            img_type="jpg"
        )
    )

# Save as raw xml:
doc.save_sff("test", Out.RAW)

# Save as gzip compressed xml:
doc.save_sff("test", Out.GZIP)

# Save as lzma compressed xml:
doc.save_sff("test", Out.LZMA)

# Save as formatted text:
doc.save_sff("test", Out.TXT)
```
