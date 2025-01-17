.. _herokutl-client:

==============
TelegramClient
==============

.. currentmodule:: herokutl.client

The `TelegramClient <telegramclient.TelegramClient>` aggregates several mixin
classes to provide all the common functionality in a nice, Pythonic interface.
Each mixin has its own methods, which you all can use.

**In short, to create a client you must run:**

.. code-block:: python

    from herokutl import TelegramClient

    client = TelegramClient(name, api_id, api_hash)

    async def main():
        # Now you can use all client methods listed below, like for example...
        await client.send_message('me', 'Hello to myself!')

    with client:
        client.loop.run_until_complete(main())


You **don't** need to import these `AuthMethods`, `MessageMethods`, etc.
Together they are the `TelegramClient <telegramclient.TelegramClient>` and
you can access all of their methods.

See :ref:`client-ref` for a short summary.

.. automodule:: herokutl.client.telegramclient
    :members:
    :undoc-members:
    :show-inheritance:

.. automodule:: herokutl.client.telegrambaseclient
    :members:
    :undoc-members:
    :show-inheritance:

.. automodule:: herokutl.client.account
    :members:
    :undoc-members:
    :show-inheritance:

.. automodule:: herokutl.client.auth
    :members:
    :undoc-members:
    :show-inheritance:

.. automodule:: herokutl.client.bots
    :members:
    :undoc-members:
    :show-inheritance:

.. automodule:: herokutl.client.buttons
    :members:
    :undoc-members:
    :show-inheritance:

.. automodule:: herokutl.client.chats
    :members:
    :undoc-members:
    :show-inheritance:

.. automodule:: herokutl.client.dialogs
    :members:
    :undoc-members:
    :show-inheritance:

.. automodule:: herokutl.client.downloads
    :members:
    :undoc-members:
    :show-inheritance:

.. automodule:: herokutl.client.messageparse
    :members:
    :undoc-members:
    :show-inheritance:

.. automodule:: herokutl.client.messages
    :members:
    :undoc-members:
    :show-inheritance:

.. automodule:: herokutl.client.updates
    :members:
    :undoc-members:
    :show-inheritance:

.. automodule:: herokutl.client.uploads
    :members:
    :undoc-members:
    :show-inheritance:

.. automodule:: herokutl.client.users
    :members:
    :undoc-members:
    :show-inheritance:
