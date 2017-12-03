# scarfquine
Inspired by the work of fbz on generative scarves. This python file prints its own source code and outputs a tiff image which encodes the source code and adds a generative segment. The source code is copied to both ends of the scarf and is bound by two chequered sections with the generative section in the middle. The source is stored as UTF-8 binary values with black pixels = 0 and white = 1

## Generating a new scarf
Simply modify the scarf vars in the source, the quine output will automatically be updating accordingly, other changes to the source code will require generating a new quine string

## Generating a new quine string
If the source is modified, change `squine = '<old source string>'` to `squine = {}` and replace all scarf vars with `{}` then run quinegen.py. Copy the output of quinegen after the `b` and replace `{}` after `squine` with it, add desired scarf vars

### Other details
The source code is compact with minimal comments to reduce the space taken up by the source in the scarf itself. Only basic latin characters are used, allowing a byte length of 7 to be used for the source encoding in the image. There is no provision for dealing with bytes longer than the specified byte length, and no method to continue a byte on a next line, so byte length must be selected to be a factor of a valid row width in the image

### Todo
Scarf decoder
