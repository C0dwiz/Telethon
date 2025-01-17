=================
Objects Reference
=================

This is the quick reference for those objects returned by client methods
or other useful modules that the library has to offer. They are kept in
a separate page to help finding and discovering them.

Remember that this page only shows properties and methods,
**not attributes**. Make sure to open the full documentation
to find out about the attributes.

.. contents::


ChatGetter
==========

All events base `ChatGetter <herokutl.tl.custom.chatgetter.ChatGetter>`,
and some of the objects below do too, so it's important to know its methods.

.. currentmodule:: herokutl.tl.custom.chatgetter.ChatGetter

.. autosummary::
    :nosignatures:

    chat
    input_chat
    chat_id
    is_private
    is_group
    is_channel

    get_chat
    get_input_chat


SenderGetter
============

Similar to `ChatGetter <herokutl.tl.custom.chatgetter.ChatGetter>`, a
`SenderGetter <herokutl.tl.custom.sendergetter.SenderGetter>` is the same,
but it works for senders instead.

.. currentmodule:: herokutl.tl.custom.sendergetter.SenderGetter

.. autosummary::
    :nosignatures:

    sender
    input_sender
    sender_id

    get_sender
    get_input_sender


Message
=======

.. currentmodule:: herokutl.tl.custom.message

The `Message` type is very important, mostly because we are working
with a library for a *messaging* platform, so messages are widely used:
in events, when fetching history, replies, etc.

It bases `ChatGetter <herokutl.tl.custom.chatgetter.ChatGetter>` and
`SenderGetter <herokutl.tl.custom.sendergetter.SenderGetter>`.

Properties
----------

.. note::

    We document *custom properties* here, not all the attributes of the
    `Message` (which is the information Telegram actually returns).

.. currentmodule:: herokutl.tl.custom.message.Message

.. autosummary::
    :nosignatures:

    text
    raw_text
    is_reply
    forward
    buttons
    button_count
    file
    photo
    document
    web_preview
    audio
    voice
    video
    video_note
    gif
    sticker
    contact
    game
    geo
    invoice
    poll
    venue
    action_entities
    via_bot
    via_input_bot
    client


Methods
-------

.. autosummary::
    :nosignatures:

    respond
    reply
    forward_to
    edit
    delete
    get_reply_message
    click
    mark_read
    pin
    download_media
    get_entities_text
    get_buttons


File
====

The `File <herokutl.tl.custom.file.File>` type is a wrapper object
returned by `Message.file <herokutl.tl.custom.message.Message.file>`,
and you can use it to easily access a document's attributes, such as
its name, bot-API style file ID, etc.

.. currentmodule:: herokutl.tl.custom.file.File

.. autosummary::
    :nosignatures:

    id
    name
    ext
    mime_type
    width
    height
    size
    duration
    title
    performer
    emoji
    sticker_set


Conversation
============

The `Conversation <herokutl.tl.custom.conversation.Conversation>` object
is returned by the `client.conversation()
<herokutl.client.dialogs.DialogMethods.conversation>` method to easily
send and receive responses like a normal conversation.

It bases `ChatGetter <herokutl.tl.custom.chatgetter.ChatGetter>`.

.. currentmodule:: herokutl.tl.custom.conversation.Conversation

.. autosummary::
    :nosignatures:

    send_message
    send_file
    mark_read
    get_response
    get_reply
    get_edit
    wait_read
    wait_event
    cancel
    cancel_all


AdminLogEvent
=============

The `AdminLogEvent <herokutl.tl.custom.adminlogevent.AdminLogEvent>` object
is returned by the `client.iter_admin_log()
<herokutl.client.chats.ChatMethods.iter_admin_log>` method to easily iterate
over past "events" (deleted messages, edits, title changes, leaving members…)

These are all the properties you can find in it:

.. currentmodule:: herokutl.tl.custom.adminlogevent.AdminLogEvent

.. autosummary::
    :nosignatures:

    id
    date
    user_id
    action
    old
    new
    changed_about
    changed_title
    changed_username
    changed_photo
    changed_sticker_set
    changed_message
    deleted_message
    changed_admin
    changed_restrictions
    changed_invites
    joined
    joined_invite
    left
    changed_hide_history
    changed_signatures
    changed_pin
    changed_default_banned_rights
    stopped_poll


Button
======

The `Button <herokutl.tl.custom.button.Button>` class is used when you login
as a bot account to send messages with reply markup, such as inline buttons
or custom keyboards.

These are the static methods you can use to create instances of the markup:

.. currentmodule:: herokutl.tl.custom.button.Button

.. autosummary::
    :nosignatures:

    inline
    switch_inline
    url
    auth
    text
    request_location
    request_phone
    request_poll
    clear
    force_reply


InlineResult
============

The `InlineResult <herokutl.tl.custom.inlineresult.InlineResult>` object
is returned inside a list by the `client.inline_query()
<herokutl.client.bots.BotMethods.inline_query>` method to make an inline
query to a bot that supports being used in inline mode, such as
`@like <https://t.me/like>`_.

Note that the list returned is in fact a *subclass* of a list called
`InlineResults <herokutl.tl.custom.inlineresults.InlineResults>`, which,
in addition of being a list (iterator, indexed access, etc.), has extra
attributes and methods.

These are the constants for the types, properties and methods you
can find the individual results:

.. currentmodule:: herokutl.tl.custom.inlineresult.InlineResult

.. autosummary::
    :nosignatures:

    ARTICLE
    PHOTO
    GIF
    VIDEO
    VIDEO_GIF
    AUDIO
    DOCUMENT
    LOCATION
    VENUE
    CONTACT
    GAME
    type
    message
    title
    description
    url
    photo
    document
    click
    download_media


Dialog
======

The `Dialog <herokutl.tl.custom.dialog.Dialog>` object is returned when
you call `client.iter_dialogs() <herokutl.client.dialogs.DialogMethods.iter_dialogs>`.

.. currentmodule:: herokutl.tl.custom.dialog.Dialog

.. autosummary::
    :nosignatures:

    send_message
    archive
    delete


Draft
======

The `Draft <herokutl.tl.custom.draft.Draft>` object is returned when
you call `client.iter_drafts() <herokutl.client.dialogs.DialogMethods.iter_drafts>`.

.. currentmodule:: herokutl.tl.custom.draft.Draft

.. autosummary::
    :nosignatures:

    entity
    input_entity
    get_entity
    get_input_entity
    text
    raw_text
    is_empty
    set_message
    send
    delete


Utils
=====

The `herokutl.utils` module has plenty of methods that make using the
library a lot easier. Only the interesting ones will be listed here.

.. currentmodule:: herokutl.utils

.. autosummary::
    :nosignatures:

    get_display_name
    get_extension
    get_inner_text
    get_peer_id
    resolve_id
    pack_bot_file_id
    resolve_bot_file_id
    resolve_invite_link
