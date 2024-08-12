from linebot import(
    LineBotApi, WebhookHandler
)
from linebot.exceptions import(
    InvalidSignatureError
)
from linebot.models import(
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage, FollowEvent, UnfollowEvent, TemplateSendMessage, CarouselTemplate, CarouselColumn, URIAction
)
line_bot_api = LineBotApi('DCk2pZiR/+/DqU24Sq2Emn/0d0ofkpH+UiQ4dQ4wFPrx40xLcdRd4fd9GiEfdTM1pOlmAGnLs6deQ8IFx0fy3Q1Jv0Dkqa1dtzCbOneSH8g38+EN3vadpe+jMz4QM9ttjAUmCyWqw9z6C6fYOVf+aQdB04t89/1O/w1cDnyilFU=')

handler = WebhookHandler('d7714aafb514783051f0b27b139eccb2')