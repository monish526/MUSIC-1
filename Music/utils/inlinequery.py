
from pyrogram.types import (InlineQueryResultArticle,
                            InputTextMessageContent)

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="ミ★ ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs ★彡",
            description=f"𝐓𝐨 𝐨𝐩𝐞𝐧 𝐭𝐡𝐞 𝐦𝐮𝐬𝐢𝐜 𝐡𝐞𝐥𝐩 𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐬.",
            thumb_url="https://te.legra.ph/file/4b86e5c72652c70c783bf.jpg",
            input_message_content=InputTextMessageContent("/mhelp"),
        ),      
        InlineQueryResultArticle(
            title="ミ★ Settings ★彡",
            description=f"𝐓𝐨 𝐨𝐩𝐞𝐧 𝐭𝐡𝐞 𝐠𝐫𝐨𝐮𝐩 𝐬𝐞𝐭𝐭𝐢𝐧𝐠𝐬 𝐩𝐚𝐧𝐧𝐞𝐥.",
            thumb_url="https://te.legra.ph/file/1f2ec02494104d2345ed0.jpg",
            input_message_content=InputTextMessageContent("/msetting"),
        ),      
        InlineQueryResultArticle(
            title="ミ★ 𝘗𝘢𝘶𝘴𝘦 𝘚𝘵𝘳𝘦𝘢𝘮 ★彡",
            description=f"𝐏𝐚𝐮𝐬𝐞 𝐭𝐡𝐞 𝐜𝐮𝐫𝐫𝐞𝐧𝐭 𝐩𝐥𝐚𝐲𝐨𝐮𝐭 𝐨𝐧 𝐠𝐫𝐨𝐮𝐩 𝐜𝐚𝐥𝐥.",
            thumb_url="https://te.legra.ph/file/0d882277912ab980e65b2.jpg",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="ミ★ 𝘙𝘦𝘴𝘶𝘮𝘦 𝘚𝘵𝘳𝘦𝘢𝘮 ★彡",
            description=f"𝐑𝐞𝐬𝐮𝐦𝐞 𝐭𝐡𝐞 𝐨𝐧𝐠𝐨𝐢𝐧𝐠 𝐩𝐥𝐚𝐲𝐨𝐮𝐭 𝐨𝐧 𝐠𝐫𝐨𝐮𝐩 𝐜𝐚𝐥𝐥.",
            thumb_url="https://te.legra.ph/file/2810692f42e178a523c90.jpg",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="ミ★ 𝘔𝘶𝘵𝘦 𝘚𝘵𝘳𝘦𝘢𝘮 ★彡",
            description=f"𝐌𝐮𝐭𝐞 𝐭𝐡𝐞 𝐨𝐧𝐠𝐨𝐢𝐧𝐠 𝐩𝐥𝐚𝐲𝐨𝐮𝐭 𝐨𝐧 𝐠𝐫𝐨𝐮𝐩 𝐜𝐚𝐥𝐥.",
            thumb_url="https://te.legra.ph/file/67598d8a34dc744fdc502.jpg",
            input_message_content=InputTextMessageContent("/mute"),
        ),
        InlineQueryResultArticle(
            title="ミ★ 𝘜𝘯𝘮𝘶𝘵𝘦 𝘚𝘵𝘳𝘦𝘢𝘮 ★彡",
            description=f"𝐔𝐧𝐦𝐮𝐭𝐞 𝐭𝐡𝐞 𝐨𝐧𝐠𝐨𝐢𝐧𝐠 𝐩𝐥𝐚𝐲𝐨𝐮𝐭 𝐨𝐧 𝐠𝐫𝐨𝐮𝐩 𝐜𝐚𝐥𝐥.",
            thumb_url="https://te.legra.ph/file/53ebf734fef8e502cbd8f.png",
            input_message_content=InputTextMessageContent("/unmute"),
        ),
        InlineQueryResultArticle(
            title="ミ★ 𝘚𝘬𝘪𝘱 𝘚𝘵𝘳𝘦𝘢𝘮 ★彡",
            description=f"𝐒𝐤𝐢𝐩 𝐭𝐨 𝐧𝐞𝐱𝐭 𝐭𝐫𝐚𝐜𝐤. | 𝐅𝐨𝐫 𝐒𝐩𝐞𝐜𝐢𝐟𝐢𝐜 𝐭𝐫𝐚𝐜𝐤 𝐧𝐮𝐦𝐛𝐞𝐫: /𝐬𝐤𝐢𝐩 [𝐧𝐮𝐦𝐛𝐞𝐫] ",
            thumb_url="https://te.legra.ph/file/596c98dc62f38ce0dd552.png",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="ミ★ 𝘌𝘯𝘥 𝘚𝘵𝘳𝘦𝘢𝘮 ★彡",
            description="𝐒𝐭𝐨𝐩 𝐭𝐡𝐞 𝐨𝐧𝐠𝐨𝐢𝐧𝐠 𝐩𝐥𝐚𝐲𝐨𝐮𝐭 𝐨𝐧 𝐠𝐫𝐨𝐮𝐩 𝐜𝐚𝐥𝐥.",
            thumb_url="https://te.legra.ph/file/13293feefb3a84b4fddfa.png",
            input_message_content=InputTextMessageContent("/stop"),
        ),
        InlineQueryResultArticle(
            title="ミ★ 𝘚𝘩𝘶𝘧𝘧𝘭𝘦 𝘚𝘵𝘳𝘦𝘢𝘮 ★彡",
            description="𝐒𝐡𝐮𝐟𝐟𝐥𝐞 𝐭𝐡𝐞 𝐪𝐮𝐞𝐮𝐞𝐝 𝐭𝐫𝐚𝐜𝐤𝐬 𝐥𝐢𝐬𝐭.",
            thumb_url="https://te.legra.ph/file/610120efcf9a8b6c90822.png",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="ミ★ 𝘚𝘦𝘦𝘬 𝘚𝘵𝘳𝘦𝘢𝘮 ★彡",
            description="𝐒𝐞𝐞𝐤 𝐭𝐡𝐞 𝐨𝐧𝐠𝐨𝐢𝐧𝐠 𝐬𝐭𝐫𝐞𝐚𝐦 𝐭𝐨 𝐚 𝐬𝐩𝐞𝐜𝐢𝐟𝐢𝐜 𝐝𝐮𝐫𝐚𝐭𝐢𝐨𝐧.",
            thumb_url="https://te.legra.ph/file/a93e8e0fc292aae22fb43.jpg",
            input_message_content=InputTextMessageContent("/seek 10"),
        ),
        InlineQueryResultArticle(
            title="ミ★ 𝘓𝘰𝘰𝘱 𝘚𝘵𝘳𝘦𝘢𝘮 ★彡",
            description="𝐋𝐨𝐨𝐩 𝐭𝐡𝐞 𝐜𝐮𝐫𝐫𝐞𝐧𝐭 𝐩𝐥𝐚𝐲𝐢𝐧𝐠 𝐦𝐮𝐬𝐢𝐜. | 𝐔𝐬𝐚𝐠𝐞: /𝐥𝐨𝐨𝐩 [𝐞𝐧𝐚𝐛𝐥𝐞|𝐝𝐢𝐬𝐚𝐛𝐥𝐞]",
            thumb_url="https://te.legra.ph/file/e7c10d9194ae8d9d5b7e3.jpg",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
        InlineQueryResultArticle(
            title="ミ★ Support us ★彡",
            description=f"ıllıllı Support us in ıllıllı.",
            thumb_url="https://te.legra.ph/file/fc96390beb168c19b1788.jpg",
            input_message_content=InputTextMessageContent("[  please join Here   😇](https://t.me/gangs_for_udanpirappu)"),
        ),        
    ]
)
