token=

5426412733:AAG6272BW7o3A478pipnm8i8H1kBceG-YjA


url
`postgres://${user}:${password}@localhost/${database}`

'postgres://postgres:root@localhost/serverlocationbot'



53.339688, -6.236688


def inter_name(update_obj, context):
    context.user_data['username_handwritten'] = update_obj.message.text
    name_entered = context.user_data['username_handwritten']
    update_obj.message.reply_text(f"Your name is {name_entered}?")
    if name_entered == None:
        update_obj.message.reply_text(f"Your name is {name_entered}?")
        return ASK_NAME_AGAIN
    else:
        # wrong answer, reply, send a new question, and loop on the QUESTION state
        update_obj.message.reply_text("Wrong name :c (how you did this?..)")
        return INTER_NAME


def ask_again(update_obj, context):
    name_entered = context.user_data['username_handwritten']
    update_obj.message.reply_text(f"Your name is {name_entered}?",
        reply_markup=telegram.ReplyKeyboardMarkup([['YES', 'TRY AGAIN']], one_time_keyboard=True)
    )
    return ASK_NAME_AGAIN_HANDLER

def ask_name_again_handler(update_obj, context):
    if update_obj.message.text.lower() in ['yes', 'y']:
        return update_obj.message.reply_text("END")



All your information: {
    'id': 413310716,
    'is_bot': False, 
    'first_name': 'kirus',
    'username': 'urodoloh',
    'last_name': None,
    'language_code': 'en',
    'can_join_groups': None,
    'can_read_all_group_messages': None, 
    'supports_inline_queries': None,
    'is_premium': None,
    'added_to_attachment_menu': None
}

    # markup_reply_resize = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    # # add BUTTONS
    # markup_reply_resize.add(
    #     types.KeyboardButton('START GAME'),
    #     types.KeyboardButton('OPTIONS')
    #     )