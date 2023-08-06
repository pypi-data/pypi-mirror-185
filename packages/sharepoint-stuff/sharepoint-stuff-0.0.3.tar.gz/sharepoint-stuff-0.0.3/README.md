# sharepoint-stuff

A package that adds a range of functionality for working with sharepoint sites from python e.g. uploading and downloading of files, creation of folders, etc. Under constant development and change as of January 2023.

## Installation

Run the following to install:

```python
python -m pip install sharepoint-stuff
```

## Usage

```python
from sharepoint_stuff import getCTX, uploadFile

# Initial authentication is necessary for all other functions in this package

ctx = getCTX("SHAREPOINT_URL", "USERNAME", "PASSWORD")

# then you can use that ClientContext (ctx) to authenticate for all the other functions, for example:

# the sharepoint relative url is relative to the name of your site so if you were in the directory -
# https://contoso.sharepoint.com/sites/MAIN_SITE/Shared%20Documents/important_docs then your relative url is "Shared Documents/important_docs/"

# the filepath should include the filename, this is so that the name of the file on sharepoint can be declared seperately to the name of the
# file on the system
uploadFile(ctx, "FILENAME_FOR_SHAREPOINT", "FILEPATH_ON_SYSTEM", "SHAREPOINT_RELATIVE_URL")
```