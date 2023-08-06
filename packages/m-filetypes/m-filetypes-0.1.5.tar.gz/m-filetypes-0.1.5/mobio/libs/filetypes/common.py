import os

PATH_FOLDER, _ = os.path.split(os.path.abspath(__file__))

FILEPATH_SIGNATURE = os.path.join(PATH_FOLDER, 'file_signature.json')


class ExtensionImage:
    GIF = "gif"
    JPG = "jpg"
    JPEG = "jpeg"
    PNG = "png"

    LIST_EXTENSION_SUPPORTED = [GIF, JPEG, PNG, JPG]


class ExtensionDocument:
    DOC = "doc"
    DOCX = "docx"
    XLS = "xls"
    XLSX = "xlsx"
    PPT = "ppt"
    PPTX = "pptx"
    PDF = "pdf"

    LIST_EXTENSION_SUPPORTED = [DOC, DOCX, XLS, XLSX, PPT, PPTX, PDF]


class ExtensionAudio:
    MP3 = "mp3"
    MP4 = "mp4"
    MOV = "mov"
    AVI = "avi"
    THREE_GP = "3gp"
    THREE_G2 = "3g2"
    M4V = "m4v"
    MPEG = "mpeg"
    MPG = "mpg"
    OGV = "ogv"
    WEBM = "webm"
    FLV = "flv"
    MKV = "mkv"
    ASX = "asx"
    WMV = "wmv"

    LIST_EXTENSION_SUPPORTED = [MP3, MP4, MOV, AVI, THREE_GP, THREE_G2, M4V, MPEG, MPG, OGV, WEBM, FLV, MKV, ASX, WMV]


class ParamFileSignature:
    SIGNS = "signs"
    MIME = "mime"
